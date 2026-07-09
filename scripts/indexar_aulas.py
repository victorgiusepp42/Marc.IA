"""
Copia AULAS extraídas pra data/kb_ip/02_aulas/ com metadata YAML.
Mapping manual baseado nos nomes dos arquivos.
"""
import re
from pathlib import Path
import shutil

ROOT = Path("C:/Users/victo/Projetos/Marc.IA")
SRC = ROOT / "data/_extracao/AULAS"
DST = ROOT / "data/kb_ip/02_aulas"
DST.mkdir(parents=True, exist_ok=True)


def detect_kind(filename: str) -> tuple[str, int, str]:
    """Retorna (tipo, etapa, topico) baseado no nome."""
    f = filename.lower()

    # Tipo primário
    if "prova" in f:
        tipo = "prova"
    elif "trabalho" in f:
        tipo = "especificacao_trabalho"
    elif "lista" in f:
        tipo = "lista_exercicios"
    elif "exercicio" in f:
        tipo = "lista_exercicios"
    elif "especific" in f:
        tipo = "especificacao"
    else:
        tipo = "slide_ou_roteiro"

    # Etapa
    if any(k in f for k in ["portugol", "algoritmos", "decisao", "repeticao", "vetores", "matrizes", "revisao_algoritmos"]):
        etapa = 1
    elif any(k in f for k in ["python", "variaveis_expressoes", "funcoes_python", "cap5_condicionais_recursividade",
                               "cap6_funcoes_com_resultado", "cap7_iteracao", "cap8_strings",
                               "cap10", "cap11", "cap12", "cap14_arquivos", "intro_aula1"]):
        etapa = 2
    elif "apresenta" in f or "fundamentos_computacao" in f:
        etapa = 0  # geral / introdução
    else:
        etapa = 0

    # Tópico aproximado (heurística)
    if "vetor" in f or "matriz" in f or "lista" in f:
        topico = "vetores_matrizes_listas"
    elif "funcoes_recursivas" in f or "cap6" in f or "cap3_funcoes_python" in f:
        topico = "funcoes"
    elif "condicionais" in f or "decisao" in f:
        topico = "condicionais"
    elif "repeticao" in f or "iteracao" in f or "cap5" in f:
        topico = "repeticao_recursao"
    elif "strings" in f or "cap8" in f:
        topico = "strings"
    elif "dicionarios" in f or "tuplas" in f or "cap10" in f or "cap11" in f or "cap12" in f:
        topico = "dicionarios_tuplas"
    elif "arquivos" in f or "cap14" in f:
        topico = "arquivos"
    elif "variaveis" in f:
        topico = "variaveis_expressoes"
    elif "introducao" in f or "fundamentos" in f or "apresenta" in f:
        topico = "introducao"
    else:
        topico = "geral"

    return tipo, etapa, topico


def main():
    files = sorted(SRC.glob("*.txt"))
    total = 0
    print(f"Encontrados {len(files)} arquivos em {SRC}")

    for src_file in files:
        if src_file.stat().st_size < 500:  # ignora vazios / quase vazios
            print(f"  SKIP (vazio): {src_file.name}")
            continue
        nome_limpo = re.sub(r"\s*\([0-9]+\)", "", src_file.stem).strip()
        nome_final = re.sub(r"[^A-Za-z0-9_.]+", "_", nome_limpo) + ".md"
        tipo, etapa, topico = detect_kind(src_file.name)

        texto = src_file.read_text(encoding="utf-8")
        header = f'''---
tipo: {tipo}
etapa: {etapa}
topico: {topico}
fonte: docs/materiais_kb/AULAS/{src_file.name}
data_processamento: 2026-07-04
autor_original: Prof. Dr. Márcio de Souza Dias (UFCAT/IMTec)
status: extraido_pdf_bruto
ordem_aula: '{re.search(r"\d+", src_file.stem).group() if re.search(r"\\d+", src_file.stem) else "0"}'
observacao: Texto extraído automaticamente do PDF; revisar figuras/diagramas que não vieram.
---

# {nome_limpo}

'''

        dst_file = DST / nome_final
        dst_file.write_text(header + texto, encoding="utf-8")
        total += 1
        print(f"  OK: {nome_final} (tipo={tipo}, etapa={etapa}, topico={topico})")

    print(f"\nTotal: {total} arquivos salvos em {DST}")


if __name__ == "__main__":
    main()
