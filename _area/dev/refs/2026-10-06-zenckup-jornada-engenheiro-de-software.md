---
date: 2026-10-06
area: dev
type: ref
status: open
tags: [carreira, engenharia, arquitetura, entrevista, zenckup, adr, backup, trade-offs]
---

# zenckup como material de estudo: o que ele ensina sobre ser um bom engenheiro

> Origem: sessão de adoção do zen-ai-workflow no zenckup (2026-10-06). Fontes no repo
> `/home/gabriel/www/zenckup`: `docs/adr/001-*.md`, `docs/learnings/replicar-dentro-da-fronteira.md`,
> `AGENTS.md`, `CONTEXT.md` (com 3 diagramas Mermaid: execução, compartilhado vs por projeto e decisão por escala), `scripts/test-local.sh`. Projeto no Brain: `_projeto/zenckup/`.
> Feita para **revisão rápida** — leia o TL;DR e vá direto ao que precisar.

## TL;DR (30 segundos)

- **Decisão central:** em vez de um hub de backup (que exigiria banco público), **uma instância
  genérica dentro de cada projeto**. Isola rede e credencial; o custo é config repetida e um bug
  que atinge todos.
- **Vocabulário:** agent-based por fronteira · silo model · bulkhead · data gravity · menor
  privilégio · twelve-factor.
- **O que diferencia o trabalho:** não foi o código (~40 linhas), foi **entender o trade-off, medir o
  raio de dano e deixar a decisão registrada e testável**.

## A tese de carreira

Um engenheiro sênior se reconhece menos por escrever mais código e mais por **decidir bem sob
restrição e deixar isso legível para quem vem depois**. O zenckup é um laboratório pequeno onde cada
uma dessas habilidades aparece de forma concreta e demonstrável.

## Mapa de competências → evidência no zenckup

| Competência | Como aparece no projeto | Onde ver |
|---|---|---|
| **Pensar em trade-offs, não em soluções** | Hub central vs instância por projeto: a escolha nasce de uma restrição real (rede privada isolada), não de preferência. | ADR-001 |
| **Raio de dano (blast radius)** | O isolamento protege a rede, **não** a execução: um bug no script atinge os três. Nomear isso e mitigar. | Learning, `AGENTS.md` (tiers) |
| **Segurança como design, não como etapa** | Recusar banco público; credencial de produção nunca em sessão de IA. | `AGENTS.md` (restrições) |
| **Operabilidade / falhar alto** | `set -euo pipefail`, sanity check de < 100 bytes, `exit 1` para o Cron Job aparecer como falho. Backup vazio "com sucesso" é o pior resultado. | `backup.sh` |
| **Testar o que importa** | Backup só vale se restaura: teste ponta a ponta com Postgres + MinIO, restaura em banco vazio e confere as linhas. | `scripts/test-local.sh` |
| **Registrar decisões** | ADR (o porquê) separado de learning (o que se generaliza) e de contexto (o estado atual). | `docs/` |
| **Calibrar cerimônia ao risco** | Tiers T0–T3 pelo raio de impacto, não pelo tamanho do diff: uma flag de uma linha no `pg_dump` é T2. | `AGENTS.md` |
| **Trabalhar com IA com critério** | Gates humanos, revisão por outro modelo, verificação rodando de verdade (não "parece certo"). | workflow, HANDOFF |

## Os padrões, com a ressalva honesta

Nomes vêm de conhecimento geral, **não** de fonte consultada na sessão — confirmar os que for citar.

- **Agent-based por fronteira** — componente pequeno dentro de cada fronteira (agentes de
  monitoramento; `CronJob` por namespace no Kubernetes). *O que mais descreve a decisão.*
- **Silo model** (AWS SaaS Lens: silo / pool / bridge) — runtime isolado por tenant com artefato
  compartilhado. Explica o trade-off bug compartilhado vs isolamento.
- **Bulkhead / cell-based** — particionar para limitar dano. Aqui limita vazamento de rede, não falha
  de código.
- **Data gravity** — leve a computação ao dado.
- **Menor privilégio / superfície de ataque** — o argumento mais forte contra o hub.
- **Twelve-Factor, fator III** — config no ambiente; é o que torna a imagem reutilizável.
- **Sidecar — só aproximado.** Mesma lógica de co-locação, mas o zenckup é job agendado, não
  contêiner de vida longa junto da app. **Não chamar de sidecar** numa entrevista.

## Roteiro de entrevista (90 segundos)

> Precisava de backup para três produtos em Railway, mas a rede privada é isolada por projeto. Um
> serviço central só alcançaria os bancos se eu os expusesse publicamente, trocando falta de backup
> por superfície de ataque. Então fiz o contrário: um artefato genérico, configurado por ambiente,
> com uma instância dentro de cada projeto — um silo com código compartilhado. O custo é
> configuração repetida e um bug que atinge os três; mitiguei com teste ponta a ponta local e tiers
> de mudança mais rígidos para o formato do dump.

**Por que funciona:** problema → restrição real → decisão → custo assumido → mitigação. O fecho
mostra que o trade-off foi entendido.

**Perguntas que isso costuma abrir** (vale ter resposta pronta):

- *"E se o banco crescer muito?"* → hoje é dump completo diário; incremental/WAL archiving está
  declarado fora do escopo, a revisitar se o tamanho ou a janela virarem problema.
- *"Como você sabe que o backup funciona?"* → o teste local restaura e confere linhas; o restore
  contra o banco real de cada projeto ainda é manual e **não** foi exercitado em produção.
- *"E o monitoramento?"* → hoje o sinal é o status do Cron Job; alerta ativo foi adiado de
  propósito. É uma limitação consciente, não um esquecimento.
- *"Por que não um serviço gerenciado?"* → o plano Hobby do Railway não oferece backup; essa foi a
  restrição de partida.

## Como o modelo escala (1, 3 ou 10 projetos)

Detalhe e diagramas em `zenckup/CONTEXT.md`, seção Arquitetura. Em resumo:

- Custo de **código** é constante (1 repositório); o que cresce linearmente é **configuração e
  operação** — 6 variáveis, 1 Cron Job e 1 restore manual por projeto.
- Dois riscos crescem junto com N: **propagação de bug** (todos buildam o mesmo repo; com 10, fixar
  tag por projeto e promover aos poucos) e **credencial compartilhada** (token com escopo de bucket
  enxerga o prefixo de todos; bucket ou token por projeto devolve o isolamento).
- Os limiares 3 e 10 são estimativas, não medidas. Dois pontos de produto seguem **sem conferir**:
  se o Railway acompanha o branch automaticamente e se o token do R2 aceita escopo por prefixo.

## Lacunas reais (para não se enganar na revisão)

Estudar isso é mais útil do que só reler o que já está bom:

- **Restore em produção nunca testado** e **sem alerta ativo** — as duas coisas que mais pesariam
  numa conversa honesta sobre confiabilidade.
- **`--no-owner`/`--no-acl`** ainda pendente (T2): restaurar em outro usuário pode falhar.
- **RPO/RTO não definidos.** Dump diário implica até ~24h de perda possível; isso nunca foi
  declarado como requisito. Saber nomear RPO e RTO é vocabulário básico de confiabilidade.

## Para estudar a seguir

Referências conhecidas; confirmar edição e capítulos antes de depender delas.

- **Release It!** (Michael Nygard) — bulkheads, circuit breakers, estabilidade em produção.
- **Designing Data-Intensive Applications** (Martin Kleppmann) — replicação, backup, trade-offs de
  consistência e durabilidade.
- **Google SRE Book** (online, gratuito) — confiabilidade, o papel de testar restauração.
- **The Twelve-Factor App** (12factor.net) — config, processos, logs.
- **AWS Well-Architected, SaaS Lens** — silo / pool / bridge.

Exercício concreto que fecharia a maior lacuna: **definir RPO/RTO do Widback**, depois exercitar um
restore real e **medir** o tempo.

## Como este material se conecta

- Decisão: `zenckup/docs/adr/001-instancia-de-backup-por-projeto.md`
- Aprendizado + padrões: `zenckup/docs/learnings/replicar-dentro-da-fronteira.md`
- Adoção do workflow: `_projeto/zenckup/insights/2026-10-06-adocao-do-zen-ai-workflow.md`
- Calibragem de tiers: `_projeto/zen-ai-workflow/insights/2026-10-06-primeira-adocao-em-projeto-pequeno-zenckup.md`
