"""
Gera o PDF "KB e RAG no Marc.IA" no mesmo estilo escuro do material de referência.
Lê o Markdown estruturado e monta páginas com ReportLab.

Uso: python scripts/gerar_pdf_kb_rag.py
Saída: docs/KB_RAG_MarcIA.pdf
"""

import os
import re
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm, mm
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, PageBreak,
    Table, TableStyle, KeepTogether, NextPageTemplate
)

# ===== Paleta (igual ao PDF modelo) =====
BG_DARK      = colors.HexColor("#0F1B2D")   # fundo
BG_DEEPER    = colors.HexColor("#0A1422")   # fundo do header/cover
BG_CARD      = colors.HexColor("#172A45")   # card de seção
BG_TABLE     = colors.HexColor("#1E2F4D")   # tabela de chunks
ACCENT       = colors.HexColor("#F5C518")   # amarelo destaque
ORANGE       = colors.HexColor("#F26B3A")   # laranja chips
TEAL         = colors.HexColor("#2DD4BF")   # teal chips
BLUE         = colors.HexColor("#4F9CF9")   # azul chips
RED          = colors.HexColor("#E5484D")
GREEN        = colors.HexColor("#22C55E")
LINE         = colors.HexColor("#2A3B5A")
TEXT_MAIN    = colors.HexColor("#E6EDF7")
TEXT_DIM     = colors.HexColor("#9DB1D1")
TEXT_MUTED   = colors.HexColor("#6B7E9F")
CODE_BG      = colors.HexColor("#0B1B30")
CODE_BORDER  = colors.HexColor("#1F3559")

# ===== Caminhos =====
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_MD   = os.path.join(BASE_DIR, "docs", "KB_RAG_MarcIA.md")
OUT_PDF  = os.path.join(BASE_DIR, "docs", "KB_RAG_MarcIA.pdf")

PAGE_W, PAGE_H = A4
MARGIN_X = 2.0 * cm
MARGIN_TOP = 2.2 * cm
MARGIN_BOTTOM = 2.0 * cm


# ===== Estilos =====
styles = getSampleStyleSheet()

def S(name, **kw):
    base = ParagraphStyle(name=name, fontName="Helvetica", fontSize=10,
                          leading=14, textColor=TEXT_MAIN, alignment=TA_LEFT)
    for k, v in kw.items():
        setattr(base, k, v)
    return base

ST = {
    "kicker":   S("kicker", fontName="Helvetica-Bold", fontSize=8.5, leading=11,
                  textColor=ACCENT, spaceAfter=8),
    "h1_cover": S("h1_cover", fontName="Helvetica-Bold", fontSize=42, leading=46,
                  textColor=TEXT_MAIN, spaceAfter=10),
    "h1":       S("h1", fontName="Helvetica-Bold", fontSize=26, leading=32,
                  textColor=TEXT_MAIN, spaceBefore=8, spaceAfter=14),
    "h2":       S("h2", fontName="Helvetica-Bold", fontSize=18, leading=24,
                  textColor=TEXT_MAIN, spaceBefore=14, spaceAfter=10),
    "h3":       S("h3", fontName="Helvetica-Bold", fontSize=12.5, leading=18,
                  textColor=ACCENT, spaceBefore=10, spaceAfter=6),
    "body":     S("body", fontSize=10.5, leading=15.5, textColor=TEXT_MAIN,
                  alignment=TA_LEFT, spaceAfter=8),
    "body_dim": S("body_dim", fontSize=10, leading=15, textColor=TEXT_DIM,
                  spaceAfter=8),
    "quote":    S("quote", fontName="Helvetica-Oblique", fontSize=11, leading=16,
                  textColor=TEXT_MAIN, leftIndent=12, spaceBefore=6, spaceAfter=10),
    "chip":     S("chip", fontName="Helvetica-Bold", fontSize=8, leading=10,
                  textColor=BG_DEEPER),
    "code":     S("code", fontName="Courier", fontSize=8.8, leading=12,
                  textColor=colors.HexColor("#CFE3FF"), leftIndent=6),
    "bullet":   S("bullet", fontSize=10.5, leading=15.5, textColor=TEXT_MAIN,
                  leftIndent=14, bulletIndent=4, spaceAfter=4),
    "footer_l": S("footer_l", fontName="Helvetica", fontSize=8, textColor=TEXT_MUTED),
    "footer_r": S("footer_r", fontName="Helvetica", fontSize=8, textColor=TEXT_MUTED,
                  alignment=TA_RIGHT),
    "tag_lbl":  S("tag_lbl", fontName="Helvetica-Bold", fontSize=7.5,
                  textColor=TEXT_DIM),
    "card_h":   S("card_h", fontName="Helvetica-Bold", fontSize=11, leading=14,
                  textColor=TEXT_MAIN),
    "card_b":   S("card_b", fontSize=9.2, leading=13, textColor=TEXT_DIM),
    "cell_h":   S("cell_h", fontName="Helvetica-Bold", fontSize=9, leading=12,
                  textColor=ACCENT),
    "cell":     S("cell", fontSize=9, leading=12.5, textColor=TEXT_MAIN),
}


# ===== Util =====
def md_inline_to_html(text: str) -> str:
    """Converte inline markdown (negrito, código, itálico) pra tags ReportLab."""
    # protege escapes
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    # código inline `...`
    text = re.sub(
        r"`([^`]+)`",
        r'<font name="Courier" color="#7CC4FF">\1</font>',
        text,
    )
    # negrito **...**
    text = re.sub(r"\*\*([^*]+)\*\*", r'<b color="#FFFFFF">\1</b>', text)
    # itálico *...*
    text = re.sub(r"(?<![\*\\])\*([^*\n]+)\*(?!\*)",
                  r'<i color="#9DB1D1">\1</i>', text)
    return text


def chip(text, fill=ACCENT, fg=BG_DEEPER):
    return Paragraph(f'<para align="center"><font color="{fg.hexval()}">{text}</font></para>',
                     ST["chip"])


def block(content, bg=BG_CARD, border=LINE, padding=10):
    """Mini-card com fundo escuro."""
    t = Table([[content]], colWidths=[PAGE_W - 2 * MARGIN_X])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), bg),
        ("BOX", (0, 0), (-1, -1), 0.6, border),
        ("LEFTPADDING", (0, 0), (-1, -1), padding),
        ("RIGHTPADDING", (0, 0), (-1, -1), padding),
        ("TOPPADDING", (0, 0), (-1, -1), padding - 2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), padding - 2),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    return t


def two_col(left_flow, right_flow, ratio=(0.5, 0.5), gap=14):
    """Duas colunas como mini-cards lado a lado."""
    inner_w = PAGE_W - 2 * MARGIN_X
    col_w = [(inner_w - gap) * r for r in ratio]
    t = Table([[left_flow, right_flow]], colWidths=col_w)
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    return t


def divider():
    return Table([[""]], colWidths=[PAGE_W - 2 * MARGIN_X], rowHeights=[0.6],
                  style=TableStyle([("LINEBELOW", (0, 0), (-1, -1), 0.5, LINE)]))


# ===== Header / Footer =====
def header_footer(canvas, doc):
    canvas.saveState()
    # fundo escuro em todas as páginas
    canvas.setFillColor(BG_DARK)
    canvas.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)

    # footer esquerdo
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(TEXT_MUTED)
    canvas.drawString(MARGIN_X, 1.0 * cm, "KB e RAG no Marc.IA")

    # footer direito — número da página / total
    page_num = canvas.getPageNumber()
    txt = f"{page_num:02d} · Material de estudo"
    canvas.drawRightString(PAGE_W - MARGIN_X, 1.0 * cm, txt)

    # linha fina acima do footer
    canvas.setStrokeColor(LINE)
    canvas.setLineWidth(0.4)
    canvas.line(MARGIN_X, 1.5 * cm, PAGE_W - MARGIN_X, 1.5 * cm)
    canvas.restoreState()


def cover_footer(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(BG_DEEPER)
    canvas.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    # rodapé da capa
    canvas.setFont("Helvetica", 8.5)
    canvas.setFillColor(TEXT_MUTED)
    canvas.drawString(MARGIN_X, 1.0 * cm, "Victor Almeida")
    canvas.drawString(MARGIN_X, 0.6 * cm, "IA aplicada — material de apoio")
    canvas.drawRightString(PAGE_W - MARGIN_X, 1.0 * cm, "jul / 2026")
    canvas.drawRightString(PAGE_W - MARGIN_X, 0.6 * cm, "Marc.IA · UFCAT")
    canvas.restoreState()


# ===== Construção do documento =====
def build():
    doc = BaseDocTemplate(
        OUT_PDF, pagesize=A4,
        leftMargin=MARGIN_X, rightMargin=MARGIN_X,
        topMargin=MARGIN_TOP, bottomMargin=MARGIN_BOTTOM,
        title="KB e RAG no Marc.IA",
        author="Victor Almeida",
    )

    frame_full = Frame(MARGIN_X, MARGIN_BOTTOM,
                       PAGE_W - 2 * MARGIN_X,
                       PAGE_H - MARGIN_TOP - MARGIN_BOTTOM,
                       id="full", showBoundary=0)
    doc.addPageTemplates([
        PageTemplate(id="cover", frames=[frame_full], onPage=cover_footer),
        PageTemplate(id="content", frames=[frame_full], onPage=header_footer),
    ])

    story = []

    # ---------- CAPA ----------
    story.append(Spacer(1, 0.6 * cm))
    # chip "MATERIAL DE ESTUDADO — IA APLICADA"
    story.append(chip("● MATERIAL DE ESTUDO — IA APLICADA"))
    story.append(Spacer(1, 1.2 * cm))

    # título kicker
    story.append(Paragraph("// como o tutor lembra do que foi ensinado",
                           S("kicker", textColor=TEAL)))
    story.append(Spacer(1, 0.4 * cm))

    story.append(Paragraph("KB e <font color='#F5C518'>RAG</font>", ST["h1_cover"]))
    story.append(Paragraph("no Marc.IA", ST["h1_cover"]))
    story.append(Spacer(1, 0.6 * cm))

    story.append(Paragraph(
        "Um guia direto sobre como o Marc.IA dá ao tutor de IA a \"memória\" "
        "do que o professor ensinou: a <b>Base de Conhecimento (KB)</b> que "
        "guarda os materiais, e o <b>RAG</b> que faz o modelo consultar essa "
        "base antes de responder.",
        S("body_dim", fontSize=12, leading=18, textColor=TEXT_MAIN)))
    story.append(Spacer(1, 1.6 * cm))

    # 4 cards horizontais — KB / Embeddings / ChromaDB / RAG
    cards = [
        ("A PASTA",   "KB",         BG_DEEPER, ORANGE),
        ("OS NÚMEROS","Embeddings", BG_DEEPER, TEAL),
        ("O BANCO",   "ChromaDB",   BG_DEEPER, BLUE),
        ("O RITUAL",  "RAG",        BG_DEEPER, RED),
    ]
    inner_w = PAGE_W - 2 * MARGIN_X
    card_w = (inner_w - 3 * 14) / 4
    rows = []
    for label, title, bg, accent in cards:
        cell = []
        cell.append(Paragraph(
            f'<para align="left"><font color="{accent.hexval()}" name="Helvetica-Bold" size="8.5">● {label}</font></para>',
            ST["body_dim"]))
        cell.append(Spacer(1, 4))
        cell.append(Paragraph(f'<font color="#FFFFFF" name="Helvetica-Bold" size="20">{title}</font>',
                              ST["body_dim"]))
        rows.append(cell)
    grid = Table([rows], colWidths=[card_w] * 4, rowHeights=[5.4 * cm])
    grid.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), BG_CARD),
        ("BOX", (0, 0), (-1, -1), 0.6, LINE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 14),
        ("RIGHTPADDING", (0, 0), (-1, -1), 14),
        ("TOPPADDING", (0, 0), (-1, -1), 14),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 14),
    ]))
    story.append(grid)
    story.append(Spacer(1, 1.6 * cm))
    story.append(divider())
    story.append(Spacer(1, 0.6 * cm))

    # "NESTE MATERIAL" — tabela de seções
    story.append(Paragraph("NESTE MATERIAL", ST["tag_lbl"]))
    story.append(Spacer(1, 0.3 * cm))

    sections = [
        ("01", "Por que o modelo 'esquece'", "o problema que a KB resolve"),
        ("02", "O que é uma KB", "estrutura da pasta data/kb_ip/"),
        ("03", "Embeddings", "como texto vira vetor"),
        ("04", "ChromaDB", "o vector store do projeto"),
        ("05", "Chunking", "quebrar arquivos em pedaços"),
        ("06", "Indexador", "o script que popula o ChromaDB"),
        ("07", "Retriever", "busca semântica com boost"),
        ("08", "RAG no agente", "como o AgenteIP consulta antes"),
        ("09", "Fluxo ponta a ponta", "do 'oi' do aluno à resposta"),
        ("10", "Glossário", "referência rápida"),
    ]
    rows = []
    for n, title, sub in sections:
        rows.append([
            Paragraph(f'<font color="#F5C518" name="Helvetica-Bold">{n}</font>', ST["cell"]),
            Paragraph(md_inline_to_html(title), ST["cell"]),
            Paragraph(f'<font color="#6B7E9F">{sub}</font>', ST["cell"]),
        ])
    sec_t = Table(rows, colWidths=[1.0 * cm, 8.0 * cm, 7.0 * cm])
    sec_t.setStyle(TableStyle([
        ("LINEBELOW", (0, 0), (-1, -2), 0.4, LINE),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ]))
    story.append(sec_t)

    # ---------- CONTEÚDO ----------
    story.append(NextPageTemplate("content"))
    story.append(PageBreak())

    # SEÇÃO 01 — Por que o modelo "esquece"
    story.append(Paragraph("01 — FUNDAMENTOS", ST["tag_lbl"]))
    story.append(Paragraph("Por que o modelo &quot;esquece&quot;", ST["h1"]))
    story.append(Paragraph(
        "Um modelo de linguagem como o Claude tem um problema clássico: ele "
        "foi treinado uma vez, num corte de conhecimento, e não sabe nada do "
        "que aconteceu depois disso. Para o Marc.IA isso é grave — o tutor "
        "precisa responder com base nos slides do Prof. Márcio, nas listas "
        "de exercícios, no material de aula do semestre 2026/S1. Se o modelo "
        "&quot;responde do que aprendeu na internet&quot;, ele erra a sintaxe "
        "de Portugol, inventa nomes de funções, cita listas que não existem.",
        ST["body"]))
    story.append(Spacer(1, 0.4 * cm))

    # duas colunas: Sem KB / Com KB
    left = [
        Paragraph('<font color="#F26B3A" name="Helvetica-Bold" size="8.5">SEM KB</font>',
                  ST["body_dim"]),
        Spacer(1, 4),
        Paragraph(
            "O aluno pergunta &quot;como faço matriz em VisuAlg?&quot; e o "
            "modelo responde algo plausível, mas genérico, em pseudocódigo "
            "inventado.",
            ST["body_dim"]),
    ]
    right = [
        Paragraph('<font color="#22C55E" name="Helvetica-Bold" size="8.5">COM KB</font>',
                  ST["body_dim"]),
        Spacer(1, 4),
        Paragraph(
            "O modelo busca nos slides do Prof. Márcio, acha a Aula 3 com a "
            "sintaxe real de <font name='Courier' color='#7CC4FF'>matriz[1..N, 1..M]</font>, "
            "e cita isso na resposta.",
            ST["body_dim"]),
    ]
    story.append(two_col(block(left, bg=BG_DEEPER), block(right, bg=BG_DEEPER)))
    story.append(Spacer(1, 0.6 * cm))

    # definição direta
    defblock = [
        Paragraph('<font color="#F5C518" name="Helvetica-Bold" size="8.5">DEFINIÇÃO DIRETA</font>',
                  ST["body_dim"]),
        Spacer(1, 4),
        Paragraph(
            "<b>KB (Knowledge Base, Base de Conhecimento)</b> é o conjunto "
            "curado de materiais da disciplina que o tutor tem autorização "
            "para citar — slides, listas, livros-texto podados, provas "
            "anteriores. É o que diferencia &quot;um tutor genérico&quot; de "
            "&quot;o tutor desta disciplina&quot;.",
            S("body", fontSize=11, leading=16)),
    ]
    story.append(block(defblock, bg=BG_CARD))
    story.append(Spacer(1, 0.5 * cm))

    # SEÇÃO 02 — O que é uma KB
    story.append(PageBreak())
    story.append(Paragraph("02 — A BASE", ST["tag_lbl"]))
    story.append(Paragraph("O que é uma KB (a pasta data/kb_ip/)", ST["h1"]))
    story.append(Paragraph(
        "No Marc.IA, a KB é literalmente uma pasta no projeto com os arquivos "
        "que o Prof. Márcio (ou a equipe) subiu. Cada subpasta tem um papel:",
        ST["body"]))

    # árvore da pasta
    tree = '''<font name="Courier" color="#CFE3FF">
data/kb_ip/<br/>
├── 00_meta/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;regras de estilo, relatórios, notas internas<br/>
├── 01_listas/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;listas 1, 2, 3 (Portugol) e 5 (Python)<br/>
├── 02_aulas/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;slides e roteiros das aulas do Prof.<br/>
├── 03_livros/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;livros-texto podados (só o essencial)<br/>
└── 04_provas/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;provas antigas + relatório de correção
</font>'''
    story.append(block([Paragraph(tree, S("code", fontSize=9, leading=14))],
                       bg=CODE_BG, border=CODE_BORDER, padding=14))
    story.append(Spacer(1, 0.4 * cm))
    story.append(Paragraph(
        "Cada arquivo <font name='Courier' color='#7CC4FF'>.txt</font>, "
        "<font name='Courier' color='#7CC4FF'>.md</font>, "
        "<font name='Courier' color='#7CC4FF'>.visualg</font>, "
        "<font name='Courier' color='#7CC4FF'>.por</font> ou "
        "<font name='Courier' color='#7CC4FF'>.py</font> vira candidato a "
        "virar parte da KB. A pasta não tem limite de tamanho, mas vale uma "
        "regra: <b>só entra o que o professor aceita que o aluno veja</b>. "
        "KB não é lugar de rascunho — é referência.",
        ST["body"]))

    # tabela de características
    story.append(Spacer(1, 0.3 * cm))
    chars = [
        [Paragraph("CARACTERÍSTICA", ST["cell_h"]),
         Paragraph("VALOR NO MARC.IA", ST["cell_h"])],
        [Paragraph("Formatos aceitos", ST["cell"]),
         Paragraph("<font name='Courier' color='#7CC4FF'>.txt</font>, "
                   "<font name='Courier' color='#7CC4FF'>.md</font>, "
                   "<font name='Courier' color='#7CC4FF'>.visualg</font>, "
                   "<font name='Courier' color='#7CC4FF'>.por</font>, "
                   "<font name='Courier' color='#7CC4FF'>.py</font>", ST["cell"])],
        [Paragraph("Quem alimenta", ST["cell"]),
         Paragraph("Equipe (Sprint 2) — uploads manuais por enquanto", ST["cell"])],
        [Paragraph("Quem lê", ST["cell"]),
         Paragraph("Só o indexador — o tutor nunca lê arquivo direto", ST["cell"])],
    ]
    ct = Table(chars, colWidths=[5.0 * cm, 11.0 * cm])
    ct.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), BG_DEEPER),
        ("BACKGROUND", (0, 1), (-1, -1), BG_TABLE),
        ("LINEBELOW", (0, 0), (-1, -1), 0.3, LINE),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))
    story.append(ct)

    # SEÇÃO 03 — Embeddings
    story.append(PageBreak())
    story.append(Paragraph("03 — VETORES", ST["tag_lbl"]))
    story.append(Paragraph("Embeddings — texto vira vetor", ST["h1"]))
    story.append(Paragraph(
        "O computador não entende &quot;diferença entre recursão e iteração&quot;. "
        "Para o modelo achar slides parecidos com a pergunta do aluno, "
        "precisamos transformar texto em <b>números</b> que preservem "
        "significado. Isso é um <b>embedding</b>.",
        ST["body"]))
    story.append(Paragraph(
        "<b>A analogia:</b> pense num mapa. Cada cidade vira um ponto no "
        "mapa. Cidades parecidas (clima, cultura, tamanho) ficam perto; "
        "cidades diferentes ficam longe. Embedding faz a mesma coisa com "
        "palavras/frases: cada texto vira um <b>ponto</b> num espaço de "
        "centenas de dimensões. Textos parecidos ficam perto; textos "
        "diferentes ficam longe.",
        ST["body"]))

    # tabela de exemplo
    emb_rows = [
        [Paragraph("TEXTO", ST["cell_h"]),
         Paragraph("VIROU UM VETOR (EXEMPLO FICTÍCIO)", ST["cell_h"])],
        [Paragraph("&quot;O que é recursão em Python?&quot;", ST["cell"]),
         Paragraph("<font name='Courier' color='#7CC4FF'>[0.12, -0.34, 0.88, …, 0.05]</font> "
                   "<font color='#6B7E9F'>(384 números)</font>", ST["cell"])],
        [Paragraph("&quot;Funções recursivas chamam a si mesmas&quot;", ST["cell"]),
         Paragraph("<font name='Courier' color='#7CC4FF'>[0.11, -0.30, 0.85, …, 0.07]</font>", ST["cell"])],
        [Paragraph("&quot;Como plantar batatas?&quot;", ST["cell"]),
         Paragraph("<font name='Courier' color='#E5484D'>[-0.55, 0.71, -0.22, …, -0.40]</font>", ST["cell"])],
    ]
    et = Table(emb_rows, colWidths=[7.5 * cm, 8.5 * cm])
    et.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), BG_DEEPER),
        ("BACKGROUND", (0, 1), (-1, -1), BG_TABLE),
        ("LINEBELOW", (0, 0), (-1, -1), 0.3, LINE),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))
    story.append(Spacer(1, 0.2 * cm))
    story.append(et)
    story.append(Spacer(1, 0.3 * cm))
    story.append(Paragraph(
        "Repare: a primeira e a segunda frase têm vetores parecidos (estão "
        "&quot;perto&quot; no espaço). A terceira está longe. Esse &quot;quão "
        "perto&quot; é o que o RAG usa para decidir o que é relevante.",
        ST["body"]))
    story.append(Spacer(1, 0.3 * cm))
    infoblock = [
        Paragraph('<font color="#2DD4BF" name="Helvetica-Bold" size="8.5">NO MARC.IA</font>',
                  ST["body_dim"]),
        Spacer(1, 4),
        Paragraph(
            "Usamos o modelo <font name='Courier' color='#7CC4FF'>all-MiniLM-L6-v2</font> "
            "da biblioteca <font name='Courier' color='#7CC4FF'>sentence-transformers</font>. "
            "Ele gera vetores de 384 dimensões, é leve o suficiente para "
            "rodar local sem GPU, e é gratuito.",
            S("body", fontSize=10.5, leading=15)),
    ]
    story.append(block(infoblock, bg=BG_DEEPER))

    # SEÇÃO 04 — ChromaDB
    story.append(PageBreak())
    story.append(Paragraph("04 — O BANCO", ST["tag_lbl"]))
    story.append(Paragraph("ChromaDB — o vector store", ST["h1"]))
    story.append(Paragraph(
        "Guardar milhões de vetores e conseguir perguntar &quot;qual está "
        "mais perto deste aqui?&quot; rápido é trabalho de um "
        "<b>vector store</b> (banco de vetores). No Marc.IA escolhemos o "
        "<b>ChromaDB</b> porque:",
        ST["body"]))
    bullets = [
        "Roda local, sem precisar de servidor externo;",
        "Persiste em disco (a pasta <font name='Courier' color='#7CC4FF'>data/chroma/</font>);",
        "Tem busca por similaridade de cosseno já embutida;",
        "Integra direto com <font name='Courier' color='#7CC4FF'>sentence-transformers</font>.",
    ]
    for b in bullets:
        story.append(Paragraph("• " + b, ST["bullet"]))

    story.append(Spacer(1, 0.4 * cm))
    tree2 = '''<font name="Courier" color="#CFE3FF">
data/chroma/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;← banco vetorial (criado pelo indexador)<br/>
└── ...&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;← arquivos binários do ChromaDB
</font>'''
    story.append(block([Paragraph(tree2, S("code", fontSize=9, leading=14))],
                       bg=CODE_BG, border=CODE_BORDER, padding=12))
    story.append(Spacer(1, 0.4 * cm))
    story.append(Paragraph(
        "A coleção (tabela) se chama <font name='Courier' color='#7CC4FF'>kb_ip</font> "
        "e é indexada com distância <b>cosseno</b> — uma medida que ignora "
        "o tamanho do vetor e mede só o ângulo entre eles. Em texto, isso "
        "funciona bem: dois parágrafos &quot;sobre o mesmo assunto&quot; "
        "apontam na mesma direção, mesmo que um seja mais longo que o outro.",
        ST["body"]))

    # SEÇÃO 05 — Chunking
    story.append(PageBreak())
    story.append(Paragraph("05 — DIVIDINDO", ST["tag_lbl"]))
    story.append(Paragraph("Chunking — quebrar o material em pedaços", ST["h1"]))
    story.append(Paragraph(
        "Modelos de embedding têm um limite: cada entrada é uma frase curta, "
        "não um livro inteiro. Se você colar as 200 páginas do <i>Pense em "
        "Python</i> de uma vez, o vetor que sai é genérico demais para "
        "encontrar qualquer coisa. A solução é <b>dividir antes</b>.",
        ST["body"]))
    story.append(Paragraph(
        "No Marc.IA, o <font name='Courier' color='#7CC4FF'>indexador.py</font> "
        "quebra cada arquivo assim:",
        ST["body"]))

    chunk_rows = [
        [Paragraph("PARÂMETRO", ST["cell_h"]),
         Paragraph("VALOR", ST["cell_h"]),
         Paragraph("O QUE SIGNIFICA", ST["cell_h"])],
        [Paragraph("<font name='Courier' color='#7CC4FF'>CHUNK_CHARS</font>", ST["cell"]),
         Paragraph("2000", ST["cell"]),
         Paragraph("Tamanho aproximado de cada pedaço (~500 tokens)", ST["cell"])],
        [Paragraph("<font name='Courier' color='#7CC4FF'>OVERLAP_CHARS</font>", ST["cell"]),
         Paragraph("200", ST["cell"]),
         Paragraph("Quanto o pedaço N &quot;repete&quot; do pedaço N-1", ST["cell"])],
    ]
    ct2 = Table(chunk_rows, colWidths=[4.5 * cm, 2.5 * cm, 9.0 * cm])
    ct2.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), BG_DEEPER),
        ("BACKGROUND", (0, 1), (-1, -1), BG_TABLE),
        ("LINEBELOW", (0, 0), (-1, -1), 0.3, LINE),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))
    story.append(ct2)
    story.append(Spacer(1, 0.4 * cm))
    story.append(Paragraph(
        "O overlap existe por um motivo prático: se uma frase importante "
        "cair exatamente no meio do corte, sem overlap ela aparece pela "
        "metade em dois chunks e nenhum dos dois fica bom. Com 200 "
        "caracteres de repetição, a chance de um conceito ficar inteiro num "
        "chunk sobe muito.",
        ST["body"]))

    code1 = '''<font name="Courier" color="#CFE3FF">
# src/rag/indexador.py — lógica do chunking
while inicio &lt; len(texto):
    fim = min(inicio + CHUNK_CHARS, len(texto))
    trecho = texto[inicio:fim].strip()
    if trecho:
        chunks.append({</font>
<font name="Courier" color="#7CC4FF">            "text": trecho, "fonte": fonte, "chunk_idx": idx</font>
<font name="Courier" color="#CFE3FF">        })
    if fim == len(texto):
        break
</font>
<font name="Courier" color="#F5C518">    inicio = fim - OVERLAP_CHARS   # volta 200 chars e recomeça</font>
<font name="Courier" color="#CFE3FF">
</font>'''
    story.append(block([Paragraph(code1, S("code", fontSize=8.5, leading=12))],
                       bg=CODE_BG, border=CODE_BORDER, padding=12))
    story.append(Spacer(1, 0.3 * cm))
    story.append(Paragraph(
        "Cada chunk ganha dois metadados: <font name='Courier' color='#7CC4FF'>fonte</font> "
        "(caminho relativo do arquivo) e <font name='Courier' color='#7CC4FF'>chunk_idx</font> "
        "(número sequencial). A <b>fonte</b> é o que depois aparece na "
        "resposta do tutor entre colchetes — "
        "<font name='Courier' color='#7CC4FF'>[Aula3_Vetores_Matrizes]</font> "
        "— para o aluno saber de onde veio.",
        ST["body"]))

    # SEÇÃO 06 — Indexador
    story.append(PageBreak())
    story.append(Paragraph("06 — INDEXANDO", ST["tag_lbl"]))
    story.append(Paragraph("Indexador — popular o ChromaDB", ST["h1"]))
    story.append(Paragraph(
        "O <font name='Courier' color='#7CC4FF'>indexador.py</font> é o "
        "script que lê a pasta <font name='Courier' color='#7CC4FF'>kb_ip/</font>, "
        "quebra em chunks, calcula o embedding de cada um e grava no "
        "ChromaDB. Ele é <b>offline</b>: você roda uma vez quando adiciona "
        "material novo, e ele só processa o que ainda não foi indexado.",
        ST["body"]))

    code2 = '''<font name="Courier" color="#7CC4FF">
# uso normal: só adiciona o que é novo
python -m src.rag.indexador

# reconstruir do zero (apaga tudo e reindexa)
python -m src.rag.indexador --forcar</font>
<font name="Courier" color="#CFE3FF">
</font>'''
    story.append(block([Paragraph(code2, S("code", fontSize=9, leading=13))],
                       bg=CODE_BG, border=CODE_BORDER, padding=12))
    story.append(Spacer(1, 0.4 * cm))

    idx_rows = [
        [Paragraph("ETAPA INTERNA", ST["cell_h"]),
         Paragraph("O QUE ACONTECE", ST["cell_h"])],
        [Paragraph("1. Listar arquivos", ST["cell"]),
         Paragraph("<font name='Courier' color='#7CC4FF'>os.walk</font> recursivo em "
                   "<font name='Courier' color='#7CC4FF'>data/kb_ip/</font>", ST["cell"])],
        [Paragraph("2. Chunkar", ST["cell"]),
         Paragraph("divide cada arquivo em pedaços de 2000 chars com overlap 200", ST["cell"])],
        [Paragraph("3. Embedding", ST["cell"]),
         Paragraph("<font name='Courier' color='#7CC4FF'>SentenceTransformer(\"all-MiniLM-L6-v2\").encode(textos)</font>", ST["cell"])],
        [Paragraph("4. Persistir", ST["cell"]),
         Paragraph("<font name='Courier' color='#7CC4FF'>collection.add(ids, embeddings, documents, metadatas)</font>", ST["cell"])],
        [Paragraph("5. Idempotência", ST["cell"]),
         Paragraph("cada chunk tem id = <font name='Courier' color='#7CC4FF'>md5(fonte:idx)[:8]</font> — re-rodar não duplica", ST["cell"])],
    ]
    it = Table(idx_rows, colWidths=[4.5 * cm, 11.5 * cm])
    it.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), BG_DEEPER),
        ("BACKGROUND", (0, 1), (-1, -1), BG_TABLE),
        ("LINEBELOW", (0, 0), (-1, -1), 0.3, LINE),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))
    story.append(it)
    story.append(Spacer(1, 0.3 * cm))
    story.append(Paragraph(
        "Esse passo é lento (pode levar minutos com KB grande) mas só roda "
        "quando você adiciona material. Em produção, o tutor <b>nunca chama "
        "o indexador</b> — ele só lê o ChromaDB já populado.",
        ST["body"]))

    # SEÇÃO 07 — Retriever
    story.append(PageBreak())
    story.append(Paragraph("07 — BUSCANDO", ST["tag_lbl"]))
    story.append(Paragraph("Retriever — busca semântica com boost", ST["h1"]))
    story.append(Paragraph(
        "O <font name='Courier' color='#7CC4FF'>retriever.py</font> é o que "
        "o agente chama toda vez que o aluno faz uma pergunta. Ele:",
        ST["body"]))
    steps = [
        "Transforma a pergunta do aluno em embedding (com o mesmo modelo usado na indexação);",
        "Pede ao ChromaDB os <b>12 chunks mais próximos</b> (cosine similarity);",
        "Aplica <b>boost por metadata</b> — pesos diferentes por tipo de documento;",
        "Detecta a <b>etapa</b> da disciplina (Portugol vs Python) por palavras-chave;",
        "Retorna os <b>top-3</b> chunks depois da reordenação.",
    ]
    for i, s in enumerate(steps, 1):
        story.append(Paragraph(f"{i}. {s}", ST["bullet"]))

    code3 = '''<font name="Courier" color="#CFE3FF">
# src/rag/retriever.py — pesos por tipo de documento
PESOS_TIPO = {</font>
<font name="Courier" color="#22C55E">    "lista_exercicios":       1.0,   </font><font name="Courier" color="#6B7E9F"># quando aluno quer treinar</font>
<font name="Courier" color="#CFE3FF">    "prova":                  0.9,
    "especificacao_trabalho": 0.85,
</font>
<font name="Courier" color="#4F9CF9">    "slide_ou_roteiro":       0.7,   </font><font name="Courier" color="#6B7E9F"># aula do Prof.</font>
<font name="Courier" color="#CFE3FF">    "resolucao_aluno":        0.6,
</font>
<font name="Courier" color="#E5484D">    "livro_referencia_podado": 0.5,  </font><font name="Courier" color="#6B7E9F"># livro didático — mais largo</font>
<font name="Courier" color="#CFE3FF">
</font>
<font name="Courier" color="#F5C518">    "guia_pedagogico":        1.2,   </font><font name="Courier" color="#6B7E9F"># skill do PyAI Professor</font>
<font name="Courier" color="#CFE3FF">    "relatorio_correcao":     1.0,
}
</font>'''
    story.append(block([Paragraph(code3, S("code", fontSize=8.5, leading=12))],
                       bg=CODE_BG, border=CODE_BORDER, padding=12))
    story.append(Spacer(1, 0.4 * cm))
    story.append(Paragraph(
        "<b>Por que o boost é necessário?</b> O modelo MiniLM é bom em "
        "&quot;isso é sobre o mesmo assunto&quot;, mas ruim em &quot;isso "
        "é uma lista de exercícios&quot;. Sem o boost, o livro didático "
        "(que tem muito texto e cobre tudo) ganha da lista (que é curta e "
        "específica). Com o boost, o retriever entende o <b>tipo</b> de "
        "material que o aluno provavelmente precisa.",
        ST["body"]))
    story.append(Spacer(1, 0.2 * cm))
    story.append(Paragraph(
        "A detecção de etapa também é uma heurística simples por "
        "palavras-chave (<font name='Courier' color='#7CC4FF'>&quot;portugol&quot;</font>, "
        "<font name='Courier' color='#7CC4FF'>&quot;visuAlg&quot;</font> → "
        "etapa 1; <font name='Courier' color='#7CC4FF'>&quot;python&quot;</font>, "
        "<font name='Courier' color='#7CC4FF'>&quot;f-string&quot;</font> → "
        "etapa 2). Não é perfeita, mas é barata e funciona no caso comum — "
        "perguntas vagas demais caem em <font name='Courier' color='#7CC4FF'>None</font> "
        "e o boost não aplica, indo pelo embedding puro.",
        ST["body"]))

    # SEÇÃO 08 — RAG no agente
    story.append(PageBreak())
    story.append(Paragraph("08 — NO AGENTE", ST["tag_lbl"]))
    story.append(Paragraph("RAG no agente — buscar antes de responder", ST["h1"]))
    story.append(Paragraph(
        "Agora a peça que junta tudo. O <font name='Courier' color='#7CC4FF'>AgenteIP</font> "
        "herda de <font name='Courier' color='#7CC4FF'>AgentBase</font>, "
        "e o método <font name='Courier' color='#7CC4FF'>responder()</font> "
        "faz, em ordem:",
        ST["body"]))

    code4 = '''<font name="Courier" color="#CFE3FF">
1. buscar_contexto(mensagem)   → chama retriever.buscar(mensagem)
2. _montar_messages(...)       → junta histórico + chunks + pergunta
3. cliente.messages.create()   → manda tudo pra API Claude
4. devolve o texto da resposta
</font>'''
    story.append(block([Paragraph(code4, S("code", fontSize=9.5, leading=14))],
                       bg=CODE_BG, border=CODE_BORDER, padding=14))
    story.append(Spacer(1, 0.3 * cm))
    story.append(Paragraph("O trecho-chave está em <font name='Courier' color='#7CC4FF'>_montar_messages()</font>:",
                           ST["body"]))

    code5 = '''<font name="Courier" color="#CFE3FF">
# src/agente_base.py — injeta a KB dentro do prompt
conteudo = mensagem
if chunks:
    contexto = "\n---\n".join(chunks)
    conteudo = (
</font>
<font name="Courier" color="#F5C518">        f"[Contexto relevante da KB]\n{contexto}\n\n"</font>
<font name="Courier" color="#F5C518">        f"[Pergunta do aluno]\n{mensagem}"</font>
<font name="Courier" color="#CFE3FF">
    )
messages.append({"role": "user", "content": conteudo})
</font>'''
    story.append(block([Paragraph(code5, S("code", fontSize=8.5, leading=12))],
                       bg=CODE_BG, border=CODE_BORDER, padding=12))
    story.append(Spacer(1, 0.3 * cm))
    story.append(Paragraph("O que o modelo <b>vê</b> quando o aluno faz uma pergunta é:",
                           ST["body"]))

    code6 = '''<font name="Courier" color="#F5C518">[Contexto relevante da KB]</font>
<font name="Courier" color="#CFE3FF">[Aula3_Vetores_Matrizes.md]
... (trecho do slide sobre vetores em Portugol) ...
</font>
<font name="Courier" color="#6B7E9F">---</font>
<font name="Courier" color="#CFE3FF">[lista3_vetores_matrizes.txt]
... (trecho da lista de exercícios) ...
</font>
<font name="Courier" color="#F5C518">[Pergunta do aluno]</font>
<font name="Courier" color="#CFE3FF">como somo duas matrizes em VisuAlg?</font>
<font name="Courier" color="#CFE3FF">
</font>'''
    story.append(block([Paragraph(code6, S("code", fontSize=9, leading=13))],
                       bg=CODE_BG, border=CODE_BORDER, padding=14))
    story.append(Spacer(1, 0.3 * cm))
    story.append(Paragraph(
        "Esse envelope é o &quot;RAG funcionando&quot;: a pergunta do "
        "aluno vai com o material relevante colado na frente. O modelo "
        "responde com base nesse material, não no que &quot;lembra&quot; do treino.",
        ST["body"]))

    # comparação sem/com RAG
    left = [Paragraph('<font color="#E5484D" name="Helvetica-Bold" size="8.5">SEM RAG</font>', ST["body_dim"]),
            Spacer(1, 4),
            Paragraph("O modelo responde de memória genérica, pode errar sintaxe.", ST["body_dim"])]
    right = [Paragraph('<font color="#22C55E" name="Helvetica-Bold" size="8.5">COM RAG</font>', ST["body_dim"]),
             Spacer(1, 4),
             Paragraph("O modelo cita o slide da Aula 3, segue a notação do professor.", ST["body_dim"])]
    story.append(two_col(block(left, bg=BG_DEEPER), block(right, bg=BG_DEEPER)))
    story.append(Spacer(1, 0.2 * cm))
    story.append(Paragraph(
        "Se o aluno pergunta algo fora da KB, o retriever devolve "
        "<font name='Courier' color='#7CC4FF'>[]</font> e o tutor responde "
        "&quot;não tenho material sobre isso&quot; em vez de alucinar.",
        ST["body"]))

    # SEÇÃO 09 — Fluxo ponta a ponta
    story.append(PageBreak())
    story.append(Paragraph("09 — PONTA A PONTA", ST["tag_lbl"]))
    story.append(Paragraph("Fluxo ponta a ponta", ST["h1"]))
    story.append(Paragraph(
        "Pergunta do aluno: <i>&quot;como faço MDC em portugol?&quot;</i>",
        S("body", fontSize=12, textColor=ACCENT)))
    story.append(Spacer(1, 0.4 * cm))

    flow_rows = [
        [Paragraph("QUEM", ST["cell_h"]),
         Paragraph("O QUE FAZ", ST["cell_h"])],
        [Paragraph('<font color="#F26B3A" name="Helvetica-Bold">chat.js</font>', ST["cell"]),
         Paragraph('<font color="#9DB1D1">navegador do aluno</font><br/>'
                   '<font name="Courier" color="#7CC4FF">POST /chat {mensagem, codigo, ...}</font>', ST["cell"])],
        [Paragraph('<font color="#F26B3A" name="Helvetica-Bold">app.py</font>', ST["cell"]),
         Paragraph('<font color="#9DB1D1">Flask</font><br/>'
                   'valida input, carrega <font name="Courier" color="#7CC4FF">Sessao</font>', ST["cell"])],
        [Paragraph('<font color="#F26B3A" name="Helvetica-Bold">AgenteIP.responder()</font>', ST["cell"]),
         Paragraph('<font color="#9DB1D1">src/agente_ip.py</font><br/>'
                   '1. <font name="Courier" color="#7CC4FF">buscar_contexto("como faço MDC em portugol?")</font>', ST["cell"])],
        [Paragraph('<font color="#F26B3A" name="Helvetica-Bold">retriever.buscar()</font>', ST["cell"]),
         Paragraph('<font color="#9DB1D1">src/rag/retriever.py</font><br/>'
                   '<font color="#9DB1D1">— encode da query → vetor 384-d</font><br/>'
                   '<font color="#9DB1D1">— busca top-12 no ChromaDB (cosine)</font><br/>'
                   '<font color="#9DB1D1">— boost por tipo: slide &gt; livro</font><br/>'
                   '<font color="#9DB1D1">— boost por etapa: detecta "portugol" → etapa 1</font><br/>'
                   '<font color="#9DB1D1">— retorna top-3 chunks com fonte</font>', ST["cell"])],
        [Paragraph('<font color="#F26B3A" name="Helvetica-Bold">_montar_messages()</font>', ST["cell"]),
         Paragraph('<font color="#9DB1D1">src/agente_base.py</font><br/>'
                   '<font color="#9DB1D1">— pega últimas 10 mensagens da Sessao</font><br/>'
                   '<font color="#9DB1D1">— cola os 3 chunks no formato [Contexto relevante da KB]</font><br/>'
                   '<font color="#9DB1D1">— cola a pergunta no formato [Pergunta do aluno]</font>', ST["cell"])],
        [Paragraph('<font color="#F26B3A" name="Helvetica-Bold">claude-opus-4-8</font>', ST["cell"]),
         Paragraph('<font color="#9DB1D1">API Anthropic</font><br/>'
                   '<font color="#9DB1D1">recebe: system_prompt + histórico + KB injetada + pergunta</font><br/>'
                   '<font color="#9DB1D1">responde em linguagem natural, citando a Aula de Funções</font>', ST["cell"])],
        [Paragraph('<font color="#F26B3A" name="Helvetica-Bold">resposta</font>', ST["cell"]),
         Paragraph('<font color="#9DB1D1">volta pro Flask</font><br/>'
                   '<font color="#9DB1D1">atualiza Sessao (histórico + +5 XP)</font><br/>'
                   '<font color="#9DB1D1">salva Sessao no SQLite</font>', ST["cell"])],
        [Paragraph('<font color="#F26B3A" name="Helvetica-Bold">chat.js</font>', ST["cell"]),
         Paragraph("renderiza a bolha do tutor", ST["cell"])],
    ]
    ft = Table(flow_rows, colWidths=[4.2 * cm, 11.8 * cm])
    ft.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), BG_DEEPER),
        ("BACKGROUND", (0, 1), (-1, -1), BG_TABLE),
        ("LINEBELOW", (0, 0), (-1, -1), 0.3, LINE),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    story.append(ft)
    story.append(Spacer(1, 0.4 * cm))
    story.append(Paragraph(
        "<b>Por que esse fluxo importa:</b> o tutor nunca lê arquivo da KB "
        "direto, nunca consulta a internet, nunca inventa sintaxe. Tudo "
        "que ele responde tem como fonte um chunk da pasta "
        "<font name='Courier' color='#7CC4FF'>data/kb_ip/</font> que ele "
        "acabou de receber no contexto.",
        S("body", fontSize=11, leading=16)))

    # SEÇÃO 10 — Glossário
    story.append(PageBreak())
    story.append(Paragraph("10 — REFERÊNCIA", ST["tag_lbl"]))
    story.append(Paragraph("Glossário rápido", ST["h1"]))
    story.append(Paragraph(
        "Para consultar quando precisar, sem reler o material inteiro.",
        ST["body_dim"]))
    story.append(Spacer(1, 0.4 * cm))

    glossary = [
        ("KB", "Knowledge Base — pasta curada com materiais da disciplina.",
         "<font name='Courier' color='#7CC4FF'>data/kb_ip/</font>"),
        ("Embedding", "Vetor numérico (384 floats) que representa o significado de um texto.",
         "saída do <font name='Courier' color='#7CC4FF'>sentence-transformers</font>"),
        ("Vector store", "Banco de dados especializado em guardar e buscar vetores por similaridade.",
         "ChromaDB, em <font name='Courier' color='#7CC4FF'>data/chroma/</font>"),
        ("ChromaDB", "Biblioteca Python de vector store, persiste em disco, sem servidor.",
         "usado pelo indexador e retriever"),
        ("Chunk", "Pedaço de texto (~2000 chars) com metadata fonte e chunk_idx.",
         "saída de <font name='Courier' color='#7CC4FF'>indexador.chunkar()</font>"),
        ("Overlap", "Repetição entre chunks vizinhos (200 chars) para não cortar frases.",
         "parâmetro <font name='Courier' color='#7CC4FF'>OVERLAP_CHARS</font>"),
        ("Cosine similarity", "Medida de &quot;quão na mesma direção&quot; dois vetores apontam (0 a 1).",
         '<font name="Courier" color="#7CC4FF">metadata={"hnsw:space": "cosine"}</font>'),
        ("Top-k", "Os k chunks mais próximos da query.",
         "<font name='Courier' color='#7CC4FF'>TOP_K = 3</font> no retriever"),
        ("Boost por metadata", "Peso extra somado à similaridade conforme o tipo do documento.",
         "<font name='Courier' color='#7CC4FF'>PESOS_TIPO</font> no retriever"),
        ("RAG", "Retrieval-Augmented Generation — buscar antes de gerar.",
         "<font name='Courier' color='#7CC4FF'>_montar_messages()</font> injeta KB no prompt"),
        ("Indexador", "Script offline que popula o ChromaDB.",
         "<font name='Courier' color='#7CC4FF'>python -m src.rag.indexador</font>"),
        ("Retriever", "Módulo online que busca chunks relevantes por query.",
         "<font name='Courier' color='#7CC4FF'>retriever.buscar(query)</font>"),
    ]
    gl_rows = [[Paragraph("TERMO", ST["cell_h"]),
                Paragraph("O QUE É", ST["cell_h"]),
                Paragraph("ONDE APARECE NO MARC.IA", ST["cell_h"])]]
    for term, what, where in glossary:
        gl_rows.append([
            Paragraph(f'<font color="#F5C518" name="Helvetica-Bold">{term}</font>', ST["cell"]),
            Paragraph(what, ST["cell"]),
            Paragraph(where, ST["cell"]),
        ])
    gt = Table(gl_rows, colWidths=[3.2 * cm, 7.0 * cm, 5.8 * cm])
    gt.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), BG_DEEPER),
        ("BACKGROUND", (0, 1), (-1, -1), BG_TABLE),
        ("LINEBELOW", (0, 0), (-1, -1), 0.3, LINE),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    story.append(gt)

    # tabela-resumo final
    story.append(Spacer(1, 0.5 * cm))
    story.append(Paragraph("TABELA-RESUMO — QUAL PERGUNTA CADA CONCEITO RESPONDE",
                           ST["tag_lbl"]))
    story.append(Spacer(1, 0.3 * cm))
    summary = [
        [Paragraph("CONCEITO", ST["cell_h"]),
         Paragraph("PERGUNTA QUE RESPONDE", ST["cell_h"]),
         Paragraph("EXEMPLO NO MARC.IA", ST["cell_h"])],
        [Paragraph('<font color="#F26B3A" name="Helvetica-Bold">KB</font>', ST["cell"]),
         Paragraph("De onde vem o material que o tutor pode citar?", ST["cell"]),
         Paragraph("<font name='Courier' color='#7CC4FF'>data/kb_ip/02_aulas/Aula3_Vetores_Matrizes.md</font>", ST["cell"])],
        [Paragraph('<font color="#2DD4BF" name="Helvetica-Bold">Embedding</font>', ST["cell"]),
         Paragraph('Como o computador compara "recursão" com "loop"?', ST["cell"]),
         Paragraph("Vetor 384-d de <font name='Courier' color='#7CC4FF'>&quot;como somar matrizes&quot;</font>", ST["cell"])],
        [Paragraph('<font color="#4F9CF9" name="Helvetica-Bold">ChromaDB</font>', ST["cell"]),
         Paragraph("Onde esses vetores ficam guardados?", ST["cell"]),
         Paragraph("Coleção <font name='Courier' color='#7CC4FF'>kb_ip</font> em <font name='Courier' color='#7CC4FF'>data/chroma/</font>", ST["cell"])],
        [Paragraph('<font color="#F5C518" name="Helvetica-Bold">Chunking</font>', ST["cell"]),
         Paragraph("Como um arquivo grande vira pedaço pesquisável?", ST["cell"]),
         Paragraph("Slide de 8 páginas → 12 chunks de 2000 chars", ST["cell"])],
        [Paragraph('<font color="#F5C518" name="Helvetica-Bold">Retriever</font>', ST["cell"]),
         Paragraph("Qual pedaço da KB responde esta pergunta?", ST["cell"]),
         Paragraph('Top-3 da busca por "MDC portugol"', ST["cell"])],
        [Paragraph('<font color="#E5484D" name="Helvetica-Bold">RAG</font>', ST["cell"]),
         Paragraph("Como esse pedaço chega até o modelo?", ST["cell"]),
         Paragraph("Cola no <font name='Courier' color='#7CC4FF'>[Contexto relevante da KB]</font> antes da pergunta", ST["cell"])],
    ]
    st = Table(summary, colWidths=[2.8 * cm, 5.5 * cm, 7.7 * cm])
    st.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), BG_DEEPER),
        ("BACKGROUND", (0, 1), (-1, -1), BG_TABLE),
        ("LINEBELOW", (0, 0), (-1, -1), 0.3, LINE),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    story.append(st)

    story.append(Spacer(1, 0.8 * cm))
    story.append(divider())
    story.append(Spacer(1, 0.4 * cm))
    story.append(Paragraph(
        '<i>&quot;KB é o material. RAG é o ritual de consultar esse '
        'material antes de falar. Embeddings e ChromaDB são a tecnologia '
        'que faz o ritual funcionar rápido.&quot;</i>',
        S("quote", fontSize=11, leading=16, textColor=TEXT_DIM)))
    story.append(Spacer(1, 0.2 * cm))
    story.append(Paragraph(
        "Victor Almeida · IA aplicada — material de apoio · jul/2026",
        S("body_dim", fontSize=9, textColor=TEXT_MUTED, alignment=TA_CENTER)))

    doc.build(story)
    print(f"[OK] PDF gerado em: {OUT_PDF}")
    return OUT_PDF


if __name__ == "__main__":
    build()