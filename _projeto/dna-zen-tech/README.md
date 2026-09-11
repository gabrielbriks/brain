---
title: Projeto — DNA Zen Tech
type: readme
status: active
tags: [design-system, ui, ux, zen-tech, transversal, frontend, filosofia]
---

# 🌿 DNA Zen Tech — Sistema Global de UI & UX

> *"Simples como deve ser. Sofisticado como merece ser. Leve como precisa ser."*  
> **Tecnologia invisível, experiência humana.**

O **DNA Zen Tech** é o sistema transversal de design, engenharia de interface e experiência de usuário compartilhado por todo o ecossistema de produtos de Gabriel (Registoo, Pictae, Historuja, Vox, Widback e futuros SaaS).

Diferente de um "tema" ou "identidade de marca" convencional — onde cada produto tem sua própria paleta, público e atmosfera —, o **Zen Tech é o DNA unificador**: uma filosofia profunda de desenvolvimento que dita como a interface acolhe o usuário, como os dados fluem sem atrito e como a tecnologia opera de forma serena e invisível nos bastidores.

---

## 🎯 Objetivo do Projeto

1. **Codificar o DNA Universal:** Consolidar os pilares, heurísticas e padrões refinados no *Registoo Check* (onde nasceu a estética e acolhimento) e no *Pictae* (onde atingiu sofisticação editorial e padrões de engenharia como Zen Sync).
2. **Independência de Marca:** Permitir que cada produto mantenha sua identidade única (o verde-esmeralda do Registoo, os tons quentes/editoriais do Pictae, os tons acolhedores do Historuja) enquanto herdam 100% da ergonomia, ritmo e tranquilidade cognitiva.
3. **Criação de uma Skill de IA Rica:** Estruturar este repositório para que possa ser empacotado como uma **Skill de Agente (SKILL.md / Claude Code / Antigravity / Cursor)**, habilitando agentes de IA a conceberem, auditarem e codificarem interfaces já nativamente no padrão Zen Tech.

---

## 🏛️ Os 4 Pilares do DNA

| Pilar | Essência | Diretriz Prática |
|---|---|---|
| **1. Acolhimento & Conforto Cognitivo** | A interface deve abraçar o usuário, nunca intimidar ou cansar. | Espaçamentos generosos ("espaço é intenção"), cantos arredondados orgânicos (16px a 32px), ausência de contrastes gélidos/agressivos, Pre-permission UI (`PermissionGuard`). |
| **2. Clareza & Hierarquia Focada** | Zero dispersão. O usuário sabe exatamente onde está e o que fazer. | Apenas um CTA primário evidente por contexto; ações secundárias recolhidas em Bottom Drawers ergonômicos no mobile; estado 100% refletido na URL. |
| **3. Fricção Zero & Empatia** | Tecnologia sem burocracia desnecessária. | Autenticação mágica/silenciosa (sem memorização forçada de senhas); totalizadores em tempo real; feedback empático e humanizado (sem códigos de erro ou jargão técnico). |
| **4. Engenharia Invisível & Resiliência** | Velocidade instantânea com segurança blindada. | *Zen Sync* (Feedback otimista imediato + Safety Net em localStorage + Sync em lote com debounce + proteção contra saída acidental); degradação elegante de recursos (*Capabilities Engine*). |

---

## 📁 Estrutura do Projeto no Vault

```text
_projeto/dna-zen-tech/
├── README.md                 ← Visão geral e guia mestre do projeto
├── insights/                 ← Fundamentos, manifestos e análises aprofundadas
│   └── 2026-09-11-manifesto-e-pilares-do-dna-zen-tech.md
├── ideas/                    ← Evoluções, planos de skills de IA e referências
│   ├── 2026-09-11-especificacao-da-skill-zen-tech-para-agentes.md
│   └── 2026-09-11-bibliotecas-ux-skills-de-referencia.md
├── decisions/                ← ADRs transversais de UI/UX
└── backlog/                  ← Tarefas de consolidação da Skill e Design Tokens
```

---

## 🔗 Relação com os Projetos

- **Registoo / Registoo Check:** Berço do conceito (Emerald Premium, acolhimento para profissionais de saúde sob alta pressão, Pre-permission UI, ergonomia de ponto móvel).
- **Pictae:** Refinamento editorial (Warm Minimalism, Zen Sync com safety net em localStorage, Collapsible Smart Bar, Lightbox cinematográfico com backdrop-blur, Capabilities Engine).
- **Futuras Aplicações (Historuja, Widback, Vox):** Herdarão diretamente os componentes, tokens e heurísticas consolidados nesta base.
