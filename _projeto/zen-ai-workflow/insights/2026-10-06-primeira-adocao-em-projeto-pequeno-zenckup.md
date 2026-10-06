---
date: 2026-10-06
projeto: zen-ai-workflow
type: insight
status: open
tags: [adocao, zenckup, tiers, calibragem]
---

# Primeira adoção em projeto pequeno: zenckup

Primeiro projeto a adotar o workflow v0.1.0 depois da materialização do repositório-base
(ver `2026-09-12-materializacao-do-repositorio-base.md`). Detalhes da adoção em
`_projeto/zenckup/insights/2026-10-06-adocao-do-zen-ai-workflow.md`.

## O que este caso ensina

- **A camada essencial basta para um projeto minúsculo.** Os 4 arquivos (`AGENTS.md`, `CONTEXT.md`,
  `HANDOFF.md`, `docs/INDEX.md`) cobrem o necessário; nenhuma pasta de `docs/` foi pré-criada.
- **O tier deve acompanhar o raio de impacto, não o tamanho do diff.** Uma flag de uma linha no
  `pg_dump` muda o contrato de restore de três projetos. O `AGENTS.md` do zenckup ganhou uma seção
  de calibragem explícita por isso — candidato a virar orientação no `WORKFLOW.md`/template se
  aparecer em outros projetos.
- **Migração de documento de partida:** o `MARCO_ZERO.md` virou `CONTEXT.md` + remoção do original,
  aplicando o Princípio 5 sem fricção.

## Em aberto

Acompanhar quais tiers o zenckup realmente usa nas próximas tarefas para alimentar a calibragem
(os tiers continuam `EXPERIMENT`).
