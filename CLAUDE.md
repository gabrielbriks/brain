# CLAUDE.md — Guia para Claude Code

> Lido automaticamente pelo Claude Code ao abrir este repositório como workspace ou ao acessar via MCP `brain-vault`.

---

## Contexto

Este repositório é o **Brain** — sistema operacional pessoal do Gabriel Briks.  
Antes de qualquer ação, leia o [`AGENTS.md`](./AGENTS.md) — ele contém todas as regras obrigatórias de estrutura, frontmatter, naming convention e Git.

---

## Instruções Específicas para o Claude Code

### Ao acessar via MCP `brain-vault` a partir de outro projeto

Quando você estiver trabalhando em um projeto (ex: `registoo-check`, `pictae`) e precisar interagir com o brain:

1. **Use exclusivamente as ferramentas do MCP `brain-vault`** — não tente acessar o diretório `/home/gabriel/www/brain` com suas ferramentas nativas de filesystem
2. O MCP tem permissão configurada globalmente em `~/.claude.json` e já sabe onde o vault está
3. Leia este `CLAUDE.md` e o `AGENTS.md` via MCP antes de gravar qualquer nota

### Ao abrir o brain diretamente como workspace

- Você tem acesso nativo ao vault — pode usar suas ferramentas de edição diretamente
- Sempre siga as convenções do `AGENTS.md`
- Sempre execute `git add`, `git commit` e `git push` após qualquer escrita ou edição

---

## Fluxo de Salvamento Rápido

```
Input do Gabriel
    ↓
Identificar: é _área/ ou _projeto/?
    ↓
Escolher subpasta correta (insights/, tasks/, issues/, etc.)
    ↓
Criar arquivo com naming: YYYY-MM-DD-titulo-kebab.md
    ↓
Preencher frontmatter completo (ver AGENTS.md)
    ↓
git add → git commit → git push
    ↓
Confirmar para o Gabriel com caminho do arquivo criado
```

---

## Regra de Ouro

**Em dúvida sobre onde salvar → `_inbox/`.** Informe o Gabriel e proponha a classificação correta.

**Nunca** crie arquivos sem frontmatter.  
**Nunca** deixe alterações sem commit + push.

---

> Para infraestrutura completa (VPS, Hermes, cron, Telegram), leia [`CONTEXT.md`](./CONTEXT.md).  
> Para o estado atual e roadmap, leia [`HANDOFF.md`](./HANDOFF.md).
