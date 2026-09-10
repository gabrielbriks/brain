---
date: 2026-09-10
type: inbox
tags: [agenda, filtro, ux, gestão, recorrência]
---

# Nova intenção para o projeto Agenda: filtro do próximo dia da semana

**Objetivo**  
Incluir um filtro para o *próximo dia da semana* no projeto digital Agenda, melhorando a UX e ajudando a gestão.

**Motivação**  
- Usuários (incluindo advogados?) precisam de uma melhor experiência ao visualizar/filtrar tarefas do dia seguinte.  
- Gestão precisa de ferramentas para **gerenciar melhor a agenda** na raiz da recorrência.  
- Desafios na **verdade da recorrência** (possivelmente inconsistências ou gaps nos dados recorrentes) devem ser tratados.

**Proposta**  
1. Adicionar filtro UI que permita selecionar "amanhã" (próximo dia da semana).  
2. Garantir que o filtro respeite regras de recorrência (ex.: eventos que se repetem semanalmente, mensalmente).  
3. Testar com casos de borda: feriados, mudança de mês/ano, exceções de recorrência.  
4. Oferecer feedback claro quando nenhum resultado for encontrado (ex.: "nenhum compromisso para amanhã").

**Próximos passos**  
- Conversar com PO/UX para validar necessidade.  
- Criar issue técnica no repositório do Agenda (se existir) ou abrir ticket.  
- Se for um novo módulo, definir estimativa e prioridade no backlog.

---
