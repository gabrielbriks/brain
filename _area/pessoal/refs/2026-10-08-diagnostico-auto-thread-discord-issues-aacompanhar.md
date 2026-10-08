---
date: 2026-10-08
area: pessoal
type: issue
status: open
priority: medium
tags: [discord, auto-thread, gateway, automatização, bug-known]
---

# Diagnóstico: auto-thread do Discord não cria threads automaticamente no Hermes

**Confidencialidade:** Esta nota documenta um problema de diagnóstico com o Hermes Agent — um assistente pessoal que interage no Discord. O problema é que o recurso de criação automática de threads (auto-thread) não está funcionando como esperado, apesar de configurações aparentemente corretas no arquivo de configuração.

## Configuração atual
```yaml
discord:
  require_mention: false
  free_response_channels: '1555379586114523190'
  auto_thread: true
  free_response_auto_thread: true
```

## Problema relatado
Mesmo com a configuração acima, o Hermes não cria threads automaticamente para mensagens do canal `1555379586114523190`. As mensagens são respondidas diretamente no canal principal, sem organização em threads.

### O que foi verificado
- Configuração do arquivo config.yaml está correta e aplicável
- Gateway Hermes está rodando (PID 88) e conectado ao Discord
- Criação manual de threads via API Discord funciona corretamente
- Mensagens são recebidas e processadas pelo bot

### Root cause analisada
O comportamento esperado é que mensagens sem @mention em canais free_response criem threads automaticamente. Porém, o código do gateway (`gateway/platforms/discord.py`) não está honrando corretamente a configuração de free_response channels na decisão de criar threads.

## Issues do GitHub para acompanhar (atualizado 2026-10-08)

1. **Free-response Discord channels spawn threads** — Issue #12750
   - Link: https://github.com/NousResearch/hermes-agent/issues/12750
   - Status: FIXED por PR #12780 e PR #12811
   - Descrição: Canais free_response não respondiam mais em threads; fixado.

2. **free_response_channels agora honrada corretamente** — Issue #15262
   - Link: https://github.com/NousResearch/hermes-agent/issues/15262
   - Descrição: Depois de fix, free_response channels funcionam corretamente, mas quebra workflows que dependiam do comportamento antigo.

3. **Auto-thread falha e cai para reply inline** — Issue #20243
   - Link: https://github.com/NousResearch/hermes-agent/issues/20243
   - Status: FIXED por PR #20260
   - Descrição: Quando auto-thread cria falha, Hermes cai silenciosamente para reply inline no canal pai.

4. **Bug code-vs-docs: free_response não honrado no skip_thread** — Issue #25310
   - Link: https://github.com/NousResearch/hermes-agent/issues/25310
   - Status: FIXED por PR #25311
   - Descrição: O skip_thread do `_handle_message` só verifica DISCORD_NO_THREAD_CHANNELS, não DISCORD_FREE_RESPONSE_CHANNELS.
   - Fix: adicionar `or is_free_channel` na linha skip_thread.

5. **Fallback de auto-thread cria threads duplicadas** — Issue #73032
   - Link: https://github.com/NousResearch/hermes-agent/issues/73032
   - Descrição: Fallback do seed-message pode criar segundo thread duplicado quando criação direta falha.
   - Fix: PR #83817 reconcilia thread antes de criar fallback.

6. **429 rate limit no auto-thread** — Issue #52422 / PR #76060
   - Link: https://github.com/NousResearch/hermes-agent/pull/76060
   - Descrição: Auto-thread cria falha silenciosamente ao 429 do Discord; fixado com honor a retry_after.

## Workaround adotado
Criação MANUAL de threads sempre que necessário, para garantir que nenhuma informação seja perdida e que cada tópico de conversa fique organizado.

## Canais de acompanhamento
- GitHub: https://github.com/NousResearch/hermes-agent (watch repos / issues listadas acima)
- Canal Discord da comunidade: (verificar canal oficial de suporte do Hermes)

---
*Nota criada em 2026-10-08 por Gabriel — diagnóstico da automação de threads do Discord*