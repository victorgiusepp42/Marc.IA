"""
Consolida resoluções curtas de aluno (1 chunk cada) por lista,
gerando um único MD por lista em data/kb_ip/01_listas/<lista>/.
"""
from pathlib import Path

ROOT = Path("C:/Users/victo/Projetos/Marc.IA")
BASE = ROOT / "data/kb_ip/01_listas"

LISTAS = [
    ("lista1_portugol", 1),
    ("lista2_portugol", 1),
    ("lista3_vetores_matrizes", 1),
    ("lista5_python", 2),
]

EXT_LABEL = {".visualg": "Visualg", ".por": "Portugol Studio", ".py": "Python"}


def build(lista_nome: str, etapa: int) -> None:
    pasta = BASE / lista_nome / "resolucoes_aluno"
    if not pasta.exists():
        print(f"  SKIP {lista_nome}: pasta nao existe")
        return
    arquivos = sorted(
        f for f in pasta.iterdir()
        if f.suffix.lower() in EXT_LABEL
    )
    if not arquivos:
        print(f"  SKIP {lista_nome}: sem arquivos")
        return

    front = (
        "---\n"
        f"tipo: resolucao_aluno\n"
        f"etapa: {etapa}\n"
        f"lista: {lista_nome}\n"
        f"autor_original: Victor Giusepp Almeida\n"
        f"fonte_dir: 01_listas/{lista_nome}/resolucoes_aluno\n"
        f"data_processamento: 2026-07-05\n"
        f"status: consolidado\n"
        f"observacao: Resolucoes de Victor consolidadas para melhor retrieval (cada uma era 1 chunk de ~500 tokens).\n"
        "---\n\n"
        f"# Resolucoes — {lista_nome}\n\n"
        f"> Consolidado de {len(arquivos)} resolucoes do aluno. "
        "Cada resolucao e separada por `=== EX NN ===`.\n"
    )

    partes = [front]
    for i, arq in enumerate(arquivos, 1):
        conteudo = arq.read_text(encoding="utf-8").strip()
        label = EXT_LABEL[arq.suffix.lower()]
        partes.append(
            f"\n## === EX {i:02d}: {arq.stem} ({label}) ===\n\n"
            f"```\n{conteudo}\n```\n"
        )

    saida = pasta.parent / f"{lista_nome}_resolucoes_consolidadas.md"
    saida.write_text("".join(partes), encoding="utf-8")
    print(f"  OK {lista_nome}: {len(arquivos)} arquivos -> {saida.name} ({saida.stat().st_size} B)")


def main() -> None:
    print("Consolidando resolucoes por lista...")
    for nome, etapa in LISTAS:
        build(nome, etapa)


if __name__ == "__main__":
    main()