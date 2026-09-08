# Brain — Sistema Operacional Pessoal

O **Brain** é o sistema operacional pessoal do Gabriel — hub central para capturar ideias, insights, issues, tarefas e registros de todas as áreas de vida e projetos ativos.

O fluxo é centrado em IA: o usuário fornece input (Telegram, voz, CLI) → o **Hermes Agent** processa, classifica e salva em Markdown estruturado → commit automático no Git.

A estrutura segue o **modelo PARA** (`_area/`, `_projeto/`, `_inbox/`), com organização semântica por contexto de vida e projeto.

---

## Estrutura do Vault

```text
brain/
│
├── _area/            ← Áreas de vida permanentes (trabalho, empreendedor, pessoal, financeiro)
├── _projeto/         ← Projetos ativos com ciclo de vida definido
├── _inbox/           ← Captura rápida sem classificação — fallback padrão
└── _docs/            ← Documentação do sistema Brain
    └── plans/        ← Planos de implementação dos agentes
```

## Áreas de Vida

| Pasta | Descrição |
|---|---|
| `_area/trabalho/` | Trabalho CLT ou freelance (tarefas, logs, refs técnicas) |
| `_area/empreendedor/` | Gestão dos produtos SaaS pessoais |
| `_area/pessoal/` | Vida pessoal, saúde, família, cotidiano |
| `_area/financeiro/` | Controle financeiro pessoal e MEI |

## Projetos Ativos

| Pasta | Descrição |
|---|---|
| `_projeto/registoo/` | PWA de registro de atendimentos domiciliares |
| `_projeto/pictae/` | SaaS de galerias premium para fotógrafos |
| `_projeto/historuja/` | SaaS de histórias sociais para neurodivergentes |
| `_projeto/vox/` | App de captura de notas (planejamento futuro) |
| `_projeto/brain/` | O próprio Brain como produto (Moot) |
| `_projeto/widback/` | Solução de feedback/bugs para apps web |

---

## Planos de Implementação

Todos os planos gerados por agentes IA devem ser salvos em `_docs/plans/` com frontmatter obrigatório:

```yaml
---
title: Título do Plano
date: YYYY-MM-DD
status: draft | approved | completed
tags: [plan, tag1, tag2]
---
```

---

> Para entender a infraestrutura completa, leia [`CONTEXT.md`](./CONTEXT.md).
