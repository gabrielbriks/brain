# Brain — Handoff Document

> **Para o agente que continuar este trabalho:** leia este documento inteiro antes de agir.
> O `CONTEXT.md` no repositório cobre a infraestrutura e a estrutura teórica atual.
> Este handoff cobre o estado atual da sessão e o bloco de trabalho exato que você deve assumir.

---

## Estado Atual (Atualizado)

Nas últimas sessões, Gabriel e o agente completaram as seguintes configurações fundamentais de infraestrutura:
- ✅ Auto-sync Git (pull --rebase + push) via cron no Hermes.
- ✅ Integração com Telegram configurada via Gateway.
- ✅ SOUL.md ajustado para responder em PT-BR.
- ✅ MCP Server local (`@modelcontextprotocol/server-filesystem`) configurado de forma global para Antigravity IDE, `agy` CLI e Claude Code (`openclaude`).

**O grande marco recente:** Nós acabamos de desenhar e **aprovar um plano de reestruturação semântica** completo para o Brain, abandonando a estrutura antiga e migrando para um modelo mais robusto inspirado no PARA (`_area/`, `_projeto/`, `_inbox/`).

O plano completo, detalhado e já aprovado por Gabriel está salvo em:
👉 [`_docs/plans/2026-09-08-reestruturacao-semantica-do-vault.md`](file:///home/gabriel/www/brain/_docs/plans/2026-09-08-reestruturacao-semantica-do-vault.md)

---

## Próximos Passos (Sua Missão)

A sua **única missão inicial** nesta nova sessão é **executar fielmente o checklist do plano de reestruturação**.

### O que você deve fazer imediatamente ao assumir:
1. Leia o arquivo `_docs/plans/2026-09-08-reestruturacao-semantica-do-vault.md` com extrema atenção.
2. Siga a seção **"Checklist de Execução"** passo a passo (da Fase 1 à Fase 9).
3. **Atenção especial às Fases 6 e 7:** Elas exigem a edição do `SOUL.md` e da skill `brain-workspace` que ficam **diretamente na VPS** (no container do Hermes em `~/.hermes/`), e não neste repositório local. O plano contém o código exato que você deve usar para atualizá-los, portanto você precisará executar comandos remotos ou orientar o Gabriel a fazê-lo.
4. Lembre-se de criar arquivos `.gitkeep` nas novas pastas vazias para que o Git as rastreie.

---

## Infraestrutura (Lembrete Rápido)

| Item | Detalhe |
|---|---|
| Provedor | PrimeClaws Base Docker (Container, sem Systemd) |
| Agente VPS | Hermes Agent |
| Vault Local | `/home/gabriel/www/brain/` (sincronizado via Git) |
| Repositório | `https://github.com/gabrielbriks/brain` (privado) |

> *Atenção: O próprio `CONTEXT.md` atual precisará ser reescrito por você durante a Fase 5 do plano de reestruturação para refletir a nova realidade do cofre.*