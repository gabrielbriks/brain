---
date: 2026-09-11
projeto: brain
type: insight
status: open
tags: [arquitetura, mcp, busca-semantica, antigravity, hermes, llm]
---

# Insight: Dois Mundos de Busca — Hermes vs. Antigravity CLI

Durante o planejamento da Busca Semântica, descobrimos uma nuance arquitetural importante: o Brain OS opera em **dois contextos distintos de acesso à IA**, e cada um tem uma forma diferente de buscar informações no vault.

## Os Dois Contextos

### Contexto 1: Telegram → Hermes (VPS)
O usuário manda uma mensagem no Telegram em movimento. O Hermes, rodando na VPS, executa o `buscar.py` que consulta o ChromaDB (banco de vetores local na VPS) e retorna a nota certa com busca semântica vetorial real.

- **Tipo de busca:** Matemática (embeddings + similaridade de cosseno).
- **Qualidade:** ⭐⭐⭐⭐⭐ Semântica pura via vetores.
- **Limitação:** Só acessível via Telegram.

### Contexto 2: Antigravity CLI / Claude CLI (Local)
O usuário está trabalhando no computador com a CLI da IA. A Antigravity tem acesso ao vault via MCP `brain-vault` (leitura de arquivos), mas **não tem acesso ao ChromaDB** — o banco de vetores vive só na VPS e é ignorado pelo Git.

- **Tipo de busca:** Textual via MCP + raciocínio semântico natural do LLM.
- **Qualidade:** ⭐⭐⭐⭐ Semântica "natural" — o próprio modelo de linguagem entende o contexto e faz a ponte, sem precisar de vetores matemáticos.
- **Limitação:** Não usa os vetores do ChromaDB; depende da capacidade de leitura de arquivos + inteligência do modelo.

## A Descoberta: O Gap e a Solução Futura

O ChromaDB fica **isolado na VPS** por design (é um arquivo local, não versionado no Git). A Antigravity CLI nunca vai conseguir consultar esse banco diretamente na sua forma atual.

A solução para fechar esse gap é expor o `buscar.py` como um **servidor MCP** rodando na VPS. Com isso, tanto o Hermes quanto a Antigravity CLI poderiam usar a mesma busca vetorial de alta precisão.

```
[Antigravity CLI]          [Telegram]
       ↓                       ↓
[brain-vault MCP]      [Hermes na VPS]
       ↓                       ↓
       └──────────────────────→ [buscar.py como MCP Server]
                                       ↓
                               [ChromaDB local VPS]
```

Essa integração está mapeada como **Fase 7** no plano de implementação (`_docs/plans/2026-09-11-implementacao-busca-semantica.md`) e representa o estado ideal do sistema — um único motor de busca semântica servindo todos os contextos de acesso.

## Conclusão Prática

Para o dia a dia, o gap é pequeno: a Antigravity CLI já faz uma busca semanticamente inteligente pelo raciocínio natural do LLM. A busca vetorial via Hermes resolve o caso de "memória rápida na correria" sem abrir o computador. A unificação via MCP é o próximo nível evolutivo do sistema.
