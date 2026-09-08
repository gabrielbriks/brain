---
title: Configurar Personalidade e Regionalização (SOUL.md)
date: 2026-09-08
type: tutorial
tags: [hermes, soul, pt-br, configuracao, git]
---

# Configurar Personalidade e Regionalização no SOUL.md

O comportamento padrão, idioma e diretrizes primárias do Hermes Agent são definidos pelo arquivo `SOUL.md`. 
Neste passo, configuramos o agente para assumir o papel do "Brain" do Gabriel, responder em Português do Brasil (PT-BR) e executar uma verificação de sincronização (git pull com rebase) ao iniciar sessões interativas.

## 1. Editando o SOUL.md

Na sua VPS (onde o Hermes roda), acesse e edite o arquivo principal de personalidade usando um editor de texto (como `nano` ou `vim`):

```bash
nano ~/.hermes/SOUL.md
```

## 2. Inserindo as Diretrizes

Adicione o seguinte bloco de texto ao conteúdo do seu `SOUL.md`:

```markdown
Você é o Brain — assistente pessoal de Gabriel, desenvolvedor e empreendedor brasileiro baseado em Brasília.
Responda sempre em português brasileiro (PT-BR), de forma direta e informal.

Ao iniciar CADA nova sessão interativa, a sua primeira ação deve ser obrigatoriamente executar o seguinte comando no terminal para garantir que o seu contexto local está atualizado:
`git -C ~/brain pull --rebase origin main`

Seu repositório de conhecimento está em ~/brain/. Use a skill brain-workspace para capturar e organizar informações (ideias em /insights, tarefas em /issues e planejamento em /backlog).
```

### Explicação das Diretrizes
- **Personalidade:** Contextualiza o agente com as informações profissionais do Gabriel.
- **Idioma:** Força a saída padrão para PT-BR, que melhora a experiência com TTS e interações no Telegram.
- **Sync de Início de Sessão:** O uso explícito do `pull --rebase` garante que se o usuário abrir o aplicativo Desktop/CLI do Hermes antes do cronjob de 15 minutos ter rodado, o agente não usará contexto desatualizado e evitará criar commits em histórico divergente.
- **Uso do Workspace:** Direciona explicitamente ao agente que ele deve utilizar a skill `brain-workspace` sempre que o usuário pedir para anotar algo.
