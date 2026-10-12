---
date: 2026-10-08
projeto: zenckup
type: issue
status: open
priority: high
tags: [cifragem, seguranca, cliente, upload, health-data, registoo]
---

# Implementar cifragem no cliente antes do upload com chaves assimétricas

## Contexto

O Zenckup é um serviço de backup agendado de Postgres para o R2. Devido à natureza sensível dos dados que o **Registoo** manipula (registos de saúde), é necessária uma camada adicional de proteção: cifragem **no cliente antes do upload**, usando um esquema de chaves assimétricas.

## Proposta de Arquitetura

### Chaves
- **Chave pública**: Armazenada no serviço Zenckup (Railway)
- **Chave privada**: Mantida **fora do Railway** — comigo (Gabriel), em local seguro

### Fluxo
1. Antes de fazer upload para o R2, o cliente **cifra** o dump do Postgres usando a **chave pública**
2. O dump cifrado é enviado para o R2
3. A **chave privada** permanece em meu posse (fora do Railway)
4. Para restaurar, é necessário a **chave privada** (que eu mantém separadamente)

## Motivação

- Dados de saúde exigem alto padrão de segurança
- Mesmo que o R2 ou Railway sejam comprometidos, os dados permanecem ininteligíveis sem a **chave privada**
- O agente do Registoo destacou essa necessidade devido à natureza dos dados

## Status

- [ ] Implementar geração de chaves assimétricas (RSA ou similar)
- [ ] Integrar cifragem no fluxo de backup do cliente
- [ ] Configurar gerenciamento seguro da **chave privada** (fora do Railway)
- [ ] Documentar processo de restauração
- [ ] Testar round-trip (backup + restauração)

## Próximos passos

- [ ] Avaliar bibliotecas de cifragem adequadas (ex: cryptography, libsodium)
- [ ] Definir formato do arquivo cifrado (header com metadados)
- [ ] Implementar rotina de backup cifrado
- [ ] Configurar armazenamento seguro da **chave privada** (ex: vault, hardware token, etc.)
- [ ] Criar script de restauração

---
*Pendência criada em 2026-10-08 por Gabriel — originada do agente do Registoo devido à natureza dos dados de saúde*