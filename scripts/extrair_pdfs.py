"""
Script único de extração de texto dos PDFs da KB.
Lê todos os PDFs em docs/materiais_kb/AULAS/ e salva texto bruto em data/_extracao/AULAS/.
Para livros_referencia/, salva em data/_extracao/LIVROS/.
"""
import os
import sys
from pathlib import Path
from pypdf import PdfReader

ROOT = Path("C:/Users/victo/Projetos/Marc.IA")
SRC_AULAS = ROOT / "docs/materiais_kb/AULAS"
SRC_LIVROS = ROOT / "docs/materiais_kb/livros_referencia"
DST_AULAS = ROOT / "data/_extracao/AULAS"
DST_LIVROS = ROOT / "data/_extracao/LIVROS"


def extrair(pdf_path: Path, dst_dir: Path) -> bool:
    """Extrai texto de um PDF e salva em .txt no destino."""
    name = pdf_path.stem
    txt_path = dst_dir / f"{name}.txt"
    try:
        reader = PdfReader(str(pdf_path))
        texto = []
        for page in reader.pages:
            try:
                t = page.extract_text() or ""
                if t.strip():
                    texto.append(t)
            except Exception as e:
                texto.append(f"\n[ERRO NA PÁGINA: {e}]\n")
        full = "\n\n===PAGE_BREAK===\n\n".join(texto)
        dst_dir.mkdir(parents=True, exist_ok=True)
        txt_path.write_text(full, encoding="utf-8")
        return True, len(texto)
    except Exception as e:
        return False, str(e)


def main():
    print("=" * 60)
    print("EXTRAÇÃO DE PDFs — KB Marc.IA")
    print("=" * 60)

    # AULAS
    print(f"\n[AULAS] Lendo de: {SRC_AULAS}")
    if not SRC_AULAS.exists():
        print(f"  Pasta não existe!")
        return
    DST_AULAS.mkdir(parents=True, exist_ok=True)
    sucessos_aulas = 0
    falhas_aulas = []
    for f in sorted(SRC_AULAS.iterdir()):
        if f.suffix.lower() != ".pdf":
            continue
        ok, info = extrair(f, DST_AULAS)
        if ok:
            print(f"  [OK] {f.name} ({info} páginas)")
            sucessos_aulas += 1
        else:
            print(f"  [FALHA] {f.name} — {info}")
            falhas_aulas.append((f.name, info))
    print(f"\n  AULAS: {sucessos_aulas} sucessos, {len(falhas_aulas)} falhas")

    # LIVROS
    print(f"\n[LIVROS] Lendo de: {SRC_LIVROS}")
    DST_LIVROS.mkdir(parents=True, exist_ok=True)
    sucessos_livros = 0
    falhas_livros = []
    for f in sorted(SRC_LIVROS.iterdir()):
        if f.suffix.lower() != ".pdf":
            continue
        ok, info = extrair(f, DST_LIVROS)
        if ok:
            print(f"  [OK] {f.name} ({info} páginas)")
            sucessos_livros += 1
        else:
            print(f"  [FALHA] {f.name} — {info}")
            falhas_livros.append((f.name, info))
    print(f"\n  LIVROS: {sucessos_livros} sucessos, {len(falhas_livros)} falhas")

    print("\n" + "=" * 60)
    print("RESUMO")
    print("=" * 60)
    print(f"Total extraído: {sucessos_aulas + sucessos_livros} PDFs")
    if falhas_aulas:
        print(f"Falhas em AULAS: {len(falhas_aulas)}")
        for n, e in falhas_aulas:
            print(f"  - {n}: {e}")
    if falhas_livros:
        print(f"Falhas em LIVROS: {len(falhas_livros)}")
        for n, e in falhas_livros:
            print(f"  - {n}: {e}")


if __name__ == "__main__":
    main()
