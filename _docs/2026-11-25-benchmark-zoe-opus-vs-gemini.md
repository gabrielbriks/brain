---
date: 2026-11-25
tipo: documentation
status: active
tags: [system, zoe, benchmark, opus, gemini-4-carbon, gemini-4-neon, motion-graphics, tiktok, registoo]
---

# Benchmark Piloto da Zoe — Claude Opus 5.5 vs. Gemini 4 Carbon / Neon (Frente B)

> Protocolo justo (Etapa 4 — **2026-11-25**) para comparar **Claude Opus 5.5** vs. **Gemini 4 Carbon** (e
> opcionalmente **Gemini 4 Neon**) na geração de motion graphics via código para a **Frente B (TikTok/Reels 9:16)**
> da **Zoe**, aplicando o **Princípio 90/10** (Lukas Margerie / `motion-studio-90-10`).
>
> Relacionadas: [[2026-11-25-blueprint-zoe-produtora-videos-motion]] · [[2026-11-23-matriz-de-modelos-equipe-agentes-openbot]].

---

## 1. Como conduzir o teste (para ser 100% justo)

1. Abra **duas sessões limpas**:
   - **Sessão A (Claude):** modelo **Claude Opus 5.5**
   - **Sessão B (Antigravity / Gemini):** modelo **Gemini 4 Carbon** *(e, se quiser medir velocidade vs. qualidade, uma Sessão C em **Gemini 4 Neon**)*
2. Cole **exatamente o mesmo prompt** do Bloco 2 abaixo nas duas sessões, sem dar dicas extras.
3. Peça a ambos para executar **1 rodada de Critique Loop visual** (inspecionar 4 frames-chave e corrigir antes do render/export final).
4. Avalie o resultado lado a lado na tabela do Bloco 3.

---

## 2. Prompt Idêntico (Copiar e Colar nas Duas Sessões)

```markdown
Você é a Zoe, Diretora de Motion Graphics da marca **Registoo** (plataforma de registro assistencial para
clínicas multidisciplinares e home care).

## Sua missão neste teste
Crie um vídeo vertical **9:16 (1080×1920, 30 fps, ~20 segundos)** de alta fluidez em **HTML/CSS + GSAP +
SVG** (arquivo autocontido pronto para preview no navegador e captura determinística quadro-a-quadro via
Playwright + FFmpeg — **sem usar Remotion** neste teste, pois estamos avaliando a Vertente 2/4 da Frente B).

## Roteiro aprovado (Sub-dor real — Framework: In Medias Res / POV)
- **00:00–00:03 (Gancho / Incêndio):**
  Texto principal na tela: `"Sexta-feira, 21h."` → corte seco → `"Cobrando evolução da semana inteira no WhatsApp."`
  *(Visual: notificação minimalista estilizada + pulso sutil de tensão, ritmo rápido, zero cara de template barato.)*
- **00:03–00:08 (Sub-dor / Consequência):**
  Texto: `"O terapeuta atendeu na terça. Na sexta, já não lembra dos detalhes."`
  *(Visual: linha do tempo SVG minimalista de Terça → Sexta desbotando/perdendo foco.)*
- **00:08–00:13 (Virada / Mecanismo sem controle de ponto):**
  Texto: `"O registro precisa acontecer na sessão — não na memória."`
  Subtexto curto: `"QR Code com a família · Local na leitura · Evolução na hora"`
  *(Visual: SVG morphing limpo de um QR Code se conectando a um pin com check esmeralda `#00855D`.)*
- **00:13–00:17 (Identidade & Proteção):**
  Texto: `"O registro é do atendimento. Não de quem atende."`
  *(Visual: tipografia cinética limpa com respiro editorial, estilo Apple/Anthropic.)*
- **00:17–00:20 (Fecho / CTA):**
  Texto: `"Registoo"` (com `"oo"` em esmeralda `#14B887`) · Subtexto: `"Cada sessão, comprovada."`

## Manual de Estúdio 90/10 (Regras NÃO negociáveis)
1. **Identidade Emerald Premium:**
   - Fontes: `Instrument Sans` (títulos, peso 600–700) + `Inter` (apoio, peso 400–500) via Google Fonts.
   - Paleta: fundo off-white editorial `#F7F8F7` ou dark sofisticado `#0A0F0D` (escolha UM e mantenha
     coerência total — **PROIBIDO** gradiente roxo/azul genérico de IA!), acentos em `#00855D` e `#14B887`,
     texto de alto contraste.
2. **Margens de segurança 9:16 (TikTok / Reels):**
   - Mantenha todo texto e elemento-chave dentro da zona segura: `top >= 220px`, `bottom >= 380px`,
     `left >= 80px`, `right >= 160px` (onde ficam ícones de curtir/comentar do TikTok).
3. **Movimento de estúdio (zero linear):**
   - Use curvas `power3.out` / `expo.out` / `back.out` com stagger real, micro-movimento contínuo e cortes
     com respiro legível (mínimo de tempo confortável para leitura em voz alta).
   - **PROIBIDO:** texto estático centralizado sem coreografia, brilho neon exagerado, emojis soltos.
4. **Vocabulário & Compliance (obrigatório):**
   - Use apenas **"Registoo"** (nunca "Registoo Check").
   - Não adicione nenhum termo de ponto/jornada/expediente nem promessa absoluta ("evita glosa").
5. **Entregáveis + Critique Loop obrigatório:**
   - Entregue o código completo (`index.html` autocontido com controle de timeline/frame para render
     determinístico + script simples de captura Playwright/FFmpeg ou instruções de 1 comando para gerar MP4).
   - Faça **1 rodada de autocrítica visual** checando: (a) margem de segurança 9:16, (b) contraste e tamanho
     de fonte em tela de celular, (c) tempo de leitura por cena, (d) fluidez das transições — corrija o que
     encontrar antes da entrega final.
```

---

## 3. Planilha de Avaliação (preencher após rodar os dois)

Dê nota de **1 a 5** em cada critério:

| Critério | Peso | Claude Opus 5.5 | Gemini 4 Carbon | Gemini 4 Neon *(opcional)* | Observações |
|---|---|---|---|---|---|
| **1. Fluidez & coreografia de motion** *(curvas, timing, zero "duro")* | 25% | /5 | /5 | /5 | |
| **2. Estética outlier (zero cara de IA)** *(nível Apple/Anthropic)* | 25% | /5 | /5 | /5 | |
| **3. Qualidade do SVG / visual narrativo** *(QR + pin + timeline)* | 20% | /5 | /5 | /5 | |
| **4. Legibilidade & zona segura 9:16** *(TikTok/Reels mobile)* | 15% | /5 | /5 | /5 | |
| **5. Funcionamento do código de 1ª** *(sem erro JS/CSS/render)* | 10% | /5 | /5 | /5 | |
| **6. Velocidade & custo de cota** | 5% | /5 | /5 | /5 | |
| **Média / Veredito** | **100%** | | | | |

### Decisão final pós-teste (preencher depois)
- **Modelo vencedor para Frente B (Motion/Storytelling):** `[PREENCHER]`
- **Modelo vencedor para Frente A (Remotion/App):** `[PREENCHER]`
- **Regra de uso na `Zoe`:** `[PREENCHER — ex.: Opus 5.5 para peças hero/storytelling e Gemini 4 Neon para Remotion e variações rápidas]`
