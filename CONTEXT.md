---
date: 2026-09-08
type: context
tags: [brain, setup, documentação, agente]
---

# Brain — Documento de Contexto para Agentes

Este documento contém tudo que um agente de IA precisa saber para continuar ajudando Gabriel com o Brain.

---

## O que é o Brain

Sistema operacional pessoal de Gabriel — hub central para capturar ideias, insights, issues e notas de todos os projetos, com organização automática por workspace e versionamento Git.

**Conceito:** input (CLI, Telegram, voz) → agente IA processa e classifica → salva em markdown estruturado → commit automático no Git.

---

## Infraestrutura

| Item | Detalhe |
|---|---|
| Hospedagem | PrimeClaws Base Docker ($9.99/mês) |
| Agente | Hermes Agent v0.21.1 (NousResearch) |
| LLM | deepseek-v3.2 (incluso no plano) |
| VPS | Servidor Europa (container Docker) |
| Usuário | container@hermes |

---

## Repositório Git

- **Remoto:** https://github.com/gabrielbriks/brain
- **Local no VPS:** ~/brain/
- **Branch principal:** main
- **Autenticação:** Fine-grained token com acesso só a este repo

---

## Estrutura do Vault
~/brain/
├── CONTEXT.md ← este arquivo
├── README.md ← descrição geral
├── registoo/
│ ├── issues/
│ ├── insights/
│ └── backlog/
├── pictae/
│ ├── issues/
│ └── insights/
├── vox/
│ ├── issues/
│ └── insights/
├── pessoal/
└── trabalho/
└── dotnet/


---

## Workspaces

| Workspace | Projeto |
|---|---|
| `registoo` | PWA de registro de atendimentos domiciliares (terapia infantil) |
| `pictae` | SaaS de galerias de fotos para fotógrafos profissionais |
| `vox` | App de captura de notas e ideias (futuro produto) |
| `pessoal` | Notas e ideias pessoais |
| `trabalho` | Sistema .NET/SQL Server (empenhos, liquidações, Restos a Pagar) |

---

## Tipos de nota

| Tipo | Pasta | Uso |
|---|---|---|
| `insights` | `<workspace>/insights/` | Aprendizados, descobertas, ideias |
| `issues` | `<workspace>/issues/` | Bugs, problemas, tarefas técnicas |
| `backlog` | `<workspace>/backlog/` | Funcionalidades e melhorias futuras |

---

## Skill customizada

- **Nome:** brain-workspace
- **Localização:** ~/.hermes/skills/productivity/brain-workspace/SKILL.md
- **Função:** ensina o Hermes a identificar workspaces e salvar notas no padrão correto
- **Naming convention de arquivos:** `YYYY-MM-DD-<slug>.md`

### Frontmatter padrão
```markdown
---
date: YYYY-MM-DD
workspace: <workspace>
type: <insights|issues|backlog>
tags: []
---
```

---

## Hermes — Comandos úteis

```bash
hermes                          # inicia sessão interativa
hermes skills list              # lista skills instaladas
hermes skills inspect <nome>    # inspeciona uma skill
hermes doctor                   # verifica saúde do sistema
hermes update                   # atualiza o Hermes
```

---

## O que já foi feito

- [x] Vault criado em ~/brain/ com estrutura de workspaces
- [x] Repositório Git inicializado e conectado ao GitHub (privado)
- [x] Skill brain-workspace criada e ativa
- [x] Teste de captura de insight funcionando (commit b269d63)

---

## Pendências (próximos passos)

- [ ] Configurar Telegram como canal de input
- [ ] Cron job de auto-push pro GitHub
- [ ] Configurar SOUL.md para respostas em PT-BR por padrão
- [ ] Corrigir pasta `insight/` → `insights/` (plural) nos commits futuros

---

## Projetos de Gabriel (contexto geral)

Gabriel é desenvolvedor Fullstack pleno e MEI com alguns produtos e projetos:
- **Registoo** — PWA de registro de atendimentos (terapia infantil/saúde)
- **Vox** — Em planejamento (captura de notas, futuro produto)
- **Pictae** — SaaS de galerias premium para fotógrafos
- **Historuja** SaaS de geração de histórias sociais para serem usadas em intervenções com pessoas neurodivergentes (crianças e adultos). 
- **Brain** — Este sistema (uso pessoal + possível produto futuro)
  - **Moot** — Site institucional do Brain (futuro produto)
- **Widback** - (Em planejamento) Uma solução pessoal mas já engatilhada para virar um SaaS, que possibilita o registro de feedbacks e bugs de usuarios em aplicações web. Sendo possivel integra-la em qualquer aplicação web através de um script. (uso pessoal + produto futuro)

---

## Como interagir com o Brain

Para salvar uma nota via CLI:

`hermes`
> Salva no Brain, workspace <workspace>, <tipo>: "<conteúdo>"
