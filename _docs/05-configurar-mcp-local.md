---
title: Configuração Global do MCP (Antigravity IDE, agy CLI e Claude Code)
date: 2026-09-08
type: tutorial
tags: [mcp, antigravity, agy-cli, claude-code, integracao, local]
---

# Configuração Fluida do MCP em Múltiplos Ambientes

O objetivo desta etapa é permitir que você consulte e alimente o **Brain** a partir de qualquer projeto ou ferramenta do seu fluxo diário:
- **Antigravity IDE**
- **Antigravity CLI (`agy`)**
- **Claude Code (Extensão no VS Code e CLI)**

Como o vault local já está em `/home/gabriel/www/brain` e sincronizado via Git com a VPS e o GitHub, a melhor abordagem é expor essa pasta localmente via o servidor oficial `@modelcontextprotocol/server-filesystem`.

Abaixo está o passo a passo para configurar de forma **global** (uma única vez por máquina), para que funcione em qualquer pasta ou projeto sem atrito.

---

## 1. Antigravity IDE & Antigravity CLI (`agy`)

Tanto o Antigravity IDE quanto o CLI (`agy`) compartilham o mesmo motor e leem a mesma configuração global de MCP em `~/.gemini/config/mcp_config.json`.

### Configuração Global:
Edite o arquivo global `~/.gemini/config/mcp_config.json` e adicione o servidor `brain-vault`:

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

> [!TIP]
> Caso você já tenha outros servidores (como o `chrome-devtools-mcp`), basta adicionar a chave `"brain-vault"` dentro de `"mcpServers"`.

### Como funciona no Antigravity:
- Uma vez salvo, qualquer janela do Antigravity IDE ou comando no terminal `agy` ganha imediatamente as ferramentas do MCP filesystem (`read_file`, `write_file`, `list_directory`, etc.).
- Ao trabalhar no projeto `registoo`, por exemplo, você pode pedir diretamente ao agente:
  > *"Consulte no brain-vault as notas sobre a arquitetura do Registoo e me explique como autenticamos usuários."*

---

## 2. Claude Code (Extensão VS Code & CLI)

O Claude Code permite definir servidores MCP no escopo global de usuário (`user scope`), garantindo que a ferramenta fique ativa em qualquer workspace aberto na extensão do VS Code ou no terminal.

### Opção A: Via CLI do Claude Code (Recomendada)
No seu terminal, execute:

```bash
claude mcp add --scope user brain-vault -- npx -y @modelcontextprotocol/server-filesystem /home/gabriel/www/brain
```

Isso registrará o servidor globalmente na sua configuração de usuário (`~/.claude.json`).

### Opção B: Por Projeto (Arquivo `.mcp.json`)
Caso prefira que o MCP seja explícito apenas em um repositório específico (ex: na raiz do `registoo` ou do próprio `brain`), crie um arquivo `.mcp.json` na raiz do projeto:

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

---

## 3. Sincronização Bidirecional (O Ciclo Completo)

Com o MCP configurado localmente:
1. **Leitura:** As IAs locais (Antigravity ou Claude) leem diretamente do disco `/home/gabriel/www/brain`.
2. **Escrita:** Quando elas criam notas novas no vault, os arquivos são salvos localmente.

### Como garantir que a VPS (Hermes / Telegram) veja as notas criadas localmente?
Na VPS, o cron já roda o auto-sync a cada minuto.
Para que a sua máquina local suba as anotações criadas pelo MCP:
- Você pode instruir o próprio agente durante o chat:
  > *"Salve a nota sobre X no brain-vault e faça o commit/push no repositório."*
- Ou criar um atalho / alias no seu `.zshrc` ou um cron local no WSL para fazer `git -C ~/www/brain pull --rebase origin main && git -C ~/www/brain push origin main`.
