"""
Benchmark de max_tokens para o Marc.IA.

Roda o mesmo conjunto de prompts com diferentes limites de max_tokens e
coleta métricas pra tabela de decisão:
- tempo médio de resposta
- stop_reason (end_turn = OK; max_tokens = truncou, ERRO funcional)
- tokens input/output
- custo estimado USD

Uso: python scripts/benchmark_tokens.py
"""

import json
import os
import sys
import time
from statistics import mean

# Adiciona raiz do projeto ao path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.agente_ip import AgenteIP


# Preços Opus 4.8 (janeiro 2026, em USD por milhão de tokens)
PRICE_INPUT_PER_M = 15.0
PRICE_OUTPUT_PER_M = 75.0

# Limites a testar
LIMITES = [4096, 6144, 8192, 10240, 12288, 16384]

# Prompts de stress test (complexidade crescente)
PROMPTS = [
    {
        "nome": "Saudacao",
        "mensagem": "Oi, tudo bem?",
        "esperado": "curta",
    },
    {
        "nome": "Conceitual medio",
        "mensagem": "Explica listas em Python com 2 exemplos praticos, e me da um desafio curto no final.",
        "esperado": "media",
    },
    {
        "nome": "Analise codigo longo",
        "mensagem": (
            "Analisa esse codigo e me explica o que acontece linha por linha, "
            "identifica bugs e sugere melhorias: "
            "def calcular_media(notas):\n"
            "    soma = 0\n"
            "    for n in notas:\n"
            "        soma += n\n"
            "    return soma / len(notas)\n"
            "\n"
            "notas = [8, 7, 9, 6, 10]\n"
            "media = calcular_media(notas)\n"
            "print('Media:', media)\n"
            "print('Notas acima da media:')\n"
            "for n in notas:\n"
            "    if n > media:\n"
            "        print(n)"
        ),
        "esperado": "longa",
    },
    {
        "nome": "Exercicio guiado",
        "mensagem": "Me da um exercicio de Portugol sobre estrutura de repeticao, do nivel iniciante. Nao me da a resposta, so o enunciado e uma pergunta pra eu comecar.",
        "esperado": "media",
    },
]


def run_one(agente, mensagem, max_tokens):
    """Roda UM prompt com UM max_tokens. Retorna dict com métricas."""
    import src.agente_base as ab
    original = ab.MODEL_TIERS["complexo"]["max_tokens"]
    ab.MODEL_TIERS["complexo"]["max_tokens"] = max_tokens

    cliente = agente._active["client"]
    modelo = agente._active["model"]

    # System prompt é só o do AgenteIP (sem histórico de sessão)
    system = agente.system_prompt
    messages = [{"role": "user", "content": mensagem}]

    t0 = time.time()
    try:
        response = cliente.messages.create(
            model=modelo,
            max_tokens=max_tokens,
            system=system,
            messages=messages,
        )
        elapsed = time.time() - t0
        texto = response.content[0].text if response.content else ""
        stop_reason = response.stop_reason
        usage = response.usage
        return {
            "ok": True,
            "elapsed_s": elapsed,
            "stop_reason": stop_reason,
            "truncated": stop_reason == "max_tokens",
            "input_tokens": usage.input_tokens if usage else 0,
            "output_tokens": usage.output_tokens if usage else 0,
            "response_chars": len(texto),
        }
    except Exception as e:
        return {
            "ok": False,
            "elapsed_s": time.time() - t0,
            "error": str(e)[:200],
        }
    finally:
        ab.MODEL_TIERS["complexo"]["max_tokens"] = original


def main():
    print("=" * 70)
    print("BENCHMARK max_tokens — Marc.IA / AgenteIP")
    print("=" * 70)

    agente = AgenteIP()
    print("Modelo:", agente._active["model"])
    resultados = []

    for max_tokens in LIMITES:
        print(f"\n>>> max_tokens = {max_tokens}")
        for prompt in PROMPTS:
            results = []
            for tentativa in range(2):
                r = run_one(agente, prompt["mensagem"], max_tokens)
                results.append(r)
                if r["ok"]:
                    print(f"  [{prompt['nome']}] t{tentativa+1}: "
                          f"{r['elapsed_s']:.2f}s stop={r['stop_reason']} "
                          f"out={r['output_tokens']} trunc={r['truncated']}")
                else:
                    print(f"  [{prompt['nome']}] t{tentativa+1}: ERRO {r['error']}")

            successes = [r for r in results if r.get("ok")]
            if successes:
                avg_time = mean(r["elapsed_s"] for r in successes)
                avg_out = mean(r["output_tokens"] for r in successes)
                avg_in = mean(r["input_tokens"] for r in successes)
                truncados = sum(1 for r in successes if r["truncated"])
                custo = (avg_in / 1e6) * PRICE_INPUT_PER_M + \
                        (avg_out / 1e6) * PRICE_OUTPUT_PER_M
            else:
                avg_time = avg_out = avg_in = custo = 0
                truncados = 0

            resultados.append({
                "max_tokens": max_tokens,
                "prompt": prompt["nome"],
                "esperado": prompt["esperado"],
                "sucessos": len(successes),
                "erros": 2 - len(successes),
                "truncados": truncados,
                "taxa_truncamento_%": round(100 * truncados / max(len(successes), 1), 1),
                "tempo_medio_s": round(avg_time, 2),
                "tokens_input_medio": int(avg_in),
                "tokens_output_medio": int(avg_out),
                "custo_medio_usd": round(custo, 5),
            })

    # Tabela
    print("\n" + "=" * 70)
    print("TABELA CONSOLIDADA")
    print("=" * 70)
    cols = ["max_tokens", "prompt", "esperado", "sucessos", "erros", "truncados",
            "taxa_truncamento_%", "tempo_medio_s", "tokens_input_medio",
            "tokens_output_medio", "custo_medio_usd"]
    print(" | ".join(f"{c:>16}" for c in cols))
    print("-" * (19 * len(cols)))
    for r in resultados:
        print(" | ".join(f"{str(r[c]):>16}" for c in cols))

    # Salva JSON
    out_path = os.path.join("data", "benchmark_resultados.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(resultados, f, indent=2, ensure_ascii=False)
    print(f"\nResultados salvos em {out_path}")

    # Resumo por max_tokens
    print("\n" + "=" * 70)
    print("RESUMO POR LIMITE")
    print("=" * 70)
    by_limit = {}
    for r in resultados:
        by_limit.setdefault(r["max_tokens"], []).append(r)
    for lim in sorted(by_limit.keys()):
        items = by_limit[lim]
        trunc_total = sum(i["truncados"] for i in items)
        ok_total = sum(i["sucessos"] for i in items)
        err_total = sum(i["erros"] for i in items)
        taxa = 100 * trunc_total / max(ok_total, 1)
        custo = sum(i["custo_medio_usd"] for i in items) / len(items)
        tempo = mean(i["tempo_medio_s"] for i in items)
        print(f"max_tokens={lim:>5}: trunc={trunc_total}/{ok_total} ({taxa:.0f}%) "
              f"err={err_total} tempo={tempo:.2f}s custo=${custo:.5f}")


if __name__ == "__main__":
    main()