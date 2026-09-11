---
date: 2026-09-08
type: context
tags: [brain, setup, documentação, agente]
---

# Brain — Documento de Contexto para Agentes

> Leia este documento inteiro antes de qualquer ação. Ele é a bíblia do sistema.

---

## O que é o Brain

Sistema operacional pessoal de Gabriel — hub central para capturar ideias, insights, issues, tarefas e registros de todas as áreas de vida e projetos, com organização semântica baseada no modelo PARA e versionamento Git automático.

**Fluxo:** input (Telegram, voz, CLI) → Hermes processa e classifica → salva em Markdown estruturado → commit automático no Git.

---

## Infraestrutura

| Item | Detalhe |
|---|---|
| Hospedagem | PrimeClaws Base Docker ($9.99/mês) |
| Agente VPS | Hermes Agent v0.21.1 (NousResearch) |
| LLM | deepseek-v3.2 (incluso no plano) |
| VPS | Servidor Europa (container Docker) |
| Usuário | container@hermes |

> [!WARNING]
> **Limitação do ambiente:** A infraestrutura na PrimeClaws é um **Container Docker sem Systemd**. Não use `systemctl`. Para processos em background, use `tmux`, `screen`, `nohup` ou configure via **Startup Command** no dashboard da PrimeClaws.

---

## Repositório Git

| Item | Detalhe |
|---|---|
| Remoto | https://github.com/gabrielbriks/brain (privado) |
| Local na VPS | `~/brain/` |
| Local na máquina | `/home/gabriel/www/brain/` |
| Branch principal | `main` |
| Autenticação | Fine-grained token com acesso só a este repo |
| Auto-sync | Cron na VPS: `git pull --rebase + push` a cada 15 min |

---

## Nova Estrutura do Vault (Modelo PARA)

```text
brain/
│
├── _area/                        ← ÁREAS DE VIDA (contextos permanentes)
│   ├── trabalho/                 ← Trabalho CLT/freelance (genérico, não fixo em empresa)
│   │   ├── README.md
│   │   ├── tasks/
│   │   ├── logs/
│   │   └── refs/
│   ├── empreendedor/             ← Gestão dos produtos SaaS pessoais
│   │   ├── README.md
│   │   ├── ideas/
│   │   ├── tasks/
│   │   └── logs/
│   ├── pessoal/                  ← Vida pessoal, saúde, família, cotidiano
│   │   ├── README.md
│   │   ├── logs/
│   │   └── listas/
│   │       ├── compras-mercado.md
│   │       └── mantimentos.md
│   └── financeiro/               ← Controle financeiro pessoal e MEI
│       ├── README.md
│       └── logs/
│
├── _projeto/                     ← PROJETOS ATIVOS (ciclo de vida definido)
│   ├── dna-zen-tech/             ← Sistema transversal de UI/UX & Skill de Design
│   ├── registoo/                 ← PWA de registro de atendimentos domiciliares
│   ├── pictae/                   ← SaaS de galerias premium para fotógrafos
│   ├── historuja/                ← SaaS de histórias sociais para neurodivergentes
│   ├── vox/                      ← App de captura de notas (planejamento futuro)
│   ├── brain/                    ← O próprio Brain como produto (Moot)
│   └── widback/                  ← Solução de feedback/bugs para apps web
│
├── _inbox/                       ← CAIXA DE ENTRADA — captura rápida, sem classificação
│
└── _docs/                        ← Documentação do sistema Brain (não salvar notas aqui)
    ├── plans/                    ← Planos de implementação dos agentes
    └── 01..05-*.md               ← Tutoriais de infraestrutura
```

---

## Áreas de Vida do Gabriel

| Área | Pasta | Descrição |
|---|---|---|
| Trabalho | `_area/trabalho/` | Trabalho CLT/freelance (atualmente Implanta — .NET/SQL Server) |
| Empreendedor | `_area/empreendedor/` | Gestão dos produtos SaaS e MEI |
| Pessoal | `_area/pessoal/` | Vida pessoal, saúde, família, cotidiano |
| Financeiro | `_area/financeiro/` | Controle financeiro pessoal e como MEI |

---

## Projetos Ativos do Gabriel

| Projeto | Pasta | Status | Descrição |
|---|---|---|---|
| DNA Zen Tech | `_projeto/dna-zen-tech/` | Ativo | Sistema transversal de UI/UX & Skill de Design |
| Registoo | `_projeto/registoo/` | Ativo | PWA de registro de atendimentos domiciliares |
| Pictae | `_projeto/pictae/` | Ativo | SaaS de galerias premium para fotógrafos |
| Historuja | `_projeto/historuja/` | Ativo | SaaS de histórias sociais para neurodivergentes |
| Vox | `_projeto/vox/` | Planejamento | App de captura de notas por voz/texto |
| Brain | `_projeto/brain/` | Ativo | Este sistema — codinome Moot |
| Widback | `_projeto/widback/` | Planejamento | Feedback/bug reporting SaaS para apps web |

---

## Tipos de Nota e Schema de Frontmatter

### Tipos por pasta

| Tipo | Pasta | Uso | Contexto |
|---|---|---|---|
| `insight` | `insights/` | Aprendizados, descobertas, "aha moments" | `_projeto/` |
| `issue` | `issues/` | Bug, problema, obstáculo técnico | `_projeto/` |
| `backlog` | `backlog/` | Features e melhorias futuras | `_projeto/` |
| `decision` | `decisions/` | Decisões técnicas ou de produto (ADR) | `_projeto/` |
| `idea` | `ideas/` | Ideias brutas sem contexto suficiente | `_area/`, `_projeto/` |
| `task` | `tasks/` | Tarefa concreta com prazo e/ou prioridade | `_area/` |
| `log` | `logs/` | Diário de bordo: reuniões, eventos, decisões | `_area/` |
| `ref` | `refs/` | Referências, links, materiais de estudo | `_area/trabalho/` |
| `lista` | `listas/` | Listas recorrentes (compras, mantimentos) | `_area/pessoal/` |
| `inbox` | `_inbox/` | Captura rápida, sem classificação | Raiz |

### Frontmatter para `_projeto/`
```yaml
---
date: YYYY-MM-DD
projeto: registoo         # nome da pasta do projeto
type: insight             # insight | issue | backlog | decision | idea
status: open              # open | in-progress | done | archived
priority: medium          # low | medium | high | critical (obrigatório só para issue e backlog)
tags: []
---
```

### Frontmatter para `_area/`
```yaml
---
date: YYYY-MM-DD
area: pessoal             # trabalho | empreendedor | pessoal | financeiro
type: task                # task | log | idea | ref | lista
status: open              # open | in-progress | done | archived
priority: medium          # low | medium | high | critical (obrigatório só para task)
tags: []
---
```

### Frontmatter para `_inbox/` (mínimo)
```yaml
---
date: YYYY-MM-DD
type: inbox
tags: []
---
```

### Naming convention
`YYYY-MM-DD-titulo-em-kebab-case.md`

---

## Regra do `_inbox/`

**Quando em dúvida, salve em `_inbox/`.** É o fallback padrão para captura rápida sem contexto claro. O Hermes deve informar o usuário quando salvar algo no inbox e propor a classificação correta quando houver mais contexto.

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

## Skill `brain-workspace` (Hermes)

| Item | Detalhe |
|---|---|
| Localização | `~/.hermes/skills/productivity/brain-workspace/SKILL.md` na VPS |
| Função | Ensina o Hermes a identificar áreas/projetos e salvar notas no padrão correto |
| Atenção | Este arquivo **não está no repositório Git** — fica apenas na VPS |

---

## Ferramentas Locais (Máquina do Gabriel)

O MCP `brain-vault` (`@modelcontextprotocol/server-filesystem`) está configurado globalmente para:
- **Antigravity IDE** (`~/www/brain/` como workspace)
- **Antigravity CLI (`agy`)** 
- **Claude Code** (extensão VS Code + CLI via `openclaude`)

Isso permite que qualquer agente local leia e escreva diretamente no vault sem precisar do Hermes.

---

## Hermes — Comandos Úteis

```bash
hermes                          # inicia sessão interativa
hermes skills list              # lista skills instaladas
hermes skills inspect <nome>    # inspeciona uma skill
hermes doctor                   # verifica saúde do sistema
hermes update                   # atualiza o Hermes
```

---

## O que já foi feito

- [x] Vault criado com estrutura PARA (`_area/`, `_projeto/`, `_inbox/`)
- [x] Repositório Git no GitHub (privado): `gabrielbriks/brain`
- [x] Auto-sync Git via cron na VPS (pull --rebase + push a cada 15 min)
- [x] Integração com Telegram configurada via Gateway
- [x] SOUL.md do Hermes ajustado para PT-BR e nova estrutura
- [x] Skill `brain-workspace` atualizada para nova estrutura
- [x] MCP `brain-vault` configurado localmente no Antigravity IDE, `agy` e Claude Code

## Pendências / Próximos Passos

- [ ] **Weekly Review automatizado:** Cron na VPS (toda sexta) que lista notas `status: open`, gera report e envia via Telegram
- [ ] **Busca semântica:** MCP com embeddings (ex: `mem0`) para perguntas como "qual foi a última decisão sobre o Registoo?"
- [ ] **Sincronização GitHub Issues ↔ backlog** dos projetos

---

## Como Interagir com o Brain

**Via Telegram (mais comum):**
> Envie mensagem de texto ou voz para o bot do Hermes. Ele classifica e salva automaticamente.

**Via terminal na VPS:**
```bash
hermes
# > Salva no Brain, projeto registoo, type issue: "descrição do bug"
```

**Via Antigravity/agy/Claude Code localmente:**
> Use o MCP `brain-vault` para ler e escrever arquivos diretamente.
