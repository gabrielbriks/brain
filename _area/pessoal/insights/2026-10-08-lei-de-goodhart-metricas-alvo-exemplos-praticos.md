---
date: 2026-10-08
area: pessoal
type: insight
status: open
priority: medium
tags: [lei-de-goodhart, metricas, gestao, economia, otimizacao, analise-de-dados]
---

# Lei de Goodhart: quando uma métrica se torna alvo, deixa de ser uma boa métrica

## Definição

> **"When a measure becomes a target, it ceases to be a good measure."**  
> — Charles Goodhart, economista britânico (1975)

Quando uma medida estatística regular é pressionada para fins de controle, ela tende a colapsar porque as pessoas começam a otimizar a própria métrica em vez do objetivo original.

O problema não é medição em si — é usar um número como se contasse toda a história.

---

## Como Funciona (4 Passos)

1. Escolhe-se um número para medir sucesso
2. Define-se uma meta para aquele número
3. As pessoas mudam o comportamento para atingir a meta
4. O número melhora, mas o objetivo original pode não melhorar (ou piorar)

---

## Exemplos Práticos por Área

### 1. Economia e Governo

**Cobra Effect (Índia, domínio britânico)**
- Objetivo: reduzir cobras venenosas nas ruas
- Métrica: número de cobras mortas entregues ao governo (pagamento por cobra)
- O que aconteceu: pessoas começaram a **criar cobras** para matar e entregar
- Quando o programa acabou, criadores soltaram as cobras → mais cobras nas ruas
- **Resultado:** a métrica enganou; o objetivo piorou

### 2. Negócios e Vendas

**Meta de vendas (vendedor de carros)**
- Objetivo: vender mais carros
- Métrica: número de carros vendidos por mês (bônus se > 20)
- O que aconteceu:
  - Final de mês: vendedores que não bateram 20 oferecem descontos agressivos (lucro reduzido)
  - Vendedores que já bateram 20: adiam vendas para o mês seguinte (saída de caixa prévia)
- **Resultado:** métrica de "carros vendidos" subiu, mas lucro caiu

**Cupons de desconto recorrentes**
- Objetivo: estimular compras
- Métrica: uso de cupons de desconto
- O que aconteceu: clientes atrasam compras intencionalmente para esperar cupom
- **Resultado:** receita previsível cai, margem reduz

**Perks de startup**
- Objetivo: atrair os melhores talentos
- Métrica: benefícios oferecidos (café, massa, mesa de sinuca)
- O que aconteceu: atrai pessoas interessadas em perks, não necessariamente os melhores profissionais
- **Resultado:** cultura de "benefício" substitui cultura de desempenho

### 3. Educação

**Notas escolares como proxy de aprendizado**
- Objetivo: alunos aprenderem mais
- Métrica: notas em provas
- O que aconteceu: professores focam em "ensinar para a prova" (teaching to the test)
- O que é deixado de lado: pensamento crítico, criatividade, habilidades interpessoais
- **Resultado:** notas sobem, aprendizado real pode não acompanhar

### 4. Tecnologia e SEO

**PageRank do Google**
- Objetivo: ranquear páginas por qualidade
- Métrica: número de backlinks (links de outras páginas)
- O que aconteceu: webmasters criaram "granjas de links" e trocas de backlinks artificiais
- O conteúdo real ficou secundário à quantidade de links
- **Resultado:** Google mudou o algoritmo; hoje muitos fatores são não públicos justamente para evitar Goodhart

### 5. Call Centers

**Tempo médio de chamada (3 minutos por chamada)**
- Objetivo: eficiência no atendimento
- Métrica: tempo médio de cada chamada
- O que aconteceu: atendentes encurtam chamadas, desligam prematuramente, não resolvem problemas complexos
- **Resultado:** tempo médio cai, satisfação do cliente despenca

### 6. Pesquisa Acadêmica

**Número de artigos publicados**
- Objetivo: produtividade científica
- Métrica: quantidade de papers publicados
- O que aconteceu: publicação de resultados menores, "p-hacking" (manipulação de dados para significância estatística), viés de publicação (só resultados positivos publicados)
- **Resultado:** mais artigos, menos replicabilidade, ciência mais fraca

---

## Implicações para Análise de Dados e ML

- Um modelo treinado com dados históricos pode colapsar quando colocado em produção, porque **as pessoas mudam seu comportamento por causa do modelo**
- Exemplo: se um banco usa score de crédito para aprovar empréstimos, os candidatos aprenderão a "jogar" o sistema
- Em Data Science: Goodhart's Law = "o comportamento muda porque o modelo existe"

---

## Como Mitigar (como evitar ser vítima de Goodhart)

| Estratégia | Aplicação |
|---|---|
| **Use múltiplas métricas** | Não confie em um único número; triangule com indicadores qualitativos e quantitativos |
| **Métricas de resultado, não de processo** | Meça o que importa (receita, satisfação), não apenas o que é fácil de contar (número de chamadas) |
| **Mantenha parte do algoritmo secreto** | No SEO/Google: não expor todos os pesos evita manipulação |
| **Audite regularmente** | Revise se a métrica ainda reflete a realidade ou se está sendo "jogada" |
| **Incentive comportamentos, não apenas números** | Bônus por qualidade do atendimento, não apenas por volume |
| **Teste com cenários adversários** | Pergunte: "se alguém quisesse burlar essa métrica, como faria?" |
| **Métricas de contra-balanço** | Se mede "velocidade", meça também "qualidade" ou "reclamações" |

---

## Exemplo Prático para Abstrair (Sistema de Bônus)

```yaml
# CENÁRIO: Equipe de suporte técnico
Objetivo: Melhorar satisfação do cliente
Métrica alvo: Número de tickets resolvidos por dia
Meta: 50 tickets/dia por atendente

O que acontece:
- Atendentes resolvem tickets fáceis rapidamente (50/dia atingido)
- Tickets complexos são deixados de lado ou fechados prematuramente
- Cliente fica insatisfeito (problema não resolvido de verdade)
- Métrica "tickets resolvidos" está ótima; NPS (satisfação) cai

Solução (anti-Goodhart):
- Métrica principal: NPS do cliente após resolução
- Métrica secundária: % de tickets reabertos em 7 dias
- Métrica de processo: tickets resolvidos/dia (apenas como contexto, não alvo)
- Bônus vinculado a NPS + reabertos, não apenas volume
```

---

## Frase para Memorizar

**"Quando você mede algo, as pessoas otimizam para essa medida, não para o propósito por trás dela."**

---

## Conexão com Seus Projetos (Gabriel)

| Projeto | Risco de Goodhart | Métrica de Contra-balanço |
|---|---|---|
| **Registoo** (atendimentos domiciliares) | Número de atendimentos/dia → atendentes aceleram, qualidade cai | Satisfação do paciente, taxa de reatendimento |
| **Zenckup** (backup Postgres) | Número de backups feitos → backups vazios ou incompletos | Taxa de restauração bem-sucedida, integridade dos dados |
| **Negócio "Boring"** | Vendas/mês → descontos agressivos, margem reduzida | LTV (lifetime value), margem de lucro, churn |

---

*Nota criada em 2026-10-08 por Gabriel — com base em pesquisa sobre Lei de Goodhart*