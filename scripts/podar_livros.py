"""
Poda livros - versão 3.
Fundamentos: usa o cabeçalho "Capítulo N NomeDoCap | página" presente em cada página.
Pense em Python: usa padrão "Capítulo N\n\nTítulo" (mais simples, sem header repetido).
"""
import re
from pathlib import Path

ROOT = Path("C:/Users/victo/Projetos/Marc.IA")
SRC = ROOT / "data/_extracao/LIVROS"
DST = ROOT / "data/_extracao/LIVROS_PODADOS"


def split_pages(texto: str) -> list[str]:
    return [p.strip() for p in texto.split("===PAGE_BREAK===")]


def fund_chapter_map(pages: list[str]) -> dict[int, list[str]]:
    """Pega páginas onde aparece 'Capítulo N NomeDoCap | página'."""
    chap_re = re.compile(r"Capítulo\s+(\d+)\s+([^|]+?)\s*\|\s*\d+", re.UNICODE)
    result = {i: [] for i in range(1, 14)}
    for p in pages:
        m = chap_re.search(p)
        if m:
            num = int(m.group(1))
            if num in result:
                result[num].append(p)
    return result


def pense_chapter_map(pages: list[str]) -> dict[int, list[str]]:
    """Pense em Python: cabeçalho do cap aparece dentro do sumário na primeira página.
    Distribui páginas pelo número do capítulo atual — a primeira página do cap é a do sumário,
    e as seguintes até o próximo 'Capítulo N' são as dele."""
    chap_re = re.compile(r"^Capítulo\s+(\d+)\s*$", re.MULTILINE)
    numbered = []
    for idx, p in enumerate(pages):
        # procura "Capítulo N" como linha isolada
        matches = chap_re.findall(p)
        if matches:
            for num_str in matches:
                numbered.append((int(num_str), idx))
    # Agora pra cada cap, achar intervalo
    result = {i: [] for i in range(1, 22)}
    # Simplificação: pra cada cap alvo, achar primeiro e próximo, pegar páginas entre eles
    targets = [1, 2, 3, 5, 6, 7, 8, 10, 11, 12, 14]
    cap_starts = {}
    for idx, p in enumerate(pages):
        for ln in p.split("\n"):
            m = chap_re.match(ln.strip())
            if m:
                cap_num = int(m.group(1))
                if cap_num not in cap_starts:
                    cap_starts[cap_num] = idx

    for n in targets:
        if n not in cap_starts:
            continue
        start = cap_starts[n]
        # acha próximo cap > n
        next_starts = [s for c, s in cap_starts.items() if c > n]
        end = min(next_starts) if next_starts else len(pages)
        for idx in range(start, end):
            result[n].append(pages[idx])
    return result


def extract_intro(pages: list[str], n: int = 25) -> list[str]:
    return pages[:n]


def podar_fundamentos():
    src = SRC / "Fundamentos_da_PROGRAMACAO_de.txt"
    pages = split_pages(src.read_text(encoding="utf-8"))
    print(f"  Total páginas Fundamentos: {len(pages)}")

    cm = fund_chapter_map(pages)
    KEEP = [1, 3, 4, 5, 6, 7, 8]

    parts = ["=== INTRODUÇÃO (capa + sumário + prefácio) ==="]
    parts.extend(extract_intro(pages, 25))
    for n in KEEP:
        if cm[n]:
            parts.append(f"\n\n=== CAPÍTULO {n} ===")
            parts.extend(cm[n])
            print(f"  Cap {n}: {len(cm[n])} páginas")

    out = "\n\n---\n\n".join(parts)
    dst = DST / "fundamentos_programacao_podado.txt"
    DST.mkdir(parents=True, exist_ok=True)
    dst.write_text(out, encoding="utf-8")
    return len(out)


def podar_pense_python():
    src = SRC / "Pense_em_Python_-_Allen_B._Downey.txt"
    pages = split_pages(src.read_text(encoding="utf-8"))
    print(f"  Total páginas Pense Python: {len(pages)}")

    cm = pense_chapter_map(pages)
    KEEP = [1, 2, 3, 5, 6, 7, 8, 10, 11, 12, 14]

    parts = ["=== INTRODUÇÃO (capa + prefácio + sumário) ==="]
    parts.extend(extract_intro(pages, 25))
    for n in KEEP:
        if cm[n]:
            parts.append(f"\n\n=== CAPÍTULO {n} ===")
            parts.extend(cm[n])
            print(f"  Cap {n}: {len(cm[n])} páginas")

    out = "\n\n---\n\n".join(parts)
    dst = DST / "pense_em_python_podado.txt"
    dst.write_text(out, encoding="utf-8")
    return len(out)


def main():
    if DST.exists():
        import shutil
        shutil.rmtree(DST)
    DST.mkdir(parents=True, exist_ok=True)

    print("=" * 50)
    print("PODA DE LIVROS v3 — KB Marc.IA")
    print("=" * 50)

    print("\n[1] Fundamentos da Programação...")
    sz1 = podar_fundamentos()
    print(f"  OK: {sz1//1024}KB")

    print("\n[2] Pense em Python...")
    sz2 = podar_pense_python()
    print(f"  OK: {sz2//1024}KB")

    print(f"\nResumo: Fundamentos={sz1//1024}KB / Pense Python={sz2//1024}KB")


if __name__ == "__main__":
    main()
