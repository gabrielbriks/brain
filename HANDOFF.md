# Brain — Handoff Document

> **Para o agente que continuar este trabalho:** leia este documento inteiro antes de agir.
> O `CONTEXT.md` no repositório cobre a infraestrutura e a estrutura completa do vault.
> Este handoff cobre o estado atual do sistema e o roadmap ativo.

---

## Estado Atual (Atualizado — 2026-09-09)

A reestruturação semântica do vault para o **Modelo PARA** foi **100% concluída com sucesso**, tanto localmente quanto na VPS.

**Últimas entregas concluídas:**
- ✅ **Estrutura Base:** Pastas de teste deletadas e nova arquitetura criada (`_area/`, `_projeto/`, `_inbox/`).
- ✅ **Configuração da IA (VPS):** `SOUL.md` e skill `brain-workspace` atualizados na VPS do Hermes para garantir roteamento inteligente de notas e uso correto do Inbox.
- ✅ **Documentação Atualizada:** `CONTEXT.md`, `README.md` e tutoriais (`_docs/`) refletem o novo modelo de forma integral.
- ✅ **Manual de Workflow Diário:** Criado o `_docs/06-workflow-diario-e-captura.md` explicando o fluxo de "Atrito Zero", triagem do Hermes e a revisão do Inbox.
- ✅ **Dogfooding e Aprendizado:** Notas sobre o conceito de *Dogfooding* (`_area/empreendedor/refs/`) e a arquitetura PARA do Brain (`_projeto/brain/insights/`) foram criadas como referências internas.
- ✅ **Integração com iOS (Ideias):** Levantamento de ideias de automação com o iOS Shortcuts foi registrado em `_docs/07-integracao-ios-shortcuts.md` e inserido no backlog ativo do projeto Brain (`_projeto/brain/ideas/`).

---

## Próximos Passos e Roadmap (Sua Missão)

O sistema central está estável e operante. O foco agora é expandir os recursos de **"Atrito Zero"** e de **Inteligência**. O próximo agente deve consultar Gabriel sobre qual destas frentes atacar:

1. **Integração com iOS Shortcuts (Atrito Zero):**
   - Implementar os atalhos de gravação de voz nativa (Action Button), Extensão de Compartilhamento ("Share to Brain") ou Widget na tela de bloqueio (ver detalhes técnicos em `_docs/07-integracao-ios-shortcuts.md`).
   - *Ação necessária:* Configurar requisição POST via iOS apontando para a API do Telegram (`/sendMessage`).

2. **Weekly Review Automatizado (Cron na VPS):**
   - Desenvolver um script na VPS (rodando via cron toda sexta-feira) que faça um loop pelas notas, identifique as com `status: open` (em `issues` ou `tasks`), gere um sumário em Markdown e envie ativamente para o Telegram do Gabriel via Gateway.

3. **Busca Semântica via Embeddings:**
   - Estudar e propor a viabilidade de plugar um MCP de memória/embeddings (ex: `mem0`) para permitir que Gabriel pergunte ao Hermes coisas complexas do tipo *"Qual foi a última decisão técnica tomada no projeto Registoo?"* e obtenha a resposta exata.

---

## Infraestrutura (Lembrete Rápido)

| Item | Detalhe |
|---|---|
| Provedor | PrimeClaws Base Docker (Container, sem Systemd) |
| Agente VPS | Hermes Agent |
| Vault na VPS | `~/brain/` |
| Vault Local | `/home/gabriel/www/brain/` (sincronizado via Git) |
| Repositório | `https://github.com/gabrielbriks/brain` (privado) |
| Auto-sync | Cron a cada 15 min — `git pull --rebase + push` |