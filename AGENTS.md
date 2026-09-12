# AGENTS.md — Guia Universal para Agentes IA

> Este arquivo é lido automaticamente por qualquer agente que acesse este vault via MCP `brain-vault` ou diretamente como workspace.
> Siga estas instruções **antes de qualquer ação** de leitura ou escrita.

---

## O que é este repositório

O **Brain** é o sistema operacional pessoal do Gabriel Briks — hub central para capturar ideias, insights, issues, tarefas e registros de todas as áreas de vida e projetos ativos.

Toda escrita aqui deve seguir o padrão estabelecido. Não improvise estrutura, nomenclatura ou frontmatter.

---

## Estrutura do Vault

```text
brain/
│
├── _area/            ← Áreas de vida permanentes
│   ├── trabalho/     ← Trabalho CLT/freelance
│   ├── empreendedor/ ← Gestão dos SaaS pessoais
│   ├── pessoal/      ← Vida pessoal, saúde, família
│   └── financeiro/   ← Controle financeiro e MEI
│
├── _projeto/         ← Projetos ativos com ciclo de vida definido
│   ├── registoo/     ← PWA de atendimentos domiciliares
│   ├── pictae/       ← SaaS de galerias para fotógrafos
│   ├── historuja/    ← SaaS de histórias sociais para neurodivergentes
│   ├── vox/          ← App de captura de notas (futuro)
│   ├── brain/        ← O próprio Brain como produto
│   ├── widback/      ← Feedback/bug reporting SaaS
│   ├── zen-ai-workflow/ ← Metodologia de dev assistido por IA
│   └── dna-zen-tech/ ← Sistema de UI/UX e Design
│
├── _inbox/           ← Captura rápida — fallback padrão quando em dúvida
│
└── _docs/            ← Documentação do sistema Brain
    └── plans/        ← Planos de implementação gerados por agentes
```

---

## Regras de Escrita — OBRIGATÓRIAS

### 1. Naming Convention

Todos os arquivos devem seguir o padrão:
```
YYYY-MM-DD-titulo-em-kebab-case.md
```

### 2. Frontmatter para `_projeto/`

```yaml
---
date: YYYY-MM-DD
projeto: nome-da-pasta  # ex: registoo, pictae, historuja
type: insight           # insight | issue | backlog | decision | idea
status: open            # open | in-progress | done | archived
priority: medium        # low | medium | high | critical (obrigatório para issue e backlog)
tags: []
---
```

### 3. Frontmatter para `_area/`

```yaml
---
date: YYYY-MM-DD
area: trabalho          # trabalho | empreendedor | pessoal | financeiro
type: task              # task | log | idea | ref | lista
status: open            # open | in-progress | done | archived
priority: medium        # low | medium | high | critical (obrigatório para task)
tags: []
---
```

### 4. Frontmatter para `_inbox/`

```yaml
---
date: YYYY-MM-DD
type: inbox
tags: []
---
```

### 5. Frontmatter para `_docs/plans/`

```yaml
---
title: Título do Plano
date: YYYY-MM-DD
status: draft           # draft | approved | completed
tags: [plan]
---
```

---

## Regra do `_inbox/`

**Quando em dúvida sobre onde salvar, use `_inbox/`.** É o fallback padrão para captura rápida. Informe o usuário quando usar o inbox e proponha a classificação correta quando houver contexto suficiente.

---

## Tipos de Nota por Contexto

| Tipo | Pasta | Contexto |
|---|---|---|
| `insight` | `insights/` | `_projeto/` |
| `issue` | `issues/` | `_projeto/` |
| `backlog` | `backlog/` | `_projeto/` |
| `decision` | `decisions/` | `_projeto/` |
| `idea` | `ideas/` | `_area/`, `_projeto/` |
| `task` | `tasks/` | `_area/` |
| `log` | `logs/` | `_area/` |
| `ref` | `refs/` | `_area/trabalho/` |
| `lista` | `listas/` | `_area/pessoal/` |
| `inbox` | `_inbox/` | raiz |

---

## Regras de Git — OBRIGATÓRIAS

Após **qualquer** criação ou edição de arquivo neste vault:

1. `git add` nos arquivos alterados
2. `git commit -m "tipo: mensagem descritiva"`
3. `git push`

**Nunca deixe arquivos criados ou editados sem commit e push.**

Padrão de mensagem de commit:
- `docs: descrição` → para notas, insights, decisões
- `feat: descrição` → para novos tipos de nota ou estrutura
- `fix: descrição` → para correções em arquivos existentes
- `chore: descrição` → para manutenção do vault

---

## Leitura Complementar

- [`README.md`](./README.md) — visão geral do sistema
- [`CONTEXT.md`](./CONTEXT.md) — infraestrutura completa, integrações e histórico
- [`HANDOFF.md`](./HANDOFF.md) — estado atual e próximos passos do roadmap
