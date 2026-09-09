---
date: 2026-09-08
projeto: brain
type: idea
status: open
tags: [ios, shortcuts, captura, mobile, atrito-zero]
---

# Feature: Integração Nativa com iOS (Shortcuts)

**Problema:** Hoje o usuário (eu) precisa abrir o Telegram, ir na conversa do Bot e digitar/falar. Existe um atrito cognitivo e distração de outras mensagens no processo.
**Objetivo:** Chegar ao estado de "Atrito Zero" absoluto na captura de notas usando os recursos nativos do sistema operacional mobile (iOS).

## Soluções propostas (MVPs)

1. **Botão de Pânico (Voz):** 
   - Usar o Action Button ou Back Tap do iPhone para acionar o microfone, ditar a nota e enviar em background para a API do Telegram do Hermes. Sem abrir tela nenhuma.
2. **Share to Brain (Extensão Safari/Sistema):** 
   - No menu de compartilhar nativo da Apple, ter um botão "🧠 Brain" que pega o link atual, formata, e manda como Referência ou Inbox.
3. **Widget Lock Screen:**
   - Botão simples na tela de bloqueio que abre só um campo de texto, envia pra API e fecha. Sem distrações do WhatsApp/Telegram.

## Considerações Técnicas
A base técnica já foi rascunhada. A implementação vai depender de requisições `POST` do app nativo Atalhos (Shortcuts) para o endpoint `https://api.telegram.org/bot<TOKEN>/sendMessage`.

> 📄 **Nota:** O passo a passo técnico inicial já está documentado em `_docs/07-integracao-ios-shortcuts.md` para facilitar quando essa feature for puxada para desenvolvimento.
