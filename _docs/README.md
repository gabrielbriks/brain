# Diretrizes da Documentação (`_docs`)

Esta pasta armazena tutoriais, guias de infraestrutura e procedimentos importantes (passo a passo) para replicar configurações ou entender a arquitetura do **Brain**.

Para manter o repositório organizado, qualquer nova documentação adicionada aqui deve seguir os padrões abaixo.

## 1. Nomenclatura de Arquivos

Os arquivos devem ser nomeados usando um prefixo numérico sequencial (para manter a ordem de leitura/criação) seguido de um nome descritivo em `kebab-case` e a extensão `.md`.

**Formato:**
`XX-nome-do-assunto.md`

**Exemplos:**
- `01-auto-sync-git.md`
- `02-configurar-telegram.md`
- `03-configuracao-mcp.md`

## 2. Cabeçalho Obrigatório (Frontmatter)

Todo arquivo deve conter um bloco YAML (frontmatter) no topo com os metadados do documento. Isso facilita a indexação futura por agentes e ferramentas.

**Estrutura do Frontmatter:**
```markdown
---
title: Título Curto e Descritivo
date: YYYY-MM-DD
type: tutorial (ou guide, reference)
tags: [tag1, tag2, tag3]
---
```

**Exemplo Prático:**
```markdown
---
title: Configurar Canal do Telegram
date: 2026-09-08
type: tutorial
tags: [hermes, telegram, bot, canal, infra]
---

# Configurar Telegram como Canal de Input
Conteúdo do tutorial começa aqui...
```

## 3. Boas Práticas

- **Clareza e Passo a Passo:** Escreva de forma que outra pessoa (ou você mesmo no futuro) consiga copiar e colar comandos facilmente.
- **Blocos de Código:** Especifique sempre a linguagem (ex: ````bash````, ````markdown````).
- **Justificativas:** Sempre que uma decisão técnica for tomada (ex: usar `--rebase` no git pull), documente o *porquê* daquela decisão, não apenas o comando.
