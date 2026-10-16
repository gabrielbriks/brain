---
date: 2026-10-16
projeto: registoo
type: decision
status: done
tags: [vendas, pitch, deck, turma-fundadora, clinicas, marketing, video, decisao]
---

# Deck de vendas para clínicas e Turma Fundadora

## Contexto

Primeiro material de venda do Registoo para clínicas e potenciais clientes, apresentado em call pela
sócia do Gabriel. Feito em 2026-10-16 com o Claude Code, a partir dos `docs/flows`, do código e da
landing do repositório `registoo-check`.

- **Deck:** Artifact privado "Registoo — Pitch para Clínicas" —
  https://claude.ai/artifact/RTjo1r7BL6EJkcNgi4EkNp (14 slides, Emerald Premium Zen Tech, exporta
  `.pptx`/PDF; compartilhado com a sócia pelo menu Share).
- **Status:** pronto, aguardando o feedback da sócia.

## Decisões

**Tese do pitch:** "Cada sessão, comprovada." — prova de cada sessão sem transformar a equipe em
funcionário batendo ponto. Três dores na ordem: glosa/contestação da família → risco trabalhista
escondido em app de ponto/planilha → gestão às cegas.

**Roteiro (14 slides):** capa → o terapeuta saiu, e depois? → o risco que ninguém vê → a virada
(o sujeito do registro é a sessão do paciente) → três gestos → dia do profissional → dia do gestor →
paciente com QR Code → quatro evidências → em uso real → simples por decisão de projeto → LGPD →
Turma Fundadora → próximos passos.

**Turma Fundadora (oferta):**
- 10 vagas (restam 9; a clínica atual já é fundadora).
- Condição **sob medida** pelo tamanho da clínica — proposta enviada em até 3 dias após a call,
  com preço travado enquanto a assinatura estiver ativa.
- Recebe: canal direto com quem desenvolve, voto de fundador nas prioridades, novidades antes de
  todos (versão nova toda semana), onboarding assistido.
- Em troca: uma conversa de feedback por mês, depoimento após 3 meses, autorização para virar case.
- É influência no roadmap, não desenvolvimento sob encomenda.
- Não mostrar a condição de outras fundadoras nem usar o Founder da sócia (R$ 14,90) como âncora.

**Preço no pitch:** sem grade de planos na apresentação; se perguntarem, "a partir de R$ 89/mês" e
teste de 30 dias. CTA só com e-mail (`oi@registoo.com`), sem WhatsApp (a apresentação é em call).

**Números só verdadeiros (regra):** dados de produção de 16/10: 42 sessões, 6 profissionais,
9 pacientes, 95,2% dentro do perímetro, em operação desde agosto/2026. Arredondar **para baixo**
para o slide durar ("+50" vale a partir de 19/10). Nunca inflar — o argumento central do produto é
"prova que se sustenta".

**Prints:** sempre com dados fictícios (org "Clínica Florescer", banco local, seed
`apps/api/scripts/seed-demo-pitch.ts`). Prints mobile usam o **mockup de iPhone com moldura e
Dynamic Island** — padrão aprovado para todos os materiais.

**Marca:** logo transparente (pin com check); "oo" em verde só onde o nome aparece como marca
(capa), nunca em rodapé ou link.

## Desdobramentos

- Issues no repositório (PR #195): **062** vídeo-manifesto + tutoriais, **063** "check-in" e mês
  em inglês na UI, **064** perfil quebra sem CPF (corrigida no PR #196), **065** formulário de
  evolução sem nome do paciente.
- **Próximo:** vídeo-manifesto de 60–90 s no estilo Apple/WhatsApp, para usar junto com o deck na
  call e publicar no YouTube (issue 062, precisa de Plan T2). Pipeline candidato: seed de
  demonstração + gravação automatizada do app + Remotion.
