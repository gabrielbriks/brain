---
title: Ideias de Integração — iOS Shortcuts + Brain OS
date: 2026-09-08
type: roadmap
tags: [ios, shortcuts, automação, telegram, ideias]
---

# Integração: iOS Shortcuts e Brain OS

O aplicativo **Atalhos (Shortcuts)** do iOS é uma ferramenta poderosa para criar mecanismos de "Atrito Zero" na captura de notas para o Brain OS. 

Como o nosso sistema usa um bot do Telegram como Gateway de entrada para o Hermes, podemos usar o Atalhos para fazer requisições web diretas para a API do Telegram, ignorando a necessidade de abrir o aplicativo de mensagens.

Aqui estão três ideias mapeadas para implementação futura:

## 1. Captura por Voz (Action Button / Back Tap) 🎙️

**A Experiência:**
Apertar o Action Button (ou dar dois toques na traseira do iPhone) > Falar a ideia > O texto vai direto para o `_inbox/`.

**Como funciona no Atalhos:**
1. Ação: *Ditar Texto* (abre o microfone automaticamente).
2. Ação: *Obter Conteúdo de URL* (faz um POST silencioso para a API do Telegram enviando o texto ditado).
3. Ação: *Mostrar Notificação* ("Enviado para o Brain 🧠").

## 2. "Share to Brain" (Extensão de Compartilhamento) 🔗

**A Experiência:**
Ler um artigo no Safari ou ver um post > Clicar em Compartilhar > Clicar em "🧠 Enviar pro Brain".

**Como funciona no Atalhos:**
1. O atalho é configurado para aparecer na "Planilha de Compartilhamento" aceitando URLs e Texto.
2. Ele pega o Título da página e a URL.
3. Formata como: `"Guarde essa referência: [Título] - [URL]"`.
4. Envia via POST para o Telegram. O Hermes classifica (geralmente como `ref` ou joga no `_inbox/`).

## 3. Widget de Captura Focada (Tela de Bloqueio) 📝

**A Experiência:**
Clicar em um widget na tela de bloqueio > Abre uma caixa de texto simples > Digita > Envia. O objetivo é evitar abrir o WhatsApp/Telegram e se distrair com notificações de outras pessoas.

**Como funciona no Atalhos:**
1. Ação: *Solicitar Entrada* (abre um prompt de texto nativo do iOS).
2. Ação: Envia o texto digitado via POST para o Telegram.

---

## 🛠️ Guia Técnico (Rascunho de Implementação)

Quando formos implementar qualquer uma das ideias acima, o "motor" por trás da comunicação no Atalhos do iOS será sempre a ação **Obter Conteúdo de URL**.

A configuração será:
- **URL:** `https://api.telegram.org/bot<SEU_TOKEN_DO_TELEGRAM>/sendMessage`
- **Método:** `POST`
- **Cabeçalhos:** `Content-Type: application/json`
- **Corpo do Pedido (JSON):**
  ```json
  {
    "chat_id": "<SEU_CHAT_ID>",
    "text": "<Texto vindo do Atalho>"
  }
  ```

*Nota: Quando for criar, basta pegar o Token do Bot (com o BotFather) e o seu Chat ID pessoal e preencher.*
