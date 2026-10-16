# Script de Promoções de Supermercados

Extrai itens de listas de compras no Brain, busca preços atuais de supermercados e gera um relatório de comparação.

## Pré-requisitos

```bash
pip install requests
```

## Uso

```bash
# Processa todas as listas de compras e gera relatório
python promocoes_supermercados.py --regiao DF

# Processa apenas um arquivo específico
python promocoes_supermercados.py --arquivo 2026-10-09-mercado-acai.md --regiao DF

# Executa sem commit/push automático (para teste)
python promocoes_supermercados.py --regiao DF --no-git
```

## Regiões suportadas

- `DF` — Distrito Federal (padrão)
- `SP` — São Paulo
- `RJ` — Rio de Janeiro
- Outras siglas de estados/municípios

## Fontes de preço

| Fonte | Status | Observação |
|-------|--------|-----------|
| Mercado Livre | ✅ Ativo | API pública MLB |
| Shopee | ⏳ Pendente | API não oficial |
| Supermercados locais | ⏳ Pendente | Scraping direto |

## Output

O relatório é salvo em `_area/pessoal/listas/` com o nome:
```
YYYY-MM-DD-promocoes-supermercados-<regiao>.md
```

E automaticamente commitado e enviado ao Git.

## Como funciona

1. **Extração**: lê arquivos `.md` em `_area/pessoais/listas/`, extrai tabelas com itens, quantidades e preços
2. **Busca**: para cada item, consulta APIs de e-commerce em busca de preços atuais
3. **Comparação**: compara preço de referência (última compra) com menor preço encontrado
4. **Relatório**: gera markdown com tabela comparativa, resumo financeiro e links para produtos
5. **Git**: faz commit e push automático

## Crontab sugerido

```bash
# Todo domingo, às 08:00
0 8 * * 0 /usr/bin/python3 /home/container/brain/_projeto/brain/scripts/promocoes_supermercados.py --regiao DF
```
