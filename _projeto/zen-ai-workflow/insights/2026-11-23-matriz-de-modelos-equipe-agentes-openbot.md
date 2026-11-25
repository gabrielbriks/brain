---
date: 2026-11-23
projeto: zen-ai-workflow
type: insight
status: in-progress
tags: [openbot, agentes, modelos, gemini, claude, registoo, estrategia]
---

# Matriz de Modelos — Equipe de Agentes no OpenBot

> Referência viva para escolher o modelo certo por papel/agente, equilibrando qualidade, velocidade, consumo de cota e termos das assinaturas (**Google AI Pro** via Antigravity CLI no OpenBot + **Claude Pro**).
> Relacionadas: [[2026-11-23-arquitetura-inicial-equipe-agentes-openbot]] · [[2026-11-18-pesquisa-openbot-equipe-de-agentes]] · [[2026-11-20-agente-secretario-do-brain]] · [[2026-11-20-fontes-de-renda-com-agentes-e-conteudo]].

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

## 2. Alocação atual (alinhada aos 5 agentes da Onda 1)

| Agente / Papel | Modelo Principal | Fallback / Alternativa | Motivo |
|---|---|---|---|
| **1. Secretário do Brain** *(dia a dia, captura, git, revisão semanal)* | Gemini 3.8 Flash | Gemini 4 Hydrogen | Alta frequência; preserva cota dos modelos pesados. Subir para Hydrogen se houver deslize de regra no `AGENTS.md`. |
| **2. Pesquisador de Mercado & Dores** *(concorrentes, jurídico/LGPD, trends brutas, dores/sub-dores)* | Gemini 4 Argon | Gemini 4 Neon | Janela de 1M tokens + destaque do Argon em análise regulatória/jurídica e síntese sem o custo de cota do Carbon. |
| **3. Estrategista de Marketing & Growth** *(review semanal de métricas, gaps, testes, validação de ideias/trends, pauta)* | Claude Opus 5.5 | Gemini 4 Carbon *(e Hydrogen para pré-leitura bruta de números)* | Baixa frequência (semanal/campanha); exige julgamento fino para decidir o que cortar, manter ou testar. |
| **4. Roteirista & Criador de Conteúdo** *(TikTok/Reels, YouTube, Stories, carrosséis, legendas, blog)* | Claude Sonnet 5.5 | Gemini 4 Neon | Melhor naturalidade em PT-BR, aderência ao `generic-language-killer`, filtro jurídico e agilidade em variações de gancho/storytelling. |
| **5. Produtor de Vídeos & Peças Visuais** *(Frente A: Remotion / Frente B: Narrativo TikTok)* | Gemini 4 Neon (Remotion) · Claude Opus/Sonnet 5.5 (narrativo) | — | Híbrido: Remotion para telas/fluxos high-level do app; fluxo narrativo/storytelling para vídeos de dor/sub-dor (TikTok/Reels). |
| **Coletor de Padrões (Fase 2)** | Gemini 4 Carbon | Gemini 4 Neon | Cruzamento pontual entre repositórios (Registoo → zen-ai-workflow, Pictae, Historuja). |

## 3. Regra de cota e limites de assinatura

- **Pirâmide 80 / 15 / 5:** ~80% do volume em Flash/Hydrogen/Sonnet 5.5; ~15% em Argon/Neon; ~5% em Opus 5.5/Carbon.
- **Claude Pro:** não plugar OAuth da conta principal em agentes autônomos/VPS no OpenBot (termos da Anthropic). Usar Claude Pro no Claude Code/app interativo; no OpenBot, usar os modelos Claude expostos via provedor Antigravity ou `ANTHROPIC_API_KEY` com teto de gasto.
- **Google AI Pro:** usar no piloto interativo (OpenBot desktop, Fase 0). Rotinas 24/7 sem supervisão em VPS futura → migrar para Gemini API key com limite de gasto.
- **Descoberta (2026-11-24) — Créditos de US$ 10/mês no Google AI Pro:** a assinatura inclui US$ 10/mês (acumuláveis por 12 meses) via Google Developer Program / Google AI Studio para uso no **Gemini API Paid Tier** (ou Google Cloud). No **Paid Tier** o Google **não usa os dados para treino** (diferente do Free Tier, que treina!). Solução ideal em nuvem para futuro Assistente Financeiro/Pessoal (sem precisar rodar local sem VRAM) e para rotinas autônomas no OpenBot — *pendente: fazer guia passo a passo de resgate, alerta de orçamento e configuração isolada no OpenBot sem sobrescrever o login do Antigravity*.

## 4. Próximos passos (ver nota de arquitetura)

- [x] Definir o recorte de agentes da **Onda 1** (5 agentes com fronteiras claras — ver [[2026-11-23-arquitetura-inicial-equipe-agentes-openbot]]).
- [ ] Estruturar rotinas, entradas/saídas e limites de cada agente individualmente (começando pelo **Secretário do Brain**).
- [ ] Detalhar o pipeline de **vídeo em duas frentes** (Remotion vs. Storytelling/TikTok).
- [ ] Buscar/construir as skills faltantes mapeadas para redes sociais, Stories, YouTube e storytelling PT-BR.
