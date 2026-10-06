---
date: 2026-10-06
projeto: zenckup
type: insight
status: open
tags: [zen-ai-workflow, adocao, metodologia, tiers]
---

# Adoção do zen-ai-workflow no zenckup (camada essencial)

O zenckup tem ~40 linhas de código, mas mexe com dados de produção e será reusado por três
projetos — um erro se multiplica por três. Isso justifica a **camada essencial** do
zen-ai-workflow v0.1.0 (`AGENTS.md`, `CONTEXT.md`, `HANDOFF.md`, `docs/INDEX.md`) e nada além
(Princípios 4 e 8: sem documentação sem propósito de recuperação, adoção gradual).

## Decisões

- **Camada essencial, não o workflow completo.** Sem pastas de `docs/` pré-criadas, sem ADR/Spec de
  rotina, sem `model-routing`.
- **`MARCO_ZERO.md` migrado para o `CONTEXT.md` e removido** (Princípio 5: nunca duas versões da
  mesma informação). O arquivo era só ponto de partida; arquitetura, decisão "uma instância por
  projeto", stack e fora-do-escopo agora vivem no `CONTEXT.md`.
- **Tiers calibrados para o raio de impacto, não para o tamanho do código:** mudança que altera o
  conteúdo/formato do dump é no mínimo T2; mudança em credenciais, retenção ou na decisão de
  arquitetura é T3; README/comentário é T0.

## Dado para calibrar os tiers (`EXPERIMENT`)

Os tiers do workflow ainda não têm validação empírica. O zenckup é um bom caso: código mínimo, risco
alto. Se o uso mostrar que tudo cai em T1/T2 e nunca em T3, isso é informação para revisar o
sistema — registrar aqui quando acontecer.
