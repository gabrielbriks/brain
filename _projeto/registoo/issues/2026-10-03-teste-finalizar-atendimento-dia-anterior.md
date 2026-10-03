---
date: 2026-10-03
projeto: registoo
type: issue
status: open
priority: medium
tags: [teste, atendimento, profissional, cross-day]
---

## Teste: Finalizar atendimento iniciado no dia anterior

**Cenário:** Um profissional inicia um atendimento no dia N e precisa finalizá-lo no dia N+1.

**Passos:**
1. Login como profissional no registoo
2. Verificar se o atendimento iniciado ontem aparece na lista do dia de hoje
3. Tentar finalizar o atendimento (concluir status)
4. Verificar se o sistema permite a finalização sem erro
5. Confirmar que o atendimento aparece como concluído no histórico

**Resultado esperado:** Profissional consegue finalizar normalmente.
**Resultado real:** ? (preencher após teste)

**Notas:** Testar também o caso de múltiplos dias entre início e fim.
