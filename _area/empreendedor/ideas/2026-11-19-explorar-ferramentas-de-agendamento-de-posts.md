---
date: 2026-11-19
area: empreendedor
type: idea
status: open
tags: [redes-sociais, agendamento, open-source, marketing, registoo, openbot, explorar]
---

# Explorar ferramentas (de preferência open source) para agendar posts e automatizar DMs

> Item exploratório, ainda sem pesquisa. Opções vistas numa rede social em 2026-11-19.

## Ideia

Encontrar alternativas, de preferência open source ou self-hosted (para rodar junto da futura VPS própria),
para duas frentes:

1. **Agendar e publicar posts** (substituir o agendador).
2. **Automatizar DMs e comentários**, no estilo do **ManyChat** (confirmado pelo Gabriel em 2026-11-19).
   Exemplo: a pessoa comenta uma palavra-chave no Reel e recebe o link ou a isca por DM.

## Candidatas para avaliar

Agendamento: **Postiz**, **Zernio**, **Buffer**.
Automação de DM (alternativas ao ManyChat): ainda não levantadas.

Confirmar a licença e se dá para self-hostear cada uma (não verificado). Para DM no Instagram, ver as
regras da API oficial da Meta: janela de 24 h e permissões do app.

## Por que interessa

- O Registoo já produz peças prontas: carrosséis e Reels em Remotion, `legenda.md` em `marketing/pecas/`,
  calendário em `marketing/calendario/`. A F4 do plano-045 prevê publicar à mão no piloto.
- Uma ferramenta com API ou webhook fecharia o ciclo de produção, aprovação humana e publicação
  agendada. Ela pode ser acionada por um agente (OpenBot ou Claude Code) e depois servir aos outros
  projetos (Pictae, Historuja).
- Ver [[2026-11-18-pesquisa-openbot-equipe-de-agentes]] (em `_projeto/zen-ai-workflow/insights/`).

## Critérios para avaliar depois

- Redes suportadas: Instagram, TikTok, YouTube Shorts, LinkedIn, Facebook.
- Pode ser self-hosted? Que licença tem? Quais os requisitos de servidor?
- Tem API ou webhook para um agente agendar? Mantém uma etapa de aprovação humana?
- Mostra métricas que alimentem `marketing/metricas/`?
- Quanto custa no início e quando escala.
- (DM) Funciona com o Instagram pela API oficial? Dá para ligar à isca e à base de contatos do plan-046 (Resend)?
