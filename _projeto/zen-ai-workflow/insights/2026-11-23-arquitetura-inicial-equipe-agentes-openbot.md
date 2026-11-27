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
| 2 | **Pesquisadora de Mercado & Dores (`EDITH`)** ✅ *desenho fechado* | Inteligência de nicho, concorrentes (Atrio, ABA+, ODAAP, ABAPlay...), jurídico/LGPD, trends brutas e mineração de dores/sub-dores com duplo foco: marketing + evolução de produto (DNA EDITH + Oracle + Heimdall + Coulson + Cerebro). Ver [[2026-11-25-blueprint-edith-pesquisadora-mercado]]. | `Gemini 4 Argon` (fallback `4 Neon`) | Dossiês em `_projeto/registoo/pesquisas/`, Banco Vivo em `registoo-check/marketing/dores-e-subdores.md` e varredura semanal de quarta (4 Lentes + auto-refinamento). | Não define pauta/estratégia, não escreve roteiros finais e não mexe em código/produção. |
| 3 | **Estrategista de Marketing & Growth (`Fury`)** ✅ *desenho fechado* | Direção do funil orgânico, review semanal de métricas (futuro MCP Free Tier), validação de ideias/trends e visão multi-rede (DNA Fury + Shuri + Gideon + Vision). Ver [[2026-11-25-blueprint-fury-estrategista-marketing]]. | `Claude Opus 5.5` (fallback `Gemini 4 Carbon`) | Review semanal (`MANTER/CORTAR/TESTAR`), Mesa de Ideias (qui/sex) e briefing cirúrgico por peça/rede para o Roteirista. | Não escreve roteiro final, não faz pesquisa bruta de campo e não mexe em código/render. |
| 4 | **Roteirista & Criadora de Conteúdo (`Hill`)** ✅ *desenho fechado* | Braço direito do `Fury`: transforma briefings em roteiros de TikTok/Reels (storytelling de dores/sub-dores), Stories, YouTube, carrosséis, legendas e blog (DNA Loki + Miss Minutes + Zatanna + Jocasta). Ver [[2026-11-25-blueprint-hill-roteirista-conteudo]]. | `Claude Sonnet 5.5` (fallback `Gemini 4 Neon`) | Rascunhos em `marketing/pecas/` com 3 hooks, tag de framework, blocos de direção pro Produtor Visual e checklist jurídico/`generic-language-killer`. | Não publica/agenda, não analisa métricas macro, não edita código do app. |
| 5 | **Produtora de Vídeos & Peças Visuais (`Zoe`)** ✅ *desenho fechado* | Materializa roteiros aprovados da `Hill` com alma Pixar (Zoetrope) + Método 90/10 + 4 vertentes de motion via código (Frente A: Remotion high-level; Frente B: HTML/GSAP, Canvas, SVG + TTS comercial). Ver [[2026-11-25-blueprint-zoe-produtora-videos-motion]]. | `Gemini 4 Neon` (Remotion) · `Claude Opus 5.5` vs. `Gemini 4 Carbon` (benchmark Frente B) | Critique Loop de frames + MP4/carrosséis renderizados ou kit de produção prontos para aprovação do Gabriel. | Só mexe em `apps/video/` e `marketing/pecas/`; nunca usa dado real (LGPD); não altera promessa do roteiro nem publica. |

> **Nota sobre codinomes (decisão de 2026-11-24):** cada agente terá papel funcional explícito (nos docs) + codinome curto inspirado em IAs/tecnologias de Marvel, DC e sci-fi (ou nome afetivo como a `Gabs`) para facilitar uso diário e `@menções` no OpenBot.
>
> **Esquadrão Casa / Família (100% isolado da startup e da `Gabs`):**
> - **Agente #6 — `Remy` (Gestora da Casa, Despensa & Compras — `xtoque`)** ✅ *desenho fechado em 2026-11-27* — modelo `Gemini 4 Hydrogen`, workspace exclusivo no `xtoque`, acesso compartilhado com a **Luana** (preferência por Canal Compartilhado `#casa` no OpenBot se houver isolamento granular/seat; fallback grupo privado no Telegram). Ver [[2026-11-27-blueprint-remy-gestora-casa-xtoque]].
> - **No radar (Onda 2 — Casa):** **Assistente Financeiro do Casal** (cartões, faturas, assinaturas) — previsto para entrar no mesmo espaço familiar compartilhado com a Luana, rodando em API paga sem treino (créditos GCP) sobre arquivos higienizados.

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

## 5. Progresso & Próximos Passos Executivos (Time da Onda 1 100% Desenhado!)

- [x] **Agente #1 — `Gabs` (Secretária do Brain):** [[2026-11-24-blueprint-gabs-secretaria-do-brain]] *(Onda 1A)*
- [x] **Agente #2 — `Fury` (Estrategista de Marketing & Growth):** [[2026-11-25-blueprint-fury-estrategista-marketing]] *(Onda 1B)*
- [x] **Agente #3 — `Hill` (Roteirista & Criadora de Conteúdo):** [[2026-11-25-blueprint-hill-roteirista-conteudo]] *(Onda 1B)*
- [x] **Agente #4 — `EDITH` (Pesquisadora de Mercado, Concorrentes & Dores):** [[2026-11-25-blueprint-edith-pesquisadora-mercado]] *(Onda 1C)*
- [x] **Agente #5 — `Zoe` (Produtora de Vídeos, Motion & Peças Visuais):** [[2026-11-25-blueprint-zoe-produtora-videos-motion]] *(Onda 1C)*

### Checklist de virada para execução (próxima etapa)
- [ ] Atualizar `AGENTS.md` do Brain registrando `_projeto/<projeto>/pesquisas/` (tipo `research`) para a `EDITH`.
- [ ] Subir a **Onda 1A (`Gabs`)** no OpenBot Windows com `git sparse-checkout` + opt-out de treino nas assinaturas PRO.
- [ ] Guia prático de ativação dos **US$ 10/mês do Google AI Pro** (Paid Tier sem treino + teste do Google Cloud TTS `Chirp 3 HD` para a `Zoe` + configuração isolada no OpenBot).
- [ ] Pacote de **Skills faltantes** (Árvore de Dores/Sub-dores, Storytelling PT-BR com 5 frameworks, Sequências de Stories, YouTube e Manual de Estúdio de Motion 90/10 da `Zoe`).
- [ ] Benchmark prático da `Zoe` (Frente B): mesma peça piloto em **Opus 5.5 vs. Gemini 4 Carbon/Neon**.

---

## 6. Atualização — 2026-11-27 (Go-live Onda 1A no Azure)

- [x] **Onda 1A (`Gabs`) no ar:** servidor **OpenBot** provisionado no **Azure (`Standard_B4as_v2`)** com **Tailscale**, e `Gabs` ativada como primeira agente operacional (substituindo o plano anterior de subir primeiro no Windows). Registro detalhado em [[2026-11-27-servidor-openbot-azure-onda-1a-gabs]].
