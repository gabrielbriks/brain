---
title: Projeto — zenckup
type: readme
status: active
tags: [infra, backup, postgres, r2, railway, docker, transversal]
---

# 🗄️ zenckup — Backup agendado de Postgres para o Cloudflare R2

> Repositório local: `/home/gabriel/www/zenckup` — adota o `zen-ai-workflow` **v0.1.0** (camada
> essencial: `AGENTS.md`, `CONTEXT.md`, `HANDOFF.md`, `docs/INDEX.md`).

Uma imagem Docker pequena, **genérica e schema-agnóstica**, que tira um `pg_dump` de um banco,
comprime e sobe para o Cloudflare R2. Construída **uma vez** e rodada como **Cron Job dentro de
cada projeto** do Gabriel — Widback, Registoo, Pictae e o que vier depois — mudando só as variáveis
de ambiente.

## Por que existe

O plano **Hobby do Railway não oferece backup de Postgres**: perder o volume significa perder todos
os dados. O problema apareceu ao fechar a pendência de backup da Res-001 (postura de dados) do
Widback, e o mesmo vale para Registoo e Pictae — resolver só para um seria retrabalho garantido.

## A decisão central: uma instância por projeto, nunca um hub

A ideia inicial era um serviço único cobrindo os três produtos. Não é viável: a **rede privada do
Railway é isolada por projeto**, então um serviço central só alcançaria os bancos se eles ficassem
expostos publicamente — trocar um problema (backup) por outro pior (banco de produção público).

Resultado: a lógica é construída uma vez, genérica, e roda **uma instância por projeto**, dentro da
rede privada dele. Mesma imagem, zero rede cruzada exposta. Consequência direta: o backup precisa
ser `pg_dump` de verdade, não código de aplicação amarrado a schema.

## Como funciona

1. `pg_dump "$DATABASE_URL" | gzip` → `/tmp/<prefixo>-<timestamp>.sql.gz`
2. Sanity check: aborta (sem subir nada) se o dump tiver < 100 bytes — banco vazio ou falha de
   conexão silenciosa.
3. Upload via `rclone` (configurado só por env vars) para `<bucket>/<prefixo>/<arquivo>`.
4. Falha alto (`exit 1`) em qualquer etapa — um Cron Job marcado como falho é o comportamento
   certo; um backup vazio "bem sucedido" é o errado.

**Retenção** não é do script: é uma *lifecycle rule* do bucket R2 (30 dias é o padrão combinado
para o Widback).

## Stack

Docker (`postgres:18-alpine`, `ARG PG_VERSION`) · bash · `pg_dump` · gzip · `rclone` · Cloudflare
R2 · Railway Cron Job.

## Rollout

| Produto | Status |
|---|---|
| Widback | **Em produção desde 2026-10-11:** dump 18 → R2 em `zenckups/widback/`. Faltam o restore real e o Cron Schedule (ver Plan-006 no repo do Widback) |
| Registoo | Planejado — mesma semana |
| Pictae | Planejado — semanas seguintes |

Configuração de R2, Cron Job, credenciais e teste de restauração por produto são passos manuais do
Gabriel — **credencial de produção não passa por sessão de IA**.

## Fora do escopo (por ora)

Teste de restauração automatizado · alerta ativo de falha (o painel do Railway já marca o job como
falho) · backup incremental / WAL archiving.

## Pontos de atenção em aberto

- **Restauração real ainda não exercitada** — o passo que dá valor ao backup; em andamento.
- Se algum projeto subir de versão do Postgres, ajustar `PG_VERSION` (`pg_dump` não dumpa servidor
  mais novo que ele). Hoje todos rodam 18.6 e o padrão é `18-alpine`.
- Conferir: se o Railway acompanha o branch automaticamente; se o token do R2 aceita escopo por
  prefixo; fuso do Cron Schedule.
- Resolvidos: `--no-owner`/`--no-acl` (plan-001), `PG_VERSION` 17→18, `shellcheck` via Docker, endpoint
  do R2 e `no_check_bucket`.

## Relação com outros projetos

- **Widback, Registoo, Pictae:** consumidores da ferramenta (uma instância em cada).
- **Zen AI Workflow:** metodologia adotada aqui — ver o insight de adoção em `insights/`.

## Material de estudo

- Aprendizados, padrões de arquitetura e roteiro de entrevista:
  `_area/dev/refs/2026-10-06-zenckup-jornada-engenheiro-de-software.md`
- No repositório: `docs/adr/001-*.md`, os diagramas de system design (1, 3 ou N projetos) na seção
  Arquitetura do `CONTEXT.md` e três learnings em `docs/learnings/`:
  `replicar-dentro-da-fronteira.md` (a decisão), `dump-roles-owner-acl.md` (roles, owner, ACL e
  restore) e `r2-endpoint-e-token-de-objetos.md` (armadilhas do R2 com rclone).
- Plano executado: `docs/plans/plan-001-no-owner-no-acl.md`.

## Estado (2026-10-11)

O backup do Widback roda em produção. Desde a fase inicial (2026-10-07): `--no-owner`/`--no-acl`
(plan-001, T2, com teste que restaura num servidor sem as roles), `PG_VERSION` 18 (o `pg_dump` 17
recusava os servidores 18), `shellcheck` via Docker e `no_check_bucket` para o token do R2.
As correções de produção vieram do deploy real, não dos testes locais. Falta: restore real num
Postgres 18 descartável, Cron Schedule e replicar em Registoo e Pictae. Detalhe no `HANDOFF.md`.

## Subpastas

- `insights/` — aprendizados e registros de decisão do projeto
