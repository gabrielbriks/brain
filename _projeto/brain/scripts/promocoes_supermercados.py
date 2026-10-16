#!/usr/bin/env python3
"""
Script de Promoções de Supermercados — Brain de Gabriel Briks

Extrai itens de listas de compras no _area/pessoal/listas/, busca preços
atuais de supermercados e gera um relatório de comparação.

Uso:
    python promocoes_supermercados.py --regiao DF
    python promocoes_supermercados.py --arquivo 2026-10-09-mercado-acai.md --regiao DF
"""

import argparse
import hashlib
import json
import os
import re
import sys
from datetime import date, datetime
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen, HTTPError

# Fallback: if requests is not available, use urllib
# try to import requests, if fails, use urllib
try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False


# ---------------------------------------------------------------------------
# Caminhos do Brain
# ---------------------------------------------------------------------------

BRAIN_ROOT = Path(__file__).resolve().parents[3]
LISTAS_DIR = BRAIN_ROOT / "_area" / "pessoal" / "listas"
LOGS_DIR = BRAIN_ROOT / "_area" / "pessoal" / "logs"
MANTIMENTOS_FILE = BRAIN_ROOT / "_area" / "pessoal" / "listas" / "mantimentos.md"
RELATORIOS_DIR = BRAIN_ROOT / "_area" / "pessoal" / "listas"

assert BRAIN_ROOT.exists(), f"Brain root não encontrado: {BRAIN_ROOT}"


# ---------------------------------------------------------------------------
# Extração de itens de listas de compras
# ---------------------------------------------------------------------------

ITEM_REGEX = re.compile(
    r"\|\s*(?P<item>.+?)\s*\|\s*(?P<qtd>.+?)\s*\|\s*R\$\s*(?P<valor>.+?)\s*\|"
)


def extrair_itens_de_arquivo(caminho: Path) -> list[dict]:
    """Lê um arquivo markdown de lista de compras e extrai itens com preços."""
    itens = []
    texto = caminho.read_text(encoding="utf-8")

    for linha in texto.splitlines():
        linha = linha.strip()
        if not linha.startswith("|") or linha.startswith("|---"):
            continue
        m = ITEM_REGEX.match(linha)
        if not m:
            continue
        item = m.group("item").strip()
        qtd = m.group("qtd").strip()
        valor_str = m.group("valor").strip().replace(",", ".")
        try:
            valor = float(valor_str)
        except ValueError:
            continue
        itens.append(
            {
                "item": item,
                "quantidade": qtd,
                "preco_referencia": valor,
                "arquivo_origem": caminho.name,
            }
        )

    return itens


def listar_arquivos_de_listas() -> list[Path]:
    """Retorna todos os arquivos de lista de compras ordenados por data."""
    arquivos = []
    for p in LISTAS_DIR.glob("*.md"):
        if p.name == "mantimentos.md" or p.name == "compras-mercado.md":
            continue  # arquivo modelo / estoque, não lista de compra específica
        arquivos.append(p)
    return sorted(arquivos, key=lambda p: p.name)


# ---------------------------------------------------------------------------
# Busca de preços em APIs de supermercados
# ---------------------------------------------------------------------------

class BuscadorPrecos:
    """Busca preços de produtos em APIs públicas."""

    def __init__(self, regiao: str = "DF"):
        self.regiao = regiao
        self.session = None
        if HAS_REQUESTS:
            self.session = requests.Session()
            self.session.headers.update(
                {"User-Agent": "Mozilla/5.0 (compatible; Brain-PromoBot/1.0)"}
            )

    def _http_get(self, url: str, params: dict = None) -> dict | None:
        """Faz uma requisição GET e retorna JSON, usando requests ou urllib."""
        if HAS_REQUESTS:
            resp = self.session.get(url, params=params, timeout=15)
            if resp.status_code != 200:
                return None
            return resp.json()
        else:
            from urllib.parse import urlencode as _ue
            full_url = url
            if params:
                full_url = f"{url}?{_ue(params)}"
            req = Request(full_url, headers={"User-Agent": "Mozilla/5.0 (compatible; Brain-PromoBot/1.0)"})
            try:
                with urlopen(req, timeout=15) as resp:
                    if resp.status != 200:
                        return None
                    return json.loads(resp.read().decode("utf-8"))
            except (HTTPError, Exception):
                return None

    def buscar_todos(self, itens: list[dict]) -> list[dict]:
        """Para cada item, busca o melhor preço encontrado."""
        resultados = []
        for item in itens:
            melhores = self._buscar_item(item["item"])
            resultado = {**item, "melhor_preco": melhores[0] if melhores else None,
                         "todas_fontes": melhores}
            resultados.append(resultado)
        return resultados

    def _buscar_item(self, nome_item: str) -> list[dict]:
        """Busca um item em múltiplas fontes e retorna lista de resultados."""
        resultados = []

        # Fontes em ordem de preferência
        fontes = [
            self._mercado_livre,
            self._shopee,
        ]

        for fonte in fontes:
            try:
                res = fonte(nome_item)
                if res:
                    resultados.extend(res)
            except Exception as e:  # noqa: BLE001
                print(f"  [warn] falha na fonte {fonte.__name__}: {e}", file=sys.stderr)

        # Ordena por preço crescente
        resultados.sort(key=lambda r: r["preco"])
        return resultados[:5]  # top 5

    def _mercado_livre(self, nome: str) -> list[dict]:
        """Busca no Mercado Livre (API pública de busca)."""
        url = "https://api.mercadolibre.com/sites/MLB/search"
        params = {"q": nome, "limit": 5}
        dados = self._http_get(url, params=params)
        if not dados:
            return []
        resultados = []
        for p in dados.get("results", []):
            preco = p.get("price")
            if preco is None:
                continue
            resultados.append(
                {
                    "fonte": "Mercado Livre",
                    "produto": p.get("title", "")[:80],
                    "preco": preco,
                    "url": p.get("permalink", ""),
                }
            )
        return resultados

    def _shopee(self, nome: str) -> list[dict]:
        """Busca na Shopee (API pública não oficial — pode falhar)."""
        # Shopee não tem API pública simples; placeholder para futura integração
        return []


# ---------------------------------------------------------------------------
# Geração de relatório
# ---------------------------------------------------------------------------

def gerar_relatorio(resultados: list[dict], regiao: str) -> str:
    """Gera conteúdo markdown do relatório de promoções."""
    hoje = date.today().isoformat()
    linhas = [
        f"---\n"
        f"date: {hoje}\n"
        f"area: pessoal\n"
        f"type: lista\n"
        f"status: open\n"
        f"tags: [promocoes, supermercado, comparacao, {regiao.lower()}]\n"
        f"---\n"
    ]
    linhas.append(f"# Relatório de Promoções — Supermercados ({regiao})")
    linhas.append(f"\n**Data da consulta:** {hoje}")
    linhas.append(f"\n---\n")

    if not resultados:
        linhas.append("\nNenhum item encontrado nas listas de compras.\n")
        return "\n".join(linhas)

    linhas.append("## Itens e Comparação de Preços\n")
    linhas.append(
        "| Item | Preço Ref. | Melhor Preço | Fonte | Diferença |"
    )
    linhas.append("|------|------------|--------------|-------|-----------|")

    total_ref = 0.0
    total_melhor = 0.0

    for r in resultados:
        preco_ref = r["preco_referencia"]
        melhor = r["melhor_preco"]
        if melhor:
            dif = melhor["preco"] - preco_ref
            total_ref += preco_ref
            total_melhor += melhor["preco"]
            sinal = "+" if dif > 0 else ""
            linhas.append(
                f"| {r['item']} | R$ {preco_ref:.2f} | "
                f"R$ {melhor['preco']:.2f} | {melhor['fonte']} | "
                f"{sinal}R$ {dif:.2f} |"
            )
        else:
            total_ref += preco_ref
            linhas.append(
                f"| {r['item']} | R$ {preco_ref:.2f} | — | — | — |"
            )

    linhas.append("\n## Resumo Financeiro\n")
    linhas.append(f"- **Total de referência:** R$ {total_ref:.2f}")
    if total_melhor > 0:
        linhas.append(f"- **Total com melhores preços:** R$ {total_melhor:.2f}")
        economia = total_ref - total_melhor
        linhas.append(f"- **Economia potencial:** R$ {economia:.2f}")

    linhas.append("\n## Detalhes das Fontes\n")
    for r in resultados:
        if not r["todas_fontes"]:
            continue
        linhas.append(f"\n### {r['item']}")
        for f in r["todas_fontes"]:
            linhas.append(
                f"- [{f['fonte']}]({f['url']}) — {f['produto']} — R$ {f['preco']:.2f}"
            )

    linhas.append("\n---\n")
    linhas.append(
        "_Gerado automaticamente pelo script de promoções do Brain._\n"
    )
    return "\n".join(linhas)


def salvar_relatorio(conteudo: str, regiao: str) -> Path:
    """Salva o relatório na pasta de listas e retorna o caminho."""
    hoje = date.today().isoformat()
    slug = f"{hoje}-promocoes-supermercados-{regiao.lower()}"
    caminho = RELATORIOS_DIR / f"{slug}.md"
    caminho.write_text(conteudo, encoding="utf-8")
    return caminho


# ---------------------------------------------------------------------------
# Git
# ---------------------------------------------------------------------------

def commit_e_push(arquivos: list[Path]) -> None:
    """Faz commit e push dos arquivos modificados."""
    import subprocess

    for arq in arquivos:
        subprocess.run(["git", "add", str(arq)], cwd=BRAIN_ROOT, check=True)

    mensagem = f"docs: relatório de promoções de supermercados ({date.today().isoformat()})"
    subprocess.run(["git", "commit", "-m", mensagem], cwd=BRAIN_ROOT, check=True)
    subprocess.run(["git", "push"], cwd=BRAIN_ROOT, check=True)
    print(f"✓ Commit e push realizados: {mensagem}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(description="Relatório de promoções de supermercados")
    parser.add_argument(
        "--regiao", default="DF", help="Região para busca de preços (ex: DF, SP, RJ)"
    )
    parser.add_argument(
        "--arquivo", help="Processar apenas um arquivo de lista específico"
    )
    parser.add_argument(
        "--no-git", action="store_true", help="Não fazer commit/push automático"
    )
    args = parser.parse_args()

    print(f"🛒 Iniciando busca de promoções — Região: {args.regiao}")

    # 1. Extrai itens
    if args.arquivo:
        caminho = LISTAS_DIR / args.arquivo
        if not caminho.exists():
            print(f"✗ Arquivo não encontrado: {caminho}")
            sys.exit(1)
        itens = extrair_itens_de_arquivo(caminho)
        print(f"  → {len(itens)} itens extraídos de {args.arquivo}")
    else:
        arquivos = listar_arquivos_de_listas()
        itens = []
        for arq in arquivos:
            itens_arq = extrair_itens_de_arquivo(arq)
            itens.extend(itens_arq)
            print(f"  → {len(itens_arq)} itens de {arq.name}")
        print(f"  → Total: {len(itens)} itens")

    if not itens:
        print("⚠ Nenhum item encontrado. Abortando.")
        sys.exit(0)

    # 2. Busca preços
    buscador = BuscadorPrecos(regiao=args.regiao)
    resultados = buscador.buscar_todos(itens)

    # 3. Gera relatório
    conteudo = gerar_relatorio(resultados, regiao=args.regiao)

    # 4. Salva
    caminho_relatorio = salvar_relatorio(conteudo, regiao=args.regiao)
    print(f"✓ Relatório salvo: {caminho_relatorio}")

    # 5. Git
    if not args.no_git:
        commit_e_push([caminho_relatorio])

    print("✓ Concluído.")


if __name__ == "__main__":
    main()