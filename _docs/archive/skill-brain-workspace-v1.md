---
name: brain-workspace
description: Gerencia o Brain — sistema operacional pessoal de projetos de Gabriel. Captura notas, insights e issues e salva na workspace correta dentro de ~/brain/.
version: 1.0.0
author: Gabriel
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Brain, Workspace, Notes, Projects, Markdown]
    related_skills: []
---

# Brain Workspace

O Brain é o repositório pessoal de conhecimento e projetos de Gabriel, localizado em `~/brain/`.

## Workspaces disponíveis

- `registoo` — PWA de registro de atendimentos domiciliares
- `pictae` — SaaS de galerias de fotos para fotógrafos
- `vox` — app de captura de notas e ideias
- `pessoal` — notas e ideias pessoais
- `trabalho` — trabalho no sistema .NET/SQL Server (empenhos, liquidações, etc)

## Estrutura de cada workspace
~/brain/<workspace>/
├── issues/ ← bugs, problemas, tarefas técnicas
├── insights/ ← aprendizados, descobertas, ideias
└── backlog/ ← funcionalidades e melhorias futuras

## Regras

1. Quando Gabriel mencionar um projeto, identifica a workspace correspondente
2. Classifica o conteúdo: issue, insight ou backlog
3. Cria o arquivo em `~/brain/<workspace>/<tipo>s/<YYYY-MM-DD>-<slug>.md`
4. Sempre faz commit após salvar: `git -C ~/brain add . && git -C ~/brain commit -m "brain: <workspace> - <resumo curto>"`
5. Confirma para Gabriel o que foi salvo e onde

## Frontmatter padrão de cada nota

```markdown
---
date: <YYYY-MM-DD>
workspace: <workspace>
type: <issue|insight|backlog>
tags: []
---
```