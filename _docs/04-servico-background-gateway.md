---
title: Configurar Gateway e Cron em Background (Docker)
date: 2026-09-08
type: tutorial
tags: [hermes, gateway, cron, background, docker, tmux, primeclaws, infra]
---

# Manter o Gateway e Cron Ativos em Background

Quando você executa `hermes gateway` diretamente no terminal, ele funciona perfeitamente, porém o processo morre assim que você fecha a conexão com a VPS.

Como os **cron jobs** do Hermes (como nosso auto-sync) dependem do Gateway rodando para serem disparados, precisamos configurar o Hermes para rodar no fundo.

## O Desafio: Ambiente Docker (Sem Systemd)

A infraestrutura da PrimeClaws roda em um **Container Docker** (e não em uma máquina virtual completa). Por conta disso, utilitários nativos de serviços do Linux, como o `systemd` (`systemctl`), **não estão disponíveis**.
Se você tentar rodar `sudo hermes gateway install --system`, o Hermes avisará que está dentro de um container Docker e a instalação falhará.

Temos duas soluções para isso no ambiente Docker:

## Solução 1: Painel da PrimeClaws (Recomendado)

A melhor forma de manter um processo vivo em containers Docker de painéis de hospedagem (como Pterodactyl/PrimeClaws) é alterando o comando de inicialização do próprio container.

1. Vá até o dashboard web da PrimeClaws.
2. Na aba **Startup** (Inicialização), procure pelo campo que define o comando de inicialização (Startup Command).
3. Certifique-se de que o comando de inicialização seja:
```bash
hermes gateway run
```
Dessa forma, toda vez que o container ligar, o Gateway iniciará automaticamente.

## Solução 2: Usar o `tmux` no Terminal

Se você não tiver acesso à aba Startup ou preferir gerenciar manualmente pelo terminal, use o `tmux`. O `tmux` cria uma sessão de terminal que não morre quando você fecha o navegador.

1. No console (`ttyd`), abra uma nova sessão do tmux:
```bash
tmux new -s hermes
```
2. Dentro dessa sessão, rode o comando:
```bash
hermes gateway run
```
3. Para **sair da sessão sem fechar o processo** (fazer o detach), pressione as teclas no teclado:
`Ctrl + B` e logo depois aperte a tecla `D`.

Você voltará ao console normal e o Hermes continuará rodando invisível!
*(Para voltar a ver o Hermes rodando no futuro, digite `tmux attach -t hermes`).*

## Como validar se deu certo?

Para garantir que o cron job voltou a funcionar, você pode rodar fora do tmux:

```bash
hermes cron status
```

O aviso de "Gateway is not running" deve ter sumido e os seus cron jobs serão disparados no horário previsto!
