# Brain - Sistema Operacional Pessoal

O **Brain** é um sistema operacional pessoal e um hub central projetado para capturar ideias, insights, problemas (issues) e notas referentes a vários projetos e facetas da vida (como Registoo, Pictae, Vox, Historuja, Moot, Widback, anotações pessoais e do trabalho).

O fluxo de funcionamento é centrado em Inteligência Artificial: o usuário fornece o input (via CLI, Telegram ou voz) e o **Hermes Agent** processa esse conteúdo, formata-o como Markdown padronizado, organiza na pasta do workspace (projeto) correto e realiza o commit automático no repositório Git usando uma skill customizada (`brain-workspace`).

A infraestrutura é hospedada em um container VPS rodando o Hermes Agent alimentado por um LLM (`deepseek-v3.2`).

## Planos de Implementação

Todos os planos de implementação e reestruturação gerados por agentes IA para o Brain devem ser salvos no diretório `_docs/plans/`.
Cada plano deve incluir, obrigatoriamente, um Frontmatter com data, status e tags.

**Formato exigido:**
```yaml
---
title: Título do Plano
date: YYYY-MM-DD
status: draft | approved | completed
tags: [plan, tag1, tag2]
---
```

## Estrutura do Vault

As notas e documentos são armazenados e organizados de forma automática em repositórios categorizados por workspace. A estrutura básica de pastas funciona da seguinte maneira:

```text
brain/
├── CONTEXT.md
├── README.md
├── <workspace>/
│   ├── insights/
│   ├── issues/
│   └── backlog/
```

- **Insights**: Aprendizados, descobertas, ideias e notas em geral.
- **Issues**: Bugs, problemas e tarefas técnicas.
- **Backlog**: Funcionalidades e melhorias futuras planejadas para o projeto.

## Workspaces Ativos

- `registoo`: PWA de registro de atendimentos domiciliares (terapia infantil).
- `pictae`: SaaS de galerias de fotos para fotógrafos profissionais.
- `vox`: App de captura de notas e ideias (futuro produto).
- `pessoal`: Notas e ideias pessoais.
- `trabalho`: Sistema .NET/SQL Server corporativo.
