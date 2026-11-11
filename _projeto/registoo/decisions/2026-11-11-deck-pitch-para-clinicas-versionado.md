---
date: 2026-11-11
projeto: registoo
type: decision
status: done
tags: [vendas, pitch, deck, marketing]
---

# Deck "Pitch para Clínicas": onde fica e como reutilizar

O deck de vendas para clínicas (14 slides, criado em 2026-10-16, identidade Emerald Premium) ficou bom e
deve ser reaproveitado nas calls, junto com o vídeo-manifesto.

## Onde está

- **Versão pronta para apresentar (Artifact de Slides no claude.ai, exporta .pptx/PDF):**
  https://claude.ai/artifact/RTjo1r7BL6EJkcNgi4EkNp
- **Fonte versionada no repositório** (`registoo-check`):
  `docs/marketing/pitch-clinicas/` — `deck.json`, os 14 slides em HTML, os prints (dados fictícios da
  "Clínica Florescer"), a logo e os scripts de captura. O `README.md` da pasta explica o roteiro, como
  republicar e como recapturar os prints. Entrou pela PR #298.

## Decisão

A fonte fica **no repositório, não no Brain**: os prints envelhecem a cada release e são refeitos com o
pipeline de captura do `apps/video`, que vive no mesmo repositório. O Brain guarda só este ponteiro.

## Roteiro do deck

Abertura ("Cada sessão, comprovada.") → o problema (sessão sem prova, risco trabalhista das ferramentas de
ponto) → a solução (quem é registrado é a sessão do paciente, nunca o profissional; três gestos) → o dia a
dia (profissional, gestor, QR do paciente) → confiança (quatro evidências, uso real, simplicidade, LGPD) →
oferta (Turma Fundadora e próximos passos).

## Antes de usar de novo

Conferir se os prints ainda batem com o app atual (houve mudanças desde out/2026, como o painel da gestão
abrindo num profissional e o selo "Local registrado"). Se não baterem, recapturar e republicar.
