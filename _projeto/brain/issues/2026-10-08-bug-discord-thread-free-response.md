---
date: 2026-10-08
projeto: brain
type: issue
status: open
priority: medium
tags: [hermes, discord, bug, gateway]
---

# Bug: Hermes não cria threads automáticas em free_response_channels

**Descrição do Problema:**
No canal do Discord configurado como `free_response_channels`, o Hermes responde normalmente sem necessidade de menção (conforme esperado). No entanto, mesmo com a configuração `free_response_auto_thread: true`, o bot não cria a thread (tópico) automaticamente para empacotar a conversa, respondendo apenas diretamente no canal principal.

**Configuração atual (config.yaml):**
```yaml
discord:
  require_mention: true
  free_response_channels: '1555379586114523190'
  auto_thread: true
  free_response_auto_thread: true
```

**Contexto e Comportamento Anterior:**
Quando a configuração de menção estava ativa (o usuário marcava `@zmoot`), o bot criava as threads normalmente (`auto_thread: true` funciona). O bug é isolado ao comportamento "free response".

**Causa Provável:**
Possível bug ou limitação na versão atual do `Hermes Agent v0.21.1`. O Gateway provavelmente está verificando apenas a presença de menções (tags) na mensagem para acionar o gatilho de criação de thread, ignorando a flag `free_response_auto_thread`.

**Próximos Passos:**
- Verificar o código fonte do módulo Discord no Hermes Gateway para validar como o gatilho de threads é disparado.
- Caso confirmado o bug, abrir issue/PR no repositório oficial do Hermes ou aguardar correção em versão futura.
- *Workaround atual:* Aceitar as respostas no canal principal, ou mencionar o bot manualmente quando quiser forçar a criação da thread.
