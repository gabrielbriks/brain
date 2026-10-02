---
date: 2026-09-30
area: empreendedor
type: ref
status: open
tags: [stripe, pagarme, gateway, pagamento, saas, billing, registoo, pictae, estrategia, infraestrutura]
---

# Stripe vs Pagar.me — Análise Estratégica de Gateway para o Portfólio SaaS

> Pesquisa realizada em 30/09/2026. Base: código-fonte real de Registoo e Pictae + documentação oficial do Pagar.me v5.
>
> **Próximo passo planejado:** Apurar o custo real de implementação dentro de cada projeto.

## Referências cruzadas nos projetos

- → [[_projeto/registoo/decisions/2026-09-30-gateway-pagamento-analise]] — Impacto e custo específico no Registoo
- → [[_projeto/pictae/insights/2026-09-30-gateway-pagamento-analise]] — Impacto e custo específico no Pictae

---

## 1. Como o Stripe está sendo usado hoje

### 🏥 Registoo Check — SaaS de Gestão de Clínicas/Profissionais de Saúde

**Natureza do produto:** Plataforma B2B para clínicas e consultórios gerenciarem pacientes, profissionais, evoluções clínicas e registros de ponto.

**Modelo de cobrança:**
- Assinatura recorrente mensal via Stripe Subscriptions
- 3 planos base: `basic`, `plus`, `pro` (+ `trial`, `enterprise`, `custom/VIP`)
- Add-ons vendidos por lotes sobre a assinatura:
  - Pacientes: lotes de 20 × R$29,00
  - Profissionais: lotes de 3 × R$49,00
  - Evoluções: packs S/M/L (R$19 / R$39 / R$89)

**Recursos do Stripe em uso:**

| Feature | Uso |
|---|---|
| Stripe Subscriptions | ✅ Core — planos + add-ons como itens da sub |
| Stripe PaymentIntent / Elements | ✅ Frontend (`@stripe/react-stripe-js`) |
| Stripe Webhooks | ✅ Completo com idempotência e lock de eventos |
| Stripe Customer Portal | ✅ Gestão de cartão/faturas (upgrades bloqueados intencionalmente) |
| Stripe Invoices | ✅ Histórico + upcoming invoice |
| Proration / Reconciliation | ✅ `proration_behavior: 'create_prorations'` |

**Webhooks mapeados:**
- `invoice.paid` / `invoice.payment_succeeded` → `PAYMENT_RECEIVED`
- `invoice_payment.paid` → `PAYMENT_RECEIVED` (com lookup da invoice)
- `invoice.payment_failed` → `PAYMENT_OVERDUE`
- `customer.subscription.deleted` → `SUBSCRIPTION_DELETED` + **churn analytics** (salva motivo, comentário, email da org)
- `customer.subscription.updated` → `SUBSCRIPTION_UPDATED`
- `charge.refunded` → `PAYMENT_REFUNDED`

**Arquitetura de billing (ponto-chave):**
- Interface `IPaymentGateway` → permite troca de provider sem alterar regras de negócio
- Providers implementados: `StripeProvider` (ativo) + `EfiBankProvider` (legado, off) + `AsaasClient` (morto, comentado)
- O `BillingService` usa injeção via construtor — **já está preparado para multi-gateway**

**Moeda:** R$ (BRL) — preços hardcoded em centavos

---

### 📸 Pictae — SaaS de Gestão de Galerias Fotográficas

**Natureza do produto:** Plataforma B2C/B2B para estúdios fotográficos entregarem galerias online com controle de armazenamento e retenção de fotos.

**Modelo de cobrança:**
- Assinatura recorrente mensal **ou anual** (com desconto)
- 3 planos base: `essential` (R$49,90/mês), `studio` (R$99,90/mês), `max`
- Planos VIP customizados por e-mail do estúdio (config YAML)
- Lógica **"Zen Tech Retain"**: não rebaixa limites quando `past_due`/`canceled`

**Recursos do Stripe em uso:**

| Feature | Uso |
|---|---|
| Stripe Subscriptions | ✅ Core — planos mensais + anuais |
| Stripe PaymentIntent / Elements | ✅ `PaymentElement` no frontend |
| Stripe Webhooks | ✅ Com `rawBody` buffer para validação de assinatura |
| Stripe Customer Portal | ✅ `createPortalSession()` |
| Annual / Monthly pricing | ✅ Price IDs separados por ciclo |
| VIP custom plans | ✅ Price ID via env var por plano VIP |

**Funcionalidade no backlog:**
- Integração com **Mercado Pago** para checkout alternativo (plano Studio)
- Pix manual (já existe como feature de plano, mas fora do Stripe)

**Moeda:** R$ (BRL)

---

## 2. O que o Pagar.me oferece (vs. Stripe)

### Meios de Pagamento

| Meio | Pagar.me | Stripe (BR) |
|---|---|---|
| Cartão de Crédito | ✅ | ✅ |
| Cartão de Débito | ✅ (Gateway only) | ✅ (limitado) |
| **Boleto Bancário** | ✅ nativo e maduro | ✅ (limitado, menos confiável) |
| **PIX** | ✅ nativo | ✅ (mais complexo de implementar) |
| Vouchers (VR, Sodexo, Ticket) | ✅ (Gateway only) | ❌ |
| **Parcelamento no cartão** | ✅ nativo | ✅ (requer config manual) |
| Multi-currency | ⚠️ Foco BR apenas | ✅ 135+ moedas |

### Assinaturas / Recorrência

| Feature | Pagar.me | Stripe |
|---|---|---|
| Recorrência pré-paga | ✅ | ✅ |
| Recorrência pós-paga | ✅ | ✅ (metered billing) |
| Cobrança em dia específico | ✅ | ✅ |
| Itens temporários na assinatura | ✅ | ✅ |
| Setup fee (taxa de matrícula) | ✅ | ✅ |
| Descontos por período | ✅ | ✅ (coupons) |
| **Add-ons / múltiplos itens variáveis** | ⚠️ Necessita workaround | ✅ nativo (usado no Registoo) |
| Trial gratuito | ✅ | ✅ |
| Proration | ❓ Não documentado claramente | ✅ nativo |
| **Customer Portal self-service** | ❌ Não existe | ✅ Billing Portal |

> ⚠️ **Limitação crítica do Pagar.me em assinaturas:** Não suporta múltiplos itens com atualização incremental. O Registoo descobriu isso empiricamente com o `EfiBankProvider` (mesmo modelo da API Efí, similar ao Pagar.me) e teve que consolidar tudo em um valor único, perdendo granularidade. O Stripe lida com isso nativamente via `proration_behavior`.

### DX e Infraestrutura

| Feature | Pagar.me | Stripe |
|---|---|---|
| SDK Node.js | ✅ | ✅ (DX superior) |
| Webhooks | ✅ | ✅ |
| Sandbox / Simuladores | ✅ | ✅ |
| Dashboard | ✅ | ✅ (mais completo) |
| Documentação | ⚠️ PT-BR, menos detalhada | ✅ Excelente, EN |
| Suporte técnico | ⚠️ Ticket-based | ✅ Chat + extensa base |
| Retentativa automática | ✅ | ✅ (Smart Retries) |

---

## 3. Análise Estratégica por Cenário

### 🇧🇷 Cenário A — SaaS 100% Brasileiro

| Critério | Stripe | Pagar.me | Vencedor |
|---|---|---|---|
| PIX nativo e maduro | ⚠️ Funciona, DX ruim | ✅ Nativo e sólido | **Pagar.me** |
| Boleto na assinatura | ⚠️ Limitado | ✅ Pleno | **Pagar.me** |
| Parcelamento em x vezes | ⚠️ Manual | ✅ Nativo | **Pagar.me** |
| Conversão de pagamentos BR | ⚠️ ~85% | ✅ ~92%+ | **Pagar.me** |
| Add-ons com múltiplos itens | ✅ Nativo + proration | ⚠️ Workaround necessário | **Stripe** |
| Customer Self-Service Portal | ✅ Billing Portal | ❌ Não tem | **Stripe** |
| DX / Ecossistema dev | ✅ Excelente | ⚠️ Aceitável | **Stripe** |
| Taxa por transação | ~3.4% + R$0,39 | ~2.49% + R$0,09 | **Pagar.me** |

> 📌 **Insight:** No Registoo e Pictae, atualmente apenas cartão de crédito é aceito na assinatura. Se os clientes forem PMEs/MEIs que preferem Boleto ou PIX, há uma lacuna real de conversão não capturada.

### 🌍 Cenário B — SaaS com Expansão Global

Para qualquer produto com ambição global, **Stripe não tem substituto viável**. O Pagar.me é 100% focado no Brasil — não processa moedas estrangeiras, não tem Apple/Google Pay global, não tem Stripe Tax, não tem Stripe Connect global.

### 🔀 Cenário C — SaaS Híbrido (BR principal + clientes estrangeiros)

Estratégia de **multi-gateway**:

```
         IPaymentGateway (interface já existe no Registoo!)
                  │
     ┌────────────┼────────────┐
     │            │            │
 Stripe       Pagar.me     Futuro...
(global +     (BR: PIX/
 card sub)     Boleto)
```

---

## 4. Recomendação por Produto

### Registoo
- **Manter Stripe** como gateway primário (proration, portal, add-ons multi-item)
- **Adicionar Pagar.me** como opção para Boleto + PIX via `PagarmeProvider` (a interface já existe)
- ⚠️ **Bloqueador para migração total:** Lógica de add-ons com múltiplos itens — Pagar.me exigiria consolidar o valor em um único item
- **Valor comercial:** Aumentar conversão em clínicas menores / MEIs que relutam em assinar via cartão

### Pictae
- **Candidato mais fácil** para experimentar Pagar.me (sem add-ons complexos)
- O público (fotógrafos / MEIs) tem alta adoção de PIX e boleto anual
- Pagar.me seria um consolidador mais robusto do que a integração avulsa com Mercado Pago que está no backlog

### Futuros Produtos

| Perfil do produto | Gateway recomendado |
|---|---|
| 🇧🇷 BR only, público popular/MEI | **Pagar.me principal** + Stripe opcional |
| 🇧🇷 BR, público enterprise/corporate | **Stripe** (DX, portal, UX premium) |
| 🌍 Global desde o início | **Stripe** (única opção real) |
| 🇧🇷+🌍 Híbrido | **Stripe global** + **Pagar.me para métodos BR** |
| Marketplace / Connect | **Stripe Connect** (Pagar.me tem versão limitada) |

---

## 5. Complexidade de Migração/Adição (Estimativa Inicial)

> ⚠️ Esta é uma estimativa macro. O custo real de implementação precisa ser apurado projeto a projeto — consulte as referências cruzadas dos projetos.

### Adicionar Pagar.me ao Registoo (sem remover Stripe)
**Esforço estimado: Médio (~2–3 semanas)**
- Criar `PagarmeProvider` implementando `IPaymentGateway` ✅ (estrutura já pronta)
- Mapear webhooks do Pagar.me → `UnifiedWebhookEvent` ✅ (padrão já existe)
- Adicionar lógica de seleção de gateway no `BillingService`
- ⚠️ Adaptar lógica de add-ons (consolidar valor único no Pagar.me)
- ⚠️ Pagar.me não tem Customer Portal → manter Stripe Elements para gestão de cartão

### Migrar Pictae para Pagar.me (Stripe out)
**Esforço estimado: Médio (~1–2 semanas)**
- Criar novo provider ou adaptar diretamente o `BillingService`
- Migrar clientes existentes (criar customers no Pagar.me)
- ⚠️ Subscriptions ativas no Stripe precisam ser canceladas e recriadas
- ✅ Ganho: PIX/Boleto nativos, taxa menor (~0.9% de diferença)

### Adicionar Pagar.me para PIX/Boleto no Pictae (Stripe permanece para cartão)
**Esforço estimado: Baixo (~1 semana)**
- Estratégia de menor risco: Stripe para assinaturas via cartão + Pagar.me para PIX/Boleto avulsos

---

## 6. Síntese — Matriz de Decisão

| # | Ação | Prioridade | Impacto |
|---|---|---|---|
| 1 | Manter Stripe no Registoo + explorar Pagar.me para Boleto/PIX | Médio prazo | ⬆️ Conversão |
| 2 | Avaliar substituição do Stripe pelo Pagar.me no Pictae | Curto prazo | ⬇️ Custo + ⬆️ PIX |
| 3 | Novos SaaS BR-only → começar com Pagar.me | Estratégico | ⬇️ Custo operacional |
| 4 | Novos SaaS com visão global → Stripe desde o dia 1 | Estratégico | 🌍 Alcance global |
| 5 | Criar shared lib `payment-gateway` reutilizável entre projetos | Longo prazo | ♻️ Reuso de código |
