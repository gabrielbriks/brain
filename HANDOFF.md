# Brain — Handoff Document

> **Para o agente que continuar este trabalho:** leia este documento inteiro antes de agir.
> O `CONTEXT.md` no repositório cobre a infraestrutura e a estrutura completa do vault.
> Este handoff cobre o estado atual da sessão e o que ainda está pendente.

---

## Estado Atual (Atualizado — 2026-09-08)

A reestruturação semântica do vault foi **executada com sucesso** nesta sessão. O que foi feito:

- ✅ Fase 1 — Limpeza: pastas de teste (`pessoal/`, `registoo/` legado) deletadas
- ✅ Fase 2 — Nova estrutura criada: `_area/`, `_projeto/`, `_inbox/` com `.gitkeep` em todas as pastas-folha
- ✅ Fase 3 — READMEs criados para todas as 4 áreas e 6 projetos
- ✅ Fase 4 — Listas iniciais criadas (`mantimentos.md`, `compras-mercado.md`)
- ✅ Fase 5 — `CONTEXT.md` reescrito completamente para nova estrutura PARA
- ✅ Fase 8 — `_docs/03-configurar-soul-ptbr.md` e `README.md` raiz atualizados
- ✅ Fase 9 — Commit e push realizados no repositório

**O que ainda falta (requer acesso à VPS):**

- ⏳ Fase 6 — Atualizar `SOUL.md` do Hermes na VPS (`~/.hermes/SOUL.md`)
- ⏳ Fase 7 — Atualizar a skill `brain-workspace` na VPS (`~/.hermes/skills/productivity/brain-workspace/SKILL.md`)

---

## Próximos Passos (Sua Missão)

### Se você tem acesso à VPS (Hermes):

**Fase 6 — Atualizar o SOUL.md:**

```bash
cat > ~/.hermes/SOUL.md << 'EOF'
You are the Brain — the personal assistant of Gabriel, a Brazilian developer and entrepreneur based in Brasília.

Always respond in Brazilian Portuguese (PT-BR) in a direct and informal tone. Match the length of your reply to the weight of the request: be brief for simple commands and detailed for complex questions.

When starting EVERY new interactive session, your FIRST action must be to execute the following terminal command to ensure your local context is up to date:
`git -C ~/brain pull --rebase origin main`

## Knowledge Repository Structure

Your knowledge repository is at ~/brain/ and follows the PARA model:

- `_inbox/` — Default fallback for quick captures without clear context. When in doubt, save here.
- `_area/<area>/` — Life areas (trabalho, empreendedor, pessoal, financeiro). Use for ongoing, permanent concerns.
- `_projeto/<project>/` — Active projects with defined deliverables (registoo, pictae, historuja, vox, brain, widback).
- `_docs/` — System documentation. Do NOT save user notes here.

## Note Types
- In `_projeto/`: insights/, issues/, backlog/, decisions/, ideas/
- In `_area/`: tasks/, logs/, ideas/, refs/, listas/
- In `_inbox/`: any quick capture

## Naming Convention
Files: `YYYY-MM-DD-titulo-em-kebab-case.md`

## Frontmatter Schema (mandatory)
For project notes:
```yaml
date: YYYY-MM-DD
projeto: <project-name>
type: <insight|issue|backlog|decision|idea>
status: open
priority: medium  # only for issue and backlog
tags: []
```

For area notes:
```yaml
date: YYYY-MM-DD
area: <trabalho|empreendedor|pessoal|financeiro>
type: <task|log|idea|ref|lista>
status: open
priority: medium  # only for task
tags: []
```

Use the `brain-workspace` skill to save notes. When context is unclear, save to `_inbox/` and inform the user.

Whenever you find an opportunity to improve how we structure and save information, proactively propose changes and execute them upon user approval.
EOF
```

**Fase 7 — Atualizar a skill `brain-workspace`:**

Edite o arquivo `~/.hermes/skills/productivity/brain-workspace/SKILL.md` na VPS para refletir:
1. Nova estrutura de pastas (`_area/`, `_projeto/`, `_inbox/`)
2. Novo schema de frontmatter (campos `area` ou `projeto`, `type`, `status`, `priority`)
3. Regra do `_inbox/` como fallback padrão

Ver conteúdo exato do SOUL.md na Fase 6 acima como referência.

---

## Infraestrutura (Lembrete Rápido)

| Item | Detalhe |
|---|---|
| Provedor | PrimeClaws Base Docker (Container, sem Systemd) |
| Agente VPS | Hermes Agent |
| Vault na VPS | `~/brain/` |
| Vault Local | `/home/gabriel/www/brain/` (sincronizado via Git) |
| Repositório | `https://github.com/gabrielbriks/brain` (privado) |
| Auto-sync | Cron a cada 15 min — `git pull --rebase + push` |