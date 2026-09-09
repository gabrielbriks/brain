---
title: Workflow Diário e Captura de Notas
date: 2026-09-08
type: tutorial
tags: [workflow, captura, gtd, review]
---

# Workflow Diário: Como interagir com o Brain OS

A estrutura de pastas do Brain (Modelo PARA) pode parecer complexa à primeira vista, mas **você não precisa (e nem deve) memorizá-la na correria do dia a dia.**

O sistema foi desenhado para que a inteligência artificial assuma o peso da organização, deixando você livre para focar apenas na **captura**.

Aqui está como o fluxo funciona na prática:

## 1. Captura com Atrito Zero (O seu único trabalho)

No dia a dia, sua única responsabilidade é "descarregar" a mente. Use o Telegram (áudio ou texto) ou o terminal para falar com o Hermes de forma natural.

**Exemplos do que você pode mandar:**
- *"Achei um bug na tela de login do Registoo, o botão não clica no iOS."*
- *"Tive uma ideia de funcionalidade pro Pictae: seleção de fotos por IA."*
- *"Preciso pagar a DAS do MEI amanhã sem falta."*
- *"Lembrar de comprar café e azeite."*

## 2. O Hermes é o seu Triador 🤖

Ao receber sua mensagem, o Hermes cruza o seu texto com as regras da skill `brain-workspace`. Ele faz o trabalho duro de roteamento:
- Ele entende que `Registoo` é um **Projeto** e `Bug` é uma **Issue**, salvando em `_projeto/registoo/issues/`.
- Ele entende que `DAS do MEI` é uma **Task** da área **Financeiro**, salvando em `_area/financeiro/tasks/`.

## 3. A Regra do Inbox (A Rede de Segurança) 📥

E se você mandar algo super vago, correndo na rua, sem especificar projeto nenhum?
Ex: *"Tive uma ideia genial de usar IA pra resumir textos, me lembre de pesquisar isso."*

O Hermes está instruído a não tentar adivinhar quando o contexto for ambíguo. A regra de ouro dele é: **Na dúvida, jogue na Caixa de Entrada (`_inbox/`).**

Ele vai salvar lá e te avisar: *"Gabriel, salvei essa ideia no seu Inbox"*. Sua ideia está segura e você não perdeu o fio da meada.

## 4. O Alinhamento Semanal (Weekly Review) 🗓️

É aqui que o ciclo se fecha. Uma vez por semana (ex: sexta-feira à tarde ou domingo de manhã), você tira 15 minutos para fazer a manutenção do seu Brain:

1. **Esvaziar o Inbox:** Olhe tudo que o Hermes jogou na pasta `_inbox/` durante a semana. Agora que você tem tempo, mova esses arquivos manualmente para o projeto ou área correta (ou apague se a ideia não fizer mais sentido).
2. **Revisar Tarefas (Tasks/Issues):** Olhe rapidamente o que está pendente para planejar a sua próxima semana.
3. **Atualizar Status:** Mudar projetos concluídos para `status: archived`.

---

> **Resumo da Ópera:** Fale com o sistema de forma natural. Deixe a IA classificar o óbvio, deixe o Inbox segurar o que for ambíguo, e limpe a bagunça 1x por semana.
