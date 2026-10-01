---
title: Configurar Canal do Discord
date: 2026-10-01
type: tutorial
tags: [hermes, discord, bot, gateway, multi-canal, infra]
---

# Configurar Discord como Canal de Input (em paralelo ao Telegram)

O Hermes Gateway suporta múltiplos canais simultaneamente. Esta configuração adiciona o Discord como segundo canal de input/output, mantendo o Telegram funcionando normalmente.

## Pré-requisitos

- Telegram já configurado e funcional (via `_docs/02-configurar-telegram.md`)
- Gateway rodando no Startup Command da PrimeClaws (`hermes gateway run`)
- Acesso ao [Discord Developer Portal](https://discord.com/developers/applications)

---

## 1. Criar o Bot no Discord Developer Portal

1. Acesse [discord.com/developers/applications](https://discord.com/developers/applications)
2. Clique em **New Application** → dê um nome (ex: `Brain`)
3. Vá na aba **Bot** (menu lateral)
4. Clique em **Reset Token** → copie o **Bot Token** gerado
5. Ainda na aba Bot, ative as seguintes **Privileged Gateway Intents**:
   - ✅ `Message Content Intent`
   - ✅ `Server Members Intent` (opcional, mas recomendado)
6. Vá em **OAuth2 → URL Generator**:
   - Scopes: `bot`
   - Bot Permissions: `Send Messages`, `Read Message History`, `Add Reactions`
7. Copie a URL gerada e cole no navegador para **adicionar o bot ao seu servidor Discord**

---

## 2. Pegar o seu User ID no Discord

Você precisa do seu User ID para restringir o acesso ao bot (só você pode interagir com ele):

1. No Discord, vá em **Configurações → Avançado** e ative o **Modo Desenvolvedor**
2. Clique com o botão direito no seu nome de usuário → **Copiar ID**

---

## 3. Configurar o Gateway via Setup Interativo

Na VPS (via terminal da PrimeClaws):

```bash
hermes gateway setup
```

1. Selecione **Discord** quando solicitado
2. Informe o **Bot Token** copiado no passo 1
3. Informe o seu **User ID** do Discord

O setup vai popular `~/.hermes/.env` com as variáveis `DISCORD_BOT_TOKEN` e `DISCORD_ALLOWED_USERS` — sem apagar as variáveis do Telegram já existentes.

---

## 4. Configurações Opcionais (config.yaml)

Para controlar o comportamento do bot no Discord, adicione ao `~/.hermes/config.yaml`:

```yaml
discord:
  require_mention: true           # Bot só responde se você marcar ele com @Brain
  free_response_channels: ""      # IDs de canais onde ele responde sem @mention (separados por vírgula)
  auto_thread: true               # Cria thread automática a cada @mention em canais
  free_response_auto_thread: false
```

> **Dica:** Se você quiser que o bot responda livremente em um canal específico (ex: `#brain-pessoal`), coloque o ID desse canal em `free_response_channels`.

---

## 5. Reiniciar o Gateway

Como o Startup Command da PrimeClaws já está configurado como `hermes gateway run`, basta **reiniciar o container** pelo dashboard para que o Discord suba junto com o Telegram.

Se quiser validar manualmente sem reiniciar:

```bash
# Conecte ao terminal da PrimeClaws e rode dentro de uma sessão tmux:
tmux new -s hermes-discord
hermes gateway run
# Ctrl+B → D para sair sem matar o processo
```

---

## 6. Testar o Funcionamento

No Discord, no canal configurado, mencione o bot:

> `@Brain Salvar no Brain, área dev, insight: testando canal do Discord.`

O Hermes deve processar a mensagem exatamente como faria pelo Telegram.

---

## Como funciona por baixo (Multi-canal)

O Hermes Gateway roda **um único processo** que escuta todos os canais configurados simultaneamente. Tanto o Telegram quanto o Discord vão responder ao mesmo Hermes, com o mesmo contexto, as mesmas skills e o mesmo vault `~/brain/`.

```
Telegram ──┐
            ├──► hermes gateway run ──► Hermes Agent ──► ~/brain/
Discord  ──┘
```

Não há conflito — cada mensagem chega identificada com o canal de origem e é processada de forma independente.

---

## Referências

- `_docs/02-configurar-telegram.md` — como o canal do Telegram foi configurado
- `_docs/04-servico-background-gateway.md` — como manter o gateway em background na PrimeClaws
