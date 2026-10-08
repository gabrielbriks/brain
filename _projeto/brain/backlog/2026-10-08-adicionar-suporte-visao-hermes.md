---
date: 2026-10-08
projeto: brain
type: backlog
status: open
priority: medium
tags: [hermes, vision, discord, infra]
---

# Suporte a Análise de Imagens no Hermes

Durante os testes de integração com o Discord, foi tentado o envio de uma imagem para o Hermes extrair notas, porém ocorreu um `erro de gateway`.

**Causa Provável:**
O modelo configurado atualmente (`deepseek-v3.2`) é primariamente focado em texto, ou a própria infraestrutura do Hermes Gateway precisa ser configurada com um modelo Multimodal (Visão) ou um plugin de OCR para processar anexos.

**Próximos Passos:**
- Investigar como o `Hermes Agent v0.21.1` gerencia payloads de imagens.
- Avaliar a configuração de um modelo multimodal (ex: GPT-4o, Claude 3.5 Sonnet ou DeepSeek-VL) para lidar com visão.
- Verificar se existe algum plugin de OCR no próprio Hermes Gateway que possa interceptar e extrair o texto antes de mandar para a LLM.
