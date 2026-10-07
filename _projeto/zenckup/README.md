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

Docker (`postgres:17-alpine`, `ARG PG_VERSION`) · bash · `pg_dump` · gzip · `rclone` · Cloudflare
R2 · Railway Cron Job.

## Rollout

| Produto | Status |
|---|---|
| Widback | Primeira instância, configuração em andamento (ver Plan-006 no repo do Widback) |
| Registoo | Planejado — mesma semana |
| Pictae | Planejado — semanas seguintes |

Configuração de R2, Cron Job, credenciais e teste de restauração por produto são passos manuais do
Gabriel — **credencial de produção não passa por sessão de IA**.

## Fora do escopo (por ora)

Teste de restauração automatizado · alerta ativo de falha (o painel do Railway já marca o job como
falho) · backup incremental / WAL archiving.

## Pontos de atenção em aberto

- `pg_dump` sem `--no-owner`/`--no-acl` pode dar atrito ao restaurar em outro usuário/banco
  (tier T2: muda o contrato de restore dos três projetos).
- Se algum projeto subir de versão do Postgres, ajustar `PG_VERSION` (`pg_dump` não dumpa servidor
  mais novo que ele).
- Restauração é manual e ainda não foi exercitada em produção.

## Relação com outros projetos

- **Widback, Registoo, Pictae:** consumidores da ferramenta (uma instância em cada).
- **Zen AI Workflow:** metodologia adotada aqui — ver o insight de adoção em `insights/`.

## Material de estudo

- Aprendizados, padrões de arquitetura e roteiro de entrevista:
  `_area/dev/refs/2026-10-06-zenckup-jornada-engenheiro-de-software.md`
- No repositório: `docs/adr/001-*.md`, `docs/learnings/replicar-dentro-da-fronteira.md` e os
  diagramas de system design (1, 3 ou N projetos) na seção Arquitetura do `CONTEXT.md`.

## Estado (2026-10-07)

Fase inicial encerrada: workflow adotado, ADR-001, learning e diagramas. Próxima etapa:
`--no-owner`/`--no-acl` no `pg_dump` (T2), depois compatibilidade de `PG_VERSION` (T1). Detalhe
no `HANDOFF.md` do repositório.

## Subpastas

- `insights/` — aprendizados e registros de decisão do projeto
