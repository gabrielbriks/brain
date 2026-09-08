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

### 1. Auto-sync Git (pull + push automáticos)

**Objetivo:** manter o repositório do Brain sincronizado automaticamente entre a VPS (onde o Hermes cria notas) e o GitHub (onde commits locais do Gabriel também chegam).

#### Por que não usar apenas `git push`?

O Brain é editado de **dois lados independentes**:
- 🤖 **VPS (Hermes):** cria notas novas em `insights/`, `issues/`, `backlog/`
- 🖥️ **Local (Gabriel):** edita documentação (`README.md`, `CONTEXT.md`, `HANDOFF.md`) e faz push direto pro GitHub

Se o cron fizer apenas `git push` na VPS e o Gabriel já tiver pushado commits do lado local, o push **vai falhar** porque o `main` remoto terá commits que a VPS não conhece. O Git se recusa a fazer push em branches divergentes.

Além disso, o pull originalmente estava atrelado ao início de uma sessão interativa com o Hermes — mas o cron roda independentemente, sem garantia de que uma sessão foi aberta antes.

#### Decisão: `pull --rebase` antes de cada `push`

A solução é unificar tudo em um único cron job que **sempre puxa antes de empurrar**:

```bash
hermes cron add "*/15 * * * *" "git -C ~/brain pull --rebase origin main && git -C ~/brain push origin main"
```

**Por que `--rebase` em vez de `pull` simples (merge)?**
- `git pull` (merge) criaria um commit de merge a cada sincronização, poluindo o histórico com mensagens como `Merge branch 'main' of github.com/...` a cada 15 minutos.
- `git pull --rebase` reaplica os commits locais da VPS **em cima** dos commits vindos do GitHub, resultando em um histórico linear e limpo — como se tudo tivesse sido feito em sequência.

**Por que `&&` entre os comandos?**
- O operador `&&` garante que o `push` **só executa se o `pull` der certo**. Se houver um conflito real (dois lados editaram o mesmo trecho do mesmo arquivo), o processo para ali sem corromper nada.

**Risco de conflito real é baixo** porque os dois lados trabalham em arquivos diferentes: o Hermes cria arquivos novos, o Gabriel edita documentação existente. O rebase resolve isso automaticamente.

#### Estratégia complementar — Pull ao iniciar sessão

Mesmo com o cron, ainda vale adicionar um pull explícito ao iniciar uma sessão interativa com o Hermes. Isso garante que ele esteja 100% atualizado antes de qualquer interação. Opções:

1. Adicionar no `SOUL.md` como instrução de comportamento:
```
Ao iniciar qualquer sessão, execute: git -C ~/brain pull origin main
```

2. Verificar se o Hermes suporta hooks de início de sessão:
```bash
hermes hooks list
cat ~/.hermes/config.yaml | grep hook
```

#### Padrão reutilizável para projetos futuros

Este padrão de sync bidirecional via cron pode ser aplicado em qualquer projeto onde múltiplos ambientes (CI/CD, agentes, máquinas locais) escrevem no mesmo repositório Git:
1. Nunca faça push cego — sempre `pull --rebase` antes
2. Use `&&` para encadear e evitar push em estado inconsistente
3. Estruture o projeto para que cada lado escreva em caminhos diferentes (reduz conflitos a quase zero)
4. Mantenha o intervalo de sync curto (15 min) para minimizar a janela de divergência

---

### 2. Configurar Telegram como canal de input

**Objetivo:** Gabriel poder mandar áudios e textos via Telegram e o Hermes processar e salvar no Brain.

**Comandos:**
```bash
hermes gateway setup
hermes gateway
```

**O que precisará:**
- Criar um bot no Telegram via @BotFather
- Obter o `TELEGRAM_BOT_TOKEN` e o seu User ID
- Rodar o assistente (`setup`) para que ele configure o `~/.hermes/.env` e depois rodar o `hermes gateway` para iniciar o bot.

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