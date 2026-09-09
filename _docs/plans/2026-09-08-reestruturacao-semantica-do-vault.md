---
title: Plano de Reestruturação Semântica do Vault
date: 2026-09-08
status: completed
tags: [plan, architecture, para-model, refactor]
---

# Brain OS — Plano de Reestruturação Semântica

> **Status:** ✅ Aprovado por Gabriel — Pronto para Execução  
> **Contexto:** Plano detalhado para que qualquer agente futuro possa executar integralmente esta reestruturação do vault. Leia este documento por completo antes de executar qualquer ação.

---

## 📋 Contexto e Decisões

### Sobre Gabriel (contexto de quem usa o sistema)
- **Desenvolvedor Fullstack** pleno e **MEI**
- **CLT na Implanta** (sistemas contabeis .NET/SQL Server — empenhos, liquidações, pagamentos, Restos a Pagar, etc)
- **Empreendedor** com múltiplos produtos SaaS em andamento
- Usa diariamente: **Antigravity IDE**, **Antigravity CLI (`agy`)** e **Claude Code** (extensão VS Code + CLI via `claude code cli`)
- Input principal no Brain: **Telegram** (mensagens de texto e voz) + sessões diretas no Hermes

### Decisões já validadas pelo Gabriel
1. ✅ **Migração total:** Todos os arquivos atuais fora de `_docs/` são dados de teste e podem ser **deletados**. A estrutura nova começa do zero.
2. ✅ **`trabalho/` ≠ Implanta** — A pasta `trabalho/` (e a área de vida correspondente) deve ser genérica para qualquer contexto profissional CLT ou prestação de serviço (Implanta é só o atual). Não pode ter o nome da empresa hardcoded.
3. ✅ **Frontmatter e SKILL.md do Hermes** devem ser atualizados para refletir a nova estrutura.
4. ✅ **`_docs/` é preservada** mas alguns arquivos precisam ser **editados** para refletir a nova estrutura (ver lista abaixo).

---

## 🗂️ Nova Estrutura de Diretórios

```text
brain/
│
├── _area/                        ← ÁREAS DE VIDA (contextos maiores e permanentes)
│   ├── trabalho/                 ← Trabalho CLT ou freelance (genérico, não fixo em Implanta)
│   │   ├── README.md
│   │   ├── tasks/
│   │   ├── logs/                 ← Diário de reuniões, demandas recebidas, anotações
│   │   └── refs/                 ← Referências técnicas, documentações internas
│   ├── empreendedor/             ← Gestão e estratégia dos produtos SaaS pessoais
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
│   └── financeiro/               ← Controle financeiro pessoal e como MEI
│       ├── README.md
│       └── logs/
│
├── _projeto/                     ← PROJETOS ATIVOS (ciclo de vida definido, entregáveis)
│   ├── registoo/                 ← PWA de registro de atendimentos domiciliares
│   │   ├── README.md
│   │   ├── insights/
│   │   ├── issues/
│   │   ├── backlog/
│   │   └── decisions/
│   ├── pictae/                   ← SaaS de galerias premium para fotógrafos
│   │   ├── README.md
│   │   ├── insights/
│   │   ├── issues/
│   │   └── backlog/
│   ├── historuja/                ← SaaS de histórias sociais para neurodivergentes
│   │   ├── README.md
│   │   ├── insights/
│   │   ├── issues/
│   │   └── backlog/
│   ├── vox/                      ← App de captura de notas (planejamento futuro)
│   │   ├── README.md
│   │   ├── ideas/
│   │   └── insights/
│   ├── brain/                    ← O próprio Brain como produto (Moot)
│   │   ├── README.md
│   │   ├── ideas/
│   │   └── decisions/
│   └── widback/                  ← Solução de feedback/bugs para apps web (planejamento)
│       ├── README.md
│       └── ideas/
│
├── _inbox/                       ← CAIXA DE ENTRADA — captura rápida sem classificação
│   └── .gitkeep
│
├── _docs/                        ← Documentação do sistema Brain (já existe, manter)
│   ├── README.md                 ← [EDITAR] — atualizar para a nova estrutura
│   ├── 01-auto-sync-git.md
│   ├── 02-configurar-telegram.md
│   ├── 03-configurar-soul-ptbr.md  ← [EDITAR] — SOUL.md atualizado com nova estrutura
│   ├── 04-servico-background-gateway.md
│   └── 05-configurar-mcp-local.md
│
├── CONTEXT.md                    ← [EDITAR] — atualizar tudo para nova estrutura
├── HANDOFF.md                    ← [EDITAR] — atualizar pendências e novas instruções
└── README.md                     ← [EDITAR] — refletir nova estrutura
```

---

## 📝 Tipagem de Notas (por pasta)

| Tipo        | Pasta        | Uso                                                           | Quem usa                    |
|-------------|--------------|---------------------------------------------------------------|-----------------------------|
| `insight`   | `insights/`  | Aprendizados, descobertas, "aha moments"                      | `_projeto/`                 |
| `issue`     | `issues/`    | Bug, problema, obstáculo técnico                              | `_projeto/`                 |
| `backlog`   | `backlog/`   | Features e melhorias futuras                                  | `_projeto/`                 |
| `decision`  | `decisions/` | Decisões técnicas ou de produto (padrão ADR)                  | `_projeto/`                 |
| `idea`      | `ideas/`     | Ideias brutas sem contexto suficiente ainda                   | `_area/`, `_projeto/`       |
| `task`      | `tasks/`     | Tarefa concreta com prazo e/ou prioridade                     | `_area/`                    |
| `log`       | `logs/`      | Diário de bordo: reuniões, eventos, decisões do dia a dia     | `_area/`                    |
| `ref`       | `refs/`      | Referências, links, materiais de estudo                       | `_area/trabalho/`           |
| `lista`     | `listas/`    | Listas recorrentes (compras, mantimentos, checklists)         | `_area/pessoal/`            |
| *(inbox)*   | `_inbox/`    | Captura rápida, sem classificação — processar depois          | Raiz                        |

---

## 🔖 Novo Schema de Frontmatter

**Padrão para notas de `_projeto/`:**
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

**Padrão para notas de `_area/`:**
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

**Padrão para `_inbox/` (captura rápida, preenchimento mínimo):**
```yaml
---
date: YYYY-MM-DD
type: inbox
tags: []
---
```

**Naming convention dos arquivos** (sem mudanças):  
`YYYY-MM-DD-titulo-em-kebab-case.md`

---

## ✅ Checklist de Execução

### Fase 1 — Limpeza do vault atual

- [ ] Deletar `pessoal/` (arquivo de teste: `pessoal/insights/2026-09-08-nova-nota-do-telegram.md`)
- [ ] Deletar `registoo/` (arquivo de teste: `registoo/insight/2026-09-08-teste-01-descobri-que-o-fluxo-de-autentica-o-do-pw.md`)
- [ ] Confirmar que não há nada em `trabalho/` ou `pictae/` ou `vox/` (verificar com `find`)

### Fase 2 — Criar nova estrutura de pastas

Para cada diretório listado na árvore acima, criar a pasta e um `.gitkeep` para que o Git rastreie pastas vazias. Lembre-se que Git não versiona pastas vazias sem um arquivo dentro.

Comando de referência:
```bash
mkdir -p _area/trabalho/{tasks,logs,refs} \
         _area/empreendedor/{ideas,tasks,logs} \
         _area/pessoal/{logs,listas} \
         _area/financeiro/logs \
         _projeto/registoo/{insights,issues,backlog,decisions} \
         _projeto/pictae/{insights,issues,backlog} \
         _projeto/historuja/{insights,issues,backlog} \
         _projeto/vox/{ideas,insights} \
         _projeto/brain/{ideas,decisions} \
         _projeto/widback/ideas \
         _inbox
```

Depois criar `.gitkeep` em todas as pastas-folha vazias.

### Fase 3 — Criar READMEs das Áreas e Projetos

Cada `README.md` deve conter:
- Nome e descrição do projeto/área
- Status atual (resumo livre)
- Links para as subpastas
- Campo "próximas ações" (a ser preenchido conforme uso)

**Template para `_area/<area>/README.md`:**
```markdown
---
title: Área — <Nome>
type: readme
---

# <Nome da Área>

<Descrição da área de vida que este contexto representa.>

## Subpastas
- `tasks/` — Tarefas e ações concretas
- `logs/` — Diário de bordo, registros de reuniões e eventos
- `ideas/` — Ideias e reflexões

## Próximas Ações
*(Atualizado automaticamente pelo Hermes na weekly review)*
```

**Template para `_projeto/<projeto>/README.md`:**
```markdown
---
title: Projeto — <Nome>
type: readme
status: active  # active | paused | archived
---

# <Nome do Projeto>

<Descrição do produto/projeto.>

## Subpastas
- `insights/` — Aprendizados e descobertas
- `issues/` — Bugs e problemas abertos
- `backlog/` — Features e melhorias planejadas
- `decisions/` — Decisões técnicas e de produto

## Próximas Ações
*(Backlog top 3 — atualizado manualmente ou pelo Hermes)*
```

### Fase 4 — Criar as Listas Iniciais do Cotidiano

**`_area/pessoal/listas/mantimentos.md`** (arquivo inicial):
```markdown
---
date: 2026-09-08
area: pessoal
type: lista
tags: [casa, estoque, mantimentos]
---

# Estoque de Mantimentos

> Atualizado pelo Hermes via Telegram. Informe quando um item acabar ou estiver acabando.

| Item          | Status       | Ação          |
|---------------|--------------|---------------|
| Arroz         | ✅ OK        |               |
| Feijão        | ✅ OK        |               |
| Azeite        | ✅ OK        |               |
| Café          | ✅ OK        |               |

```

**`_area/pessoal/listas/compras-mercado.md`** (arquivo inicial):
```markdown
---
date: 2026-09-08
area: pessoal
type: lista
tags: [casa, compras, mercado]
---

# Lista de Compras — Mercado

> Lista de itens para comprar. Peça ao Hermes via Telegram para adicionar ou remover itens.

- [ ] (lista vazia — adicione itens conforme necessidade)
```

### Fase 5 — Atualizar `CONTEXT.md`

O `CONTEXT.md` é o arquivo **mais crítico** — é a bíblia que qualquer agente lê para entender o sistema. Ele precisa ser reescrito por completo para refletir:

1. A nova estrutura de pastas (`_area/`, `_projeto/`, `_inbox/`)
2. Os novos tipos de notas e o novo schema de frontmatter
3. A instrução de que o `_inbox/` é o fallback padrão para captura sem contexto
4. O contexto do Gabriel (CLT + empreendedor + pessoal)
5. O MCP brain-vault já configurado nas ferramentas locais

**Seções obrigatórias no novo CONTEXT.md:**
- O que é o Brain
- Infraestrutura (VPS PrimeClaws Docker + Hermes + deepseek-v3.2)
- Repositório Git
- Nova estrutura do vault (com árvore atualizada)
- Áreas de vida do Gabriel
- Projetos ativos do Gabriel
- Tipos de nota e schema de frontmatter
- Regra do `_inbox/`
- Skill brain-workspace (localização e função)
- Hermes — comandos úteis
- Ferramentas locais (Antigravity + Claude Code com MCP configurado)
- O que já foi feito + Pendências

### Fase 6 — Atualizar SOUL.md do Hermes (na VPS)

O **SOUL.md** atual (`~/.hermes/SOUL.md` na VPS) referencia a estrutura antiga. Após a reestruturação, o agente que estiver conectado à VPS deve editá-lo com o seguinte conteúdo:

```markdown
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
```

### Fase 7 — Atualizar a Skill `brain-workspace` (na VPS)

Localização na VPS: `~/.hermes/skills/productivity/brain-workspace/SKILL.md`

A skill precisa ser atualizada para:
1. Conhecer a nova estrutura de pastas (`_area/`, `_projeto/`, `_inbox/`)
2. Usar o novo schema de frontmatter
3. Ter a regra do `_inbox/` como fallback

> [!IMPORTANT]
> **Isso deve ser feito diretamente na VPS** (via terminal PrimeClaws ou pelo próprio Hermes). O arquivo não existe localmente neste repositório — ele fica em `~/.hermes/` que é o diretório de configuração do Hermes no container Docker.

### Fase 8 — Atualizar os arquivos `_docs/`

Os seguintes arquivos em `_docs/` precisam ser editados para mencionar a nova estrutura:

| Arquivo | O que mudar |
|---|---|
| `_docs/README.md` | Apenas boas práticas — **sem mudança de conteúdo necessária** |
| `_docs/03-configurar-soul-ptbr.md` | Atualizar o bloco de código do SOUL.md para refletir o novo conteúdo (Fase 6) |
| `CONTEXT.md` | Reescrever completamente (Fase 5) |
| `README.md` | Atualizar a árvore de diretórios e a lista de workspaces |

### Fase 9 — Commit e Push

```bash
git -C ~/www/brain add -A
git -C ~/www/brain commit -m "refactor: reestruturação semântica do vault (PARA model)"
git -C ~/www/brain push origin main
```

---

## 🔗 Arquivos de Referência (já existentes, não mexer)

| Arquivo | Função |
|---|---|
| [`_docs/01-auto-sync-git.md`](file:///home/gabriel/www/brain/_docs/01-auto-sync-git.md) | Como configurar o cron de sync Git na VPS |
| [`_docs/02-configurar-telegram.md`](file:///home/gabriel/www/brain/_docs/02-configurar-telegram.md) | Como configurar o bot do Telegram |
| [`_docs/04-servico-background-gateway.md`](file:///home/gabriel/www/brain/_docs/04-servico-background-gateway.md) | Como manter o gateway ativo no Docker (tmux / Startup Command) |
| [`_docs/05-configurar-mcp-local.md`](file:///home/gabriel/www/brain/_docs/05-configurar-mcp-local.md) | MCP brain-vault já configurado no Antigravity IDE, agy e Claude Code |

---

## 🏗️ Roadmap (Médio e Longo Prazo — Para Depois da Execução Inicial)

> Esses itens **não fazem parte desta execução**. São próximos passos a planejar no futuro.

- **Weekly Review Automatizado:** Cron na VPS que toda sexta-feira lista notas com `status: open`, gera um report e envia via Telegram
- **READMEs de área com "próximas ações"** atualizados periodicamente pelo Hermes
- **Busca semântica:** MCP com embeddings (ex: `mem0`) para perguntas como "qual foi a última decisão sobre o Registoo?"
- **Sincronização GitHub Issues ↔ backlog** dos projetos
- **Brain como Produto (Moot):** A documentação em `_docs/` é o embrião do playbook

---

## ⚠️ Pontos de Atenção para o Agente Executor

1. **Não mexer em `_docs/`** além do indicado na Fase 8. Os tutoriais de infra (Telegram, Gateway, Auto-sync) estão corretos.
2. **A skill `brain-workspace` fica na VPS** (`~/.hermes/`), não neste repositório. Para editá-la é necessário ou logar na VPS via SSH/ttyd ou pedir ao Hermes para se auto-editar.
3. **O `.gitkeep`** deve ser criado em todas as pastas-folha vazias — Git não versiona diretórios vazios.
4. **Não renomear `_docs/`** — a convenção de prefixo numérico é intencional e funciona bem.
5. **Após o commit** deste repositório, a VPS vai puxar via cron (a cada 15 min). O SOUL.md do Hermes, no entanto, **não está neste repo** — precisa ser editado manualmente na VPS.
