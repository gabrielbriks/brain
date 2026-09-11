---
date: 2026-09-11
projeto: dna-zen-tech
type: idea
status: open
priority: high
tags: [skill, agent, claude-code, cursor, antigravity, hermes, ux-review]
---

# Ideia: Especificação da Skill de Agente "Zen Tech UI/UX"

> **Visão**: Uma Skill rica e padronizada (`SKILL.md`) que ensine qualquer agente de IA (Antigravity CLI/IDE, Claude Code, Cursor, Hermes) a projetar, auditar e implementar interfaces sob os princípios do **DNA Zen Tech**.

---

## 1. O Problema Atual dos Agentes gerando Frontend

Quando pedimos para LLMs gerarem código de interface:
1. **Falta de sensibilidade ergonômica:** Eles enchem o mobile de ícones minúsculos e tabelas apertadas.
2. **Ansiedade visual:** Usam sombras agressivas, quinas secas e cores frias sem contraste aconchegante.
3. **Fragilidade de estado:** Confinam filtros e paginação em `useState` local sem persistência na URL.
4. **Tratamento de erro robótico:** Geram alertas assustadores ("Network Error 500", "Failed to fetch") em vez de conforto e alternativas de recuperação.

---

## 2. Estrutura Proposta da Skill (`zen-tech-ui-ux`)

A skill será empacotada como um arquivo `SKILL.md` (com scripts e referências de suporte) contendo 4 grandes módulos operacionais:

```text
skills/zen-tech-ui-ux/
├── SKILL.md                          ← Prompt mestre de sistema e regras de geração
├── references/
│   ├── heuristics-checklist.md       ← Checklist de 10 heurísticas Zen Tech
│   ├── design-tokens-guide.md        ← Guia de adaptação HSL por produto
│   └── signature-components.md       ← Código de referência dos componentes-chave
└── templates/
    ├── action-drawer.tsx             ← Template de Drawer ergonômico mobile
    ├── permission-guard.tsx          ← Template de tela de pré-permissão
    ├── collapsible-smart-bar.tsx     ← Template de pílula retrátil
    └── zen-sync-hook.ts              ← Template de hook com optimistic UI e safety net
```

---

## 3. Módulos Funcionais da Skill

### Módulo A: Auditoria Heurística Zen Tech (`zen-tech-audit`)
O agente inspeciona uma tela ou componente existente e valida:
- [ ] O componente tem área de respiração adequada ou está comprimido?
- [ ] As quinas respeitam o raio orgânico (`rounded-2xl` a `rounded-3xl` / 16-32px)?
- [ ] No mobile, as ações secundárias estão em um `Bottom Drawer` (`vaul`) ou espremidas na linha?
- [ ] Estados de busca/filtro/página estão refletidos na URL (`validateSearch`)?
- [ ] Existe `PermissionGuard` antes de solicitar hardware (GPS/Câmera)?
- [ ] O feedback otimista e a persistência local (*Zen Sync*) estão implementados para ações críticas?

### Módulo B: Gerador de Componentes de Assinatura (`zen-tech-scaffold`)
Ao gerar novos componentes, o agente aplica por padrão:
- Variáveis HSL sem cores hexadecimais *hardcoded*.
- Micro-interações suaves com transições `ease-in-out` de 200-300ms.
- Toasts semânticos com `sonner` e durações adequadas (3.5s sucesso / 8s erro).
- Mobile-first real com ergonomia do polegar.

### Módulo C: UX Writing & Feedback Humanizado (`zen-tech-copy`)
Revisão de todos os textos de interface:
- Eliminar qualquer jargão técnico (evitar "payload", "timeout", "null", "404").
- Redigir mensagens empáticas que acolhem o momento de frustração e oferecem uma saída prática.

---

## 4. Integração com as Bibliotecas de Referência de UX Skills

Conforme levantado na pesquisa de mercado, integraremos as melhores práticas das bibliotecas existentes:

1. **AI UX Playground:**
   - Aproveitar os checklists de acessibilidade (WCAG AA) e padrões de especificação de PRDs/componentes.
   - Adaptar para o vocabulário e filosofia Zen Tech.
2. **Vibe Building Skills:**
   - Incorporar as técnicas de auditoria heurística rápida e visão estratégica de produto.
3. **UI Skills (EveryDev.ai):**
   - Utilizar as técnicas de polimento de animações e workflows com `shadcn/ui` e TailwindCSS.

---

## 5. Próximos Passos para Implementação da Skill

1. Redigir o arquivo `SKILL.md` oficial consolidando as instruções.
2. Testar a skill em um fluxo real do **Registoo** e do **Pictae** para validar o ganho de qualidade.
3. Disponibilizar a skill nas ferramentas de trabalho locais (Antigravity CLI / Hermes / Claude Code / Cursor).
