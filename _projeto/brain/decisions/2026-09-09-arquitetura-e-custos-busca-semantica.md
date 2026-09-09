---
date: 2026-09-09
projeto: brain
type: decision
status: open
tags: [arquitetura, custos, embeddings, local-vs-cloud, akita]
---

# Decisão: Arquitetura de Custos e Embeddings Locais (Busca Semântica)

**Contexto:**
Durante a análise para implementar a Busca Semântica no Brain OS (hospedado num container PrimeClaws de $9.99/mês), estudamos a atualização `ai-memory 2.0` de Fábio Akita, que introduziu **Embeddings Locais por Padrão**. Precisávamos avaliar a viabilidade técnica disso na nossa VPS limitada e projetar os custos.

## As Duas Opções de Arquitetura

### Opção 1: Abordagem "Akita" (100% Local)
Rodar modelos matemáticos focados e minúsculos (ex: `all-MiniLM-L6-v2` ou `nomic-embed-text`) diretamente na CPU da VPS e salvar em banco local via arquivo (ex: ChromaDB ou LanceDB).
- **Custos adicionais:** $0.00
- **Consumo de Hardware:** ~150MB a 300MB de RAM adicionais no container da PrimeClaws.
- **Prós:** Privacidade máxima (Air-gapped architecture para a memória), sem dependência de chaves de API para leitura/escrita.

### Opção 2: Abordagem "Cloud-Native API"
Usar a API da OpenAI (`text-embedding-3-small`) ou equivalente para gerar o vetor e hospedar em um Vector DB serverless (Pinecone, Upstash).
- **Custos adicionais:** ~$0.02 a cada 1 milhão de tokens (estimativa de < $0.10 por ANO para um usuário final). O Vector DB é coberto pela Free Tier permanente (Pinecone/Upstash).
- **Consumo de Hardware:** 0MB na VPS.
- **Prós:** Preserva 100% dos recursos limitados da VPS PrimeClaws. Modelos de API geram vetores com mais dimensões e maior precisão contextual que os modelos minúsculos locais.

## Conclusão Atual
**O PrimeClaws é suficiente para ambas as abordagens**, provando que não precisamos fazer upgrade ou mudar de servidor.

A decisão de qual caminho seguir na implementação dependerá estritamente de quanto de memória RAM o Hermes já está consumindo atualmente no container da PrimeClaws:
- Se houver `> 300MB` de RAM livres de sobra, o caminho Local (Opção 1) é viável e adotaremos a filosofia do `ai-memory 2.0`.
- Se a VPS estiver no gargalo de memória, adotaremos a Opção 2 (API) considerando que o custo anual de 10 centavos é economicamente trivial.
