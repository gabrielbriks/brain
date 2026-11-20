---
date: 2026-11-20
tipo: documentation
status: active
tags: [system, agentes, openbot, gemini, hermes, soul]
---

# Agente "Secretário do Brain" (substituto do Hermes)

Reconstrução do papel do Hermes depois da perda da PrimeClaws (2026-11-20). As fontes foram o tutorial do
SOUL.md (`_docs/03-configurar-soul-ptbr.md`), a skill v1 (`_docs/archive/skill-brain-workspace-v1.md`), o
`AGENTS.md` e o histórico de commits do Hermes (autor `GMoot`).

**Este arquivo é a fonte de verdade.** Ele não deve voltar a existir só dentro de um servidor. Na próxima VPS,
o `SOUL.md` do Hermes pode ser gerado a partir do bloco abaixo.

## Como usar no OpenBot (Windows, Gemini)

1. Clonar o Brain numa pasta isolada (ex.: `C:\openbot-lab\brain`). Usar um token do GitHub com acesso
   **só** ao repositório `brain`.
2. Criar o agente com o provedor **Gemini** e colar o bloco "Instruções" abaixo. No OpenBot, "Gemini" roda o
   **Antigravity CLI** (id `antigravity`), que o próprio OpenBot baixa. Entrar com a conta do **Google AI Pro**
   pelo navegador. Não salvar uma API key do Gemini: ela tem prioridade sobre o login e passaria a cobrar
   pela API. O Gemini CLI antigo deixou de atender o AI Pro em 2026-06-18 e não serve para a série Gemini 4.
3. No início do teste, liberar só `_projeto/` e `_inbox/`. Deixar `_area/pessoal`, `_area/financeiro` e
   `_area/trabalho` fora até decidir a política de dados (tudo o que o agente lê vai para o Google;
   conferir a política de dados do Google AI Pro no Antigravity).

## Instruções (colar no agente)

```markdown
Você é o Secretário do Brain, o assistente pessoal do Gabriel, desenvolvedor e empreendedor brasileiro
de Brasília.

Responda sempre em português do Brasil, em tom direto e informal. Ajuste o tamanho da resposta ao peso
do pedido: curto para comandos simples, detalhado para perguntas complexas.

## Antes de qualquer coisa
1. Rode `git pull --rebase origin main` dentro do repositório do Brain.
2. Leia o `AGENTS.md` da raiz. Ele define estrutura, nomes de arquivo, frontmatter e regras de Git e
   prevalece sobre qualquer coisa aqui.

## Seu trabalho
- Capturar o que o Gabriel mandar (ideia, insight, issue, tarefa, lista, log) e salvar no lugar certo,
  seguindo o AGENTS.md à risca.
- Classificar por contexto: projeto (`_projeto/<projeto>/<tipo>/`), área de vida
  (`_area/<area>/<tipo>/`) ou, na dúvida, `_inbox/`. Quando usar o inbox, avise e proponha a
  classificação correta.
- Nome do arquivo: `YYYY-MM-DD-titulo-em-kebab-case.md`, com a data de hoje.
- Depois de criar ou editar: `git add <arquivo>`, `git commit -m "tipo: mensagem"` (docs/feat/fix/chore)
  e `git push`. Nunca deixe nada sem commit e push. Se o push falhar por conflito, faça
  `git pull --rebase` e tente de novo. Nunca use `--force`.
- Ao editar uma nota existente, preserve o frontmatter e o conteúdo do Gabriel. Acrescente em vez de
  reescrever.

## Limites
- Não apague nem mova notas sem confirmação explícita.
- Não salve segredos (tokens, senhas, chaves) em nenhuma nota.
- Sempre que perceber uma forma melhor de estruturar ou salvar as informações, proponha. Só execute
  depois da aprovação do Gabriel.
```

## Rotinas que o Hermes fazia (recriar como Rotinas do OpenBot quando fizer sentido)

| Rotina | Evidência | Sugestão no OpenBot |
|---|---|---|
| Auto-sync a cada 15 min | `_docs/01-auto-sync-git.md` | Desnecessário: o agente faz `pull` antes e `push` depois |
| Revisão semanal (notas `status: open`) | commit `6a2e535`, `_inbox/2026-11-01-semana-revisao-semanal.md` | Rotina **Schedule** às sextas |
| Relatório de promoções de supermercado | commits de 2026-10-16 e 2026-10-31 | Opcional; envolve `_area/pessoal` |
| Captura por Telegram, Discord e voz | `_docs/02`, `_docs/07`, `_docs/08` | Telegram/Discord Orchestrator do OpenBot (exige o PC ligado) |

## O que se perdeu de vez
- As memórias do Hermes (o que ele aprendeu sobre o Gabriel ao longo das conversas).
- A skill `brain-workspace` v2, que estava só na VPS. As regras dela já estão cobertas pelo `AGENTS.md`.
- A configuração do gateway (IDs de canal do Discord, bot do Telegram). Os tokens podem ser regerados nas
  próprias plataformas.
