---
date: 2026-09-30
area: dev
type: ref
status: done
tags: [seguranca, cloudflare, proxy, x-forwarded-for, trust-proxy, rate-limit, railway, vercel, fastify]
---

# IP real do cliente atrás de proxies (Cloudflare, Railway, Vercel) e quando ligar o proxy laranja

> Origem: auditoria de segurança do Registoo Check — PR #75 / issue 037 (2026-09-29/30).
> Vale para qualquer projeto com domínio no Cloudflare.

## 1. O problema: quem "fala" com a sua API é o último proxy, não o usuário

Caminho de uma requisição no Registoo (produção):

```
Usuário 200.1.1.1 → Borda Cloudflare 104.16.5.5 → Borda Railway 100.64.0.9 → API (Fastify)
```

A conexão TCP que chega na API vem sempre do salto anterior (`100.64.0.9`). Sem configuração,
`request.ip` é o IP do proxy para TODO mundo. Consequências reais: rate limit por IP vira um balde único
(um usuário abusivo bloqueia todos) e a trilha de auditoria (`audit_logs.ip_address`) fica inútil.

## 2. `X-Forwarded-For`: a lista de quem passou pelo caminho

Cada proxy honesto **acrescenta à direita** o IP de quem falou com ele:

```
X-Forwarded-For: 200.1.1.1, 104.16.5.5
```

Mas o cliente também pode escrever esse header. Se mandar `X-Forwarded-For: 1.2.3.4`, chega:

```
X-Forwarded-For: 1.2.3.4, 200.1.1.1, 104.16.5.5
                 ^mentira  ^verdade   ^verdade (proxies)
```

**A esquerda pode ser mentira; a direita foi escrita por proxies.**

## 3. A regra de ouro: ler da direita, parar no primeiro não confiável

Configure a lista de proxies confiáveis (CIDRs) e leia da direita para a esquerda:

1. `104.16.5.5` → é Cloudflare (confiável) → continua
2. `200.1.1.1` → não está na lista → **é o cliente. Para.**
3. `1.2.3.4` nunca é lido.

No Fastify: `trustProxy: ['100.64.0.0/10', ...faixas]` (semântica `proxy-addr`). No Express:
`app.set('trust proxy', [...])`. Mesmo conceito em qualquer framework.

**Nunca:**
- `trustProxy: true` — confia em tudo e devolve o valor mais à esquerda (o que o atacante escolhe).
- "número de saltos" (`trustProxy: 2`) — quebra silenciosamente quando a topologia muda
  (ex.: alguém liga o proxy laranja).
- Deixar bibliotecas lerem o header cru (ex.: Better Auth lê `X-Forwarded-For` sozinho): reescreva o
  header com o IP já resolvido pelo framework, para ter uma única fonte de verdade.

## 4. A pegadinha: Cloudflare Workers

Confiar "no Cloudflare" significa confiar que qualquer IP daquela faixa só anexa verdades. Porém
qualquer pessoa cria um Worker de graça, e ele sai por IP do Cloudflare (`2a06:98c0::/29`). O atacante
escreve o `X-Forwarded-For` que quiser e o Cloudflare só anexa o IP do Worker:

```
X-Forwarded-For: 1.2.3.4(forjado), 2a06:98c0:3600::103(Worker), 104.16.5.5(borda)
```

Se `2a06:98c0::/29` estiver na lista, a leitura pula o Worker e para no forjado → IP falso na
auditoria e **balde de rate limit novo a cada requisição** (brute force no login).

**Regra:** use as faixas de <https://www.cloudflare.com/ips-v4> e `/ips-v6` **menos `2a06:98c0::/29`**.
Alternativa mais robusta: quando o salto anterior é do Cloudflare, usar `CF-Connecting-IP` (valor
único, que o Worker não consegue alterar — doc do Cloudflare, `fundamentals/reference/http-headers`).

## 5. Como validar (depois de todo deploy que mexa nisso)

**Primeiro: confirme que o código chegou em produção.** No Registoo, a correção estava mergeada na
`develop`, a variável estava no Railway… e nada mudava, porque Railway/Vercel publicam a `main` e a
release `develop → main` não tinha sido feita. Olhe o **commit do deployment ativo** antes de investigar
qualquer outra coisa.

Validação sem login nem cookie, pelos logs da hospedagem (o Fastify loga `remoteAddress = request.ip`
em toda requisição, até nas sem autenticação):

```bash
curl -s -o /dev/null -w '%{http_code}\n' -H 'X-Forwarded-For: 1.2.3.4' 'https://<api>/health?probe=xff-teste'
```

Nos logs, a linha `incoming request` com `probe=xff-teste` precisa mostrar **o seu IP real** (veja em
<https://www.cloudflare.com/cdn-cgi/trace>):
- seu IP → correto;
- `1.2.3.4` → IP forjável: reverter;
- IP privado (`100.64.x`, `10.x`) → trust proxy não aplicado (código não publicado ou faixa errada);
- IP do Cloudflare → faltam as faixas do Cloudflare na lista.

Não cole IPs reais em canal público (dado pessoal).

Como descobrir se um domínio está laranja sem abrir o painel:
- DNS resolve para `104.16–31.x`, `172.64–71.x` etc. (faixas do Cloudflare);
- a resposta tem `server: cloudflare` e `cf-ray`;
- atenção: confira o host que o front REALMENTE chama (no Registoo era `bkd.`, e a doc dizia `api.`).

## 6. Quando ligar o proxy laranja do Cloudflare — e quando NÃO

Laranja = o tráfego passa pelo Cloudflare (esconde o IP de origem, WAF, DDoS, cache, regras).
Cinza = só DNS; o usuário fala direto com a hospedagem.

**Faz sentido laranja quando:**
- a origem é um servidor seu/VPS/Railway/Render **sem** CDN/WAF próprio e você quer esconder o IP
  de origem, ter proteção contra DDoS, WAF e rate limiting na borda;
- quer usar recursos da borda: cache de estáticos, Page/Redirect Rules, Turnstile/Bot Fight,
  Access (Zero Trust) na frente de um painel interno;
- e você **ajusta a aplicação** para a nova topologia (faixas do Cloudflare no trust proxy, SSL/TLS
  em **Full (strict)**, nunca "Flexible").

**Deixe cinza quando:**
- **a hospedagem já é uma CDN/edge: Vercel, Netlify.** A própria CLI da Vercel, ao detectar
  nameservers do Cloudflare, recomenda os registros com `Proxy: Disabled`. Com laranja você tem CDN
  em cima de CDN: o firewall/analytics/rate limit da Vercel passam a ver IPs do Cloudflare, o cache
  fica duplicado e a emissão de certificado pode falhar;
- **não é HTTP(S) web comum:** MX/e-mail, SSH, banco de dados, SMTP, portas arbitrárias
  (o proxy só cobre HTTP nas portas suportadas);
- **uploads grandes** (plano Free/Pro limita o corpo da requisição a 100 MB) ou **requisições longas**
  (timeout de ~100 s na borda: relatórios pesados, exportações, SSE mal configurado);
- durante a **verificação/emissão de certificado** de hospedagens que validam por HTTP (ex.: Railway
  pede o domínio cinza até o SSL ficar verde; depois pode ligar);
- quando você **não vai** ajustar a aplicação para ler o IP real e o IP importa (auditoria, LGPD,
  rate limit) — laranja "de enfeite" quebra isso silenciosamente.

**Heurística rápida:** "A hospedagem já tem borda própria?" → cinza. "É servidor meu exposto e
eu configurei trust proxy + Full (strict)?" → laranja. Na dúvida, cinza é o default seguro; ligue o
laranja como decisão consciente, com checklist.

## 7. Aplicado ao Registoo (2026-09-30)

- `bkd.registoo.com.br` (API no Railway): laranja, correto, com `TRUSTED_PROXY_CIDRS` = Railway +
  faixas do Cloudflare sem Workers (PR #75; vale em produção após a release `develop → main`).
- `app.registoo.com.br` e `registoo.com.br` (Vercel): laranja — pela recomendação da Vercel, deveriam
  ser cinza. A avaliar com calma (mudar exige conferir SSL e cookies antes).
