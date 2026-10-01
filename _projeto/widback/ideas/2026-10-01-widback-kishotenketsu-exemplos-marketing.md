---
date: 2026-10-01
projeto: widback
type: idea
status: open
priority: medium
tags: [marketing, storytelling, kishotenketsu, copywriting, ads, landing-page, widback]
---

# widback — Rascunhos aplicando Kishotenketsu

## Contexto
O widback é uma solução de feedback/bug reporting para apps web. O diferencial: captura contexto automático (screenshot, console, network, device info) sem o usuário precisar descrever o bug tecnicamente.

Público-alvo: PMs, devs, QA, fundadores de SaaS que perdem tempo reproduzindo bugs.

---

## 1. Anúncio curto (Meta/LinkedIn/Twitter) — 90s de leitura

### Ki (Introdução)
> Seu usuário reportou: *"O botão não funciona"*
> 
> Sem screenshot. Sem steps. Sem console log. Só frustração.

### Sho (Desenvolvimento)
> Seu time gasta 40min só tentando reproduzir.
> Abre o Sentry — nada. Pergunta no Slack — "funciona aqui".
> O ticket vira "não reproduzível" e o bug continua lá.

### Ten (O Vira)
> E se o **próprio usuário** enviasse o bug **com tudo que você precisa** — screenshot, console, network, device, steps — **sem digitar uma linha de código**?

### Ketsu (Conclusão)
> widback. Feedback que chega pronto pra corrigir.
> 
> [Teste grátis 14 dias →]

---

## 2. Landing Page Hero + Abaixo da dobra

### Seção Hero (Ki + Sho)
**Headline:** Bugs que seu usuário vê, mas seu time não consegue reproduzir  
**Subhead:** O widback captura screenshot, console, network e device info automaticamente — no momento exato do erro. Zero atrito pro usuário. Contexto completo pro seu time.

---

### Abaixo da dobra — Bloco "Como funciona" (Sho expandido)
> **Hoje:** Usuário clica → erro → abre ticket → "não consigo reproduzir" → dev perde 1h → bug vive no backlog por semanas.
> 
> **Com widback:** Usuário clica → widget abre → 1 clique envia tudo → dev abre e vê exatamente o que aconteceu.

---

### Bloco "O diferencial" (Ten)
> **A maioria das ferramentas te dá o stack trace.**
> 
> **O widback te dá o contexto humano.**
> 
> Screenshot do momento exato. Cliques que antecederam. Request que falhou. Versão do app. Navegador. Tela. Tudo junto. Em um link.

---

### CTA Final (Ketsu)
> **Pare de caçar bugs. Comece a corrigir.**
> 
> Instale em 5 min. 14 dias grátis. Sem cartão.
> 
> [Começar agora →]

---

## 3. E-mail de onboarding (sequência de 3 e-mails)

### E-mail 1 — Dia 0 (Ki + Sho)
**Assunto:** Bem-vindo ao widback — seus bugs vão chegar prontos pra corrigir

> Oi [nome],
> 
> Sabe aquele bug que o usuário reporta e ninguém consegue reproduzir?
> 
> Você pede steps. Pede screenshot. Pede console. O usuário some. O ticket envelhece.
> 
> O widback nasceu exatamente pra acabar com esse ciclo.
> 
> Amanhã te mostro como funciona na prática.

---

### E-mail 2 — Dia 1 (Ten)
**Assunto:** O segredo não é o que você captura. É *quando* você captura.

> A maioria das ferramentas captura *depois* que o erro acontece.
> 
> O widback captura **no exato momento** em que o usuário sente a frustração — antes de fechar a aba, antes de esquecer os detalhes.
> 
> 1 clique. Screenshot + console + network + device + steps. Tudo num link que abre no seu dashboard.
> 
> Quer ver ao vivo? [Agenda 15 min comigo →]

---

### E-mail 3 — Dia 3 (Ketsu)
**Assunto:** De "não reproduzo" para "corrigido em 10 min" — case real

> Time da [empresa SaaS] usava 3 ferramentas pra debugar.
> 
> Trocou pro widback mês passado.
> 
> Resultado: **68% menos tempo** pra reproduzir bugs. 3 bugs críticos corrigidos no mesmo dia que chegaram.
> 
> O diferencial não foi a ferramenta. Foi o contexto que o usuário enviou *sem perceber que estava enviando*.
> 
> Quer o mesmo? [Ativar widback no seu app →]

---

## 4. Case study / Depoimento (formato kishotenketsu)

### Ki
> Rafael, CTO de uma fintech com 50k usuários, recebia 20+ tickets/semana de "bugs não reproduzíveis".

### Sho
> Seu time gastava 60% do tempo de debug só tentando entender *o que* aconteceu. Sentry mostrava o erro, mas não o caminho. Usuários não sabiam descrever.

### Ten
> Até instalar o widback e descobrir: **o bug não estava no código — estava no fluxo que só usuários reais faziam**. Um clique duplo rápido num botão de pagamento. O widback mostrou o request duplicado, o network timeout, e o device exato.

### Ketsu
> Hoje, 90% dos bugs chegam com contexto completo. Tempo médio de reprodução: **3 minutos**.
> 
> *"A gente parou de caçar fantasmas e voltou a shippar features."* — Rafael

---

## 5. Script de vídeo curto (30-45s) — Reels/TikTok/Shorts

| Tempo | Visual | Áudio/Texto | Fase |
|-------|--------|-------------|------|
| 0-3s | Dev olha tela confuso, ticket aberto: *"Botão não funciona"* | "Usuário: 'O botão não funciona'. Dev: 'Funciona aqui'." | Ki |
| 3-10s | Corte rápido: Slack, Sentry, Jira, calls, café frio | "40 min pra reproduzir. Nada. Ticket fechado 'não reproduzível'." | Sho |
| 10-18s | Animação: widget widback abre → 1 clique → pacote de dados voa pro dashboard | "E se o bug chegasse *com* screenshot, console, network, steps — sem o usuário digitar nada?" | Ten |
| 18-30s | Dev abre link, vê tudo, corrige, faz deploy, sorri | "widback. Feedback que chega pronto pra corrigir. Teste grátis." | Ketsu |

---

## 6. Headlines para testar (A/B)

| Variante | Headline (Ki + Ten condensados) |
|----------|----------------------------------|
| A | "Seu usuário viu o bug. Seu time não. O widback resolve isso." |
| B | "Bugs não reproduzíveis? O contexto que faltava chega em 1 clique." |
| C | "Pare de pedir screenshot. O widback captura pra você." |
| D | "O que o Sentry não te mostra: o que o usuário *fez* antes do erro." |

---

## Próximos passos
- [ ] Validar com 5-10 prospects qual ressoa mais
- [ ] Criar variações de Ten (surpresa) diferentes
- [ ] Testar em anúncios Meta/LinkedIn
- [ ] Adaptar para cold outreach (LinkedIn/email)
- [ ] Medir CTR e tempo de permanência na LP

---

> Baseado no framework Kishotenketsu (Ki-Sho-Ten-Ketsu) — estrutura narrativa japonesa de 4 partes sem depender de conflito como motor. Ver insight completo em `_area/pessoal/ideas/2026-10-01-kishotenketsu-storytelling-framework-marketing-saas.md`.
