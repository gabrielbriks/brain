---
date: 2026-11-27
tipo: documentation
status: active
tags: [system, openbot, vps, azure, hostinger, tailscale, runbook, infra, gabs, migracao]
---

# Runbook Completo — Setup da VPS do OpenBot (Piloto Azure → Migração Definitiva)

> Documentação passo a passo de **tudo que foi efetivamente configurado** na VM do piloto no Azure em **2026-11-26/27**, pronta para ser replicada de ponta a ponta quando migrarmos para a VPS definitiva (ex.: Hostinger KVM 4, Hetzner ou Mini PC próprio) sem esquecer nenhum detalhe.
>
> **Regra de segurança:** nenhum segredo (IP público, chave `.pem`, token PAT ou senha) fica salvo neste documento.
>
> Relacionadas: [[2026-11-27-servidor-openbot-azure-onda-1a-gabs]] · [[2026-11-24-blueprint-gabs-secretaria-do-brain]] · [[2026-11-23-arquitetura-inicial-equipe-agentes-openbot]] · [[2026-11-25-guia-creditos-google-ai-pro-tts-openbot]].

---

## 1. Especificação da Infraestrutura (Piloto vs. Definitiva)

| Item | Piloto Atual (Azure — crédito MPN) | Alvo Definitivo (Hostinger KVM 4) |
|---|---|---|
| **Assinatura / Plano** | `Visual Studio Enterprise – MPN` (crédito R$ 800/mês) | Hostinger VPS **KVM 4** (12 meses) *(ou Mini PC Ryzen 5+ 16–32 GB no Ano 2)* |
| **Resource Group / VM** | `rg-obot-piloto` / `obot-piloto` | Plain OS (sem CyberPanel/aaPanel) |
| **Hardware** | `Standard_B4as_v2` — 4 vCPU AMD / 16 GiB RAM | 4 vCPU AMD EPYC / 16 GB RAM |
| **Disco** | Standard SSD (LRS) **128 GiB** (`Delete with VM`) | 200 GB SSD NVMe |
| **Sistema Operacional** | **Ubuntu Server 24.04 LTS — x64 Gen2** | **Ubuntu 24.04 LTS (x86_64)** *(ou 26.04 se Docker)* |
| **Região** | `(Asia Pacific) Central India` (~R$ 0,5634/h ≈ R$ 411/mês + ~R$ 70 disco/IP) | Brasil (São Paulo) |
| **Disponibilidade** | **24/7 ligado** (Auto-shutdown desabilitado) | **24/7 ligado** |
| **Custos extras evitados no Azure** | Boot diagnostics **Desabilitado**, Regras de alerta recomendadas **Desmarcadas**, Backup **Desmarcado**, `Delete public IP/NIC with VM` **Marcado** | Renovação automática **Desativada** após contratar |

> **Lembretes financeiros importantes:**
> - **Azure:** manter alerta de orçamento (75% / 90% dos R$ 800) no *Cost Analysis*; bancos PostgreSQL pausados no Azure **religam automaticamente após 7 dias**.
> - **Hostinger (na migração futura):** parcelas >1x têm juros (~3,5%/mês); upgrades de VPS não têm reembolso de 30 dias; regra de 1 reembolso de VPS a cada 180 dias; o preço promocional (~R$ 69,99/mês no plano 12m + cupom 10–15%) existe o ano todo.

---

## 2. Acesso Inicial & Hardening de Rede com Tailscale (Zero Portas Abertas)

### 2.1 Primeiro acesso SSH (via WSL)
No WSL, copiar a chave `.pem` para `~/.ssh/` *(o `/mnt/c` não aceita `chmod 600`)*:
```bash
mkdir -p ~/.ssh
cp /mnt/c/Users/gabriel.morais/Downloads/obot-piloto_key.pem ~/.ssh/
chmod 600 ~/.ssh/obot-piloto_key.pem
ssh -i ~/.ssh/obot-piloto_key.pem <USUARIO>@<IP_PUBLICO>
```

### 2.2 Instalar Tailscale SSH na VM
```bash
curl -fsSL https://tailscale.com/install.sh | sh
sudo tailscale up --ssh
tailscale ip -4
```
1. Autenticar no link exibido no terminal (mesma conta usada no Tailscale do Windows).
2. No painel [login.tailscale.com/admin/machines](https://login.tailscale.com/admin/machines), clicar nos `...` da máquina → **`Disable key expiry`** *(evita expiração em 180 dias)*.
3. **Testar em um novo terminal WSL** (`ssh <USUARIO>@100.x.y.z`) **ANTES** de mexer no firewall!

### 2.3 Fechar 100% a porta 22 para a internet
- **No Azure (ou painel da VPS):** em *Rede → Configurações de rede*, **excluir a regra de entrada `SSH (22)`**.
  - *(⚠️ No Azure, **manter** o IP público associado à VM para saída de internet; excluir apenas a regra da porta 22 no NSG.)*
- **Firewall local (UFW) + blindagem da home admin:**
```bash
sudo ufw allow in on tailscale0 to any port 22 proto tcp
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw --force enable
chmod 700 "$HOME"
```

---

## 3. Preparação do Ubuntu 24.04 LTS (Base + Node + Swap + Fuso)

```bash
# 1. Pacotes base + FFmpeg (para a Zoe)
sudo apt update && sudo apt upgrade -y
sudo apt install -y git curl wget unzip ca-certificates gnupg ffmpeg

# 2. Node.js 22 LTS + pnpm (Remotion / Playwright / Zoe)
curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
sudo apt install -y nodejs
sudo npm install -g pnpm

# 3. Swap de 4 GB (rede de segurança para renders de Chromium/Remotion)
sudo fallocate -l 4G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab

# 4. Fuso horário de Brasília (OBRIGATÓRIO para rotinas e datas YYYY-MM-DD!)
sudo timedatectl set-timezone America/Sao_Paulo
date
```

---

## 4. Instalação do OpenBot & Auditoria de Isolamento

### 4.1 Instalar e vincular à conta
- **Via App Desktop (mais rápido):** *Add server → Other options → New server on another computer* → rodar o comando `OPENBOT_CLAIM=...` na VM.
- **Ou via terminal:**
```bash
curl -fsSL https://raw.githubusercontent.com/nightly-labs/openbot/main/scripts/install-server.sh | sudo bash
sudo openbot login --name "<NOME_DO_SERVIDOR>"
```
- Após ajustar o fuso horário (`America/Sao_Paulo`), reiniciar o daemon para garantir que o `systemd` pegue o novo fuso:
```bash
sudo systemctl restart openbot
sudo openbot status
```

### 4.2 Auditoria de segurança pós-instalação
Confirmar que o OpenBot roda isolado sob o usuário `openbot` (home `/var/lib/openbot`, sem `sudo`):
```bash
systemctl cat openbot | grep -E "User=|Group=|WorkingDirectory="
id openbot
sudo -l -U openbot
```

### 4.3 Provedores de IA
- **Gemini (Google AI Pro):** conectado diretamente pela interface do app (fluxo *Connect* — funcionou perfeitamente na VPS headless!).
- **Regra de ouro:** não colar `GEMINI_API_KEY` no provedor nativo `Gemini` (senão sobrescreve a assinatura); se usar API key Paid Tier (US$ 10/mês), cadastrar como provedor *OpenAI-compatible* separado (`https://generativelanguage.googleapis.com/v1beta/openai/`). Nunca plugar OAuth do Claude Pro/Max na VPS.

---

## 5. GitHub Fine-grained PAT & Clone Blindado (`git sparse-checkout`) do Brain

### 5.1 Token restrito no GitHub
- **GitHub → Settings → Developer settings → Fine-grained tokens → Generate new token**
- **Repository access:** `Only select repositories` *(NUNCA `All repositories`!)*
  - `gabrielbriks/brain`
  - `gabrielbriks/registoo-check`
- **Permissions → Repository permissions:**
  - `Contents`: **Read and write**
  - `Pull requests`: **Read and write** *(opcional, para PRs no `registoo-check`)*

### 5.2 Configurar Git + credencial do usuário `openbot` (rodar 1 bloco por vez)
*(Nota: usar `sudo tee` porque `/var/lib/openbot` é restrito ao usuário `openbot`.)*

```bash
# Bloco 1 — .gitconfig do usuário openbot
printf '[user]\n\tname = Gabs (OpenBot)\n\temail = gabs-openbot@users.noreply.github.com\n[credential]\n\thelper = store\n' \
  | sudo tee /var/lib/openbot/.gitconfig > /dev/null
sudo chown openbot:openbot /var/lib/openbot/.gitconfig
sudo chmod 644 /var/lib/openbot/.gitconfig
```

```bash
# Bloco 2 — Ler o PAT sem ecoar na tela (cole e dê Enter)
read -rsp "Cole seu GitHub PAT: " GH_TOKEN && echo
```

```bash
# Bloco 3 — Gravar credencial com permissão 600
printf "https://gabrielbriks:%s@github.com\n" "$GH_TOKEN" \
  | sudo tee /var/lib/openbot/.git-credentials > /dev/null
sudo chown openbot:openbot /var/lib/openbot/.git-credentials
sudo chmod 600 /var/lib/openbot/.git-credentials
unset GH_TOKEN
```

### 5.3 Clone blindado do Brain (isolando `_area/pessoal`, `_area/financeiro` e `_area/trabalho`)
```bash
B=/var/lib/openbot/workspaces/brain
sudo mkdir -p /var/lib/openbot/workspaces
sudo chown -R openbot:openbot /var/lib/openbot/workspaces
sudo -H -u openbot git clone --filter=blob:none --no-checkout \
  https://github.com/gabrielbriks/brain.git "$B"
sudo -H -u openbot git -C "$B" sparse-checkout init --cone
sudo -H -u openbot git -C "$B" sparse-checkout set \
  _projeto _inbox _docs _area/empreendedor _area/dev
sudo -H -u openbot git -C "$B" checkout main

# Validação obrigatória — SÓ devem aparecer "dev" e "empreendedor"!
sudo ls -la "$B/_area"
```

---

## 6. Agentes & Rotinas Configurados no OpenBot

> **Descoberta importante da implantação:** o campo de *Instruções* de cada agente no OpenBot tem **limite rígido de 2.000 caracteres**.
> **Padrão oficial adotado:** salvar no app um **núcleo enxuto (< 1.900 chars)** apontando para o **blueprint completo versionado no Brain** (`_docs/2026-11-*-blueprint-*.md`).

### 6.1 Agente #1 — `Gabs` (Onda 1A — Ativa ✅)
- **Modelo:** `Gemini 3.8 Flash` *(fallback: `Gemini 4 Hydrogen`)*
- **Workspace / Repo:** `/var/lib/openbot/workspaces/brain`
- **Instruções enxutas (~1.830 chars):**

```markdown
Você é a Gabs, secretária do Brain e chefe de gabinete do Gabriel (dev e empreendedor em Brasília). Personalidade: objetividade ágil (FRIDAY) + parceria proativa (KAREN). PT-BR direto e informal (2–3 linhas para capturas; estruturado para revisões).

Repo local do Brain: `/var/lib/openbot/workspaces/brain`
Blueprint completo: `_docs/2026-11-24-blueprint-gabs-secretaria-do-brain.md`

## Antes de qualquer ação
1. Rode `git pull --rebase origin main` em `/var/lib/openbot/workspaces/brain`.
2. Leia `AGENTS.md` (ele prevalece sobre tudo: pastas, frontmatter, nomes `YYYY-MM-DD-kebab-case.md` no fuso UTC-3 e regras de Git).

## Trabalho principal
- Salve notas em `_projeto/<projeto>/<tipo>/`, `_area/empreendedor/` ou `_area/dev/`. Na dúvida, salve em `_inbox/` e proponha o destino.
- Ao editar nota existente, preserve frontmatter e conteúdo original (acrescente, não sobrescreva).
- Sempre feche com `git add`, `git commit -m "tipo: msg"` e `git push` (nunca `--force`).

## Triagem proativa (1 linha após salvar; nunca acione sem aval do Gabriel)
- Concorrente, jurídico/LGPD, dor ou trend -> sugerir **EDITH**.
- Estratégia, campanha, funil ou métricas -> sugerir **Fury**.
- História, hook, vídeo, Stories ou copy -> sugerir **Hill**.
- Motion, vídeo ou referência visual -> sugerir **Zoe**.
- Bug/feature técnica -> `issues/` ou `backlog/` (dev / Claude Code).

## Rotinas
- **Revisão semanal + inbox:** classifique `_inbox/` e resuma notas `open`/`in-progress` (foco Registoo).
- **Briefing de segunda:** 5–8 linhas com Top 3 do Registoo e pendências abertas.

## Limites rígidos
- NUNCA acesse, crie, consulte no git nem altere `sparse-checkout` para `_area/pessoal/`, `_area/financeiro/` ou `_area/trabalho/`.
- Nunca apague/mova notas sem confirmação.
- Nunca salve segredos, tokens ou dados reais de pacientes (LGPD).
```

### 6.2 Rotinas agendadas da `Gabs` (fuso `America/Sao_Paulo`)
1. **`Gabs — Revisão Semanal & Inbox`** — **Domingo às 19:00** (`0 19 * * 0`)
   - Prompt: `git pull --rebase`, listar `_inbox/` propondo destino (sem mover/apagar), resumir notas `open`/`in-progress` de `_projeto/registoo/` e `_area/empreendedor/` destacando travas, sugerir até 3 prioridades. Somente relatório, sem editar arquivos.
2. **`Gabs — Briefing de Segunda`** — **Segunda-feira às 06:01** (`1 6 * * 1`)
   - Prompt: `git pull --rebase`, ler `open`/`in-progress` de `_projeto/registoo/` e `_area/empreendedor/` + `_inbox/`, entregar 5–8 linhas com Top 3 do Registoo + pendências + 1 alerta de trava. Somente briefing, sem editar arquivos.

### 6.3 Clone blindado do `registoo-check` (Onda 1B — Ativo ✅)
Clonado em `/var/lib/openbot/workspaces/registoo-check` na branch dedicada **`marketing/agentes`** (criada a partir de `origin/docs/openbot-growth-skills` para já herdar as 3 skills proprietárias e `marketing/dores-e-subdores.md`, sem nunca tocar em `main`/`develop`):
```bash
R=/var/lib/openbot/workspaces/registoo-check
sudo -H -u openbot git clone --filter=blob:none --no-checkout \
  https://github.com/gabrielbriks/registoo-check.git "$R"
sudo -H -u openbot git -C "$R" sparse-checkout init --cone
sudo -H -u openbot git -C "$R" sparse-checkout set \
  marketing .agents .claude apps/video \
  docs/issues docs/legal docs/marketing
sudo -H -u openbot git -C "$R" checkout \
  -b marketing/agentes origin/docs/openbot-growth-skills
sudo -H -u openbot git -C "$R" config user.name "OpenBot Team"
sudo -H -u openbot git -C "$R" push -u origin marketing/agentes
# Validação: em $R/apps só deve existir "video" (zero api/web/landing)
sudo ls -la "$R" "$R/apps"
```

### 6.4 Agente #2 — `Fury` (Onda 1B — Ativo ✅)
- **Modelo:** `Claude Opus 5.5` *(via Antigravity)* ou `Gemini 4 Carbon` · **Esforço atual:** `High` *(adequado — baixa frequência, alta decisão)*
- **Repos:** `/var/lib/openbot/workspaces/registoo-check` (`marketing/agentes`) + `/var/lib/openbot/workspaces/brain`
- **Rotinas agendadas (fuso `America/Sao_Paulo`):**
  1. **`Fury — Review Semanal`** — **Segunda às 07:11** (`11 7 * * 1`) *(logo após o Briefing da `Gabs` às 06:01)*
  2. **`Fury — Check-in Mesa de Ideias`** — **Sexta às 16:30** (`30 16 * * 5`)
- **Pendência registrada (v2):** quando fecharmos a integração de agendamento/métricas via MCP (**Zernio** vs. **Postiz** — ver [[2026-11-19-explorar-ferramentas-de-agendamento-de-posts]]), atualizar as instruções do `Fury` para ler métricas direto pela integração em vez de só `marketing/metricas/`.

### 6.5 Agente #3 — `Hill` (Onda 1B — Ativa ✅)
- **Modelo:** `Claude Sonnet 5.5` *(via Antigravity)* ou `Gemini 4 Neon` · **Esforço atual:** `High` *(ponto de revisão: testar baixar para `Medium` se ficar lenta ou gastar muita cota no dia a dia)*
- **Repos:** `/var/lib/openbot/workspaces/registoo-check` (`marketing/agentes`) + `/var/lib/openbot/workspaces/brain`
- **Rotinas:** nenhuma *(100% sob demanda)*

### 6.6 Calibração de Nível de Esforço (Reasoning Effort) — Revisão Pós-Setup
*(Todos iniciados em `High`; revisar após a 1ª semana de uso real para equilibrar velocidade e cota:)*
| Agente | Esforço recomendado na revisão | Motivo |
|---|---|---|
| **`Gabs`** | `Low` / `Medium` | Alta frequência de capturas simples; `High` só adiciona latência e consome cota à toa. |
| **`Fury`** | `High` | Baixa frequência, análise de funil e decisões estratégicas críticas. |
| **`Hill`** | `Medium` *(ou `High` em roteiro hero/YouTube)* | Escrita natural em volume semanal com boa velocidade. |
| **`EDITH`** | `High` | Pesquisa densa, cruzamento de fontes e análise regulatória/jurídica. |
| **`Zoe`** | `High` | Motion via código + Critique Loop visual exigem precisão máxima. |

### 6.7 Próximas ondas *(atualizar este runbook conforme ativarmos)*
- [x] **Onda 1A (`Gabs`):** ativa com 2 rotinas (Dom 19:00 / Seg 06:01).
- [x] **Onda 1B (`Fury` + `Hill`):** ativos no `registoo-check` (`marketing/agentes`) + rotinas do `Fury` (Seg 07:11 / Sex 16:30).
- [ ] **Onda 1C (`EDITH` + `Zoe`):** dependências de sistema do Playwright/Chromium (`npx playwright install-deps chromium`), `apps/video` (`pnpm install`), `.env` de TTS da `Zoe` (`gemini-3.8-flash-tts`), prompts < 2k chars e rotina de quarta da `EDITH`.
- [ ] **Pós-Onda 1C:** usar a `EDITH` para fechar o comparativo **Zernio vs. Postiz** (Free Tier + MCP) e depois plugar nas instruções do `Fury`; revisar o nível de esforço de cada agente.

---

## 7. Checklist de Migração Futura (Azure → VPS Definitiva)

Quando formos sair do Azure para a Hostinger KVM 4 (ou Hetzner / Mini PC):
1. Subir a nova máquina com **Ubuntu 24.04 LTS x64** e executar as **Seções 2 a 5** deste runbook (leva ~15 min).
2. **Atenção aos logins do OpenBot:** credenciais de provedores (Google AI Pro, etc.) **não migram** entre hosts — reconectar pela interface do app no novo servidor.
3. Replicar os agentes e rotinas da **Seção 6** *(todos os blueprints, histórico e skills já vêm automaticamente via `git clone` do Brain e do `registoo-check`)*.
4. Validar 1 captura da `Gabs` + 1 render da `Zoe` no servidor novo antes de desligar o antigo.
5. No Azure, **deletar o Resource Group `rg-obot-piloto` inteiro** (remove VM, disco, IP público e NSG de uma só vez sem deixar nada órfão cobrando) e remover a máquina antiga do painel do Tailscale.
