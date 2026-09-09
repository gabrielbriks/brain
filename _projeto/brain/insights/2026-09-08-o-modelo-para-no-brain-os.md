---
date: 2026-09-08
projeto: brain
type: insight
status: open
tags: [para-model, gtd, pkm, arquitetura, organizacao, aprendizado]
---

# O Modelo PARA aplicado ao Brain OS

Nesta data, reestruturamos o **Brain OS** para adotar uma adaptação do **Modelo PARA** (criado por Tiago Forte em seu método *Building a Second Brain*), em conjunto com conceitos do GTD (*Getting Things Done*).

O objetivo desta nota é servir como um guia rápido para internalizar como o conhecimento e as tarefas devem fluir dentro do sistema a partir de agora.

## O que é o PARA?

O acrônimo PARA significa **P**rojects, **A**reas, **R**esources e **A**rchives. No nosso Brain OS, a estrutura foi adaptada da seguinte forma:

### 1. Projetos (`_projeto/`)
São esforços com **começo, meio e um fim definido**, vinculados a um objetivo claro ou um entregável.
- **Exemplos:** Registoo, Pictae, Historuja, Widback.
- **Mentalidade:** *"Qual é o próximo passo para concluir isso ou entregar a feature?"*
- **No Brain:** Guardamos aqui *insights*, *issues*, *backlog*, *ideas* e *decisions*.

### 2. Áreas (`_area/`)
São esferas de atividade contínua. Elas exigem que **padrões sejam mantidos**, não possuem data de conclusão ou linha de chegada.
- **Exemplos:** Trabalho (CLT), Empreendedorismo, Finanças, Vida Pessoal.
- **Mentalidade:** *"Como posso manter ou melhorar o padrão desta área para que minha vida flua bem?"*
- **No Brain:** Guardamos aqui *tasks* cotidianas, *listas* (ex: compras), *logs* (diários, anotações de reuniões) e *refs* (referências).

### 3. Recursos (Resources)
São tópicos de interesse que podem ser úteis no futuro (uma biblioteca pessoal).
- **No Brain:** Em vez de uma pasta gigante solta, nós otimizamos isso colocando os recursos (*refs*) diretamente dentro da respectiva `_area/` (ex: referências de arquitetura .NET ficam em `_area/trabalho/refs/`). A documentação do próprio sistema vive em `_docs/`.

### 4. Arquivos (Archives)
Itens inativos, projetos concluídos ou áreas da vida que não fazem mais parte do foco atual.
- **No Brain:** Para não precisar mover arquivos de pasta o tempo todo e quebrar links, nós apenas mudamos o campo `status` no Frontmatter para `archived`. Isso mantém o histórico no lugar original e o controle é feito via filtro de busca do próprio Antigravity / Hermes.

---

## O Coração do Sistema: Caixa de Entrada (`_inbox/`)

Trazido do método GTD, o Inbox é a **área de captura rápida de atrito zero**.

Se você está na rua, manda um áudio no Telegram e tem uma ideia solta, mas não sabe se é um projeto, uma área ou apenas um devaneio: **vai para o Inbox**.
- **Regra de ouro:** A captura não pode interromper o seu fluxo de pensamento. O Hermes está treinado para jogar no `_inbox/` sempre que o contexto da sua mensagem for ambíguo.
- Depois, no seu próprio tempo, nós processamos o que está no inbox e classificamos para a pasta correta.

## Por que isso é melhor que a estrutura antiga?

Antes, misturávamos responsabilidades contínuas (como as rotinas da Implanta) com produtos finitos (como um bug do Registoo). A separação semântica garante que:
1. Os **Projetos avancem** de forma ágil para a conclusão (issues e backlogs claros).
2. As **Áreas sejam mantidas sob controle** (diários de reuniões e checklists do dia a dia não poluem o código).
3. O cérebro foque na execução, deixando a IA fazer a triagem (ou delegando para o Inbox).
