"""
Comprime o PDF de uma edição reamostrando as imagens embutidas (limita a maior
dimensão e recomprime como JPEG). O texto não é tocado — continua selecionável
e pesquisável; só imagens (gráficos, capa, fundo) perdem peso.

Uso: python scripts/comprimir_pdf.py <entrada.pdf> <saida.pdf> [max_dimensao] [qualidade_jpeg]
Ex.: python scripts/comprimir_pdf.py "../Relatórios/Relatorio 09.pdf" public/relatorios/edicao-09.pdf
"""
import io
import sys

import pymupdf
from PIL import Image


def comprimir(caminho_entrada, caminho_saida, max_dim=1600, qualidade=72):
    doc = pymupdf.open(caminho_entrada)

    # largura com que cada imagem aparece na página — evita reamostrar abaixo do necessário
    largura_exibicao = {}
    for pagina in doc:
        for img in pagina.get_images(full=True):
            xref = img[0]
            for retangulo in pagina.get_image_rects(xref):
                largura_exibicao[xref] = max(largura_exibicao.get(xref, 0), retangulo.width)

    vistos = set()
    trocados, ignorados = 0, 0

    for pagina in doc:
        for img in pagina.get_images(full=True):
            xref = img[0]
            if xref in vistos:
                continue
            vistos.add(xref)

            try:
                dados = doc.extract_image(xref)["image"]
                im = Image.open(io.BytesIO(dados))
                im.load()
            except Exception:
                ignorados += 1
                continue

            if im.mode == "CMYK":
                im = im.convert("RGB")
            elif im.mode == "P":
                im = im.convert("RGBA" if "transparency" in im.info else "RGB")

            alvo = min(max_dim, max(800, int(largura_exibicao.get(xref, 0) * 2)))
            maior_lado = max(im.width, im.height)
            if maior_lado > alvo:
                fator = alvo / maior_lado
                im = im.resize((max(1, int(im.width * fator)), max(1, int(im.height * fator))), Image.LANCZOS)

            saida = io.BytesIO()
            if im.mode in ("RGBA", "LA"):
                im.save(saida, format="PNG", optimize=True)
            else:
                if im.mode != "RGB":
                    im = im.convert("RGB")
                im.save(saida, format="JPEG", quality=qualidade, optimize=True)

            novos = saida.getvalue()
            if len(novos) < len(dados):
                pagina.replace_image(xref, stream=novos)
                trocados += 1
            else:
                ignorados += 1

    doc.save(caminho_saida, garbage=4, deflate=True, deflate_images=True, deflate_fonts=True)
    doc.close()
    return trocados, ignorados


if __name__ == "__main__":
    entrada, saida = sys.argv[1], sys.argv[2]
    max_dim = int(sys.argv[3]) if len(sys.argv) > 3 else 1600
    qualidade = int(sys.argv[4]) if len(sys.argv) > 4 else 72
    trocados, ignorados = comprimir(entrada, saida, max_dim, qualidade)
    print(f"imagens recomprimidas: {trocados} | ignoradas (já pequenas/erro): {ignorados}")
