"""
Busca semântica top-k na KB indexada no ChromaDB.
Carrega o modelo e a coleção uma vez (singleton) para evitar overhead por query.

Adiciona **boost por metadata**: depois do embedding, prioriza chunks cujo
metadata `tipo` bate com pesos configuráveis. O `tipo` e a `etapa` são
preenchidos pelo `indexador.py` no momento da indexação (via path + frontmatter),
então o retriever não depende mais de substring por nome de arquivo.

Isso é necessário porque o embedding model (MiniLM) não distingue bem entre
"exercício X" e "explicação sobre X" — sem o boost, o retriever puxa o livro
didático antes da lista de exercícios, mesmo quando a query é específica.
"""

import os
import chromadb
from sentence_transformers import SentenceTransformer

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CHROMA_DIR = os.path.join(BASE_DIR, "data", "chroma")

MODELO_EMBED = "all-MiniLM-L6-v2"
COLLECTION_NAME = "kb_ip"
TOP_K = 3
TOP_K_INICIAL = 12  # pega mais do que k pra poder reordenar com boost

# Boost por tipo de documento (quanto maior, mais no topo).
# Foco da KB é "exercícios do jeito do Prof." > "aulas do Prof." > "livros didáticos"
PESOS_TIPO = {
    "lista_exercicios": 1.0,
    "prova": 0.9,
    "especificacao_trabalho": 0.85,
    "slide_ou_roteiro": 0.7,        # aula do Prof.
    "resolucao_aluno": 0.6,
    "livro_referencia_podado": 0.5,  # livro didático (mais largo, menos alinhado)
    "guia_pedagogico": 1.2,          # regras de estilo (sempre relevante quando aluno pede exemplo)
    "relatorio_correcao": 1.0,
    "nota_pendencia": 0.3,
    None: 0.5,                       # sem tipo definido
}

# Boost por etapa — quando a query indica Portugol, prioriza etapa 1; quando Python, etapa 2
# Detecção simples via palavras-chave (heurística barata, não-LLM)
MAPA_KEYWORDS_ETAPA = {
    # etapa: palavras-chave
    1: ["portugol", "visuAlg", "algoritmo", "vetor", "matriz", "repita", "para", "caso selecione",
        "enquanto", "variavel", "mod", "resto", "divisao inteira"],
    2: ["python", "input", "print", "f-string", "lista", "tupla", "dicionario", "string",
        "arquivo", "recursao", "recurso", "lambda", "decorador", "classe", "objeto"],
}


def _detectar_etapa_da_query(query: str) -> int | None:
    q = query.lower()
    pts1 = sum(1 for kw in MAPA_KEYWORDS_ETAPA[1] if kw in q)
    pts2 = sum(1 for kw in MAPA_KEYWORDS_ETAPA[2] if kw in q)
    if pts1 > pts2 and pts1 >= 1:
        return 1
    if pts2 > pts1 and pts2 >= 1:
        return 2
    return None


# singletons — inicializados na primeira chamada
_modelo = None
_collection = None


def _carregar():
    global _modelo, _collection
    if _modelo is None:
        _modelo = SentenceTransformer(MODELO_EMBED)
    if _collection is None:
        client = chromadb.PersistentClient(path=CHROMA_DIR)
        _collection = client.get_or_create_collection(
            name=COLLECTION_NAME,
            metadata={"hnsw:space": "cosine"},
        )


def _score(dist: float, tipo: str | None, etapa: int | None, etapa_query: int | None) -> float:
    """Combina distância do embedding com pesos de metadata.
    Embedding distance é cosseno (menor = melhor). Boost adiciona offset.
    """
    base = 1.0 - dist  # converte para "similaridade" (maior = melhor)
    boost = PESOS_TIPO.get(tipo, 0.5)
    if etapa_query is not None and etapa == etapa_query:
        boost += 0.4   # prioriza a etapa da query
    return base + boost


def buscar(query: str, top_k: int = TOP_K) -> list[str]:
    """Retorna os top-k chunks mais relevantes para a query, com boost por metadata."""
    _carregar()

    if _collection.count() == 0:
        return []

    embedding = _modelo.encode([query]).tolist()
    # Pega mais do que k pra permitir reordenação por boost
    n = min(TOP_K_INICIAL, _collection.count())
    resultados = _collection.query(
        query_embeddings=embedding,
        n_results=n,
        include=["documents", "metadatas", "distances"],
    )

    docs = resultados.get("documents", [[]])[0]
    metas = resultados.get("metadatas", [[]])[0]
    dists = resultados.get("distances", [[]])[0]

    etapa_query = _detectar_etapa_da_query(query)

    scored = []
    for doc, meta, dist in zip(docs, metas, dists):
        # Lê tipo/etapa direto do metadata (preenchido pelo indexador).
        tipo = None
        etapa = None
        if meta:
            tipo_meta = meta.get("tipo")
            if tipo_meta and tipo_meta != "desconhecido":
                tipo = tipo_meta
            etapa_meta = meta.get("etapa")
            if isinstance(etapa_meta, int) and etapa_meta >= 0:
                etapa = etapa_meta
        s = _score(dist, tipo, etapa, etapa_query)
        scored.append((s, doc, meta, fonte := meta.get("fonte", "") if meta else ""))

    scored.sort(key=lambda x: x[0], reverse=True)

    out = []
    for _, doc, meta, fonte in scored[:top_k]:
        out.append(f"[{fonte}]\n{doc}")
    return out
