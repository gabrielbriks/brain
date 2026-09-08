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

## 2. Configurar o Token na VPS

Acesse o terminal da sua VPS (onde o Hermes está rodando) e adicione o token como uma variável de ambiente para o Hermes.

```bash
# Crie ou adicione ao arquivo .env do Hermes
echo 'TELEGRAM_BOT_TOKEN="SEU_TOKEN_AQUI"' >> ~/.hermes/.env
```
*(Não esqueça de substituir o `SEU_TOKEN_AQUI` pelo token real fornecido pelo BotFather).*

## 3. Ativar o Canal no Hermes

Ainda no terminal da VPS, ative o canal do Telegram com o comando:

```bash
hermes channel telegram
```

> **Aviso de Dependência:** O Hermes utiliza a biblioteca `python-telegram-bot` por baixo dos panos. Se o comando acima retornar um erro de "módulo não encontrado", instale a dependência manualmente rodando `pip install python-telegram-bot` e tente novamente.

## 4. Testar o Funcionamento

Assim que ativado, o bot já deve estar ouvindo.
Vá no Telegram, abra a conversa com o seu novo bot e faça um teste enviando um comando de texto:

> *"Salvar no Brain, workspace pessoal, insights: Esta é uma nota de teste via Telegram."*

Você também pode testar o envio de **mensagens de voz (áudio)**, já que versões recentes do Hermes oferecem suporte a transcrição de voz (STT).
