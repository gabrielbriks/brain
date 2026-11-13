---
date: 2026-11-13
area: dev
type: ref
status: open
tags: [video, ux, ritmo, legenda, aprendizagem-multimidia, mayer, zen-tech]
---

# Tempo de leitura e ritmo em vídeos de produto e tutoriais

Cópia de consulta para outros projetos. A versão viva, aplicada ao pipeline de vídeo, fica no Registoo:
`registoo-check/docs/learnings/video-tempo-de-leitura-e-ritmo.md`.

**Origem:** template dos tutoriais do Registoo (2026-11-13). No primeiro render, o título ficou inteiro
na tela por ~0,8 s e cada passo acendia junto com a ação, sem respiro.

## 1. Quanto tempo um texto precisa ficar na tela

- **Netflix (legendas):** mínimo de 5/6 s (~0,83 s), máximo de 7 s por legenda. Limite de leitura
  medido em caracteres por segundo: **17 CPS para adultos, 13 CPS para conteúdo infantil** na maior
  parte dos idiomas. Para o inglês, fontes de terceiros citam 20 CPS (não conferido).
- **BBC:** ~160–180 palavras/min, ~0,3 s por palavra como mínimo (citado por terceiros).
- **Produtores de vídeo:** deixar o texto o bastante para ser lido **duas vezes** (leitor lento, 200
  palavras/min), ou ~**2 s a mais** que a leitura normal. Piso de ~0,8 s até para uma palavra; 1–2 s para
  qualquer bloco.
- **Não há número único validado** por estudo de rastreamento ocular. É heurística: confirmar assistindo.

## 2. Como se aprende com vídeo (Richard E. Mayer, aprendizagem multimídia)

- **Segmentação:** blocos menores com pausa entre eles ajudam a aprender (menos carga na memória de
  trabalho, estrutura mais clara).
- **Pausa do vídeo > pausa da pessoa:** quase ninguém aperta o pause. Em aprendizagem de **procedimento**,
  pausas definidas pelo vídeo funcionaram melhor que pausas pela pessoa.
- **Modalidade:** com imagem em movimento, **ouvir** a explicação ensina mais que **ler** (olhos livres
  para a tela).
- **Sinalização:** destacar onde olhar liga o texto à ação.
- **Redundância:** narração + o mesmo texto inteiro na tela atrapalha. Na tela, só rótulos curtos.

## 3. Regra prática (a que o Registoo adotou)

- **Sem narração:** 13 CPS + 0,5 s para o olho achar o texto, contados depois que a animação de entrada
  termina. Piso de 1,5 s. Ex.: 31 caracteres → ~2,4 s + 0,5 s com o texto completo.
- **Passo de tutorial em três tempos:** (1) o passo aparece com a tela parada e o ponto de toque
  destacado; (2) a ação; (3) o resultado parado ≥ 1,2 s. Nunca texto e ação ao mesmo tempo.
- **Com narração:** cada passo dura a fala + ~0,8 s de respiro; a regra de leitura vira só o piso para
  quem assiste sem som.
- **Teste:** quem nunca viu o fluxo consegue dizer o título ou o passo em voz alta antes de ele sair?

## Fontes

- https://backlothelp.netflix.com/hc/en-us/articles/215758617
- https://www.ssw.com.au/rules/post-production-do-you-give-enough-time-to-read-texts-in-your-videos
- https://typito.com/blog/4-common-mistakes-avoid-adding-text-videos/
- https://u.osu.edu/multimedialearning/multimedia-learning-principles/6-the-segmenting-principle
- https://hal.archives-ouvertes.fr/hal-01783949
- Richard E. Mayer, *Multimedia Learning*
