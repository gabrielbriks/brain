---
date: 2026-11-20
area: financeiro
type: log
status: open
tags: [custos, saas, infraestrutura, openbot, planejamento, registoo, pictae]
---

# Gestão dos custos mensais dos apps (levantamento a fazer)

> Pedido do Gabriel em 2026-11-20: começar a gerenciar os custos mensais ligados aos apps. Um agente do
> OpenBot (ou o Claude Code) pode ajudar a consolidar e acompanhar. **Os valores ainda não foram
> levantados**: esta nota é o esqueleto.

## Já sabemos (de conversas desta semana)

| Item | Valor | Observação |
|---|---|---|
| PrimeClaws (Hermes) | US$ 9,99/mês | **Cancelado em 2026-11-20** por falha de pagamento |
| Servidor do OpenBot (candidato) | ~R$ 50–55/mês | Hostinger KVM 4, promoção de 24 meses (preço de terceiros); renovação citada ~R$ 130 |
| Servidor do OpenBot (alternativa) | €16,49/mês | Hetzner CX43, por hora |
| Chaves de API com teto | US$ 20–30/mês | Teto sugerido para a Fase 0 |
| Licença comercial do OpenBot | desconhecido | Plano Starter, 1 pessoa; preço só dentro do app |
| Azure (crédito da empresa) | crédito mensal | Já consumido em parte por bancos de dados e outros recursos; ver o consumo real no Cost analysis |

## O que levantar (por projeto)

Para cada item: serviço, valor, moeda, dia de cobrança, forma de pagamento, projeto que usa, e se dá
para cortar.

- **Registoo**: hospedagem (Railway), banco, e-mail (Resend e o domínio `ola.`), Stripe (taxas), domínio,
  IA, ferramentas de vídeo e design.
- **Pictae, Historuja, Widback, Zenckup**: hospedagem, banco, armazenamento (R2), domínios.
- **Transversais**: GitHub, IAs (Claude, Google AI Pro, outras), domínios, ferramentas de agendamento
  de posts (ver a ideia de Postiz, Zernio e Buffer).

## Passos

1. Listar as faturas dos últimos 3 meses (cartão, Railway, Azure, Cloudflare, Stripe, Resend, Google, Anthropic).
2. Preencher a tabela acima por projeto, em moeda original e em reais.
3. Marcar cobranças **sem alerta de falha de pagamento** (o caso da PrimeClaws): ativar um segundo cartão
   ou e-mail de aviso em cada serviço crítico.
4. Definir um **teto mensal** por projeto e para a exploração de IA e agentes.
5. Decidir a rotina: revisão mensal, possivelmente por um agente que leia um arquivo de custos
   mantido à mão (nunca dar ao agente acesso a cartão ou banco).

## Cuidados

- Dados financeiros são sensíveis: não colar números de cartão, tokens ou faturas completas em notas.
- Esta área (`_area/financeiro`) fica **fora do alcance** do agente do OpenBot no piloto
  (ver `_docs/2026-11-20-agente-secretario-do-brain.md`). Liberar só por decisão explícita.

Relacionada: [[2026-11-20-fontes-de-renda-com-agentes-e-conteudo]].
