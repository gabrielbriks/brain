---
date: 2026-10-28
area: dev
type: ref
status: done
tags: [stripe, seguranca, chave-restrita, rak, deploy, billing, registoo, pictae]
---

# Permissões de chave restrita da Stripe (`rk_live_…`) e o que conferir no deploy

> Origem: plan-039 do Registoo Check (recurso extra cobrado na hora), F3 em 2026-10-27/28.
> Vale para qualquer projeto que fale com a Stripe (Registoo, Pictae).

## 1. Os dois tipos de chave de servidor

| Chave | Pode | Quando usar |
|---|---|---|
| `sk_live_…` (secreta) | tudo na conta | o padrão; nada a conferir de permissão |
| `rk_live_…` (restrita) | só os recursos liberados nela | menor estrago se vazar (privilégio mínimo) |

A chave publicável (`pk_…`) é outra coisa: roda no navegador (Payment Element, `confirmCardPayment`, 3DS)
e não passa por estas permissões.

**Registoo hoje:** produção usa `sk_live` (Railway). O ambiente local usa `rk_test` da área restrita.

## 2. Como a chave restrita decide

Cada recurso da API (Customers, Invoices, Subscriptions, PaymentMethods, Charges…) fica em **None**,
**Read** ou **Write**. Write inclui Read.

- `GET` → Read. `POST`/`DELETE` → Write.
- **Exceções documentadas:** a prévia de fatura é `POST /v1/invoices/create_preview` e pede só
  `invoice_read`. Na dúvida, a referência é `docs.stripe.com/keys/permissions-reference`.
- **`expand` conta como leitura do recurso expandido.** Buscar a assinatura "com o cartão dentro"
  (`expand: ['default_payment_method']`) pede Subscriptions Read **e** PaymentMethods Read.

Sem a permissão, a Stripe responde com erro de permissão. Se a sua API embrulha erros da Stripe numa
mensagem genérica (o Registoo responde 502 "Não foi possível concluir a operação com o meio de
pagamento"), **a falta de permissão aparece para o usuário como "a compra não funciona"**, não como
"falta permissão".

## 3. A armadilha do teste

A chave restrita de teste costuma ter mais permissão que a Live (foi criada larga para desenvolver). O
teste passa e o Live quebra. Por isso a pergunta de deploy, sempre que o código passar a chamar um
endpoint novo da Stripe ou a expandir um objeto novo:

> **"A chave Live tem esse recurso nesse nível?"**

## 4. Como conferir (2 minutos)

1. Dashboard **em modo Live** → Desenvolvedores → Chaves de API → seção de chaves restritas.
2. Ache a chave que o servidor usa (começo/fim batem com a variável no Railway/Vercel).
3. ⋯ → **Editar chave** → confira cada recurso que o código usa, no nível certo.
4. Salvar vale na hora, sem deploy.
5. **Depois do deploy:** a mesma tela tem o log de requisições da chave. Filtre as sem sucesso: o erro de
   permissão diz o recurso e o nível que faltam.

Não teste a chave Live trazendo-a para a máquina local.

## 5. Exemplo real: o que o recurso extra do Registoo passou a pedir (plan-039)

| Chamada | Recurso e nível | Se faltar |
|---|---|---|
| Atualizar a assinatura (compra pendente) | Subscriptions: Write | compra não acontece |
| Prévia do valor de hoje (`create_preview`) | Invoices: Read | ninguém compra (o diálogo não calcula o valor) |
| Anular a fatura (cancelar compra; cancelar assinatura com compra pendente) | Invoices: **Write** | cancelar a compra falha; **cancelar a assinatura com compra pendente também** |
| Faturas da assinatura com a cobrança (regra do estorno) | Invoices: Read + Charges: Read | estorno mal classificado |
| Cartão salvo (assinatura/cliente com o cartão expandido) | **PaymentMethods: Read** | degrada sem quebrar: some o "um clique", cai em digitar o cartão |

Repare na última linha: **desenhar a tela para degradar** quando uma leitura falha (sem cartão salvo →
fluxo de digitar) transforma uma permissão esquecida em incômodo, não em perda de venda.

## 6. Vale migrar de `sk_live` para `rk_live`?

- **A favor:** se a chave vazar (log, variável exposta, dependência comprometida), o estrago fica
  limitado aos recursos liberados. É o que a Stripe recomenda.
- **Contra:** cada endpoint novo vira um item de deploy (a seção 3), e esquecer quebra em produção.
- **Quando compensa:** quando o projeto tiver mais gente ou integrações com acesso às variáveis, ou depois
  de um incidente. Se migrar: criar a restrita a partir do log de requisições da `sk_live` (o que ela de
  fato chamou), trocar no Railway, observar o log da restrita por alguns dias, só então revogar a antiga.
