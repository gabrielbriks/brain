---
date: 2026-11-23
projeto: zen-ai-workflow
type: insight
status: in-progress
tags: [openbot, agentes, modelos, gemini, claude, registoo, estrategia]
---

# Matriz de Modelos — Equipe de Agentes no OpenBot

> Referência viva para escolher o modelo certo por papel/agente, equilibrando qualidade, velocidade, consumo de cota e termos das assinaturas (**Google AI Pro** via Antigravity CLI no OpenBot + **Claude Pro**).
> Relacionadas: [[2026-11-18-pesquisa-openbot-equipe-de-agentes]] · [[2026-11-20-agente-secretario-do-brain]] · [[2026-11-20-fontes-de-renda-com-agentes-e-conteudo]].

## 1. Modelos disponíveis e perfil de cada um

| Modelo | Perfil | Melhor uso |
|---|---|---|
| **Gemini 4 Carbon** | Raciocínio máximo / longo prazo (pesado, consome mais cota) | Arquitetura complexa, decisões estruturais, auditoria profunda, planos longos. |
| **Gemini 4 Neon** | Equilíbrio forte entre fronteira de raciocínio e velocidade | Engenharia/código complexo (ex.: pipeline Remotion), análises técnicas e tarefas multi-etapas. |
| **Gemini 4 Argon** | Frontier eficiente (menos tokens que Carbon) | Pesquisa densa, **análise regulatória/jurídica** (home care, LGPD, conselhos profissionais) e síntese de mercado. |
| **Gemini 4 Hydrogen** | Workhorse rápido da série Gemini 4 | Execução rotineira com uso pesado de ferramentas/arquivos, sub-agentes, relatórios recorrentes. |
| **Gemini 3.8 Flash** | Ultra-rápido e econômico | Captura rápida, classificação, triagem, resumos simples e tarefas de alta frequência. |
| **Claude Opus 5.5** | Estrategista + escrita de altíssima nuance | Posicionamento, estratégia de campanhas, storytelling/narrativa de alto impacto, pitch decks, definição de voz. |
| **Claude Sonnet 5.5** | Braço direito de copy + execução ágil | Roteiros curtos (Reels/TikTok), carrosséis, legendas naturais em PT-BR (menos "cara de IA") e código bem delimitado. |

## 2. Alocação inicial (em refinamento)

| Agente / Papel | Modelo Principal | Fallback / Alternativa | Motivo |
|---|---|---|---|
| **Secretário do Brain** *(dia a dia, captura, git, revisão semanal)* | Gemini 3.8 Flash | Gemini 4 Hydrogen | Alta frequência; preserva cota dos modelos pesados. Subir para Hydrogen se houver deslize de regra no `AGENTS.md`. |
| **Pesquisador de Mercado, Nicho & Jurídico** | Gemini 4 Argon | Gemini 4 Neon | Janela de 1M tokens + destaque do Argon em análise regulatória/jurídica e síntese sem o custo de cota do Carbon. |
| **Estrategista de Marketing / Growth** | Claude Opus 5.5 | Gemini 4 Carbon | Baixa frequência (semanal/campanha); define direção, posicionamento e mapa de dores/sub-dores. |
| **Editor de Conteúdo & Roteirista** | Claude Sonnet 5.5 | Gemini 4 Neon | Melhor naturalidade em PT-BR, aderência ao `generic-language-killer` e geração rápida de variações de gancho. |
| **Produtor de Vídeos (Tutoriais / Remotion / Storytelling)** | Gemini 4 Neon (Remotion/código) · Claude Opus/Sonnet 5.5 (narrativa/vídeo sem Remotion) | — | Híbrido: Remotion para telas/fluxos high-level do app; fluxo narrativo/storytelling para vídeos de dor/sub-dor (TikTok/Reels). |
| **Analista de Métricas** | Gemini 4 Hydrogen | Gemini 3.8 Flash | Leitura estruturada de `marketing/metricas/` e decisão semanal. |
| **Coletor de Padrões (Fase 2)** | Gemini 4 Carbon | Gemini 4 Neon | Cruzamento pontual entre repositórios (Registoo → zen-ai-workflow, Pictae, Historuja). |

## 3. Regra de cota e limites de assinatura

- **Pirâmide 80 / 15 / 5:** ~80% do volume em Flash/Hydrogen/Sonnet 5.5; ~15% em Argon/Neon; ~5% em Opus 5.5/Carbon.
- **Claude Pro:** não plugar OAuth da conta principal em agentes autônomos/VPS no OpenBot (termos da Anthropic). Usar Claude Pro no Claude Code/app interativo; no OpenBot, usar os modelos Claude expostos via provedor Antigravity ou `ANTHROPIC_API_KEY` com teto de gasto.
- **Google AI Pro:** usar no piloto interativo (OpenBot desktop, Fase 0). Rotinas 24/7 sem supervisão em VPS futura → migrar para Gemini API key com limite de gasto.

## 4. Pontos em definição (próxima etapa antes de escrever instruções)

- [ ] Definir o recorte exato de agentes da **Onda 1** (sem inflar o time antes de validar).
- [ ] Estruturar rotinas, entradas e saídas (handoffs) de cada agente.
- [ ] Desenhar o pipeline de **vídeo em duas frentes**:
  1. *Produto/Tutorial (Remotion)* — telas animadas do Registoo em nível high-level.
  2. *Storytelling / Dor e Sub-dores (TikTok/Reels)* — histórias conectadas às dores reais de gestores e profissionais (avaliar produção com/sem Remotion).
- [ ] Auditar skills já existentes em `registoo-check` (`.agents/skills/` e `.claude/skills/`) vs. lacunas para redes sociais, TikTok e storytelling.
