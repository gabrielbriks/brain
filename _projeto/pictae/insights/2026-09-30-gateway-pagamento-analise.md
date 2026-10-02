---
date: 2026-09-30
projeto: pictae
type: insight
status: open
tags: [stripe, pagarme, gateway, pagamento, billing, pix, boleto]
---

# Gateway de Pagamento — Análise e Próximos Passos (Pictae)

> Referência completa: [[_area/empreendedor/refs/2026-09-30-stripe-vs-pagarme-gateway-saas]]

## Contexto

O Pictae usa Stripe com um modelo mais simples que o Registoo — sem add-ons multi-item. Planos mensais e anuais, com Price IDs separados por ciclo. O backlog já menciona integração com Mercado Pago como feature do plano Studio.

## Por que o Pictae é o candidato mais fácil para Pagar.me

- Sem add-ons complexos → migração mais direta
- Público (fotógrafos / MEIs) tem alta adoção de PIX e boleto
- Planos anuais com boleto bancário são comuns no mercado BR de ferramentas para fotógrafos
- Pagar.me substituiria a integração avulsa com Mercado Pago que está no backlog — de forma mais robusta

## Decisão em Aberto

Escolher entre três estratégias:

1. **Migração total:** Substituir Stripe pelo Pagar.me (assinaturas + PIX/Boleto)
2. **Híbrido:** Stripe para cartão + Pagar.me para PIX/Boleto avulsos
3. **Status quo:** Continuar com Stripe, implementar Mercado Pago do backlog como planejado

## Pontos Críticos para Apuração de Custo

- [ ] Mapear quais clientes ativos têm assinaturas no Stripe — qual o impacto de migrar (cancelar + recriar no Pagar.me)?
- [ ] O Pagar.me não tem Customer Portal — o que precisaria ser construído internamente?
- [ ] Qual o impacto real da diferença de taxa (~0.9%) no volume atual do Pictae? Vale o custo de migração?
- [ ] Avaliar se o plano anual via boleto é demanda real dos fotógrafos ou só suposição.

## Estimativa Macro de Esforço

| Cenário | Esforço |
|---|---|
| Adicionar Pagar.me para PIX/Boleto (Stripe permanece para cartão) | ~1 semana |
| Migração total para Pagar.me | ~1–2 semanas + risco de migração de clientes |
