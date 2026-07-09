"""
Indexa os TXTs/MDs de data/kb_ip/ no ChromaDB usando sentence-transformers.
Chunka cada arquivo em pedaços de ~500 tokens com overlap de 50.

Para cada arquivo, detecta o `tipo` e a `etapa` (via path + frontmatter YAML) e
persiste como metadata. O retriever usa esses campos diretamente — sem heurística
de substring por nome de arquivo.

Uso direto: python -m src.rag.indexador [--forcar]
"""

import os
import re
import hashlib
import chromadb
from sentence_transformers import SentenceTransformer

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
KB_DIR = os.path.join(BASE_DIR, "data", "kb_ip")
CHROMA_DIR = os.path.join(BASE_DIR, "data", "chroma")

MODELO_EMBED = "all-MiniLM-L6-v2"
CHUNK_TOKENS = 500   # aprox. caracteres / 4
OVERLAP_TOKENS = 50
CHUNK_CHARS = CHUNK_TOKENS * 4
OVERLAP_CHARS = OVERLAP_TOKENS * 4

COLLECTION_NAME = "kb_ip"


def chunkar(texto: str, fonte: str) -> list[dict]:
    """Divide texto em chunks com overlap. Retorna lista de dicts com text e metadata."""
    chunks = []
    inicio = 0
    idx = 0
    while inicio < len(texto):
        fim = min(inicio + CHUNK_CHARS, len(texto))
        trecho = texto[inicio:fim].strip()
        if trecho:
            chunks.append({
                "text": trecho,
                "fonte": fonte,
                "chunk_idx": idx,
            })
            idx += 1
        if fim == len(texto):
            break
        inicio = fim - OVERLAP_CHARS
    return chunks


def id_chunk(fonte: str, idx: int) -> str:
    h = hashlib.md5(f"{fonte}:{idx}".encode()).hexdigest()[:8]
    return f"{h}_{idx}"


# --- Detecção de tipo/etapa ---------------------------------------------

# Regras de path -> tipo canônico. Ordem importa (mais específica primeiro).
_REGRAS_TIPO_PATH = [
    (r"00_meta[\\/].*skill", "guia_pedagogico"),
    (r"00_meta[\\/]", "guia_pedagogico"),
    (r"04_provas[\\/]", "prova"),
    (r"03_livros[\\/]", "livro_referencia_podado"),
    (r"02_aulas[\\/]", "slide_ou_roteiro"),
    (r"01_listas[\\/].*consolidadas", "resolucao_aluno"),
    (r"01_listas[\\/]", "lista_exercicios"),
]

_FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def _parse_frontmatter(texto: str) -> dict:
    """Extrai um dict simples do frontmatter YAML (apenas linhas `chave: valor`)."""
    m = _FRONTMATTER_RE.match(texto)
    if not m:
        return {}
    bloco = m.group(1)
    out = {}
    for linha in bloco.splitlines():
        if ":" not in linha:
            continue
        k, _, v = linha.partition(":")
        out[k.strip()] = v.strip()
    return out


def detectar_tipo(fonte: str, front: dict) -> str:
    """Decide o tipo de documento pelo caminho (e confirma com frontmatter se houver)."""
    fonte_norm = fonte.replace("\\", "/")
    # Primeiro, tenta inferir pelo frontmatter
    fm_tipo = front.get("tipo")
    if fm_tipo and fm_tipo not in ("slide_ou_roteiro", ""):
        # aceita tipo declarado no YAML quando não é genérico
        return fm_tipo
    # Senão, pelas regras de path
    for pattern, tipo in _REGRAS_TIPO_PATH:
        if re.search(pattern, fonte_norm):
            return tipo
    return "desconhecido"


def detectar_etapa(fonte: str, front: dict) -> int | None:
    """Decide a etapa (1=Portugol, 2=Python) pelo frontmatter ou pelo path."""
    fm_etapa = front.get("etapa")
    if fm_etapa and fm_etapa.isdigit():
        return int(fm_etapa)
    # Heurística de path
    f = fonte.lower()
    if "python" in f or "lista5" in f:
        return 2
    if "portugol" in f or "vetor" in f or "matriz" in f or "lista1" in f or "lista2" in f or "lista3" in f:
        return 1
    return None


# --- Indexação ----------------------------------------------------------

def indexar(forcar: bool = False):
    """Indexa todos os TXTs/MDs da KB no ChromaDB. Pula arquivos já indexados."""
    modelo = SentenceTransformer(MODELO_EMBED)

    client = chromadb.PersistentClient(path=CHROMA_DIR)

    if forcar:
        try:
            client.delete_collection(COLLECTION_NAME)
        except Exception:
            pass

    collection = client.get_or_create_collection(
        name=COLLECTION_NAME,
        metadata={"hnsw:space": "cosine"},
    )

    ids_existentes = set(collection.get()["ids"])

    arquivos = [
        os.path.join(raiz, f)
        for raiz, _, files in os.walk(KB_DIR)
        for f in files
        if f.endswith(".txt") or f.endswith(".md") or f.endswith(".visualg") or f.endswith(".por") or f.endswith(".py")
    ]

    total_chunks = 0
    for caminho in arquivos:
        fonte = os.path.relpath(caminho, KB_DIR)
        with open(caminho, "r", encoding="utf-8") as fh:
            texto = fh.read()

        front = _parse_frontmatter(texto)
        tipo = detectar_tipo(fonte, front)
        etapa = detectar_etapa(fonte, front)

        chunks = chunkar(texto, fonte)
        novos = [c for c in chunks if id_chunk(c["fonte"], c["chunk_idx"]) not in ids_existentes]

        if not novos:
            continue

        textos = [c["text"] for c in novos]
        embeddings = modelo.encode(textos, show_progress_bar=False).tolist()
        ids = [id_chunk(c["fonte"], c["chunk_idx"]) for c in novos]
        metadatas = [
            {
                "fonte": c["fonte"],
                "chunk_idx": c["chunk_idx"],
                "tipo": tipo,
                "etapa": etapa if etapa is not None else -1,
            }
            for c in novos
        ]

        collection.add(
            ids=ids,
            embeddings=embeddings,
            documents=textos,
            metadatas=metadatas,
        )
        total_chunks += len(novos)
        print(f"  [OK] {fonte} — tipo={tipo} etapa={etapa} — {len(novos)} chunks")

    print(f"\nTotal indexado: {total_chunks} chunks novos")
    print(f"Total na coleção: {collection.count()}")
    return collection


if __name__ == "__main__":
    import sys
    forcar = "--forcar" in sys.argv
    indexar(forcar=forcar)
