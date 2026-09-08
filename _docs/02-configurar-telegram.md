---
title: Configurar Canal do Telegram
date: 2026-09-08
type: tutorial
tags: [hermes, telegram, bot, canal, infra]
---

# Configurar Telegram como Canal de Input

O Hermes Agent pode receber comandos e informações através de um bot no Telegram. Este tutorial mostra como criar o bot e vinculá-lo ao Hermes rodando na sua VPS.

## 1. Criar o Bot no Telegram

O primeiro passo é criar o bot diretamente pelo aplicativo do Telegram:

1. Busque pelo bot oficial chamado **@BotFather**.
2. Envie o comando `/newbot`.
3. Escolha um **nome** para o bot (ex: `Meu Brain`).
4. Escolha um **username** (precisa terminar com `bot`, ex: `gabriel_brain_bot`).
5. Ao finalizar, o BotFather fornecerá um **Token de Acesso** (parecido com `123456789:ABCdefGHIjkl...`). Guarde este token.

## 2. Configurar o Hermes via Setup Interativo

A integração de mensagens (Telegram, Slack, etc.) acontece através do módulo **Gateway** do Hermes.
Acesse o terminal da sua VPS (onde o Hermes está rodando) e execute o assistente de configuração:

```bash
hermes gateway setup
```
1. Selecione **Telegram** quando solicitado.
2. O assistente pedirá o **Bot Token** (que você pegou no passo anterior).
3. O assistente pedirá também o seu **User ID** do Telegram (para garantir que só você tenha acesso ao seu Brain). *Dica: você pode descobrir seu User ID mandando uma mensagem para o bot `@userinfobot` no Telegram.*

O setup vai preencher automaticamente o arquivo `~/.hermes/.env` com as variáveis corretas (`TELEGRAM_BOT_TOKEN` e `TELEGRAM_ALLOWED_USERS`).

## 3. Iniciar o Gateway

Ainda no terminal da VPS, ative o gateway do Hermes com o comando:

```bash
hermes gateway
```

*(Nota: Você pode querer rodar este comando em background usando `nohup`, `tmux`, `screen` ou configurando um serviço do `systemd` para que o bot continue rodando mesmo após você fechar o console da VPS).*
## 4. Testar o Funcionamento

Assim que ativado, o bot já deve estar ouvindo.
Vá no Telegram, abra a conversa com o seu novo bot e faça um teste enviando um comando de texto:

> *"Salvar no Brain, workspace pessoal, insights: Esta é uma nota de teste via Telegram."*

Você também pode testar o envio de **mensagens de voz (áudio)**, já que versões recentes do Hermes oferecem suporte a transcrição de voz (STT).
