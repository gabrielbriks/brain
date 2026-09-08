---
title: Expor o Vault via MCP (Claude Code e Gemini)
date: 2026-09-08
type: tutorial
tags: [mcp, claude-code, gemini, integração, local]
---

# Expor o Brain via MCP (Model Context Protocol)

O objetivo final do Brain é que todo o conhecimento gerado e armazenado nele (suas ideias, issues e planejamento) esteja acessível enquanto você estiver programando em outros projetos (como Registoo, Pictae, etc).

O protocolo **MCP (Model Context Protocol)** permite que IAs como o Claude Code ou o Gemini consultem ferramentas e pastas externas.

Como nós já resolvemos a sincronização do Brain com o seu computador local através do Git (Passo 1), **não precisamos** fazer um túnel complexo até a VPS. O seu repositório local (`/home/gabriel/www/brain`) já tem tudo o que precisamos.

## Configurando no Claude Code

Para permitir que o Claude Code (ou o Gemini) leia suas anotações do Brain quando você estiver trabalhando no código do seu projeto (por exemplo, na pasta do Registoo), basta configurar o servidor oficial de Sistema de Arquivos (Filesystem) do MCP.

Dentro da pasta do projeto que você estiver desenvolvendo, crie ou edite o arquivo de configuração do MCP (no Claude Code é o arquivo `.claude.json` ou `claude.json`, dependendo da versão):

```json
{
  "mcpServers": {
    "brain-vault": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/home/gabriel/www/brain"
      ]
    }
  }
}
```

### O que isso faz?
Sempre que você abrir o Claude Code nesse projeto e perguntar algo como *"Consulte minhas notas no Brain sobre a arquitetura do Registoo"*, ele usará esse servidor local para vasculhar a pasta `/home/gabriel/www/brain`, ler os arquivos Markdown relevantes que o Hermes salvou lá, e te dar a resposta!

## Vantagens dessa abordagem local
1. **Velocidade:** A leitura é instantânea, pois os arquivos já estão no SSD da sua máquina local.
2. **Offline:** Funciona mesmo sem internet ou se a VPS estiver fora do ar (graças ao clone local do Git).
3. **Segurança:** Não exige abrir portas na VPS ou criar túneis (como Pinggy ou Ngrok) que poderiam expor seus dados na internet.
