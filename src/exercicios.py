"""
exercicios.py — Catálogo estático e validador simples por similaridade.

Esqueleto FRO-05 (08/07/2026). Validação NÃO tenta executar o código —
só faz match de keywords normalizadas. É proposital: prioriza cobertura
rápida sobre correção semântica profunda. Próximas sprints podem
acoplar um sandbox pra portugol/python e validar saída real.

Reaproveita o padrão de cache em memória usado em `agente_base.py`
(_PLANO_CACHE): o JSON raramente muda no curto prazo e o custo de
recarregar é desprezível.
"""

import json
import os
import re
import unicodedata
from typing import Optional


# Caminho absoluto do JSON de exercícios — robusto a variações de cwd.
_CAMINHO_JSON = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "data", "exercicios.json"
)

_cache: Optional[list[dict]] = None


def _carregar() -> list[dict]:
    """Carrega (e cacheia) data/exercicios.json. Retorna lista de exercícios."""
    global _cache
    if _cache is None:
        with open(_CAMINHO_JSON, "r", encoding="utf-8") as f:
            _cache = json.load(f).get("exercicios", [])
    return _cache


def _normalizar(texto: str) -> str:
    """Lowercase + remove acentos + tira comentários de linha + colapsa whitespace.

    - `unicodedata.normalize("NFKD", ...)` separa 'á' em 'a' + combining acute.
    - Filtramos os combining chars pra remover acentos sem alterar letras.
    - Comentários `//` (portugol/c-style) e `#` (python/portugol) viram espaço
      pra keywords não casarem acidentalmente com texto comentado.
    - Não-alfanumérico vira espaço (mantém "f2f" coerente).
    """
    if not texto:
        return ""
    nfkd = unicodedata.normalize("NFKD", texto)
    sem_acentos = "".join(c for c in nfkd if not unicodedata.combining(c))
    sem_comentarios = re.sub(r"(//[^\n]*|#[^\n]*)", " ", sem_acentos)
    minusculo = sem_comentarios.lower()
    espacado = re.sub(r"[^a-z0-9]+", " ", minusculo)
    return re.sub(r"\s+", " ", espacado).strip()


def _keyword_presente(kw: str, texto_normalizado: str) -> bool:
    """Match de palavra inteira (\\b) — evita 'se' casar em 'segundo'."""
    padrao = r"\b" + re.escape(_normalizar(kw)) + r"\b"
    return re.search(padrao, texto_normalizado) is not None


def listar(topico_id: Optional[str] = None) -> list[dict]:
    """Lista exercícios, opcionalmente filtrando por topico_id."""
    exs = _carregar()
    if topico_id:
        return [e for e in exs if e.get("topico_id") == topico_id]
    return exs


def buscar(exercicio_id: str) -> Optional[dict]:
    """Busca exercício pelo id. Retorna None se não encontrar."""
    for ex in _carregar():
        if ex["id"] == exercicio_id:
            return ex
    return None


def validar(exercicio_id: str, resposta: str) -> tuple[bool, int, str, str]:
    """Valida resposta do aluno por similaridade de keywords.

    Retorna: (correta: bool, score: 0-100, feedback: str, gabarito_completo: str)

    Algoritmo:
      1. Normaliza a resposta do aluno.
      2. Conta keywords obrigatórias presentes (peso 70% do score).
      3. Soma desejáveis (peso 25%).
      4. Subtrai 30% por negativa detectada (limita a 0).
      5. correta = True ⇔ TODAS obrigatórias presentes E score >= 70.
      6. Feedback cita o que falta + linguagem esperada quando há cruzamento.

    Diferenciação portugol vs python:
      - Cada exercício traz `linguagem`. As `negativas` já filtram tokens
        da linguagem "errada" (ex: `def `, `if ` penalizam respostas em portugol).
      - Assim o aluno que responde python num exercício portugol recebe
        feedback orientando a trocar de linguagem.
    """
    ex = buscar(exercicio_id)
    if ex is None:
        return (
            False,
            0,
            f"Exercício '{exercicio_id}' não encontrado.",
            "",
        )

    resposta_norm = _normalizar(resposta or "")
    if not resposta_norm:
        return (
            False,
            0,
            "Resposta vazia. Tente novamente.",
            ex.get("gabarito_completo", ""),
        )

    criterios = ex.get("criterios_keywords", {})
    obrigatorias = criterios.get("obrigatorias", [])
    desejaveis = criterios.get("desejaveis", [])
    negativas = criterios.get("negativas", [])

    # Obrigatórias: peso 70%
    obrig_total = len(obrigatorias)
    obrig_ok = sum(1 for kw in obrigatorias if _keyword_presente(kw, resposta_norm))
    score_obrig = (obrig_ok / obrig_total) * 70 if obrig_total else 70

    # Desejáveis: peso 25%
    desej_total = len(desejaveis)
    desej_ok = sum(1 for kw in desejaveis if _keyword_presente(kw, resposta_norm))
    score_desej = (desej_ok / desej_total) * 25 if desej_total else 25

    # Negativas: –30% cada
    neg_penais = sum(1 for kw in negativas if _keyword_presente(kw, resposta_norm))

    score = max(0, min(100, int(score_obrig + score_desej - 30 * neg_penais)))

    todas_obrigatorias = obrig_ok == obrig_total
    correta = todas_obrigatorias and score >= 70

    # Feedback contextual
    if correta:
        feedback = (
            f"Boa! Score {score}/100. Resposta cobre os pontos esperados em {ex['linguagem']}."
        )
    else:
        partes = []
        if obrig_total and obrig_ok < obrig_total:
            faltam = [kw for kw in obrigatorias if not _keyword_presente(kw, resposta_norm)]
            partes.append(f"Faltam keywords essenciais: {', '.join(faltam)}")
        if neg_penais:
            partes.append(
                "Detectei tokens da linguagem errada — confirme se você respondeu em "
                + ex["linguagem"]
            )
        if not partes:
            partes.append(
                f"Quase lá (score {score}/100). Releia o enunciado e revise a estrutura."
            )
        feedback = " ".join(partes)

    return (correta, score, feedback, ex.get("gabarito_completo", ""))
