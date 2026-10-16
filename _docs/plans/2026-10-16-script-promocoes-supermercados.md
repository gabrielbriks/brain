---
title: Script de Promoções de Supermercados
date: 2026-10-16
status: draft
tags: [plan, supermercado, compras, scraping]
---

# Plano: Script de Promoções de Supermercados

## Contexto

Gabriel faz compras regularmente em supermercados e mercados locais (ex: Mercado Açaí). Ele mantém listas de compras no Brain (`_area/pessoal/listas/`) com preços pagos. O objetivo é automatizar a comparação de preços: identificar promoções atuais e gerar um relatório que mostre onde cada item está mais barato.

## Objetivos

1. Extrair itens de listas de compras existentes no Brain
2. Buscar preços atuais de supermercados brasileiros
3. Comparar com preços de referência (última compra)
4. Gerar relatório de promoções por item

## Arquitetura

```
brain/_projeto/brain/scripts/
├── promocoes_supermercados.py    ← Script principal
└── README.md                     ← Documentação de uso
```

### Fluxo

```
1. Lê arquivos em _area/pessoal/listas/
2. Extrai itens + preços (tabelas markdown)
3. Para cada item, busca em APIs de supermercados
4. Compara preços atuais com os pagos
5. Gera relatório em _area/pessoal/listas/promocoes-<data>.md
```

### Fontes de Preço (Fase 1)

- [ ] **Mercado Livre** — API de produtos
- [ ] **Shopee** — API de produtos
- [ ] **Supermercados locais** — scraping direto (a depender do mercado)

> Nota: APIs oficiais de supermercados (Carrefour, Pão de Açúcar, etc.) têm rate limiting severo. Uma abordagem realista é usar APIs de e-commerce + scraping direto para lojas locais.

## Critérios de Aceitação

- [ ] Script lê listas do Brain e extrai itens automaticamente
- [ ] Busca preços em pelo menos 1 fonte por item
- [ ] Gera relatório markdown com comparação de preços
- [ ] Salva relatório em `_area/pessoal/listas/` com data atual
- [ ] Faz commit e push automático no Git

## Riscos

- Rate limiting em APIs → usar delays e retry
- Preços variam por região → pedir cidade/UF ao usuário
- Itens não encontrados → marcar como "não encontrado" no relatório

## Próximos Passos

1. Implementar script Python com extração de listas
2. Integrar com pelo menos uma API de produtos
3. Testar com a lista do Mercado Açaí (2026-10-09)
4. Ajustar com feedback do Gabriel