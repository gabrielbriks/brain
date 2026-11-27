---
date: 2026-11-27
area: empreendedor
type: log
status: done
tags: [openbot, azure, tailscale, onda-1a, gabs, infra]
---

# Go-live do servidor OpenBot no Azure e ativação da Onda 1A (`Gabs`)

> Marco operacional registrado no teste de estreia da [[2026-11-24-blueprint-gabs-secretaria-do-brain|Gabs]], parte da [[2026-11-23-arquitetura-inicial-equipe-agentes-openbot|Arquitetura Inicial da Equipe de Agentes no OpenBot]].

## O que entrou no ar

- **Infraestrutura:** servidor do **OpenBot** no **Azure** (instância `Standard_B4as_v2`) conectado via **Tailscale**.
- **Agente ativa (Onda 1A):** **Gabs** (Secretária do Brain & Chefe de Gabinete), primeira agente em operação neste ambiente.
- **Escopo validado:** acesso ao Brain isolado via `git sparse-checkout` (sem `_area/pessoal/`, `_area/financeiro/` e `_area/trabalho/`), leitura do `AGENTS.md` e ciclo `git pull --rebase` → escrita → `git commit` → `git push`.

## Contexto em relação ao desenho anterior

- O plano inicial da Onda 1A previa subida local no Windows (ou VPS Hostinger, citada no guia de 2026-11-25); a implantação real aconteceu diretamente no servidor Azure (`Standard_B4as_v2`) com acesso privado via Tailscale.

## Próximos passos naturais

- Validar o uso diário da `Gabs` (capturas rápidas, revisão de `_inbox/` e rotinas no OpenBot).
- Avançar para a **Onda 1B** (`Fury` + `Hill`) quando a operação da Onda 1A estiver estável.
