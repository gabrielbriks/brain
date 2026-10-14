---
date: 2026-10-14
projeto: zen-ai-workflow
type: insight
status: open
tags: [adocao, pictae, migracao, claude-code, tiers, handoff]
---

# Adoção em projeto legado de origem Gemini: Pictae

Segunda adoção registrada, depois do zenckup
(`2026-10-06-primeira-adocao-em-projeto-pequeno-zenckup.md`). O perfil é o oposto do zenckup:
monorepo com meses de documentação viva, 38 planos e 5 fontes de instrução para agentes. Foi a
primeira adoção na v0.2.0. Os detalhes da execução estão em
`_projeto/pictae/insights/2026-10-14-adocao-do-zen-ai-workflow.md`.

## O que este caso ensina

- **A stack documentada voltou a contradizer a stack real.** No Pictae, as instruções proibiam
  Next.js, mas a landing roda Next.js 16. No Registoo, a contradição era Prisma × Drizzle. São dois
  casos independentes do mesmo padrão. Isso confirma que o `CONTEXT.md` precisa ser conferido
  contra os `package.json`, e não copiado dos docs. Pelo Princípio 8, vira candidato a instrução
  explícita no roteiro de migração.
- **O plano se perdeu no corte de sessão.** O rascunho do plan-039 foi escrito, mas não foi
  commitado antes do limite de conta, e a sessão seguinte teve de reconstruí-lo. A regra de "corte
  de sessão forçado" cobre o WIP de código, mas não deixa explícito que **o plano em revisão
  também é WIP**. Candidato: o Plan nasce commitado numa branch já no momento em que vai para o
  gate, e não só depois de aprovado.
- **A calibragem de tier pelo raio de impacto se repetiu.** Ela surgiu no zenckup e coube direto
  no Pictae (billing, isolamento entre tenants, sessão do cliente, deleção irreversível no R2).
  Com dois projetos, é candidata a seção no template do `AGENTS.md`.
- **O Claude Code precisa de uma ponte própria.** Ele não lê `AGENTS.md` nem `.agents/` por conta
  própria. A solução foi `CLAUDE.md` com `@AGENTS.md` e o symlink
  `.claude/skills → .agents/skills`. O Registoo já tinha o `CLAUDE.md`, então são dois casos.
  Candidato a passo explícito no roteiro de migração e a template.
- **O contador único de Spec/Plan se justificou na prática.** No INDEX retroativo apareceram
  spec e plan com o mesmo número tratando de assuntos diferentes (013, 023 e 024). É exatamente a
  colisão que o contador compartilhado previne.
- **O idioma dos commits é preferência do Gabriel, não herança do repositório.** O histórico do
  Pictae estava em inglês e o agente seguiu esse padrão. O Gabriel corrigiu: os commits são em
  português, como no Registoo. A regra de ouro 11 do template não fala de idioma; vale deixar
  explícito.
- **Adoção também mexeu no fluxo de branches.** A `develop` substituiu a `staging`. A parte de
  CI/CD foi separada numa issue própria para o plano de adoção continuar só com documentação.
  Funcionou bem: a branch é barata, enquanto os workflows envolvem segredos e painéis externos.

## Em aberto

- Verificar se o Claude Code descobre skills aninhadas (`pasta/sub/SKILL.md`) pelo symlink. Se não
  descobrir, o padrão `.agents/skills/` com subpastas precisa de ajuste para ser portátil.
- Decidir se os candidatos acima entram numa v0.3.0. Em especial: o plano commitado ao ir para o
  gate, a ponte do Claude Code no roteiro de migração e a calibragem por raio de impacto no
  template.
