---
date: 2026-11-23
projeto: zen-ai-workflow
type: insight
status: in-progress
tags: [openbot, agentes, arquitetura, registoo, marketing, video, storytelling, skills, decisoes]
---

# Arquitetura Inicial da Equipe de Agentes no OpenBot (Ciclo 1 — Visão e Papéis)

> Registro completo do raciocínio e das decisões tomadas em **2026-11-23** antes de escrever qualquer instrução/prompt de agente.
> Objetivo: usar o **Registoo** como laboratório real para tracionar aquisição orgânica (sem tráfego pago) e, a partir disso, consolidar a estrutura operacional da startup replicável para os próximos projetos (`pictae`, `historuja`, `zen-ai-workflow`, etc.).
>
> Relacionadas: [[2026-11-18-pesquisa-openbot-equipe-de-agentes]] · [[2026-11-23-matriz-de-modelos-equipe-agentes-openbot]] · [[2026-11-20-agente-secretario-do-brain]] · [[2026-11-20-fontes-de-renda-com-agentes-e-conteudo]].

---

## 1. Linha de raciocínio e decisões-chave deste ciclo

### Decisão A — Não escrever instruções antes de desenhar o sistema
Em vez de criar prompts soltos, vamos primeiro fechar:
1. Quais agentes existem e **onde termina o papel de um e começa o do outro** (zero sobreposição).
2. Como os agentes conversam entre si (**handoffs** claros: o que entra e o que sai de cada um).
3. Quais rotinas recorrentes cada agente opera.
4. Quais skills já temos e quais precisamos buscar/construir.

Só depois de refinar cada agente individualmente é que redigimos suas instruções finais para o OpenBot.

### Decisão B — Produção de vídeo dividida em 2 frentes distintas
Durante a discussão ficou claro que "fazer vídeo" engloba **dois produtos muito diferentes**, com estética, ferramenta e objetivo de funil diferentes:

1. **Frente A — Produto & Tutoriais (com Remotion):**
   - **Objetivo:** mostrar o Registoo vivo, animando telas, fluxos (QR Code, evolução no celular, Painel da clínica) com acabamento *high-level* e identidade Zen Tech.
   - **Por que manter Remotion:** mesmo com modelos fortes (como Opus) conseguindo produzir vídeos sem Remotion, para demonstrar e animar telas da aplicação com precisão de ritmo, consistência visual e escala, o Remotion continua entregando um patamar superior.
   - **Onde atua no funil:** meio → fundo de funil (YouTube, tutoriais, demos no Instagram/carrosséis em `apps/video`).

2. **Frente B — Storytelling de Dores & Sub-dores (foco TikTok / Reels topo de funil):**
   - **Objetivo:** romper a bolha organicamente com **retenção nos primeiros 3 segundos** e identificação emocional imediata — sem "cara de propaganda de SaaS".
   - **Lógica de Dor vs. Sub-dor:**
     - *Dor macro:* "O convênio glosou atendimentos e a clínica perdeu dinheiro."
     - *Sub-dores (ouro pro TikTok):* "Sexta à noite cobrando evolução da semana inteira no WhatsApp"; "Família questionando se a sessão aconteceu e você sem prova"; "Fechar repasse no fim do mês cruzando planilha e áudio de WhatsApp"; "Medo silencioso de processo trabalhista por usar app de ponto para profissional autônomo".
   - **Produção:** aqui faz sentido testar fluxo narrativo/storytelling **sem depender do Remotion** (roteiro baseado em conflito/cena/virada, frameworks como *Kishōtenketsu*, cortes dinâmicos, narração/legendas gravadas) — e usar Opus/Sonnet na direção criativa.

### Decisão C — Separar **Estrategista** de **Roteirista** (evolução de 4 → 5 agentes)
Inicialmente consideramos juntar Estratégia + Roteiro num único agente. Decidimos **separar** por três razões práticas:
1. **Escopo real de cada um:** o **Roteirista** não escreve só o Reel semanal — ele vai criar histórias de dor/sub-dor (TikTok/Reels), **sequências de Stories**, **roteiros longos de YouTube**, carrosséis, legendas e blog.
2. **Mentalidade e cadência diferentes:** o **Estrategista** olha o sistema de cima (lê métricas semanais, encontra gaps, propõe testes, valida ideias do Gabriel e filtra tendências/trends); o **Roteirista** executa peças com foco total em retenção, storytelling, tom PT-BR natural e filtro jurídico.
3. **Eficiência de modelo/cota:** Estrategista usa modelo pesado (`Claude Opus 5.5` / `Gemini 4 Carbon`) poucas vezes na semana; Roteirista usa `Claude Sonnet 5.5` em volume diário/semanal.

### Decisão D — Fronteira limpa entre **Pesquisador** e **Estrategista**
Ponto de atenção levantado para evitar bagunça de papéis (especialmente em "tendências/trends"):
- **Pesquisador = Coleta e Evidência** (vai buscar concorrentes, leis/LGPD/conselhos, grupos/comentários reais, trends brutas e mina dores/sub-dores com fonte verificada → entrega **dossiê cru**).
- **Estrategista = Decisão e Direção** (recebe os dossiês do Pesquisador + métricas semanais + ideias do Gabriel → decide o que faz sentido pro Registoo, valida se uma trend serve ou é distração, conduz o **review semanal de métricas** e gera o **briefing/pauta**).

---

## 2. Desenho da Equipe — Os 5 Agentes (Onda 1)

| # | Agente (Codinome) | Missão central | Modelo sugerido | O que entrega (saída) | O que NÃO faz |
|---|---|---|---|---|---|
| 1 | **Secretária do Brain (`Gabs`)** ✅ *desenho fechado* | Operação pessoal do Gabriel, memória viva do Brain e **triagem proativa** (essência FRIDAY + KAREN). Ver [[2026-11-24-blueprint-gabs-secretaria-do-brain]]. | `Gemini 3.8 Flash` (fallback `4 Hydrogen`) | Notas no Brain (`git sparse-checkout`), limpeza do `_inbox/`, revisão semanal, briefing de segunda e sugestões de handoff. | Não acessa `_area/pessoal`, `_area/financeiro`, `_area/trabalho`; não produz marketing nem acessa produção/banco. |
| 2 | **Pesquisador de Mercado & Dores** *(codinome a definir)* | Inteligência de nicho, concorrentes, jurídico/home care, trends brutas e mineração de dores/sub-dores. | `Gemini 4 Argon` (fallback `4 Neon`) | Dossiês verificados com fonte primária + banco vivo de dores e sub-dores (gestor e profissional). | Não define pauta nem decide o que publicar. |
| 3 | **Estrategista de Marketing & Growth** *(codinome a definir)* | Direção do funil orgânico, análise de métricas, validação de ideias/trends com o Gabriel e definição de testes. | `Claude Opus 5.5` (fallback `Gemini 4 Carbon`) | Review/overview semanal de métricas (manter/cortar/testar) + pauta/briefing priorizado por dor/funil. | Não escreve roteiro final nem mexe em código/render. |
| 4 | **Roteirista & Criador de Conteúdo** *(codinome a definir)* | Transformar briefings em peças prontas para aprovação: TikTok/Reels (storytelling), YouTube, sequências de Stories, carrosséis, legendas e blog. | `Claude Sonnet 5.5` (fallback `Gemini 4 Neon`) | Rascunhos em `marketing/pecas/` revisados no checklist jurídico + `generic-language-killer`. | Não publica/agenda, não analisa métricas macro, não edita código do app. |
| 5 | **Produtor de Vídeos & Peças Visuais** *(codinome a definir)* | Materializar roteiros aprovados nas 2 frentes: **Remotion** (telas do app, tutoriais, carrosséis) e **Narrativo/TikTok** (cenas, ritmo, legenda). | `Gemini 4 Neon` (Remotion) · `Claude Opus/Sonnet 5.5` (narrativo) | Vídeos renderizados, prévias visuais e slides prontos para aprovação do Gabriel. | Não inventa promessa fora do roteiro aprovado; nunca usa dado real de paciente (LGPD). |

> **Nota sobre codinomes (decisão de 2026-11-24):** cada agente terá papel funcional explícito (nos docs) + codinome curto inspirado em IAs/tecnologias de Marvel, DC e sci-fi (ou nome afetivo como a `Gabs`) para facilitar uso diário e `@menções` no OpenBot.
>
> **No radar da Onda 2 (fora do escopo atual para manter foco no Registoo):**
> - **Agente Casa & Dispensa** — dedicado a estoque doméstico, lista semanal/mensal e estratégia de compras/promoções em mercados, com acesso **compartilhado com a esposa** (isolado do Brain profissional).
> - **Assistente Financeiro / Pessoal** — rodando com privacidade reforçada (modelo 100% local via Ollama/LM Studio ou API paga sem treino, sempre sobre arquivos higienizados).

### Fluxo operacional (linha de montagem)

```text
[Ideias do Gabriel] ─────────────────────────┐
                                             ▼
[Pesquisador] ──(dossiê + dores/trends)──▶ [Estrategista] ──(briefing + pauta)──▶ [Roteirista]
                                             ▲                                         │
                                             │                                   (roteiro/texto)
                                    (métricas semanais)                                ▼
                                             │                                [Produtor Visual/Vídeo]
                                             │                                         │
                                      [Publicação Manual] ◀── [Gate: Aprovação do Gabriel] ◀──┘

* Em paralelo/transversal: [Secretário do Brain] captura ideias do Gabriel, registra aprendizados e apoia o dia a dia.
```

---

## 3. Inventário de Skills: o que já existe vs. lacunas a buscar

### Já instalado no `registoo-check` (`.agents/skills/` e `.claude/skills/`)
- **Fundamentos & Conversão:** `avatar-extraction`, `offer-extraction`, `schwartz-awareness-mapper`, `objection-crusher`, `headline-matrix`, `mechanism-builder`, `conversion-path-builder`, `marketing-psychology`.
- **Social, Conteúdo & Criativo:** `content-strategy`, `product-marketing`, `social`, `video`, `image`, `copywriting`, `copy-editing`, `lead-magnets`, `scroll-stopping-creative`, `ad-angle-multiplier`.
- **Análise & QA:** `performance-diagnosis`, `generic-language-killer`, `lgpd-audit`.

### Lacunas identificadas para buscar ou construir
1. **Árvore de Dores → Sub-dores → Histórias:** mapear sistematicamente as dores secundárias do gestor de clínica e do profissional domiciliar e convertê-las em ângulos de narrativa.
2. **Storytelling nativo para TikTok/Reels em PT-BR:** ganchos de 0–3s, conflito, virada e retenção com linguagem brasileira real (compensando o viés americano/LinkedIn das skills de terceiros).
3. **Sequências de Stories (engajamento + conversão suave):** estrutura de sequências diárias/semanais com enquetes reais que retroalimentam a linguagem do cliente.
4. **Roteiro de YouTube (tutoriais + autoridade de nicho):** estrutura de retenção para vídeos médios/longos e demonstrações.
5. **Produção de vídeo narrativo fora do Remotion (ou híbrido):** fluxo prático de direção de cena, B-roll/geração visual, narração e legenda dinâmica para o TikTok.

---

## 4. Ordem recomendada de construção e ativação (sem sobrecarregar)

Ter os **5 agentes** claros no papel evita misturar papéis, mas **não ligamos todos no mesmo dia**:

1. **Onda 1A (próximo passo):** **Secretário do Brain** — valida o OpenBot no dia a dia e libera carga mental.
2. **Onda 1B:** **Estrategista** + **Roteirista** — já destrava o review semanal de métricas, validação de ideias/trends, Stories, TikTok, YouTube e carrosséis.
3. **Onda 1C:** **Pesquisador** + **Produtor de Vídeos (2 frentes)** — escala a mineração contínua de dores/sub-dores e a produção visual/Remotion + TikTok.

*(Mantendo a regra da Fase 0: se em 2 semanas a operação não economizar horas reais ou não gerar tração mensurável, reavaliamos antes de expandir.)*

---

## 5. Progresso & Ponto de retomada

- [x] **Agente #1 — `Gabs` (Secretária do Brain):** desenho fechado em 2026-11-24 — ver [[2026-11-24-blueprint-gabs-secretaria-do-brain]] (pronta para subir na Onda 1A).
- [ ] **Próximo a estruturar em profundidade:** **Estrategista de Marketing & Growth** *(ou **Pesquisador**, seguindo a Onda 1B)* — definir codinome, rotinas (review semanal de métricas, validação de ideias/trends), entradas/saídas e skills.
- [ ] **Depois:** Roteirista → Pesquisador → Produtor de Vídeos (2 frentes) + busca/construção das skills faltantes de redes sociais e vídeo.
