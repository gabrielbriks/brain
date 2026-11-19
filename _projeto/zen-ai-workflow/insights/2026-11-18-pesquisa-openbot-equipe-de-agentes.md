---
date: 2026-11-18
projeto: zen-ai-workflow
type: insight
status: open
tags: [openbot, agentes, orquestracao, vps, claude, gemini, hermes, registoo, conteudo, pesquisa]
---

# Pesquisa: OpenBot (Nightly Labs) como "equipe de agentes" para tocar os projetos

> Pesquisa feita com Claude Code em 2026-11-18. Próximo passo decidido pelo Gabriel: **teste no Windows** (Fase 0).
> Projeto jovem (~3 meses, v0.7x, release quase diária) — reconferir tudo antes de agir.

## O que é

- **OpenBot** (openbot.run, `nightly-labs/openbot`) — não confundir com o "OpenBot" da CopilotKit.
- Não é um modelo: é um **orquestrador** dos CLIs que já usamos — Claude Code, Gemini CLI, Codex,
  **Hermes**, OpenCode, Ollama, endpoints OpenAI-compatíveis etc.
- Agentes persistentes com nome, instruções e workspace próprio (`~/OpenBot/Agents/<id>` + `~/OpenBot/Shared`).
- Canais compartilhados humano+agente, delegação explícita (um dono por tarefa), handoff entre agentes.
- Skills compartilhadas versionadas + marketplace (Skills, Agents, Apps: Notion, Figma, Linear, Obsidian…).
- Troca de provedor sem perder contexto; fallback automático quando o plano estoura limite.
- **Rotinas**: gatilho por **Schedule** ou **Webhook** (HMAC-SHA256; aceita Standard Webhooks — Resend, Clerk, Svix).
- Mensageria: **Telegram, Discord, Slack, WhatsApp** (WhatsApp via cliente não oficial → risco de bloqueio do número).
- App mobile (iPhone/Android) pareado por QR (`openbot mobile-connect`).

## Servidor próprio (resumo técnico)

- Instalação nativa: Ubuntu **24.04/26.04** + systemd, x86_64/arm64:
  `curl -fsSL https://raw.githubusercontent.com/nightly-labs/openbot/main/scripts/install-server.sh | sudo bash` → `sudo openbot login`.
- Docker: imagem `ghcr.io/nightly-labs/openbot` (amd64/arm64). Obrigatório: `seccomp.json` deles,
  `--shm-size 1g`, `--stop-timeout 60`, volume `/data`. **Fixar versão** (não `:latest`), backup do
  `/data` antes de atualizar — **não existe downgrade** (banco migrado não abre em versão antiga).
- **Não publica portas**; só conexões de saída. Mas login, sinalização (Signal/TURN) e app web
  dependem da nuvem deles. Dá para self-hostear conta+Signal (Cloudflare Workers/D1/R2 + SMTP),
  mas perde app web, Telegram bot, Slack, GitHub App.
- Concorrência por memória: **2 turnos até 5 GiB, 8 até 10 GiB, 16 acima**.

## ⚠️ Riscos que bloqueiam o uso "ingênuo"

1. **Assinatura do Claude**: termos da Anthropic (code.claude.com/docs/en/legal-and-compliance) —
   OAuth de Pro/Max é para uso ordinário do Claude Code e apps nativos; produtos com Agent SDK devem usar
   **API key**. O OpenBot usa sessão do Claude Agent SDK. A própria doc deles classifica agentes
   autônomos/VPS/compartilhados com assinatura como **risco alto**. → **Nunca plugar a conta Max
   principal**; usar `ANTHROPIC_API_KEY` com limite de gasto.
2. **Licença PolyForm Noncommercial 1.0.0**: uso para a startup = comercial → precisa da licença paga
   (Starter, 1 usuário — preço só em Settings → Billing; não publicado).
3. Agentes rodam com **`danger-full-access` + `approvalPolicy: never`**.
4. Registoo tem **dados de saúde (LGPD)** → nenhum agente do OpenBot com credencial de produção/banco.

## Comparação com o stack atual

| Necessidade | Já existe |
|---|---|
| Captura Telegram → Brain | Hermes na PrimeClaws (US$ 9,99, DeepSeek) |
| Tarefas agendadas | Rotinas do Claude Code (`/schedule`) |
| Agente de conteúdo Registoo | `.claude/agents/agente-de-conteudo.md` + skills de marketing + Remotion (PRs #312–#320) |
| Mobile | Claude app + Remote Control |

**Ganho real do OpenBot**: equipe visível multi-modelo (Claude + Gemini + Hermes) num lugar, handoff
entre agentes com aprovação pelo celular, central única. Pelo **Princípio 8** → justifica **piloto**, não migração.

## Servidor recomendado (quando sair do teste local)

- PrimeClaws atual **não serve** (container sem systemd).
- **Hetzner CAX21** (4 vCPU ARM / 8 GB, ~€10,49/mês após reajuste de jun/2026); subir para CAX31 (16 GB)
  se render de Remotion pesar (preço da CAX31 não confirmado).
- Alternativa sem administrar: hosted servers do OpenBot (~€20–25/mês), mas **dormem após 15 min** — ruim para rotinas.

## Plano de piloto

- **Fase 0 — teste no Windows (custo zero, 1 semana)**: app desktop; Claude via API key com limite;
  Gemini CLI. Assinatura do Claude segue só no Claude Code normal.
- **Fase 1 — 3 agentes**:
  1. *Editor de conteúdo Registoo* (Claude/API) — peças da W49 com skills/calendário/template Remotion existentes; prévia → aprovação no celular; nada publica sem gate humano.
  2. *Pesquisador* (Gemini) — concorrentes, jurídico home care → `marketing/` e Brain.
  3. *Métricas* (rotina semanal) — lê `marketing/metricas/`, relatório da F4.
- **Fase 2 (só se a 1 provar valor)**: *coletor de padrões* — leva ADRs/skills/templates do Registoo
  para zen-ai-workflow, DNA Zen Tech, Pictae, Historuja. Hermes pode entrar como agente nativo.
- **Fica fora**: dev principal do Registoo (worktrees, PRs, migrations) — continua no Claude Code.
- **Critério de saída**: se em 2 semanas não economizar horas reais/semana no conteúdo, desliga.

## Rodar no WSL? (verificado na máquina em 2026-11-18)

Máquina: WSL2 Ubuntu **22.04**, systemd ligado, Docker nativo (~8 GB de RAM para o WSL), WSLg ativo.

- **Instalação nativa no WSL**: ❌ não recomendada — o script é documentado só para Ubuntu 24.04/26.04.
- **Docker dentro do WSL**: ✅ caminho viável — a imagem traz o próprio Linux, então o 22.04 do host não importa.
  Aparece como "servidor" na conta e é usado pelo app desktop do Windows ou pelo celular.
- **App desktop**: usar o **instalador Windows** (Windows 10+ x64), não o AppImage via WSLg.
- Cuidados: o WSL desliga quando ocioso/fechado (rotinas param); os 8 GB são divididos com o dev do
  Registoo (→ 2 turnos simultâneos no máximo); ajustar `memory=` e `vmIdleTimeout` no `.wslconfig`
  se for deixar ligado.

## Fontes

- https://openbot.run/ · https://github.com/nightly-labs/openbot
- docs: self-hosted-server.md, docker.md, self-hosting.md, messaging.md, webhooks.md, provider-terms.md
- https://openbot.run/guides/install-openbot-vps
- https://code.claude.com/docs/en/legal-and-compliance
- https://docs.hetzner.com/general/infrastructure-and-availability/price-adjustment/
- https://github.com/c-wenlong/setup-server/issues/157 (avaliação de self-hosting, inviável sem nuvem do fornecedor)
