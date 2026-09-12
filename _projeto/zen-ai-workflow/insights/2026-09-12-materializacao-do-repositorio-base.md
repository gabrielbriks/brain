---
date: 2026-09-12
projeto: zen-ai-workflow
type: insight
status: open
tags: [metodologia, marco-zero, materializacao, v0.1.0]
---

# Materialização do repositório-base v0.1.0

O `zen-ai-workflow` nasceu de um processo de investigação (documentado em `docs/` do próprio
repo: `01-marco-zero-analysis.md` até `16-second-review-and-materialization.md`) que comparou como
Gabriel já trabalhava de fato em dois projetos reais contra um modelo teórico ("Frankstain") de
workflow com IA, extraiu convergências e conflitos, e destilou isso em 8 princípios com status de
validação explícito — em vez de se apresentar como metodologia pronta e comprovada.

O commit `66e84d6` ("feat: materializa repositório-base zen-ai-workflow v0.1.0") marca o
repositório como usável pela primeira vez: `README.md`, `PRINCIPLES.md`, `WORKFLOW.md`,
`CHANGELOG.md` e os templates em `templates/` prontos para adoção por qualquer projeto novo ou
existente.

## Por que isso interessa ao Brain

Este projeto define o mecanismo de trabalho com agentes de IA em código — é candidato natural a
ser referenciado a partir do `CONTEXT.md` de qualquer projeto de produto do Gabriel
(Registoo, Pictae, Historuja, Vox, Widback) no momento em que cada um decidir adotar o workflow.
Nenhum desses projetos foi migrado ainda; a adoção é gradual e por decisão individual de cada um
(Princípio 8).

## Pendência levantada nesta sessão

O MCP `brain-vault` (`@modelcontextprotocol/server-filesystem`) está corretamente configurado em
escopo de usuário (`~/.claude.json`, fora de `projects.*`), então já vale para qualquer projeto —
não precisou de nova instalação. O único problema encontrado foi uma sessão do Claude Code com
conexão MCP presa ao path antigo (`zen-ai-workflow` em vez de `brain`), resolvido reiniciando o
processo por completo. Registrado aqui para não repetir o diagnóstico: `/rename` ou `attach` numa
sessão em background **não** reinicia processos MCP filhos já abertos.
