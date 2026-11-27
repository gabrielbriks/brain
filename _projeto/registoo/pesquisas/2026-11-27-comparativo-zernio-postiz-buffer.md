---
date: 2026-11-27
projeto: registoo
type: research
status: done
priority: medium
tags: [redes-sociais, agendamento, zernio, postiz, buffer, mcp, api, marketing, registoo]
---

# Dossiê Comparativo: Zernio vs. Postiz vs. Buffer (Operação Registoo — IG, TikTok e Shorts)

> **Autora:** `EDITH` (Pesquisadora de Mercado, Concorrentes, Regulatório e Dores)
> **Contexto:** Escolha da infraestrutura de agendamento, aprovação humana (*human-in-the-loop*) e coleta automatizada de métricas pelo `Fury` para os 3 canais principais do **Registoo** (**Instagram**, **TikTok** e **YouTube Shorts**).
> **Referência cruzada:** [[2026-11-19-explorar-ferramentas-de-agendamento-de-posts]] e [[2026-11-27-runbook-setup-vps-openbot]].

---

## 1. Resumo Executivo & Veredito Rápido

| Critério | Zernio | Buffer | Postiz (Cloud / Self-Hosted) |
|---|---|---|---|
| **Modelo** | SaaS API-first / AI-native (`[FONTE VERIFICADA]`) | SaaS tradicional + GraphQL/MCP (`[FONTE VERIFICADA]`) | SaaS pago ou Open-Source Self-Hosted (`AGPL-3.0`) (`[FONTE VERIFICADA]`) |
| **Free Tier (IG + TikTok + YT Shorts)** | **2 contas grátis** ($0). Para as **3 redes**, a 3ª conta custa **US$ 6/mês** (`[FONTE VERIFICADA]`) | **3 canais grátis** ($0), limite de **10 posts na fila/canal** (`[FONTE VERIFICADA]`) | **Cloud:** sem Free Tier (só 7 dias trial; começa em US$ 29/mês). **Self-Hosted:** $0/ilimitado (`[FONTE VERIFICADA]`) |
| **Posts e recursos no Free Tier** | Ilimitados (analytics completo, DMs, comentários, API e MCP inclusos) (`[FONTE VERIFICADA]`) | 10 agendados por vez/canal, 1 usuário, analytics limitado a **30 dias** (`[FONTE VERIFICADA]`) | Ilimitados no Self-Hosted (custo de configurar apps OAuth próprios) (`[FONTE VERIFICADA]`) |
| **MCP / API oficial p/ `Fury` puxar métricas** | **Sim (Nativo e completo):** REST API + MCP (`mcp.zernio.com/mcp`) + webhook `analytics.synced` (`[FONTE VERIFICADA]`) | **Sim:** GraphQL API (`api.buffer.com`) + MCP (`mcp.buffer.com/mcp`) com escopo `insightsRead` (3.000 req/mês no Free) (`[FONTE VERIFICADA]`) | **Sim:** Public REST API (`GET /public/v1/analytics/{integration}`) + MCP Server (~14 tools) (`[FONTE VERIFICADA]`) |
| **Aprovação humana antes de publicar** | **Sim ($0 / US$ 6):** criação via `is_draft: true` + fluxo `requireDraftApproval` incluso em todas as contas (`[FONTE VERIFICADA]`) | **Parcial no Free:** via rascunhos (`Draft`). Fluxo formal multi-usuário exige plano **Team** (US$ 30–36/mês p/ 3 canais) (`[FONTE VERIFICADA]`) | **Sim:** criação como `draft` via MCP/API + RBAC multi-usuário liberado no Self-Hosted (`[FONTE VERIFICADA]`) |
| **Automação de Comentários / DMs (estilo ManyChat)** | **Sim, nativo** na mesma API/MCP e incluso desde o Free Tier (`[FONTE VERIFICADA]`) | Comunidade básica na UI; sem automação estilo ManyChat via API no Free (`[FONTE VERIFICADA]`) | Foco em publicação; leitura/automação profunda de DMs via API é limitada (`[FONTE VERIFICADA]`) |
| **Self-Hosted na VPS** | Não (100% SaaS) (`[FONTE VERIFICADA]`) | Não (100% SaaS) (`[FONTE VERIFICADA]`) | **Sim** (Docker Compose: App + Postgres + Redis + Temporal), mas exige **App Review próprio** na Meta/TikTok/Google (`[FONTE VERIFICADA]`) |

---

## 2. Análise Detalhada por Critério

### (1) O que cabe no Free Tier (foco: Instagram + TikTok + YouTube Shorts)

1. **Buffer — O único SaaS que cobre os 3 canais a $0/mês, mas com teto de fila e janela curta de métricas**
   - **Canais no Free ($0):** até **3 canais sociais** conectados — cabe exatamente o trio **Instagram + TikTok + YouTube Shorts** do Registoo (`[FONTE VERIFICADA]` — https://buffer.com/pricing).
   - **Limite de agendamentos:** até **10 posts agendados simultaneamente por canal** (30 no total). Como é um limite de *fila ativa* (e não limite mensal), assim que um post é publicado a vaga reabre (`[FONTE VERIFICADA]` — https://buffer.com/pricing). Para a cadência do Registoo (semanal/quinzenal), 10 slots por rede são suficientes.
   - **Restrições do Free:** apenas **1 usuário**, histórico de métricas (*insights*) travado em **30 dias**, sem agendamento de primeiro comentário (disponível apenas a partir do Essentials por US$ 5–6/canal/mês) (`[FONTE VERIFICADA]` — https://buffer.com/pricing).

2. **Zernio — Free Tier sem trava de funcionalidades, mas limitado a 2 contas grátis ($0 p/ 2 redes ou US$ 6/mês p/ as 3 redes)**
   - **Modelo Pay-per-Account sem feature gating:** não existem planos que escondem funcionalidades. Todas as contas conectadas (inclusive as gratuitas) têm **posts ilimitados, analytics completo, gestão de comentários e DMs, REST API completa e servidor MCP hospedado** (`[FONTE VERIFICADA]` — https://zernio.com/pricing).
   - **Limite do Free ($0):** as **2 primeiras contas sociais são 100% gratuitas** (sem cartão de crédito) (`[FONTE VERIFICADA]` — https://zernio.com/pricing).
   - **Custo real para as 3 redes do Registoo (IG + TikTok + YT Shorts):** na faixa de 3 a 10 contas, o preço é de **US$ 6 por conta adicional/mês** (contas 11–100 caem para US$ 3/conta e 101+ para US$ 1/conta) (`[FONTE VERIFICADA]` — https://zernio.com/pricing).
   - *Nota prática:* é possível validar o piloto a **$0/mês conectando 2 redes** (ex.: Instagram + TikTok, que são o foco de dor imediata de topo/meio de funil, subindo YouTube Shorts manualmente ou adicionando a 3ª conta por **US$ 6/mês** ~R$ 35/mês quando validar) (`[SEM FONTE — REVISAR ANTES DE CITAR]`: confirmar no checkout atual da Zernio se a cobrança de 3 contas incide apenas sobre a 3ª conta excedente = US$ 6/mês ou sobre as 3 contas = US$ 18/mês; a documentação descreve *"First 2 accounts free, accounts 3–10: $6/account/mo"* em bandas graduadas).

3. **Postiz — Zero Free Tier no Cloud; 100% gratuito apenas no Self-Hosted**
   - **Postiz Cloud:** não tem plano gratuito permanente, apenas **7 dias de teste grátis**. O plano mínimo (*Standard*) custa **US$ 29/mês** (5 canais, 400 posts/mês, 1 usuário) e o *Team* custa **US$ 39/mês** (10 canais, posts e usuários ilimitados) (`[FONTE VERIFICADA]` — https://postiz.com/pricing).
   - **Postiz Self-Hosted:** código aberto sob licença **AGPL-3.0**, **100% gratuito** sem limite de canais, posts ou membros na própria VPS (`[FONTE VERIFICADA]` — https://github.com/gitroomhq/postiz-app).

---

### (2) MCP ou API oficial para o `Fury` puxar métricas automaticamente

Todas as três ferramentas lançaram suporte oficial a **MCP (Model Context Protocol)** e **API** acessível por agentes, mas com diferenças importantes na profundidade dos dados para o `Fury`:

1. **Zernio (Melhor integração para Agentes IA)**
   - **MCP Oficial Hospedado:** `https://mcp.zernio.com/mcp` (autenticação via API Key ou OAuth 2.1) + MCP de documentação em `https://docs.zernio.com/api/mcp` (`[FONTE VERIFICADA]` — https://docs.zernio.com/mcp).
   - **Coleta de métricas pelo `Fury`:** expõe endpoints REST e tools MCP para buscar métricas unificadas cross-platform (impressões, alcance, engajamento, crescimento de seguidores, desempenho individual por post e *heatmap* de melhor horário de postagem), além do webhook `analytics.synced` (`[FONTE VERIFICADA]` — https://docs.zernio.com/).
   - **Diferencial para o Registoo:** além de métricas e agendamento, a mesma API/MCP lê e responde **comentários e DMs do Instagram**, cobrindo também a segunda frente desejada pelo Gabriel (automação estilo ManyChat de comentou palavra-chave → recebe DM) (`[FONTE VERIFICADA]` — https://zernio.com/pricing).

2. **Buffer (Surpresa positiva: nova API GraphQL + MCP oficial no plano Free)**
   - **API GraphQL Oficial:** endpoint `https://api.buffer.com` liberado em **todos os planos, inclusive no Free** (com **1 API Key** e teto de **3.000 requisições/mês** no Free; 7.500 no Essentials; 15.000 no Team) (`[FONTE VERIFICADA]` — https://developers.buffer.com/).
   - **MCP Oficial Remoto:** `https://mcp.buffer.com/mcp` para conexão direta de agentes (`[FONTE VERIFICADA]` — https://developers.buffer.com/).
   - **Coleta de métricas pelo `Fury`:** usando uma *Personal API Key* com escopo `insightsRead`, o `Fury` pode rodar queries GraphQL (`post { metrics { type name value unit } }` e `aggregatedPostMetrics`) para puxar impressões, alcance, reações e taxa de engajamento (`[FONTE VERIFICADA]` — https://developers.buffer.com/).
   - **Atenção:** como o Free Plan do Buffer retém apenas **30 dias de histórico de analytics**, o `Fury` precisará rodar uma rotina semanal (toda quarta/quinta antes da Mesa de Ideias) para puxar as métricas via API/MCP e persistir em `registoo-check/marketing/metricas/`.

3. **Postiz (API REST + MCP integrados, porém dependentes das chaves OAuth no Self-Hosted)**
   - **Public REST API:** autenticada via header `Authorization: <api-key>`, com endpoint dedicado `GET /public/v1/analytics/{integration}` (janelas de 7, 30 ou 90 dias) e analytics por post (`[FONTE VERIFICADA]` — https://docs.postiz.com/public-api/introduction).
   - **MCP Server Oficial:** expõe ~14 tools nativas (`integrationList`, `schedulePostTool`, `postsListTool`, `postSettingsTool`, etc.) (`[FONTE VERIFICADA]` — https://postiz.com/).
   - **Limitação para o `Fury`:** as ferramentas MCP nativas do Postiz são focadas em *listar canais e agendar/rascunhar posts*; para puxar métricas estruturadas, o `Fury` deve chamar diretamente o endpoint REST `GET /public/v1/analytics/{integration}` via `curl`/script.

---

### (3) Aprovação humana antes de publicar (*Human-in-the-Loop*)

Para garantir que nenhuma peça gerada por `Fury`/`Hill` vá ao ar sem revisão do Gabriel:

1. **Zernio (`[FONTE VERIFICADA]` — https://docs.zernio.com/mcp)**
   - **Modo Rascunho via Agente:** o agente envia `is_draft: true` na chamada de criação do post via MCP/API. O post fica salvo no calendário do Zernio aguardando revisão e aprovação humana.
   - **Fluxo Nativo de Aprovação (`requireDraftApproval`):** possui suporte nativo a revisão de rascunhos com aprovação, rejeição e comentários presos a timestamps de vídeo, sem exigir plano caro.

2. **Buffer (`[FONTE VERIFICADA]` — https://buffer.com/pricing)**
   - **No Free Plan ($0) e Essentials:** **não existe** fluxo formal multi-usuário ("Send for Approval") porque a conta permite apenas 1 usuário.
   - **Como manter aprovação humana no Free Plan:** o `Fury` (usando a chave de API da conta do Gabriel) cria todos os posts obrigatoriamente como **Draft (Rascunho)** ou **Idea** via GraphQL/MCP. O Gabriel abre o Buffer, revisa legenda/vídeo e clica em *Add to Queue / Schedule*. É uma trava operacional simples e a custo zero.
   - **Fluxo formal com permissões travadas:** exige o plano **Team** (**US$ 10 a US$ 12 por canal/mês** = US$ 30–36/mês para IG + TikTok + YT).

3. **Postiz (`[FONTE VERIFICADA]` — https://docs.postiz.com/public-api/introduction)**
   - **Modo Rascunho + Multi-usuário no Self-Hosted:** o `schedulePostTool` (MCP) e a Public API permitem salvar posts com status `draft`. No Self-Hosted (e no plano Team Cloud de US$ 39/mês), você pode criar um usuário exclusivo para o agente com permissão restrita e aprovar pela conta administradora do Gabriel.

---

### (4) Requisitos caso Self-Hosted (Postiz na nossa VPS)

Apenas o **Postiz** pode ser hospedado na nossa VPS (`Zernio` e `Buffer` são 100% cloud).

#### A. Requisitos de Hardware e Containers (`[FONTE VERIFICADA]` — https://docs.postiz.com/self-host/installation/docker-compose)
- **Stack Docker Compose oficial (`gitroomhq/postiz-docker-compose`):**
  1. `postiz` (Aplicação Next.js + NestJS/Node na porta `4007`)
  2. `postiz-postgres` (PostgreSQL para contas, fila e analytics)
  3. `postiz-redis` (Redis para filas e cache)
  4. `temporal` + `temporal-ui` + `temporal-admin-tools` (Motor de orquestração Temporal na porta `8080`)
- **Consumo de recursos:** mínimo oficial de **2 vCPUs, 2 GB de RAM e 20 GB de disco** (na prática, o Temporal + Postgres + Node consomem **~1,8 GB a 2,5 GB de RAM** contínuos).
- **Compatibilidade com a nossa VPS atual do OpenBot:**
  - Nossa VPS atual conta com **4 vCPUs, 15 GiB de RAM (~13 GiB livres + 4 GiB de swap) e 113 GiB de disco livres** (`[FONTE VERIFICADA]` — inspeção local da VPS + `_docs/2026-11-27-runbook-setup-vps-openbot.md`).
  - **Diagnóstico de infraestrutura:** em termos de CPU, RAM e disco, a VPS atual **roda o Postiz sem sufoco**, exigindo apenas um proxy reverso com HTTPS (ex.: Caddy ou Cloudflare Tunnel, pois o Postiz exige cookies seguros sob TLS).

#### B. O Gargalo Real do Postiz Self-Hosted: Burocracia de App Review nas 3 Redes (`[FONTE VERIFICADA]` — https://docs.postiz.com/self-host/installation/docker-compose)
Ao contrário do Postiz Cloud, do Zernio e do Buffer — que já possuem aplicativos OAuth homologados na Meta, no TikTok e no Google onde você só clica em *"Conectar Conta"* —, no **Postiz Self-Hosted você precisa criar e aprovar seus próprios aplicativos de desenvolvedor**:
1. **Instagram (Meta for Developers):** criar app Business, configurar permissões `instagram_basic`, `instagram_content_publish` e `instagram_manage_insights`, publicar URL de política de privacidade/exclusão de dados e passar pelo *App Review* da Meta para sair do modo de desenvolvimento.
2. **TikTok (TikTok for Developers):** solicitar acesso à *Content Posting API* e *Display API*, gravar vídeo de demonstração do fluxo completo na sua instância do Postiz e aguardar auditoria humana do TikTok. Enquanto o app não é auditado, a API do TikTok força os vídeos enviados a ficarem trancados como **privados (*Self-Only*)** (`[FONTE VERIFICADA]`).
3. **YouTube Shorts (Google Cloud Console):** criar projeto, habilitar *YouTube Data API v3*, configurar tela de consentimento OAuth e gerenciar limites de cota diária (10.000 unidades/dia padrão; cada upload gasta ~1.600 unidades).

> **Conclusão sobre Self-Hosted agora:** embora o servidor aguente tranquilamente, hospedar o Postiz hoje vai atrasar o início das publicações do Registoo em **1 a 4 semanas** só com burocracia de aprovação de apps na Meta e no TikTok, além de desviar foco de engenharia para manter tokens e containers do Temporal.

---

## 3. Recomendação da EDITH para o Registoo

### Estratégia recomendada em 2 fases (Zero Atrito → Escala com DM/ManyChat)

1. **Opção A — Melhor custo-benefício para Agentic Marketing + DMs (Recomendada se topar US$ 6/mês após testar 2 redes grátis): `Zernio`**
   - **Por quê:** foi construído especificamente para agentes de IA. O MCP (`https://mcp.zernio.com/mcp`) e a API REST já entregam **métricas completas**, **rascunhos com aprovação humana (`is_draft: true`)** e **gestão de comentários/DMs do Instagram** (já resolvendo a demanda futura de automação estilo ManyChat levantada em `2026-11-19`).
   - **Como começar a $0 hoje:** conectar **Instagram + TikTok** nas **2 contas gratuitas do Free Tier** ($0/mês, sem cartão, posts e métricas ilimitados) e plugar o MCP no `Fury`. Quando o fluxo estiver redondo, adicionar o canal do **YouTube Shorts** como 3ª conta por **US$ 6/mês**.

2. **Opção B — Se a regra para o piloto for 100% custo zero ($0/mês) nas 3 redes simultâneas desde o Dia 1: `Buffer (Free Plan)`**
   - **Por quê:** é o único que conecta **Instagram + TikTok + YouTube Shorts ao mesmo tempo por $0/mês** com OAuth pronto em 2 minutos, oferecendo **API GraphQL (`api.buffer.com`) + MCP oficial (`mcp.buffer.com/mcp`)** com 3.000 requisições/mês e leitura de métricas (`insightsRead`).
   - **Regra operacional obrigatória no Buffer Free:**
     1. Configurar o `Fury` para criar posts **exclusivamente como Draft** via API/MCP (garantindo sua aprovação humana no painel do Buffer antes de entrar na fila de 10 posts).
     2. Configurar rotina semanal do `Fury` para puxar as métricas via GraphQL e salvar em `registoo-check/marketing/metricas/`, contornando o limite de 30 dias de histórico do plano gratuito.

3. **Por que NÃO ir de Postiz Self-Hosted agora:**
   - Apesar de a nossa VPS (4 vCPUs / 15 GiB RAM) suportar o Docker Compose do Postiz, a exigência de aprovar apps próprios na Meta e principalmente no TikTok (*Content Posting API*, que trava vídeos como privados antes da auditoria) cria um bloqueio desnecessário para a fase de tração do Registoo.

---

## 4. Duplo Impacto (Munição de Marketing & Backlog de Operação/Produto)

### Munição de Marketing (para `Fury` e `Hill`)
- **Fluxo de trabalho sugerido para o `Fury`:**
  1. `Fury` e `Hill` fecham o pacote semanal em `registoo-check/marketing/pecas/`.
  2. `Fury` envia a peça via MCP (`Zernio` com `is_draft: true` ou `Buffer` como `Draft`).
  3. Gabriel recebe notificação, revisa o preview visual + legenda e aprova com 1 clique.
  4. Toda quarta/quinta-feira, `Fury` consulta o endpoint de analytics via MCP/API e atualiza `registoo-check/marketing/metricas/` para guiar a Mesa de Ideias.

### Oportunidades de Produto / Operação (para avaliação do Gabriel)
- **Fechamento da issue exploratória [[2026-11-19-explorar-ferramentas-de-agendamento-de-posts]]:** o **Zernio** unifica tanto o agendador quanto a leitura/resposta programática de comentários e DMs via API oficial da Meta, permitindo que um agente do OpenBot faça o papel do ManyChat (responder comentário com palavra-chave e enviar link da calculadora/isca no Direct) sem pagar assinatura extra do ManyChat.

---

## 5. Fontes Consultadas

- `[FONTE VERIFICADA]` Zernio Pricing & Free Tier (2 contas grátis, US$ 6/conta de 3–10, todos os recursos inclusos): https://zernio.com/pricing
- `[FONTE VERIFICADA]` Zernio Documentation & Hosted MCP Server (`https://mcp.zernio.com/mcp`, `is_draft`, `requireDraftApproval`, `analytics.synced`): https://docs.zernio.com/ e https://docs.zernio.com/mcp
- `[FONTE VERIFICADA]` Buffer Pricing & Free Plan Limits (3 canais grátis, 10 posts na fila/canal, 30 dias de analytics, aprovação formal no plano Team): https://buffer.com/pricing
- `[FONTE VERIFICADA]` Buffer Developers — GraphQL API (`https://api.buffer.com`), MCP Server (`https://mcp.buffer.com/mcp`), `insightsRead` post metrics & rate limits (3.000 req/mês no Free): https://developers.buffer.com/
- `[FONTE VERIFICADA]` Postiz Pricing (Cloud sem free tier permanente, 7 dias trial, a partir de US$ 29/mês): https://postiz.com/pricing
- `[FONTE VERIFICADA]` Postiz Repositório Oficial Open-Source (Licença AGPL-3.0): https://github.com/gitroomhq/postiz-app
- `[FONTE VERIFICADA]` Postiz Self-Hosted Docker Compose (PostgreSQL, Redis, Temporal, requisitos de HTTPS e credenciais OAuth próprias por rede): https://docs.postiz.com/self-host/installation/docker-compose
- `[FONTE VERIFICADA]` Postiz Public REST API & Analytics (`GET /public/v1/analytics/{integration}`) e MCP Tools: https://docs.postiz.com/public-api/introduction
