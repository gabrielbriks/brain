---
date: 2026-09-11
projeto: dna-zen-tech
type: decision
status: open
tags: [adr, arquitetura, design-system, transversal]
---

# ADR-001 — Adoção do DNA Zen Tech como Sistema Transversal de UI/UX

## Contexto
Tanto o **Registoo Check** (aplicação voltada para profissionais de saúde e cuidadores) quanto o **Pictae** (plataforma premium para fotógrafos e clientes de ensaios) desenvolveram de forma independente padrões ricos de UI, UX e resiliência:
- O Registoo Check concebeu a filosofia de acolhimento sob alta pressão operacional, o `PermissionGuard`, os Bottom Drawers ergonômicos e a paleta "Emerald Premium".
- O Pictae refinou a experiência com sofisticação editorial (*Warm Minimalism*), o padrão de sincronização resiliente *Zen Sync* (otimista + `localStorage` + debounce + `beforeunload`), o estado 100% na URL via TanStack Router e a *Capabilities Engine*.

À medida que novos produtos são idealizados no Brain (como Historuja, Vox, Widback), replicar ou reinventar esses padrões gera esforço duplicado e inconsistência de qualidade na experiência do usuário.

## Decisão
1. **Desacoplamento de Marca vs. DNA:** Separamos estritamente a identidade de marca (cores institucionais, logos, tipografia de display de cada nicho) do **DNA Zen Tech** (ergonomia, ritmo visual, resiliência técnica, ausência de fricção, psicologia do acolhimento).
2. **Repositório Central no Brain:** Centralizar a documentação, padrões e decisões deste ecossistema em `_projeto/dna-zen-tech/`.
3. **Criação de uma Skill de IA:** Empacotar este conhecimento em um formato de *Skill* (`SKILL.md`) para que agentes de código (Antigravity, Claude Code, Cursor, Hermes) possam automaticamente projetar e auditar código dentro desses preceitos.

## Consequências
- **Positivas:**
  - Redução drástica do tempo de design e implementação de novas telas em qualquer produto.
  - Experiência de altíssima qualidade (Apple-like / acolhedora) consistente em todo o portfólio.
  - Os agentes de IA passam a gerar código de frontend com sensibilidade ergonômica e resiliência comprovadas.
- **Tradeoffs:**
  - Exige manter a documentação transversal atualizada sempre que um novo produto inovar em um padrão de UI/UX.
