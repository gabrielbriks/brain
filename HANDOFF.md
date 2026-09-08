# Brain — Handoff Document

> **Para o agente que continuar este trabalho:** leia este documento inteiro antes de agir.
> O CONTEXT.md no repositório cobre a infraestrutura. Este handoff cobre o estado atual da sessão, decisões tomadas e o próximo bloco de trabalho.

---

## Estado atual (2026-09-08)

### O que está funcionando

- ✅ Hermes Agent v0.21.1 rodando no PrimeClaws Base Docker
- ✅ LLM: deepseek-v3.2 (incluso no plano)
- ✅ Vault criado em `~/brain/` com estrutura de workspaces
- ✅ Git inicializado, remote conectado ao GitHub (`gabrielbriks/brain`, privado)
- ✅ Skill `brain-workspace` ativa em `~/.hermes/skills/productivity/brain-workspace/SKILL.md`
- ✅ Teste de captura validado — insight salvo, frontmatter correto, commit realizado
- ✅ `CONTEXT.md` documentado e pushado no repositório

### Problema conhecido

A pasta criada no primeiro teste foi `insight/` (singular) em vez de `insights/` (plural).
A skill já foi corrigida para plural. Os commits futuros vão usar o padrão correto.
O arquivo de teste em `registoo/insight/` pode ser movido manualmente se quiser manter consistência.

---

## Infraestrutura

| Item | Detalhe |
|---|---|
| Provedor | PrimeClaws Base Docker |
| Acesso | Console via dashboard PrimeClaws (ttyd) |
| Usuário VPS | `container@hermes` |
| Agente | Hermes Agent |
| LLM | deepseek-v3.2 |
| Vault | `~/brain/` |
| Repositório | `https://github.com/gabrielbriks/brain` (privado) |
| Autenticação Git | Fine-grained token, acesso restrito ao repo `brain` |

---

## Próximos passos (em ordem de prioridade)

### 1. Auto-sync Git (push e pull automáticos)

**Objetivo:** cada nota salva pelo Hermes deve ser automaticamente pushada pro GitHub. E ao iniciar uma sessão, o Hermes deve fazer pull pra garantir que está com o vault atualizado.

**O que explorar:**

O Hermes tem suporte nativo a cron jobs. Comandos úteis:
```bash
hermes cron list          # lista cron jobs ativos
hermes cron add           # adiciona um novo cron job
```

**Estratégia sugerida:** dois cron jobs.

**Cron 1 — Auto-push a cada 15 minutos:**
```bash
hermes cron add "*/15 * * * *" "git -C ~/brain push origin main"
```

**Cron 2 — Pull ao iniciar sessão (via hook):**
Verificar se o Hermes tem suporte a hooks de início de sessão:
```bash
hermes hooks list
cat ~/.hermes/config.yaml | grep hook
```

Alternativa: adicionar pull no próprio SOUL.md como instrução de comportamento:
```
Ao iniciar qualquer sessão, execute: git -C ~/brain pull origin main
```

**Investigar também:**
- Se o Hermes já faz push automaticamente após commits (verificar o output dos próximos testes)
- Se há configuração de `post-commit` hook do Git que pode chamar o push

---

### 2. Configurar Telegram como canal de input

**Objetivo:** Gabriel poder mandar áudios e textos via Telegram e o Hermes processar e salvar no Brain.

**Comandos:**
```bash
hermes channel telegram
```

O doctor já avisou que `python-telegram-bot` não está instalado. O Hermes provavelmente instala automaticamente ao configurar o canal.

**O que precisará:**
- Criar um bot no Telegram via @BotFather
- Obter o `TELEGRAM_BOT_TOKEN`
- Configurar em `~/.hermes/.env`

**Para áudio:** verificar se o Hermes tem suporte a transcrição de voz no canal Telegram (o v0.20.0 adicionou TTS/voice — verificar se inclui STT também).

---

### 3. Configurar SOUL.md para PT-BR

**Objetivo:** Hermes responder em português por padrão, com o contexto do Brain já carregado.

**Localização:** `~/.hermes/SOUL.md` (já existe — doctor confirmou)

**Ver o conteúdo atual:**
```bash
cat ~/.hermes/SOUL.md
```

**Adicionar no início do SOUL.md:**
```markdown
Você é o Brain — assistente pessoal de Gabriel, desenvolvedor e empreendedor brasileiro baseado em Brasília.
Responda sempre em português brasileiro (PT-BR), de forma direta e informal.
Ao iniciar cada sessão, faça: git -C ~/brain pull origin main
Seu repositório de conhecimento está em ~/brain/. Use a skill brain-workspace para capturar e organizar informações.
```

---

### 4. MCP — Expor o Brain para Claude Code e Gemini

**Objetivo:** poder consultar o Brain diretamente de dentro do Claude Code ou Gemini CLI enquanto desenvolve.

**Investigar:**
```bash
hermes mcp list
hermes mcp --help
```

O Hermes v0.21.0 melhorou significativamente o MCP surface. A ideia é expor o vault do Brain como um MCP server que o Claude Code possa consumir via `.mcp.json` no projeto.

---

## Estrutura do vault atual

```
~/brain/
├── CONTEXT.md              ← documentação para agentes
├── README.md               ← descrição geral
├── registoo/
│   ├── insight/            ← ⚠️ singular (corrigir para insights/)
│   │   └── 2026-09-08-teste-01-*.md
│   ├── issues/
│   └── backlog/
├── pictae/
│   ├── issues/
│   └── insights/
├── vox/
│   ├── issues/
│   └── insights/
├── pessoal/
└── trabalho/
    └── dotnet/
```

---

## Skill brain-workspace — localização e conteúdo

```
~/.hermes/skills/productivity/brain-workspace/SKILL.md
```

**Comportamento esperado da skill:**
1. Identifica workspace pelo nome do projeto mencionado
2. Classifica em `insights/`, `issues/` ou `backlog/`
3. Cria arquivo: `~/brain/<workspace>/<tipo>/YYYY-MM-DD-<slug>.md`
4. Faz commit: `git -C ~/brain add . && git -C ~/brain commit -m "brain: <workspace> - <resumo>"`
5. Confirma o que foi salvo

---

## Comandos de referência rápida

```bash
# Iniciar sessão com Hermes
hermes

# Listar skills
hermes skills list

# Ver skill do Brain
hermes skills inspect brain-workspace

# Saúde do sistema
hermes doctor

# Atualizar Hermes
hermes update

# Ver cron jobs
hermes cron list

# Status do vault
git -C ~/brain status
git -C ~/brain log --oneline -10
```

---

## Contexto de Gabriel (para o agente)

- Desenvolvedor .NET/SQL Server pleno, MEI em Brasília
- Produtos: Registoo (PWA saúde), Pictae (SaaS fotografia), Vox (em planejamento)
- Prefere explicações diretas, informais e stepwise
- Prioridade: baixo custo, alta performance, experiência fluida em PT-BR
- Usa Claude Code no dia a dia — integração MCP com Brain é objetivo futuro

---

*Gerado em 2026-09-08 | Sessão de setup inicial do Brain MVP*