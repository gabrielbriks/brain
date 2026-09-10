---
date: 2026-09-10
projeto: registoo
type: backlog
status: open
priority: medium
tags: [agenda, filtro, dias-semana, gestao, administracao, recorrencia]
---

# Novo filtro de dias da semana para a tela de Agenda do registoo

**Objetivo**  
Implementar um novo filtro de dias da semana na tela de Agenda, focado na aba "agendamento recorrentes", para ajudar gestores e administradores a filtrar os registros de forma mais eficiente.

**Contexto**  
A tela Agenda do registoo possui uma aba dedicada a agendamentos recorrentes. Gestores e administradores precisam de uma maneira rápida de visualizar e filtrar esses agendamentos por dia da semana, tornando a gestão mais ágil e precisa.

**Recursos Esperados**
- Filtro dropdown/selector de dias da semana (segunda, terça, ..., domingo)
- Filtro combinável com outros filtros existentes na tela
- Resultado atualizado em tempo real conforme o dia é selecionado
- Indicador visual do dia atualmente selecionado
- Opção de limpar o filtro (mostrar todos os dias)

**Critérios de Aceitação**
- Filtro deve aparecer na aba "agendamento recorrentes" da tela Agenda
- Ao selecionar um dia, apenas os agendamentos recorrentes daquele dia devem ser exibidos
- O filtro deve respeitar as regras de recorrência dos agendamentos (ex.: agendamentos que ocorrem toda sexta)
- Deve haver feedback visual quando nenhum registro for encontrado para o dia selecionado
- Filtro deve ser responsivo e acessível

**Tarefas Técnicas**
1. Criar componente de selector de dias da semana
2. Integrar com o estado atual da tela Agenda
3. Atualizar query de agendamentos recorrentes para filtrar por dia
4. Testar com dados de recorrência semanal, quinzenal, mensal
5. Testar casos de borda: feriados, exceções de recorrência, agendamentos sem dia fixo
6. Validar com gestores e administradores

**Dependências**
- API de consulta de agendamentos recorrentes
- Dados de recorrência consolidados no banco
- Design system do registoo para componentes de UI

**Prioridade**
- Média — melhoria significativa na UX para gestores, mas não bloqueia funcionalidades principais

**Estimativa**
- 5 dias de desenvolvimento (incluindo testes e ajustes)

**Observações**
- Considerar adicionar atalho de teclado para alternar entre dias
- Avaliar se o filtro deve ser persistido (lembrar última seleção do usuário)

---
