---
date: 2026-11-27
area: empreendedor
type: idea
status: open
tags: [monetizacao, reforma-tributaria, receita-federal, cbs, ibs, clinicas, precificacao, slo, registoo]
---

# Ideia & Análise de Viabilidade: Reforma Tributária (Repos Receita Federal) para Reajuste e Caixa de Clínicas/Profissionais

> Conexão direta com [[2026-11-26-arquitetura-4-vias-giro-alto-e-2-vias-100k]] e [[2026-11-26-monetizacao-know-how-socia-aba-openbot-6-digitos]].
> Pesquisa de mercado e análise técnica realizadas em **2026-11-27**.

---

## 1. O que a Receita Federal liberou no GitHub (`github.com/ReceitaFederal`)

Todos os repositórios oficiais da **Calculadora RTC (Reforma Tributária do Consumo — LC 214/2025)** estão sob **licença MIT** (uso comercial permitido), atualizados ativamente (commits em 2026-11-27):

| Repositório | Stack | O que entrega na prática |
|---|---|---|
| `calculadora-rtc-regime-regular` | Java 25 / Spring Boot 4.1.2 / SQLite | API REST para cálculo de CBS, IBS e Imposto Seletivo (`/regime-geral`), base unificada de NFS-e, geração/validação XML e endpoints `/dados-abertos/` (NBS, `cClassTrib`, alíquotas União/UF/Município, fundamentações legais). |
| `calculadora-rtc-simples-nacional` | Java 25 / Spring Boot 4.1.2 / SQLite | API REST de cálculo CBS/IBS no Simples Nacional + `/calculadora/simples-nacional/atividades` (anexos, tipo de documento, `cClassTrib`). |
| `calculadora-rtc-gerador-danfse` | Go 1.27+ | Serviço HTTP/Docker para gerar PDF do DANFSe a partir de XML de NFS-e. |

---

## 2. A dor é real em 2026–2027? (Pesquisa Web)

**Sim — e o timing (fim de Nov/2026 às portas de Jan/2027) é forte:**

1. **Virada de chave em Jan/2027:** a **CBS** entra em vigor de forma efetiva substituindo PIS/Cofins (antes ~3,65% "por dentro" no Lucro Presumido; agora cálculo **"por fora"** somado ao preço, com referência padrão estimada pelo TCU em ~11,3% e ~4,5% para saúde após o redutor de 60%), junto com o início gradual do **split payment** (retenção automática do imposto na liquidação do cartão/Pix/boleto).
2. **Armadilhas específicas de clínicas e terapeutas:**
   - **Redutor de 60% não é automático:** exige enquadramento correto no código **NBS** e ausência de "nota mista" (misturar atendimento de saúde com produto/serviço acessório sem separar derruba o benefício).
   - **Folha/repasse de ATs não gera crédito de IBS/CBS:** como a maior parte do custo de uma clínica é mão de obra/honorários, o aproveitamento de créditos da não-cumulatividade é baixo — a carga líquida tende a subir e espremer margem.
   - **Sem reajuste automático:** contratos e pacotes fechados não corrigem sozinhos; quem não recalcular sessão/pacote perde margem silenciosamente.
   - **Simples Híbrido vs. Tradicional e PF (Carnê-Leão) vs. PJ:** mudança no ponto de equilíbrio para quem atende operadoras/B2B vs. famílias B2C.

---

## 3. Veredito Honesto de Viabilidade (Onde trava vs. Onde dá caixa rápido)

### Onde NÃO funciona (armadilha)
- **Vender "calculadora de imposto da Reforma Tributária" isolada:** a própria Receita Federal oferece calculadora gratuita, e dezenas de contabilidades médicas (Caveo, Dr. Finanças, Pigatti, ReciboNaHora) já dão simuladores de IBS/CBS **de graça** como isca de lead.
- **Tentar competir com ERPs hospitalares (SimTax / TOTVS / Afya)** em clínicas grandes sem ter chancela contábil.
- **Dispersar em uma empresa nova fora do ecossistema** (quebraria a regra de foco de [[2026-11-26-arquitetura-4-vias-giro-alto-e-2-vias-100k]]).

### Onde TEM brecha real de caixa rápido (viável se empacotado certo)
O contador diz *quanto imposto vai pagar*; quase ninguém entrega para o dono da clínica/terapeuta o **painel comercial de sobrevivência de margem para 2027**:
> *"Qual deve ser o novo preço da minha sessão/pacote em 2027, quanto o split payment vai tirar do meu caixa na hora do Pix/cartão, e qual texto eu mando para as famílias/convênios justificando o reajuste?"*

**3 formatos possíveis (do mais rápido para o mais estruturado):**

1. **Formato A — Kit / Micro-ferramenta SLO de Virada de Ano (R$ 47–97, giro rápido em Dez–Jan):**
   - Mini-app/agente usando a API da Receita (`calculadora-rtc-*` em Docker/Java no Azure) + camada de precificação: clínica/terapeuta informa regime, município, NBS/tipo de atendimento, valor atual da sessão, % de repasse para ATs e insumos.
   - **Entrega:** preço-alvo 2027 para manter margem, impacto do *split payment* no fluxo de caixa, alerta de nota mista/NBS e **kit de scripts prontos** (WhatsApp/PDF) para comunicar o reajuste anual aos pais/pacientes sem desgaste.
   - *Por que vende agora:* urgência sazonal de **reajuste de tabela de janeiro**.
2. **Formato B — "Cavalo de Troia B2B" para o `Coulson` (SDR) & Registoo:**
   - Diagnóstico gratuito/low-ticket ("Raio-X de Margem & Repasse 2027") para abordar donos de clínicas ABA/saúde agora no fim do ano e converter para a **Via Principal A** (*Operação Domiciliar Blindada + Registoo Anual*).
3. **Formato C — Módulo nativo no Registoo (médio prazo):**
   - Calculadora de margem líquida de sessão/repasse dentro do próprio Registoo, usando os endpoints oficiais de NBS e alíquotas da Receita Federal.

---

## 4. Blindagens Obrigatórias

1. **Responsabilidade contábil (CRC):** posicionar explicitamente como **simulador de precificação, margem e fluxo de caixa** baseado nos motores públicos da Receita Federal (MIT), com aviso claro de que enquadramento fiscal definitivo e NBS devem ser validados pelo contador da clínica.
2. **Anti-dispersão:** só executar se entrar **como isca sazonal de Dez/2026–Jan/2027 alimentando a trilha Registoo/Clínicas**, sem atrasar o Workshop #1 e as vias principais definidas em [[2026-11-26-arquitetura-4-vias-giro-alto-e-2-vias-100k]].
3. **Infra técnica:** os motores `calculadora-rtc-regime-regular` e `simples-nacional` rodam em Java 25 + SQLite (~512MB–1GB RAM cada se subirem juntos); verificar folga de memória da VM `Standard_B4as_v2` antes de subir em produção contínua.

---

## 5. Próximo passo sugerido (se Gabriel aprovar)

- Estacionada com `status: open` para retomar após subir as próximas ondas de agentes no OpenBot.
- Quando retomar: acionar a **`EDITH`** para mapear concorrentes/preços de ferramentas de precificação para 2027 e dores reais de clínicas, e o **`Fury`** para definir se entra como **Via de Giro sazonal** ou **isca B2B do `Coulson` para a Via Principal A (Registoo)**.

---

## 6. Glossário Rápido (sem economês)

- **CBS (Contribuição sobre Bens e Serviços):** imposto federal novo que substitui PIS e Cofins (entra valendo em Jan/2027).
- **IBS (Imposto sobre Bens e Serviços):** imposto estadual + municipal novo que substitui ICMS e ISS de forma gradual.
- **Imposto "por dentro" vs. "por fora":** no modelo antigo ("por dentro"), o imposto já vinha embutido dentro do preço da sessão; no novo ("por fora"), ele é calculado e somado por cima do preço líquido na nota.
- **Redutor de 60% e código NBS:** serviços de saúde pagam apenas 40% da alíquota padrão de CBS/IBS, mas só se a nota usar o código oficial certo do serviço (**NBS**, equivalente ao catálogo de serviços da Receita).
- **Nota mista:** emitir uma única nota juntando atendimento de saúde (com desconto de 60%) e outro item sem desconto (ex.: venda de produto ou sala); se não separar, corre risco de perder o benefício na nota inteira.
- **Não-cumulatividade / crédito:** o imposto que você pagou ao comprar insumos/softwares vira "vale-desconto" para abater do imposto da sua venda. Como clínica gasta muito com gente (salário/repasse de ATs) e pouco com mercadoria, quase não sobra crédito para abater.
- **Split payment (pagamento dividido):** na hora que o cliente passa o cartão ou Pix, o banco/maquininha já manda a fatia do imposto direto para o governo e só deposita o líquido na conta da clínica — reduz o dinheiro livre em caixa no mês.
- **Simples Híbrido:** opção para quem está no Simples Nacional escolher pagar CBS/IBS separado para conseguir repassar crédito fiscal quando atende empresas/planos de saúde (B2B).
