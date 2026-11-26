---
date: 2026-11-26
tipo: documentation
status: active
tags: [system, zoe, tts, gemini-38-flash-tts, voz, apple-safari, dialogos, typescript, registoo]
---

# Referência Técnica de Voz da Zoe — `gemini-3.8-flash-tts`

> Código e configurações validados pelo Gabriel em **2026-11-26** no Google AI Studio Speech Playground.
> Relacionadas: [[2026-11-25-blueprint-zoe-produtora-videos-motion]] · [[2026-11-25-guia-creditos-google-ai-pro-tts-openbot]].

---

## 1. Catálogo de Vozes da Frente B

| Apelido / Uso | Voice ID | Origem | Temperatura | Referência / Observação |
|---|---|---|---|---|
| **Monarca (Narrador Sóbrio / Apple Safari)** | `voice_n6ochgvc6bix` | *The Regal Monarch 3* | `0.9` | Pegada do anúncio Apple Safari *"Tire os rastreadores dos seus dados"* (`youtube.com/watch?v=9jKSy5GYcx4`) |
| **Voz Masculina Custom (Diálogo)** | `[PREENCHER ID via Custom voices]` | Voice Design | `0.7–0.9` | Para cenas de diálogo 2 pessoas (dual-speaker) |
| **Voz Feminina Custom (Diálogo)** | `[PREENCHER ID via Custom voices]` | Voice Design | `0.7–0.9` | Para cenas de diálogo 2 pessoas (dual-speaker) |

### Onde reencontrar vozes criadas no Google AI Studio
- Não ficam em *History*; ficam na **Voice Library persistente do projeto pago** (`Default Gemini Project`).
- Na UI: `aistudio.google.com/generate-speech` → painel direito **Run settings → Speaker settings** → topo da lista em **`Custom voices`**.
- Se não aparecerem: clique no ícone de chave do AI Studio e confirme que a **mesma API key paga** do projeto está ativa na sessão (marque *"Save Paid API Key"*), depois feche e reabra *Speaker settings*.
- Via SDK (`google-genai >= 2.25.0`, `v1beta`): `client.voices.list(type_=["prompted", "replicated"])`.

---

## 2. Snippet TypeScript de Referência (já corrigido!)

> **Duas correções importantes aplicadas sobre o snippet bruto do AI Studio:**
> 1. `speechMetadata.style` recebe a **direção de atuação** (o snippet exportado repetia o transcript por engano).
> 2. `convertToWav` calcula `buffer.length` (bytes decodificados) antes de chamar `createWavHeader` (o snippet original passava `rawData.length` em base64, o que podia corromper o tamanho no header WAV).

```ts
// Dependências: npm install @google/genai mime && npm install -D @types/node
import { GoogleGenAI } from '@google/genai';
import mime from 'mime';
import { writeFile } from 'fs';

function saveBinaryFile(fileName: string, content: Buffer) {
  writeFile(fileName, content, (err) => {
    if (err) {
      console.error(`Error writing file ${fileName}:`, err);
      return;
    }
    console.log(`File ${fileName} saved to file system.`);
  });
}

async function main() {
  const ai = new GoogleGenAI({
    apiKey: process.env['GEMINI_API_KEY'],
    httpOptions: { apiVersion: 'v1beta' },
  });

  const config = {
    temperature: 0.9,
    responseModalities: ['audio'],
    speechConfig: {
      voiceConfig: {
        voice: 'voice_n6ochgvc6bix', // The Regal Monarch 3
      },
    },
  };

  const model = 'gemini-3.8-flash-tts';
  const contents = [
    {
      role: 'user',
      parts: [
        {
          text: `## Transcript:
Sexta-feira, nove da noite. <short pause> Você ainda está cobrando evolução da semana inteira no WhatsApp. <short pause> O terapeuta atendeu na terça... mas na sexta, a memória já falhou. <short pause> O registro precisa acontecer na sessão. Não na memória. <short pause> O registro é do atendimento. Não de quem atende. <short pause> Registoo. Cada sessão, comprovada.`,
          speechMetadata: {
            style:
              'Narração cinematográfica em português do Brasil, estilo anúncio de privacidade da Apple (calma, precisa, confiante, levemente tensa no início e clara e segura no fechamento). Sem tom publicitário exagerado.',
          },
        },
      ],
    },
  ];

  const response = await ai.models.generateContentStream({ model, config, contents });
  let fileIndex = 0;
  for await (const chunk of response) {
    const inlineData = chunk.candidates?.[0]?.content?.parts?.[0]?.inlineData;
    if (!inlineData) continue;

    const fileName = `zoe_audio_${fileIndex++}`;
    let fileExtension = mime.getExtension(inlineData.mimeType || '');
    let buffer = Buffer.from(inlineData.data || '', 'base64');
    if (!fileExtension) {
      fileExtension = 'wav';
      buffer = convertToWav(inlineData.data || '', inlineData.mimeType || '');
    }
    saveBinaryFile(`${fileName}.${fileExtension}`, buffer);
  }
}

interface WavConversionOptions {
  numChannels: number;
  sampleRate: number;
  bitsPerSample: number;
}

function convertToWav(rawData: string, mimeType: string) {
  const options = parseMimeType(mimeType);
  const buffer = Buffer.from(rawData, 'base64');
  const wavHeader = createWavHeader(buffer.length, options);
  return Buffer.concat([wavHeader, buffer]);
}

function parseMimeType(mimeType: string): WavConversionOptions {
  const [fileType, ...params] = mimeType.split(';').map((s) => s.trim());
  const [, format] = fileType.split('/');
  const options: Partial<WavConversionOptions> = { numChannels: 1 };

  if (format && format.startsWith('L')) {
    const bits = parseInt(format.slice(1), 10);
    if (!isNaN(bits)) options.bitsPerSample = bits;
  }
  for (const param of params) {
    const [key, value] = param.split('=').map((s) => s.trim());
    if (key === 'rate') options.sampleRate = parseInt(value, 10);
  }
  return options as WavConversionOptions;
}

function createWavHeader(dataLength: number, options: WavConversionOptions) {
  const { numChannels, sampleRate, bitsPerSample } = options;
  const byteRate = (sampleRate * numChannels * bitsPerSample) / 8;
  const blockAlign = (numChannels * bitsPerSample) / 8;
  const buffer = Buffer.alloc(44);

  buffer.write('RIFF', 0);
  buffer.writeUInt32LE(36 + dataLength, 4);
  buffer.write('WAVE', 8);
  buffer.write('fmt ', 12);
  buffer.writeUInt32LE(16, 16);
  buffer.writeUInt16LE(1, 20);
  buffer.writeUInt16LE(numChannels, 22);
  buffer.writeUInt32LE(sampleRate, 24);
  buffer.writeUInt32LE(byteRate, 28);
  buffer.writeUInt16LE(blockAlign, 32);
  buffer.writeUInt16LE(bitsPerSample, 34);
  buffer.write('data', 36);
  buffer.writeUInt32LE(dataLength, 40);
  return buffer;
}

main();
```
