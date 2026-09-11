---
title: Plano de Implementação — Busca Semântica no Brain OS
date: 2026-09-11
author: Gabriel + Antigravity
status: draft
tags: [busca-semantica, embeddings, hermes, chromadb, all-minilm, plano]
---

# Plano de Implementação: Busca Semântica no Brain OS

> **Objetivo:** Adicionar ao Agente Hermes (na VPS PrimeClaws) a capacidade de encontrar notas por **significado semântico** e não apenas por palavras-chave. O usuário deve conseguir perguntar no Telegram *"Qual era aquela decisão técnica sobre banco de dados?"* e o Hermes recuperar a nota certa, mesmo que ela não contenha essas palavras exatas.

> **Arquitetura Aprovada:** 100% Local (ver `decisions/2026-09-09-arquitetura-e-custos-busca-semantica.md`)
> - **Modelo de Embeddings:** `all-MiniLM-L6-v2` (roda na CPU, ~80MB em disco, ~200MB RAM)
> - **Banco de Vetores:** ChromaDB (arquivo local em `~/brain/.chromadb/`)
> - **Custo adicional:** $0.00

---

## Fases do Projeto

### Fase 0 — Pré-requisitos e Auditoria da VPS
**Objetivo:** Garantir que o ambiente tem o que é necessário e medir o consumo atual.

- [ ] **T0.1 — Auditar memória RAM atual na VPS**
  - Pedir ao Gabriel para rodar na VPS: `free -h` e `docker stats --no-stream`
  - Registrar o baseline de uso atual de memória.
  - *Critério de sucesso:* Confirmar que há pelo menos 600MB de RAM livre (200MB modelo + 400MB folga).

- [ ] **T0.2 — Verificar a versão do Python disponível na VPS**
  - Pedir ao Gabriel para rodar: `python3 --version`
  - Precisamos de Python >= 3.9.
  - *Critério de sucesso:* Python 3.9+ confirmado.

- [ ] **T0.3 — Criar pasta do banco de vetores e proteger do Git**
  - No repositório Git local: criar pasta `~/brain/.chromadb/` com `.gitignore` cobrindo-a.
  - *Motivo:* O banco de vetores é gerado localmente e nunca deve ser commitado no Git (é regenerável e pode ficar grande).

---

### Fase 1 — Instalação das Dependências na VPS
**Objetivo:** Instalar os pacotes Python necessários no container da PrimeClaws.

- [ ] **T1.1 — Instalar dependências via pip**
  ```bash
  pip install chromadb sentence-transformers
  ```
  - `chromadb` — Banco de dados de vetores local baseado em arquivo.
  - `sentence-transformers` — Biblioteca que carrega e roda o modelo `all-MiniLM-L6-v2`.

- [ ] **T1.2 — Validar instalação**
  ```bash
  python3 -c "import chromadb; from sentence_transformers import SentenceTransformer; print('OK')"
  ```
  - *Critério de sucesso:* Output `OK` sem erros.

- [ ] **T1.3 — Primeiro download do modelo**
  - Na primeira execução, o `sentence-transformers` vai baixar o modelo (~80MB) da internet e cacheá-lo em `~/.cache/torch/`.
  - Pedir ao Gabriel para rodar o script de validação da Fase 2 uma vez manualmente para confirmar o download e o cache.

---

### Fase 2 — Script de Indexação (`indexar.py`)
**Objetivo:** Criar o script responsável por ler todas as notas `.md` do vault `~/brain/` e popular o ChromaDB com seus vetores.

- [ ] **T2.1 — Criar `~/brain/.scripts/indexar.py`**

  O script deve:
  1. Conectar ao ChromaDB em `~/brain/.chromadb/`.
  2. Criar ou abrir a "Collection" chamada `brain-notas`.
  3. Percorrer recursivamente todos os arquivos `.md` em `~/brain/_area/`, `~/brain/_projeto/` e `~/brain/_inbox/`.
  4. Para cada arquivo `.md`:
     - Ler o conteúdo.
     - Extrair o frontmatter (como título, tags, date, type).
     - Converter o conteúdo em vetor usando o modelo `all-MiniLM-L6-v2`.
     - Inserir no ChromaDB com metadados (caminho do arquivo, date, type, project/area, tags).
  5. Printar o total de notas indexadas ao finalizar.

  ```python
  # Estrutura do script indexar.py
  import chromadb
  from sentence_transformers import SentenceTransformer
  from pathlib import Path
  import yaml, re

  VAULT = Path.home() / "brain"
  DB_PATH = VAULT / ".chromadb"
  DIRS = ["_area", "_projeto", "_inbox"]

  client = chromadb.PersistentClient(path=str(DB_PATH))
  model = SentenceTransformer("all-MiniLM-L6-v2")
  collection = client.get_or_create_collection("brain-notas")

  def parse_md(path):
      text = path.read_text(encoding="utf-8")
      frontmatter = {}
      match = re.match(r"^---\n(.*?)\n---\n(.*)", text, re.DOTALL)
      if match:
          frontmatter = yaml.safe_load(match.group(1)) or {}
          body = match.group(2)
      else:
          body = text
      return frontmatter, body

  arquivos = []
  for d in DIRS:
      arquivos.extend((VAULT / d).rglob("*.md"))

  for path in arquivos:
      fm, body = parse_md(path)
      if not body.strip():
          continue
      embedding = model.encode(body).tolist()
      collection.upsert(
          ids=[str(path)],
          embeddings=[embedding],
          documents=[body],
          metadatas=[{
              "path": str(path),
              "date": str(fm.get("date", "")),
              "type": str(fm.get("type", "")),
              "projeto": str(fm.get("projeto", "")),
              "area": str(fm.get("area", "")),
              "tags": ", ".join(fm.get("tags", [])),
          }]
      )

  print(f"✅ {len(arquivos)} notas indexadas no ChromaDB.")
  ```

- [ ] **T2.2 — Testar manualmente o script**
  ```bash
  cd ~/brain && python3 .scripts/indexar.py
  ```
  - *Critério de sucesso:* Script finaliza sem erros e printa o total de notas indexadas.

---

### Fase 3 — Script de Busca (`buscar.py`)
**Objetivo:** Criar o script de busca semântica que recebe uma query e retorna as notas mais relevantes.

- [ ] **T3.1 — Criar `~/brain/.scripts/buscar.py`**

  O script deve:
  1. Receber a query como argumento de linha de comando.
  2. Carregar o mesmo modelo `all-MiniLM-L6-v2`.
  3. Converter a query em vetor.
  4. Buscar no ChromaDB os `N` documentos mais parecidos (padrão: 5).
  5. Retornar os resultados em JSON formatado (caminho, score de similaridade, trecho do texto).

  ```python
  # Exemplo de uso esperado:
  # python3 buscar.py "decisão sobre banco de dados"
  # python3 buscar.py "ideia de SaaS produtividade" --top 3
  ```

  ```python
  # Estrutura do script buscar.py
  import chromadb, json, sys, argparse
  from sentence_transformers import SentenceTransformer
  from pathlib import Path

  VAULT = Path.home() / "brain"
  DB_PATH = VAULT / ".chromadb"

  parser = argparse.ArgumentParser()
  parser.add_argument("query", type=str)
  parser.add_argument("--top", type=int, default=5)
  args = parser.parse_args()

  client = chromadb.PersistentClient(path=str(DB_PATH))
  model = SentenceTransformer("all-MiniLM-L6-v2")
  collection = client.get_or_create_collection("brain-notas")

  query_embedding = model.encode(args.query).tolist()
  results = collection.query(
      query_embeddings=[query_embedding],
      n_results=args.top,
      include=["documents", "metadatas", "distances"]
  )

  output = []
  for i in range(len(results["ids"][0])):
      output.append({
          "score": round(1 - results["distances"][0][i], 3),
          "path": results["metadatas"][0][i]["path"],
          "type": results["metadatas"][0][i].get("type", ""),
          "date": results["metadatas"][0][i].get("date", ""),
          "trecho": results["documents"][0][i][:300],
      })

  print(json.dumps(output, ensure_ascii=False, indent=2))
  ```

- [ ] **T3.2 — Testar manualmente a busca**
  - Buscar por algo que foi indexado com palavras diferentes das do arquivo.
  - *Critério de sucesso:* O script retorna a nota correta mesmo sem as palavras exatas.

---

### Fase 4 — Automação da Indexação (Cron)
**Objetivo:** Garantir que novas notas criadas pelo Hermes sejam indexadas automaticamente.

- [ ] **T4.1 — Criar cron para re-indexação automática**
  - Configurar um cron job na VPS para rodar `indexar.py` a cada 30 minutos.
  - Pedir ao Gabriel para adicionar via `crontab -e`:
    ```
    */30 * * * * python3 ~/brain/.scripts/indexar.py >> ~/brain/.scripts/indexar.log 2>&1
    ```
  - *Nota:* O script usa `upsert`, portanto re-indexar uma nota já existente é seguro (idempotente).

- [ ] **T4.2 — Verificar o cron após 30 minutos**
  - Checar o log: `tail -20 ~/brain/.scripts/indexar.log`
  - *Critério de sucesso:* Log mostra execução bem-sucedida sem erros.

---

### Fase 5 — Integração com o Hermes (Gateway Telegram)
**Objetivo:** Ensinar o Hermes a usar a busca semântica ao receber comandos no Telegram.

- [ ] **T5.1 — Definir o comando de trigger**
  - Mapear comandos naturais para acionar a busca. Exemplos:
    - *"Hermes, busca semântica: [query]"*
    - *"Hermes, me ajuda a lembrar de algo sobre [assunto]"*
    - *"Hermes, encontra aquela nota sobre [tópico]"*

- [ ] **T5.2 — Atualizar a Skill `brain-workspace` no Hermes (VPS)**
  - Adicionar a lógica de busca semântica no `~/.hermes/skills/productivity/brain-workspace/SKILL.md`:
    - Quando o usuário pedir para "lembrar", "buscar" ou "encontrar" algo no Brain, o Hermes deve:
      1. Executar: `python3 ~/brain/.scripts/buscar.py "[query extraída da mensagem]" --top 5`
      2. Ler o resultado JSON.
      3. Formatar os top resultados em uma resposta amigável no Telegram (com caminho relativo do arquivo e data).
  - *Nota:* Esta fase exige que Gabriel atualize o SKILL.md na VPS via ttyd.

- [ ] **T5.3 — Testar fluxo completo no Telegram**
  - Mandar uma nota genérica para o Brain via Hermes.
  - Acionar a indexação manualmente com `python3 ~/brain/.scripts/indexar.py`.
  - Perguntar ao Hermes usando palavras diferentes das da nota original.
  - *Critério de sucesso:* Hermes retorna a nota correta no Telegram.

---

### Fase 6 — Monitoramento e Ajustes Pós-Implantação (1-2 semanas)
**Objetivo:** Observar o comportamento do sistema em uso real e afinar a experiência.

- [ ] **T6.1 — Monitorar consumo de memória após ativação**
  ```bash
  free -h
  ```
  - Comparar com o baseline da Fase 0.
  - *Critério de sucesso:* Consumo adicional dentro do esperado (~200MB).

- [ ] **T6.2 — Calibrar o número de resultados (top N)**
  - Ajustar de 5 para 3 se o Hermes estiver retornando notas demais; aumentar para 8 se estiver faltando.

- [ ] **T6.3 — Avaliar qualidade semântica**
  - Por 1-2 semanas, comparar se as notas retornadas pelo Hermes fazem sentido para as queries feitas.
  - Se a qualidade for baixa: estudar substituir o modelo por `paraphrase-multilingual-MiniLM-L12-v2` (melhor suporte a PT-BR).

- [ ] **T6.4 — Atualizar HANDOFF.md**
  - Registrar que a Busca Semântica foi implementada, ativada e está estável.

---

## Resumo de Custos e Impacto na VPS

| Item                      | Detalhe                                     | Custo Adicional |
|---------------------------|---------------------------------------------|-----------------|
| VPS PrimeClaws (base)     | 2vCPU Intel i9, 4GB RAM, 50GB SSD          | $9.99/mês (já pago) |
| Modelo `all-MiniLM-L6-v2` | ~80MB no SSD, ~200MB de RAM em uso         | $0.00 |
| ChromaDB                  | Arquivo local em `~/brain/.chromadb/`      | $0.00 |
| API de Embeddings         | Nenhuma (100% local)                       | $0.00 |
| **Total Adicional**       |                                             | **$0.00** |

*A RAM disponível (4GB - consumo atual do Hermes ~400MB estimado = ~3.6GB livres) é mais que suficiente para carregar o modelo e o banco local sem impacto perceptível.*

---

## Diagrama de Fluxo (Visão Geral)

```
[Telegram: "Lembra daquela nota sobre SaaS?"]
              ↓
         [Hermes recebe]
              ↓
     [Extrai a query da mensagem]
              ↓
  [buscar.py "nota sobre SaaS" --top 5]
              ↓
  [all-MiniLM converte query em vetor]
              ↓
  [ChromaDB (arquivo local) busca por similaridade]
              ↓
  [Top 5 notas mais próximas matematicamente]
              ↓
   [Hermes formata e responde no Telegram]
```

---

*Plano gerado em 2026-09-11. Status: `draft` — aguardando aprovação de Gabriel para iniciar execução.*
