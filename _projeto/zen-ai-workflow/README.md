---
title: Projeto — Zen AI Workflow
type: readme
status: active
tags: [workflow, metodologia, ia, agentes, engenharia, transversal]
---

# 🧭 Zen AI Workflow — Metodologia de Desenvolvimento Assistido por IA

> Repositório: [`gabrielbriks/zen-ai-workflow`](https://github.com/gabrielbriks) — local em
> `/home/gabriel/www/zen-ai-workflow` — versão atual **v0.1.0**.

O **Zen AI Workflow** é o repositório-base que define **como** Gabriel trabalha com agentes de
IA em qualquer projeto de código — não o quê construir, mas o mecanismo: tipos de documento,
ciclo de trabalho, arquitetura de contexto e como o conhecimento persiste entre sessões e
ferramentas diferentes (Claude Code, Antigravity, outras).

É **model-agnostic** por design: nenhum nome de modelo entra no núcleo da metodologia — isso vive
em arquivo de ambiente separado, descartável.

Não é uma metodologia teórica. Cada regra ou (a) já era como Gabriel trabalhava em dois projetos
reais e só foi formalizada, ou (b) corrige uma falha que aconteceu de forma independente nos
dois. O que ainda não passou por nenhum desses dois critérios é marcado `EXPERIMENT`.

---

## 🎯 Objetivo do Projeto

Permitir que **qualquer agente, de qualquer ferramenta**, entre num projeto de Gabriel, descubra
onde as coisas estão, saiba o que já foi decidido e retome de onde a última sessão parou — sem
ter herdado a conversa anterior.

---

## 🏛️ Os 8 Princípios (ver `PRINCIPLES.md` no repo)

Cada um carrega um status de validação (`VALIDADO`, `PARCIAL`, `NOVO`, `ASPIRACIONAL`) — o sistema
não se apresenta com mais confiança do que realmente tem.

1. Contexto obrigatório é mínimo; o resto é recuperável sob demanda.
2. Persistir decisões e estado operacional, não a conversa.
3. Conhecimento é para reaproveitar, não para diário.
4. Documentação só existe se tiver propósito claro de recuperação futura.
5. Ao migrar uma convenção, depreciar ou remover explicitamente a anterior.
6. Gate humano no plano, sempre que o risco justificar.
7. O nível de raciocínio necessário determina o agente — não o contrário.
8. Automação só quando remove fricção comprovada; evolução por adoção gradual.

---

## 🔄 O Ciclo (ver `WORKFLOW.md` no repo)

```
INTAKE → TRIAGE (T0–T3) → DISCOVERY (T2/T3) → REASONING → CONTRACT (spec/plan/ADR)
   → HUMAN GATE → EXECUTION → REVIEW → DOCUMENTATION → HANDOFF
```

- **Tier (T0–T3)** define o piso de cerimônia exigido (não o teto) — de "1 arquivo, risco baixo"
  até "arquitetura, domínio novo, segurança". `EXPERIMENT`, sem validação empírica ainda.
- **Camada obrigatória de contexto** em qualquer projeto que adote o workflow: `AGENTS.md`,
  `CONTEXT.md` e o bloco "Estado Atual" do `HANDOFF.md`. Tudo o resto (specs, plans, ADRs,
  learnings, guides) é recuperado sob demanda.
- **`HANDOFF.md` na raiz do projeto** (preferência pessoal já registrada) — bloco "Estado Atual"
  reescrito no topo, corpo histórico anexado abaixo, nunca reescrito.

---

## 📁 Estrutura do Repositório

```text
zen-ai-workflow/
├── README.md        — o que é, como adotar num projeto novo ou migrar um existente
├── PRINCIPLES.md     — os 8 princípios, com status de validação
├── WORKFLOW.md        — o ciclo de trabalho + arquitetura de contexto
├── CHANGELOG.md       — versionamento do workflow-base
├── templates/          — o que se copia para dentro de um projeto (AGENTS.md, CONTEXT.md,
│                          HANDOFF.md, INDEX.md, adr.md, issue.md, plan.md, spec.md,
│                          model-routing.md.example)
└── docs/               — bastidor: como este workflow foi investigado e decidido
                          (não carregado por agentes trabalhando em projetos que o adotam)
```

---

## 🔗 Relação com Outros Projetos/Sistemas do Ecossistema

- **DNA Zen Tech** (`_projeto/dna-zen-tech/`): repositório irmão e independente. A divisão é
  deliberada — Zen AI Workflow define **como** o conhecimento evolui (mecanismo, ciclo, tipos de
  documento); DNA Zen Tech define **o que** é a filosofia de experiência (UI/UX, interaction
  design). Um projeto de produto consome os dois ao mesmo tempo, referenciando ambos a partir do
  seu próprio `CONTEXT.md` — por link, nunca por cópia de conteúdo.
- **Brain** (este vault): é o sistema operacional pessoal de captura (áreas de vida, projetos,
  inbox). O Zen AI Workflow é ortogonal a ele — rege como o *código* é trabalhado com agentes,
  enquanto o Brain rege como *notas, tarefas e conhecimento pessoal* são capturados e
  organizados. Ambos compartilham o princípio de "persistir decisão/estado, não a conversa".
- **Registoo, Pictae, Historuja, Vox, Widback**: projetos de produto candidatos a adotar o
  workflow — cada um decide independentemente, com adoção gradual (Princípio 8), sem exigir
  big-bang.

---

## Como Adotar num Projeto Novo (resumo — ver README do repo para o completo)

1. Copiar `templates/AGENTS.md`, `templates/CONTEXT.md`, `templates/HANDOFF.md` para a raiz do
   projeto e preencher os placeholders.
2. Copiar `templates/INDEX.md` para `docs/INDEX.md`, vazio.
3. Não pré-criar pastas de `docs/` — cada uma nasce quando o primeiro documento daquele tipo
   existir de verdade.
4. Registrar em `CONTEXT.md` qual versão do workflow-base o projeto adotou.

Para projeto existente, a migração é incremental em 7 passos por retorno decrescente sobre risco
(começando por consolidar `CONTEXT.md`) — ver `README.md` do repositório.
