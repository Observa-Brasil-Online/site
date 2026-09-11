# -*- coding: utf-8 -*-
"""
Gera as imagens de compartilhamento (Open Graph, 1200x630) do site.

Roda uma vez por edição nova — mesma filosofia do resto do projeto
("publicar = copiar 2 arquivos"): aqui, gerar a OG image é um passo a mais,
mas continua sendo "rodar um comando", não desenho manual.

Uso:
    python scripts/gerar_og.py                  # regenera a padrão + todas as edições
    python scripts/gerar_og.py edicao-03         # regenera só uma edição específica

Requer: Pillow (já é dependência do projeto — usado também na compressão dos PDFs).
As fontes TTF em scripts/fonts-og/ foram extraídas do Google Fonts (o site usa woff2,
mas Pillow precisa de TTF/OTF) — ver o próprio script para a extração, se precisar
gerar outro peso no futuro.
"""
import os
import re
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

RAIZ = Path(__file__).resolve().parent.parent
FONTES = Path(__file__).resolve().parent / "fonts-og"
SAIDA = RAIZ / "public" / "og"
CONTEUDO = RAIZ / "src" / "content" / "relatorios"

W, H = 1200, 630
PAD = 72

# paleta da marca
NAVY = "#12345C"
AMBER = "#D9A227"
CREAM = "#FBF7EF"
SKY = "#7FB2E8"
OBSERVA_BLUE = "#0B4F9E"

f_archivo_extrabold = lambda size: ImageFont.truetype(str(FONTES / "Archivo-800.ttf"), size)
f_archivo_regular = lambda size: ImageFont.truetype(str(FONTES / "Archivo-400.ttf"), size)
f_mono = lambda size: ImageFont.truetype(str(FONTES / "IBMPlexMono-500.ttf"), size)


def desenhar_simbolo(img, cx, cy, escala):
    """Losango + lente + pupila — mesma geometria de Symbol.astro, variante 'negative'."""
    d = ImageDraw.Draw(img)
    # viewBox original 156x116, centro do losango em (78,58)
    pts = [(78, 23), (133, 58), (78, 93), (23, 58)]
    pts = [((x - 78) * escala + cx, (y - 58) * escala + cy) for x, y in pts]
    d.polygon(pts, outline=CREAM, width=max(2, round(8 * escala)))
    r_lente = 23 * escala
    d.ellipse([cx - r_lente, cy - r_lente, cx + r_lente, cy + r_lente], fill=OBSERVA_BLUE, outline=CREAM, width=max(1, round(escala)))
    r_pupila = 8 * escala
    d.ellipse([cx - r_pupila, cy - r_pupila, cx + r_pupila, cy + r_pupila], fill=CREAM)


def quebrar_linhas(texto, fonte, largura_max, draw):
    palavras = texto.split()
    linhas, atual = [], ""
    for p in palavras:
        teste = (atual + " " + p).strip()
        if draw.textlength(teste, font=fonte) <= largura_max:
            atual = teste
        else:
            if atual:
                linhas.append(atual)
            atual = p
    if atual:
        linhas.append(atual)
    return linhas


def gerar_imagem(caminho_saida, *, kicker, titulo, stat_valor=None, stat_label=None):
    img = Image.new("RGB", (W, H), NAVY)
    draw = ImageDraw.Draw(img)

    # símbolo, canto superior esquerdo
    desenhar_simbolo(img, PAD + 22, PAD + 12, escala=0.9)

    x_texto = PAD + 70
    draw.text((x_texto, PAD), "OBSERVA", font=f_archivo_extrabold(26), fill=CREAM)
    draw.text((x_texto, PAD + 32), "UMA SÉRIE DO BRASIL ONLINE", font=f_archivo_regular(13), fill=SKY)

    # kicker
    y = 190
    draw.text((PAD, y), kicker.upper(), font=f_mono(20), fill=SKY)
    y += 46

    # título — quebra em até 3 linhas, encolhendo a fonte se precisar
    largura_max = W - PAD * 2 - (340 if stat_valor else 0)
    tamanho = 56
    while tamanho > 34:
        fonte_titulo = f_archivo_extrabold(tamanho)
        linhas = quebrar_linhas(titulo, fonte_titulo, largura_max, draw)
        if len(linhas) <= 3:
            break
        tamanho -= 4
    linhas = linhas[:3]
    for linha in linhas:
        draw.text((PAD, y), linha, font=fonte_titulo, fill=CREAM)
        y += int(tamanho * 1.08)

    # stat callout, canto inferior direito — mesmo padrão do StatCallout.astro
    if stat_valor:
        fv = f_archivo_extrabold(88)
        largura_valor = draw.textlength(stat_valor, font=fv)
        x_stat = W - PAD - largura_valor
        y_stat = H - PAD - 100
        draw.text((x_stat, y_stat), stat_valor, font=fv, fill=AMBER)
        if stat_label:
            fl = f_mono(15)
            linhas_label = quebrar_linhas(stat_label.upper(), fl, 300, draw)
            yl = y_stat + 96
            for linha in linhas_label:
                largura_l = draw.textlength(linha, font=fl)
                draw.text((W - PAD - largura_l, yl), linha, font=fl, fill=SKY)
                yl += 20

    # régua inferior fina — assinatura sempre presente
    draw.line([(PAD, H - PAD + 6), (W - PAD, H - PAD + 6)], fill=(251, 247, 239, 60), width=1)

    caminho_saida.parent.mkdir(parents=True, exist_ok=True)
    img.save(caminho_saida, "PNG", optimize=True)
    print(f"gerado: {caminho_saida.relative_to(RAIZ)}")


def ler_frontmatter(caminho_md):
    """Parser propositalmente simples: pega qualquer 'chave: valor', ignorando
    indentação/aninhamento — suficiente pra extrair os poucos campos escalares
    que este script usa (título, edição, interacoesDireita), mesmo os que
    vivem aninhados dentro de `dados:`. Não serve para editar o YAML de volta."""
    texto = caminho_md.read_text(encoding="utf-8")
    bloco = texto.split("---")[1]
    campos = {}
    for linha in bloco.splitlines():
        m = re.match(r'^\s*(\w+):\s*"?([^"\n]*?)"?\s*$', linha)
        if m and m.group(2) and not m.group(2).startswith("-"):
            campos.setdefault(m.group(1), m.group(2).strip())
    return campos


def gerar_padrao():
    gerar_imagem(
        SAIDA / "default.png",
        kicker="OBSERVA · Eleições 2026",
        titulo="A eleição de 2026 também acontece no feed",
    )


def gerar_edicao(caminho_md):
    campos = ler_frontmatter(caminho_md)
    slug = caminho_md.stem
    edicao = campos.get("edicao", "")
    direita = campos.get("interacoesDireita", "")
    direita_ptbr = direita.replace(".", ",")  # 66.3 -> 66,3 (padrão brasileiro)
    gerar_imagem(
        SAIDA / f"{slug}.png",
        kicker=f"Semana {edicao}",
        titulo=campos.get("titulo", ""),
        stat_valor=f"{direita_ptbr}%" if direita else None,
        stat_label=f"Interações da direita, semana {edicao}" if direita else None,
    )


if __name__ == "__main__":
    alvo = sys.argv[1] if len(sys.argv) > 1 else None
    if alvo:
        gerar_edicao(CONTEUDO / f"{alvo}.md")
    else:
        gerar_padrao()
        for md in sorted(CONTEUDO.glob("*.md")):
            gerar_edicao(md)
