---
date: 2026-10-14
projeto: pictae
type: insight
status: in-progress
tags: [zen-ai-workflow, adocao, documentacao, claude-code, git-flow]
---

# Adoção do zen-ai-workflow v0.2.0 no Pictae

Primeira vez que o Pictae foi trabalhado com o Claude Code (até aqui, só Gemini CLI/Antigravity).
A adoção seguiu o plan-039 (T2), executado entre 2026-10-13 e 2026-10-14, e está no **PR #43**
(`docs/plan-039-adocao-zen-ai-workflow` → `develop`), aguardando revisão.

## O que mudou no repositório

- **Camada obrigatória criada:** `AGENTS.md` (índice fino), `CONTEXT.md` (estado estrutural
  conferido contra os `package.json`) e `HANDOFF.md` na raiz, com o bloco "Estado Atual". O
  handoff antigo, de 57 KB, virou a entrada mais antiga do histórico.
- **`docs/INDEX.md` retroativo**, com as colisões herdadas registradas sem renumerar
  (`plan-004` ×3, `plan-008` ×3, ADR 003 ×3, `issues/001` ×4). Próximos números livres: ADR 016,
  Spec/Plan 040 e Issue 010.
- **Ponte para o Claude Code:** `CLAUDE.md` contendo só `@AGENTS.md`, e o symlink
  `.claude/skills → .agents/skills` para as duas ferramentas lerem as mesmas skills do TanStack.
- **Removidas cinco fontes de instrução que se contradiziam:** `GEMINI.md`, `agent-identity`,
  `explanation`, os morais-guides e uma parte duplicada das regras. A contradição mais grave:
  elas proibiam Next.js, mas a landing roda Next.js 16. A proibição agora vale só para
  `apps/web`.
- **`docs/_issues/` virou `docs/issues/`.**
- **Tier calibrado pelo raio de impacto:** billing, isolamento entre estúdios, sessão e magic link
  do cliente, proteção da galeria e limpeza de fotos contam como T3 mesmo com diff de uma linha.
- **Commits em português** a partir de agora (regra de ouro 7 do `AGENTS.md`).

## Fluxo de branches

Foi criada a `develop` a partir da `main`. Ela substitui a `staging`, seguindo o fluxo do Registoo:
`feature → develop → main`. A `staging` não tinha nenhum commit exclusivo.

## Pendências

- [ ] Revisar e mergear o PR #43.
- [ ] **Issue 009:** CI e CD de homologação ainda disparam em `staging`, então PRs para `develop`
      não rodam CI. Inclui trocar a branch do serviço `pictae-api-staging` no painel do Render,
      conferir o domínio de staging na Vercel e apagar a `staging` depois do primeiro deploy pela
      `develop`.
- [ ] Abrir uma sessão nova do Claude Code e conferir:
  - se o `/memory` mostra o `AGENTS.md`;
  - se as skills aninhadas do TanStack aparecem pelo symlink.

Aprendizados para o próprio workflow:
`_projeto/zen-ai-workflow/insights/2026-10-14-adocao-em-projeto-legado-pictae.md`.
