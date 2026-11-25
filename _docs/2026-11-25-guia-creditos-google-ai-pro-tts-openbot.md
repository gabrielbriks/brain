---
date: 2026-11-25
tipo: documentation
status: active
tags: [system, openbot, google-ai-pro, creditos, billing, gemini-api, tts, chirp3, privacidade, vps, zoe]
---

# Guia Prático: Resgatar US$ 10/mês do Google AI Pro, Ativar Chirp 3 HD (Zoe) e Isolar no OpenBot

> Passo a passo verificado em **2026-11-25** para preparar a camada de API Paid Tier (sem treino de dados),
> voz comercial PT-BR (`Chirp 3 HD`) e configuração isolada na VPS Hostinger com OpenBot.
>
> Relacionadas: [[2026-11-23-matriz-de-modelos-equipe-agentes-openbot]] · [[2026-11-25-blueprint-zoe-produtora-videos-motion]] · [[2026-11-18-pesquisa-openbot-equipe-de-agentes]].

---

## 1. Resgatar seus US$ 10/mês do Google AI Pro

> **Regra obrigatória:** use **exatamente a mesma Conta Google** da assinatura Google AI Pro em todas as etapas abaixo.

### Passo 1 — Criar/validar conta de faturamento (Prepaid) no Google Cloud
1. Acesse `https://console.cloud.google.com/billing` (ou siga o fluxo de Billing dentro do `https://aistudio.google.com/`).
2. Crie uma conta de faturamento **Prepaid** (pré-paga) vinculada a um cartão.
   - *Observação:* o Google costuma pedir um depósito mínimo inicial (ex.: ~US$ 5) para ativar a conta prepaid, mas **os créditos mensais de US$ 10 do Developer Program são sempre consumidos primeiro**, antes de encostar no saldo pré-pago.
   - **Dica de segurança:** desative recarga automática se houver a opção, para o saldo funcionar como trava física.

### Passo 2 — Ativar o benefício mensal no Google Developer Program
1. Acesse **`https://developers.google.com/program/my-benefits`** (ou `https://me.developers.google.com/benefits`).
2. Faça login com a conta do Google AI Pro (se for o primeiro acesso, complete o perfil básico de dev).
3. Localize o benefício **"$10 monthly Generative AI and Cloud credit"**.
4. Clique em **Select billing account**, escolha a conta de Billing do Passo 1 e marque **"Always use / Auto-apply"** para creditar automaticamente todos os meses *(cada crédito acumula e vale por 12 meses)*.

### Passo 3 — Criar Alerta de Orçamento (Budget Alert) antes de rodar qualquer coisa
1. Em `https://console.cloud.google.com/billing` → menu lateral **Budgets & alerts** → **Create Budget**.
2. Defina o valor mensal de referência em **US$ 9** (ou **US$ 10**).
3. Configure alertas por e-mail em **50%**, **80%** e **100%**.
   *(Importante: o Budget Alert avisa por e-mail, mas não corta chamadas sozinho — manter o acompanhamento nos primeiros dias de teste.)*

### Passo 4 — Vincular o projeto no Google AI Studio e gerar a chave (Paid Tier = sem treino)
1. Acesse `https://aistudio.google.com/` → **API Keys**.
2. Vincule o projeto Google Cloud à conta de Billing onde você aplicou os US$ 10/mês.
3. Confirme que o projeto aparece como **Paid Tier** *(é isso que garante por contrato que seus prompts e dados **não** serão usados para treino de modelos — diferente do Free Tier)*.
4. Gere a chave de API (`GEMINI_API_KEY`) e guarde em local seguro (nunca commitar no Git).

---

## 2. Ativar e testar o Google Cloud TTS (`Chirp 3 HD` PT-BR) para a `Zoe`

1. No **Google Cloud Console** (no mesmo projeto com Billing + US$ 10/mês):
   - Menu **APIs & Services → Library** → procure **Cloud Text-to-Speech API** → clique em **Enable**.
2. Em **APIs & Services → Credentials → Create Credentials → API Key**:
   - Crie uma chave dedicada e, em **API restrictions**, restrinja **somente** à `Cloud Text-to-Speech API` (guarde como `GOOGLE_TTS_API_KEY`).
3. **Teste rápido no terminal (gera um MP3 em segundos para ouvir a qualidade):**

```bash
# Voz feminina PT-BR: pt-BR-Chirp3-HD-Achernar (ou Aoede, Autonoe, Callirrhoe)
# Voz masculina PT-BR: pt-BR-Chirp3-HD-Enceladus (ou Achird, Algenib, Iapetus)

curl -s -X POST \
  "https://texttospeech.googleapis.com/v1/text:synthesize?key=SUA_GOOGLE_TTS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "input": {
      "text": "Sexta-feira às nove da noite e você ainda cobrando evolução da semana inteira no WhatsApp. Existe um jeito mais leve de provar cada atendimento."
    },
    "voice": {
      "languageCode": "pt-BR",
      "name": "pt-BR-Chirp3-HD-Achernar"
    },
    "audioConfig": {
      "audioEncoding": "MP3"
    }
  }' | jq -r '.audioContent' | base64 --decode > teste_zoe_chirp3.mp3
```

- *Nota técnica:* vozes **Chirp 3 HD** não aceitam tags SSML; o ritmo e as pausas vêm da pontuação natural do texto (vírgulas, pontos, reticências).
- *Licença comercial:* **100% liberado** para uso comercial no Registoo (registrar no checklist da issue 114 como `Google Cloud TTS — Chirp 3 HD`).

---

## 3. Como configurar no OpenBot (VPS Hostinger) SEM quebrar o login do Google AI Pro

> **Armadilha conhecida do OpenBot:** se você colar sua `GEMINI_API_KEY` direto no provedor nativo **Gemini**, ela toma prioridade sobre o login do Google AI Pro (Antigravity) e passa a cobrar da API até no uso interativo!

### Arquitetura limpa com 2 provedores independentes no OpenBot

1. **Provedor 1 — `Gemini` nativo (Antigravity / Login Google AI Pro):**
   - Deixe **sem API key** nesse provedor; autentique com sua conta Google AI Pro (pelo fluxo *Connect* do app Windows → VPS).
   - **Uso:** conversas **interativas** com `Gabs`, `Fury`, `Hill`, `EDITH` e `Zoe` (custo zero extra — usa sua assinatura).
2. **Provedor 2 — Endpoint customizado *OpenAI-compatible* (`Gemini Paid API — US$ 10/mês`):**
   - Em **Settings → Providers → Add Custom / OpenAI-compatible Provider**:
     - **Base URL:** `https://generativelanguage.googleapis.com/v1beta/openai/`
     - **API Key:** sua `GEMINI_API_KEY` do Paid Tier (Passo 4)
     - **Modelos recomendados para economizar crédito:** `gemini-3.8-flash` / `gemini-4-hydrogen` *(conferir o ID exato listado no AI Studio na hora de configurar)*.
   - **Uso:**
     - **Rotinas autônomas agendadas 24/7 na VPS** (ex.: revisão semanal da `Gabs`, varredura de quarta da `EDITH`, alerta de sexta do `Fury`), mantendo conformidade com os termos do Google.
     - **Failover** automático caso o Google AI Pro bata algum rate limit pontual.
     - **Futuro Assistente Financeiro/Pessoal (Onda 2)** — Paid Tier garantido sem treino!
3. **Voz da `Zoe` (`GOOGLE_TTS_API_KEY`):**
   - Salvar no `.env` local de `registoo-check/apps/video/.env` (já está no `.gitignore`) para os scripts de narração da `Zoe`.

---

## 4. Checklist rápido de validação (5 minutos após ativar)

- [ ] Conferir em `console.cloud.google.com/billing` → **Credits** que o crédito de **US$ 10** aparece ativo e com *Auto-apply*.
- [ ] Rodar 1 chamada de teste na `GEMINI_API_KEY` (Paid Tier) e 1 no `curl` do `Chirp 3 HD` (`teste_zoe_chirp3.mp3`).
- [ ] No dia seguinte, abrir **Billing → Reports** e confirmar que o custo aparece coberto na linha **Promotions / Credits** (saldo líquido US$ 0,00).
