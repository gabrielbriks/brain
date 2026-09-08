---
title: Configurar Auto-Sync Git (Cron Jobs)
date: 2026-09-08
type: tutorial
tags: [hermes, git, auto-sync, cron, infra]
---

# Configurar Auto-Sync Git no Hermes

Este documento descreve como configurar o Hermes Agent em uma VPS para sincronizar automaticamente as notas com o repositório GitHub, sem causar conflitos com as edições feitas na máquina local.

## O Problema do `git push` Simples

O repositório é editado de dois lados:
1. **VPS (Hermes):** cria arquivos novos (as notas processadas).
2. **Local (Você):** edita arquivos de documentação (como `README.md`).

Se você comitar e fizer push localmente, o repositório remoto ficará "na frente" da VPS. Se o Hermes tentar fazer um `git push` simples, a operação falhará porque os branches estão divergentes.

## A Solução: Pull (Rebase) + Push

Para evitar isso, sempre fazemos um pull com rebase antes do push. O rebase reaplica os commits da VPS por cima dos commits recém-chegados do repositório remoto, garantindo um histórico linear e sem conflitos (já que editamos arquivos diferentes).

### Comando de Sincronização

No terminal da VPS (onde o Hermes roda), adicione o seguinte cron job:

```bash
hermes cron add "*/15 * * * *" "git -C ~/brain pull --rebase origin main && git -C ~/brain push origin main"
```

Este comando:
1. Roda a cada 15 minutos (`*/15 * * * *`).
2. Puxa as alterações do repositório remoto, fazendo rebase (`pull --rebase`).
3. Somente se o pull for bem sucedido (`&&`), envia as alterações locais da VPS (`push`).

Para validar se o cron job foi adicionado com sucesso, você pode listar os agendamentos ativos rodando:

```bash
hermes cron list
```
