---
date: 2026-11-25
tipo: documentation
status: active
tags: [system, skills, openbot, registoo, marketing, storytelling, motion-graphics, remotion, hyperframes, tiktok]
---

# Catálogo & Estratégia de Skills — Equipe OpenBot (Onda 1)

> Mapeamento feito na **Etapa 3 (2026-11-25)** combinando o que já existe no `registoo-check`,
> o melhor da comunidade (`skills.sh` / GitHub) e as **3 skills proprietárias** que diferenciam a operação
> do Registoo (e serão replicáveis na startup via `zen-ai-workflow`).
>
> Relacionadas: [[2026-11-23-arquitetura-inicial-equipe-agentes-openbot]] · [[2026-11-25-blueprint-fury-estrategista-marketing]] · [[2026-11-25-blueprint-hill-roteirista-conteudo]] · [[2026-11-25-blueprint-edith-pesquisadora-mercado]] · [[2026-11-25-blueprint-zoe-produtora-videos-motion]].

---

## 1. Regra de Precedência (Obrigatória para todas as skills)

Skills de terceiros **não conhecem** o vocabulário jurídico nem as travas do Registoo. Vale sempre a hierarquia:
1. `registoo-check/.agents/product-marketing.md` + `docs/issues/114-*` *(soberanos — nome público só **"Registoo"**, nunca controle de ponto/jornada, zero dado real / LGPD, zero promessa absoluta)*.
2. `registoo-check/marketing/estrategia.md` *(pilares, formatos, regras de texto, UTMs)*.
3. Skills proprietárias da startup *(PT-BR real, frameworks medidos pelo `Fury`, Estúdio 90/10 da `Zoe`)*.
4. Skills de terceiros *(mecânicas de plataforma, hooks, retenção, sintaxe Remotion/HyperFrames)*.
5. Portão final obrigatório: `qa/generic-language-killer`.

---

## 2. O que já está instalado no `registoo-check`

- **Fury (Estrategista):** `content-strategy`, `product-marketing`, `performance-diagnosis`, `schwartz-awareness-mapper`, `conversion-path-builder`, `offer-extraction`, `avatar-extraction`, `marketing-psychology`, `lead-magnets`.
- **Hill (Roteirista):** `social`, `video`, `copywriting`, `copy-editing`, `headline-matrix`, `objection-crusher`, `mechanism-builder`, `scroll-stopping-creative`, `ad-angle-multiplier`, `generic-language-killer`, `lgpd-audit`.
- **Zoe (Produtora Visual):** `video`, `image`, `apps/video/README.md` + `src/brand/` (Emerald Premium).

---

## 3. Melhores Skills da Comunidade para Avaliar / Instalar (Curadoria 2026-11-25)

> **Cuidado de segurança:** sempre auditar o conteúdo de cada `SKILL.md` de terceiros antes de instalar no workspace (revisar comandos shell, scripts e instruções).

| Agente | Skill / Repositório | O que agrega | Comando / Origem |
|---|---|---|---|
| **Zoe** *(Frente A)* | **Remotion Official Skills** | Padrões oficiais de composição, `spring()`, lint e render no Remotion. | `npx remotion skills add` (docs oficiais Remotion) |
| **Zoe** *(Frente B)* | **HyperFrames Skills (HeyGen)** | Motion graphics via **HTML/CSS + GSAP/Lottie/Three.js** → MP4 determinístico via Headless Chrome (perfeito para a Vertente 2 da `Zoe`!). | GitHub `hyperframes` (`skills/`) |
| **Hill + Fury** *(TikTok / Shorts)* | **`vyralcontent/content-skills`** | `viral-short-form` + TikTok/YouTube destilados de 200k+ vídeos (*Hook → Escalation → Payoff → CTA* + detector de queda de retenção). | `npx skills add vyralcontent/content-skills` |
| **Hill + EDITH** *(TikTok)* | **`sergebulaev/tiktok-skills`** | `tt-hook-scripter` (gancho 1–3s falado + texto na tela), `tt-humanizer`, `tt-trend-mapper` (sem "cringe"), `tt-content-planner`. | `npx skills add sergebulaev/tiktok-skills` |
| **Hill** *(Instagram & Stories)* | **`sergebulaev/instagram-skills`** | 26+ fórmulas de gancho nos primeiros 125 chars, Stories slide-a-slide para respostas/enquetes e carrosséis. | `npx skills add sergebulaev/instagram-skills` |

---

## 4. As 3 Skills Proprietárias da Startup (Sob Medida PT-BR + Registoo)

O que a comunidade **não** entrega pronto — nosso diferencial *outlier*:

1. **`pain-tree-growth`** *(para **`Fury`** + **`EDITH`**)*
   - Estrutura o **Banco Vivo `marketing/dores-e-subdores.md`**: `Dor Macro → Sub-dores reais → Linguagem literal do cliente → Abordagem TikTok vs. Instagram vs. YouTube → Oportunidade de Produto`.
   - Codifica o **Método das 4 Lentes** da `EDITH` com auto-refinamento semanal e tags `[FONTE VERIFICADA]` vs. `[SEM FONTE — REVISAR ANTES DE CITAR]`.
2. **`storytelling-ptbr-shortform`** *(para **`Hill`**)*
   - 5 frameworks de storytelling prontos para teste A/B medido pelo `Fury`: `Kishōtenketsu`, `3 Atos Curto`, `In Medias Res / POV`, `Crença Quebrada / Contrarian Loop` e `PAS/BAB Narrativo`.
   - Adaptação para português falado brasileiro (zero calque de copy americana), entrega obrigatória de **3 hooks de 0–3s**, blocos de direção prontos para a `Zoe`, **Sequências de Stories (3–5 telas)** e **Roteiro de YouTube**.
3. **`motion-studio-90-10`** *(para **`Zoe`**)*
   - **Manual de Estúdio de Motion 90/10** travado na identidade **Emerald Premium / Zen Tech** (`#00855D`, `#14B887`, `Instrument Sans` + `Inter`, nome público só **"Registoo"**, referência Apple/WhatsApp/Anthropic).
   - Árvore de decisão entre as **4 vertentes** (*Remotion / HTML+GSAP / Canvas / SVG*), margens seguras 9:16 do TikTok/Reels, proibição de clichês de IA, **Critique Loop visual obrigatório** (still frames antes do MP4) e registro de licença comercial (ElevenLabs voz Carolina `-16 LUFS` ou Google Cloud TTS `Chirp 3 HD` PT-BR).
