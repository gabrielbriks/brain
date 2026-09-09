---
date: 2026-09-09
projeto: brain
type: decision
status: closed
tags: [arquitetura, custos, embeddings, local-vs-cloud, hardware]
---

# Decisão: Arquitetura de Custos e Embeddings Locais (Busca Semântica)

**Contexto:**
Durante a análise para implementar a Busca Semântica no Brain OS, estudamos a atualização `ai-memory 2.0` de Fábio Akita, que introduziu **Embeddings Locais por Padrão**. Precisávamos avaliar a viabilidade técnica disso na nossa VPS PrimeClaws de $9.99/mês.

## O Fator Decisivo: Hardware
Descobrimos que a configuração do plano PrimeClaws entrega **2 vCPU Intel i9, 4GB RAM e 50GB SSD**. Esse hardware é excepcionalmente robusto para o preço.

## As Duas Opções de Arquitetura Avaliadas

### Opção 1: Abordagem "Akita" (100% Local)
Rodar modelos matemáticos focados (ex: `all-MiniLM-L6-v2`) diretamente na CPU da VPS e salvar em banco local via arquivo (ChromaDB).
- **Custos adicionais:** $0.00
- **Consumo de Hardware:** ~200MB a 300MB de RAM.
- **Prós:** Privacidade máxima (Air-gapped), zero latência de rede, zero custo de API.

### Opção 2: Abordagem "Cloud-Native API"
Usar a API da OpenAI (`text-embedding-3-small`) para gerar o vetor e hospedar em um Vector DB serverless (Pinecone, Upstash).
- **Custos adicionais:** ~$0.10 por ano + Free tier de banco.
- **Consumo de Hardware:** 0MB.
- **Prós:** Terceiriza o processamento totalmente.

## Conclusão e Veredito (Status: Closed)
A **Opção 1 (100% Local)** é a vencedora indiscutível.

Como a PrimeClaws nos fornece 4GB de RAM e 2 vCPUs potentes (Intel i9), dedicar ~300MB de memória para carregar o modelo de embeddings não fará nem "cócegas" na infraestrutura. 

Com isso, o Brain OS será totalmente autossuficiente e privado, seguindo o padrão ouro da indústria atual para agentes locais (como o *ai-memory 2.0*), sem adicionar absolutamente nenhum custo extra à fatura de $9.99/mês.
