---
date: 2026-11-26
projeto: registoo
type: idea
status: open
priority: medium
tags: [feedback, email, widback, engajamento, retencao, openbot, marcos-de-uso]
---

# Fluxo de E-mail de Feedback por Marcos de Uso (+ Widback)

## Resumo da Ideia

Construir um fluxo automatizado (inicialmente avaliado e testado com uma **organização piloto específica**) para disparar e-mails personalizados solicitando feedback qualitativo de usuários ativos do **Registoo** que já atingiram marcos reais de uso na plataforma.

A mensagem combina duas camadas de valor:
1. **Reconhecimento de marco de uso** (celebrando números reais do usuário ou da clínica);
2. **Convite para compartilhar a experiência**, redirecionando direto para o **Widback** já contextualizado na organização correta do Registoo.

O disparo teria duas variantes de composição — **Profissional** e **Gestor/Admin** — e rodaria em rotina periódica (ex.: **1x por mês**), explorando inclusive a possibilidade de orquestrar via **OpenBot** com solução de envio em free tier, baixo custo ou open-source.

---

## Segmentação por Papel e Regras Propostas

### 1. Camada Profissional (`role = 'PROFESSIONAL'`)

- **Critério inicial de elegibilidade (a calibrar):** profissional que já registrou **mais de 15 sessões** na organização.
- **Dados consultados no banco (por organização):**
  - Quantidade de sessões registradas pelo profissional (`check_ins`);
  - Quantidade de evoluções clínicas registradas (`session_evolutions`).
- **Estrutura da copy do e-mail:**
  1. **Abertura pessoal + marco de sessões:**
     > *"Olá, [Nome], eu sou o Gabriel aqui do Registoo e estou vindo falar duas coisas com você. Primeiro, te parabenizar por já ter alcançado [N] registros de sessões..."*
  2. **Complemento condicional de evoluções:**
     - **Se tiver evoluções (`> 0`):** incluir frase complementar celebrando o marco de evoluções registradas (ex.: *"...e também por já ter alcançado [M] evoluções registradas!"*).
     - **Se não tiver evoluções (`= 0`):** substituir pela observação leve (ex.: *"...mas vimos que você ainda não tem nenhuma evolução registrada."*).
  3. **Pedido de feedback + CTA (Widback):**
     > *"Como você alcançou esse marco, queríamos muito ouvir de você qual está sendo a sua experiência com o Registoo..."*
     - Botão/link direcionando para o **Widback** com a organização do Registoo selecionada para envio do feedback.

### 2. Camada Gestor / Admin (`role IN ('ADMIN', 'MANAGER')` / `isOwner`)

- **Critério inicial de elegibilidade (a calibrar):** patamar **mais alto** de sessões da organização, considerando que a clínica pode ter 1, 2, 4, 6, 10+ profissionais no time. Precisamos definir uma média/fórmula coerente (e eventualmente recalibrar também o corte individual do profissional).
- **Dados consultados no banco (agregados da organização):**
  - Total de **usuários/profissionais** (marco do time);
  - Total de **pacientes cadastrados** (`patients`);
  - Total de **sessões registradas** (`check_ins`);
  - Total de **evoluções registradas** (`session_evolutions`).
- **Estrutura da copy do e-mail:**
  1. **Abertura + marcos da clínica:** celebrar os números consolidados de pacientes cadastrados, sessões registradas e evoluções (e, quando aplicável, tamanho do time).
  2. **Complemento condicional de evoluções:** se a organização ainda não tiver evoluções (`= 0`), usar variação equivalente (*"mas vocês ainda não têm nenhuma evolução cadastrada"*).
  3. **Pedido de feedback adaptado à gestão + CTA (Widback):** phrasing ajustado para a visão do gestor/admin sobre a operação da clínica no Registoo, redirecionando para o Widback no contexto da organização.

---

## Contexto Técnico no Codebase (Enriquecimento para Discussão)

Levantamento feito em `registoo-check` (`apps/api`, `apps/web`) e `widback` para apoiar a sessão de refinamento:

### 1. Schema e Modelo de Dados (`apps/api/src/db/schema.ts` — Drizzle + PostgreSQL)

- **Papéis e multi-organização (`organization_members`):**
  - `role` usa enum `['ADMIN', 'MANAGER', 'PROFESSIONAL']` + flag `isOwner` e `isActive`.
  - Há `uniqueIndex` em `(userId, organizationId)`: **o mesmo usuário pode pertencer a mais de uma organização**, inclusive com papéis diferentes. Portanto, toda contagem e o link de feedback precisam ser **escopados por `organizationId`**.
- **Sessões (`check_ins`):**
  - Campos relevantes: `organizationId`, `professionalId`, `patientId`, `checkInAt`, `checkOutAt`, `isManuallyClosed`, `evolutionWaived`.
  - **Ponto de atenção:** decidir se contamos todas as linhas de `check_ins` ou apenas sessões concluídas (`checkOutAt IS NOT NULL`).
- **Evoluções (`session_evolutions`):**
  - Campos relevantes: `organizationId`, `professionalId`, `createdByUserId`, `patientId`, `checkInId`.
  - **Nuance importante do schema:** `professionalId` representa o profissional responsável pelo atendimento, enquanto `createdByUserId` registra quem de fato redigiu a evolução (outro membro pode preencher). Definir qual campo contar no e-mail do profissional.
  - **Nuance de plano/configuração (`organizations`):** existem `requireSessionEvolution` (`boolean`) e `maxEvolutionsPerMonth` (`integer`, default `0`). Se o plano da organização **não libera evoluções** (`maxEvolutionsPerMonth === 0` sem add-on), mencionar *"você ainda não tem evoluções registradas"* pode soar incoerente — ou precisa ser adaptado para não gerar confusão (ou usado deliberadamente como descoberta de recurso para o gestor).
- **Pacientes (`patients`):**
  - Possui flag `isActive` (`boolean`). Definir se no resumo do gestor contamos apenas pacientes ativos ou o total histórico cadastrado.
- **Isolamento multi-tenant (`CONTEXT.md` / ADR-009 / ADR-016):**
  - Jobs que varrem múltiplas organizações devem aplicar filtro explícito de `organization_id` em cada query agregada (nunca vazar dados entre clínicas) e, no piloto, filtrar pela `organization_id` específica.

### 2. Restrição de Vocabulário Jurídico (`CONTEXT.md`)

- O posicionamento do Registoo como **prontuário/registro assistencial** (e não controle de ponto) é inegociável.
- Na copy dos e-mails, **evitar** termos como *check-in/check-out*, *batida de ponto*, *jornada* ou *provar presença*. Usar sempre **sessões assistenciais / registros de sessões / atendimentos** e **evoluções clínicas**.

### 3. Integração com o Widback (`apps/web/src/lib/widback.ts` + `use-widback.ts`)

- O **Widback já está integrado** no dashboard logado (`app.registoo.com.br`), com `launcher: false` e identificação automática via:
  ```ts
  identifyWidback({ id, email, name, plan, organizationId, role })
  ```
- **Ponto arquitetural importante:** o Widback é um **widget embutido** (`cdn.widback.com/widget.js`), sem página pública standalone própria (e valida `origins` permitidas na API).
- Logo, para o clique no e-mail cair direto no Widback com a **organização certa selecionada**, o caminho mais limpo é um **deep link no `app.registoo.com.br`** — por exemplo:
  - `https://app.registoo.com.br/dashboard?org=<organizationId>&feedback=1` (ou rota dedicada `/feedback?org=<organizationId>`).
  - Ao abrir: garante autenticação (preservando destino após login), seleciona `activeOrganizationId = <organizationId>` na store/sessão e chama `openWidback()` assim que o script estiver `ready` e `identifyWidback` sincronizado.
  - **Bônus:** o feedback chega no Discord com `userId`, `email`, `name`, `plan`, `organizationId` e `role` já preenchidos, e mantendo os avisos de LGPD já configurados em `WIDBACK_TEXTS` (não enviar dados de pacientes).

### 4. Infraestrutura de E-mail e Jobs já Existente

- **E-mail no Registoo:** `apps/api/src/utils/email.ts` já utiliza **Resend** (`RESEND_API_KEY`, `EMAIL_FROM`).
- **Jobs no Registoo:** já existe a pasta `apps/api/src/jobs/` (`trial-expiration.job.ts`, `retention.job.ts`, `recurrence-scheduler.ts`).
- **OpenBot + E-mail Marketing / Baixo Custo:**
  - Possibilidade de centralizar a rotina mensal (e futuras campanhas de relacionamento/lifecycle) em uma agenda no **OpenBot**, conectando a uma ferramenta de disparo com free tier generoso ou open-source (ex.: Resend free tier, Brevo, Amazon SES, Listmonk self-hosted, Plunk, etc.).

---

## Complexidades e Pontos em Aberto para a Sessão de Discussão

1. **Organização Piloto:**
   - Qual organização específica será usada para o teste inicial?
   - Puxar os números reais dela (profissionais, pacientes, sessões, evoluções, plano) para validar se os cortes fazem sentido na prática.
2. **Calibração dos Marcos (Thresholds):**
   - Profissional: 15 sessões é total histórico ou em uma janela (ex.: últimos 30 dias)? Vale testar marcos progressivos (ex.: 15, 50, 100)?
   - Gestor/Admin: número fixo de sessões da clínica ou fórmula baseada no tamanho do time (ex.: `max(30, 15 * profissionais_ativos)`)?
3. **Cadência, Idempotência e Anti-Spam:**
   - Como garantir que o usuário não receba o **mesmo e-mail todo mês** após bater 15 sessões?
   - Definir tabela/registro de envios (ex.: `feedback_email_logs` ou marco atingido por `(user_id, organization_id, milestone)`), período de cooldown (ex.: no máximo 1 pedido a cada 90 dias ou por novo marco) e respeito a quem já enviou feedback recentemente.
4. **Sobreposição de Papéis:**
   - Se um `ADMIN` ou `MANAGER` também realiza atendimentos como profissional (clínica solo ou dono que atende), recebe só o e-mail de Gestor/Admin ou uma versão híbrida?
   - Se o usuário estiver em 2 organizações elegíveis no mesmo mês, consolidar ou priorizar?
5. **Tratamento do Caso "Sem Evoluções":**
   - Diferenciar quando a organização **tem** evoluções habilitadas no plano e não usa vs. quando o plano atual **não inclui** evoluções (`maxEvolutionsPerMonth === 0`).
6. **Deep Link vs. Fricção de Login no Widback:**
   - Se o profissional abrir o e-mail no celular/desktop sem sessão ativa no navegador, o login (magic link / Google / senha) pode derrubar a taxa de conversão? Vale avaliar o fluxo de redirect pós-login ou um formulário leve/tokenizado no futuro.
7. **Arquitetura de Disparo & Ferramenta (OpenBot vs. API do Registoo):**
   - Onde mora a lógica de consulta ao banco + disparo?
     - *Opção A:* Job/endpoint na própria API do Registoo usando Resend (zero infra nova, acesso direto ao Drizzle/Postgres, ideal para o piloto).
     - *Opção B:* Agenda no OpenBot consultando endpoint protegido/read-only e disparando via provedor de e-mail marketing / open-source (ex.: Listmonk, Brevo, Resend Broadcasts/Audiences).
   - Comparar limites de free tier, entregabilidade (SPF/DKIM/DMARC no domínio `registoo.com.br`), separação de reputação entre e-mail transacional e marketing/relacionamento, e custo mensal.
8. **LGPD e Conformidade:**
   - E-mail periódico de relacionamento/feedback precisa de **link de descadastro (opt-out)** e flag de preferência no usuário/membro?
   - Verificar Política de Privacidade do Registoo quanto a comunicações de pesquisa/feedback.

---

## Referências Relacionadas

- Ideia complementar de feedback qualitativo no Brain: [2026-09-29-a-sua-voz-pode-guiar-a-registoo.md](../2026-09-29-a-sua-voz-pode-guiar-a-registoo.md)
- Schema do Registoo: `registoo-check/apps/api/src/db/schema.ts`
- Integração atual do Widback no Registoo: `registoo-check/apps/web/src/lib/widback.ts` e `registoo-check/apps/web/src/hooks/use-widback.ts`
- Envio de e-mail atual do Registoo: `registoo-check/apps/api/src/utils/email.ts`
