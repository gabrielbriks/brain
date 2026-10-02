---
date: 2026-09-30
projeto: registoo
type: decision
status: open
tags: [stripe, pagarme, gateway, pagamento, billing, decisao]
---

# Gateway de Pagamento — Análise e Próximos Passos (Registoo)

> Referência completa: [[_area/empreendedor/refs/2026-09-30-stripe-vs-pagarme-gateway-saas]]

## Contexto

O Registoo usa Stripe como gateway primário com uma arquitetura de billing avançada:
- Interface `IPaymentGateway` com providers plugáveis (já multi-gateway ready)
- Add-ons com múltiplos itens de assinatura (pacientes, profissionais, evoluções)
- Webhook controller com idempotência e lock de eventos
- Stripe Billing Portal para gestão de cartão pelo cliente

## Decisão em Aberto

Avaliar a adição do **Pagar.me como provider secundário** para aceitar PIX e Boleto — sem remover o Stripe.

## Pontos Críticos para Apuração de Custo

- [ ] A lógica de add-ons multi-item (`patients` + `professionals` + `evolutions` como itens separados na sub) **não tem equivalente no Pagar.me** — exigiria consolidar em valor único. Qual o impacto real no modelo de cobrança?
- [ ] O Customer Portal do Stripe (autoatendimento de cartão/faturas) não existe no Pagar.me — o que precisaria ser construído internamente para substituir?
- [ ] Avaliar se o público-alvo atual (clínicas, consultórios) realmente converte melhor com PIX/Boleto — ou se é só cartão mesmo.
- [ ] Estimar custo de manutenção de dois gateways simultâneos (dois conjuntos de webhooks, dois providers, dois customer IDs por organização).

## Estimativa Macro de Esforço

| Cenário | Esforço |
|---|---|
| Adicionar Pagar.me como provider alternativo (PIX/Boleto) | ~2–3 semanas |
| Migração total para Pagar.me | ❌ Não recomendada (bloqueador: add-ons) |
