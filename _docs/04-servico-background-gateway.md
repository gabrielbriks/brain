---
title: Configurar Gateway e Cron em Background (Systemd)
date: 2026-09-08
type: tutorial
tags: [hermes, gateway, cron, background, systemd, linux, infra]
---

# Manter o Gateway e Cron Ativos em Background

Quando você executa `hermes gateway` diretamente no terminal, ele funciona perfeitamente, porém o processo morre assim que você fecha a conexão com a VPS ou reinicia o servidor.

Como os **cron jobs** do Hermes (como nosso auto-sync) dependem do Gateway rodando para serem disparados, precisamos configurar o Hermes para rodar como um **serviço nativo do Linux (systemd)**. Isso garante que ele fique rodando silenciosamente no fundo 24 horas por dia e reinicie automaticamente junto com a VPS.

## Instalação do Serviço

O próprio Hermes já possui um utilitário para gerar e registrar esse serviço de forma automática.

Na sua VPS, execute o seguinte comando:

```bash
# Instala o Hermes Gateway como um serviço de sistema (inicia junto com o boot)
sudo hermes gateway install --system
```

*(Se o usuário `container` não tiver permissões de `sudo`, você pode omitir o `sudo` e o `--system` executando apenas `hermes gateway install`. Isso instalará o serviço localmente para o seu usuário usando o `systemd --user`).*

## Comandos Úteis de Gerenciamento

Depois de instalado, o Hermes passa a ser gerenciado pelo sistema operacional. Você pode usar os comandos normais do Linux (systemctl) para controlá-lo:

```bash
# Ver se está rodando e sem erros
sudo systemctl status hermes-gateway

# Iniciar ou Parar o serviço
sudo systemctl start hermes-gateway
sudo systemctl stop hermes-gateway

# Ver os logs do Hermes em tempo real (muito útil para debugar)
journalctl -u hermes-gateway -f
```

## Como validar se deu certo?

Para garantir que o cron job voltou a funcionar, você pode rodar:

```bash
hermes cron status
```

O aviso de "Gateway is not running" deve ter sumido e os seus cron jobs serão disparados no horário previsto!
