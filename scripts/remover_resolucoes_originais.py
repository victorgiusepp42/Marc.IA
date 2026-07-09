"""
Remove os arquivos curtos originais em resolucoes_aluno/ (consolidados em arquivos _resolucoes_consolidadas.md).
"""
from pathlib import Path

ROOT = Path("C:/Users/victo/Projetos/Marc.IA")
BASE = ROOT / "data/kb_ip/01_listas"

LISTAS = [
    "lista1_portugol",
    "lista2_portugol",
    "lista3_vetores_matrizes",
    "lista5_python",
]

EXT = {".visualg", ".por", ".py"}

total = 0
for lista in LISTAS:
    pasta = BASE / lista / "resolucoes_aluno"
    if not pasta.exists():
        continue
    for f in pasta.iterdir():
        if f.is_file() and f.suffix.lower() in EXT:
            f.unlink()
            total += 1

print(f"{total} arquivos removidos em resolucoes_aluno/")