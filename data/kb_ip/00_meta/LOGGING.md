# Logging — Marc.IA

> Documentação do sistema de logs persistentes.
> Implementado em 2026-07-05 (decisão: SQLite, nível médio de detalhe).

---

## Onde os logs ficam

**`data/logs.db`** (SQLite) — engine **separado** do banco principal (`data/marcia.db`) via SQLAlchemy BIND_KEYS.

**Por que engine separado?**
- Logs nunca bloqueiam queries de aluno (sessão, perfil).
- Pode-se fazer backup/limpeza do `logs.db` sem tocar no banco principal.
- Tamanho do `logs.db` cresce rápido — manter isolado facilita manutenção.

---

## Schema

### Tabela `execucoes` (uma linha por chamada HTTP bem-sucedida)

| Coluna | Tipo | Descrição |
|---|---|---|
| `id` | INTEGER PK | Auto-incremento |
| `timestamp` | DATETIME | UTC, indexada |
| `usuario_id` | STRING(128) | Indexada |
| `mensagem_chars` | INTEGER | Tamanho da mensagem do aluno |
| `codigo_chars` | INTEGER | Tamanho do código anexado (0 se não enviou) |
| `linguagem` | STRING(16) | `python` ou `portugol` |
| `complexidade` | STRING(16) | `simples` ou `complexo` (saída da heurística) |
| `tier` | STRING(32) | `Opus 4.8 High` ou `Sonnet 4.6 Medium` |
| `perfil_topico` | STRING(256) | Tópico atual do perfil do aluno |
| `perfil_preferencias` | INTEGER | Quantidade de preferências declaradas |
| `perfil_topicos_explicados` | INTEGER | Quantidade de tópicos na lista do que tutor explicou |
| `xp_total` | INTEGER | XP do aluno após essa mensagem |
| `nivel` | INTEGER | Nível do aluno (1-4) após |
| `duracao_ms` | INTEGER | Tempo total da request em ms |
| `kb_chunks_usados` | INTEGER | Quantos chunks do RAG foram usados |

### Tabela `erros` (uma linha por exception capturada)

| Coluna | Tipo | Descrição |
|---|---|---|
| `id` | INTEGER PK | Auto-incremento |
| `timestamp` | DATETIME | UTC, indexada |
| `usuario_id` | STRING(128) | Se identificável |
| `endpoint` | STRING(64) | Rota que falhou (ex: `/chat`) |
| `erro_tipo` | STRING(64) | Nome da classe da exception (indexada) |
| `erro_mensagem` | STRING(500) | `str(e)` truncado |
| `traceback` | TEXT | Traceback completo, até 5KB |
| `contexto_json` | TEXT | JSON com variáveis relevantes (msg_chars, linguagem) |

---

## Queries úteis (rodar com `sqlite3 data/logs.db "..."`)

### Quantas chamadas por dia na última semana?
```sql
SELECT DATE(timestamp) AS dia, COUNT(*) AS chamadas
FROM execucoes
WHERE timestamp >= DATE('now', '-7 days')
GROUP BY dia ORDER BY dia;
```

### Distribuição de tier (Opus vs Sonnet) na última semana?
```sql
SELECT tier,
       COUNT(*) AS qtd,
       ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM execucoes WHERE timestamp >= DATE('now', '-7 days')), 1) AS pct
FROM execucoes
WHERE timestamp >= DATE('now', '-7 days')
GROUP BY tier;
```

### Quais erros aconteceram nas últimas 24h?
```sql
SELECT erro_tipo,
       COUNT(*) AS qtd,
       MAX(timestamp) AS ultimo_erro,
       MAX(usuario_id) AS exemplo_usuario
FROM erros
WHERE timestamp >= DATETIME('now', '-1 day')
GROUP BY erro_tipo ORDER BY qtd DESC;
```

### Ver traceback completo de um erro específico
```sql
SELECT timestamp, usuario_id, traceback
FROM erros WHERE id = 42;  -- substituir pelo id do erro
```

### Tempo médio de resposta por tier
```sql
SELECT tier,
       AVG(duracao_ms) AS ms_medio,
       MAX(duracao_ms) AS ms_max,
       COUNT(*) AS n
FROM execucoes
WHERE timestamp >= DATE('now', '-1 day')
GROUP BY tier;
```

### Quem são os usuários mais ativos?
```sql
SELECT usuario_id,
       COUNT(*) AS chamadas,
       MAX(timestamp) AS ultima,
       MAX(nivel) AS nivel_atual
FROM execucoes
GROUP BY usuario_id ORDER BY chamadas DESC LIMIT 10;
```

### Quais tópicos estão sendo estudados?
```sql
SELECT perfil_topico, COUNT(*) AS qtd
FROM execucoes
WHERE timestamp >= DATE('now', '-7 days') AND perfil_topico IS NOT NULL
GROUP BY perfil_topico ORDER BY qtd DESC;
```

### Quantos erros em sequência por usuário (possível bug)?
```sql
SELECT usuario_id, COUNT(*) AS erros_seguidos
FROM erros
WHERE timestamp >= DATETIME('now', '-1 hour')
GROUP BY usuario_id HAVING COUNT(*) >= 3 ORDER BY erros_seguidos DESC;
```

---

## Retenção

- **Política default:** manter últimos **90 dias**.
- Limpar manualmente:
  ```bash
  python scripts/limpar_logs.py              # mantém últimos 90 dias
  python scripts/limpar_logs.py --dias 30   # mantém últimos 30 dias
  ```
- (Futuro) Agendar via cron: `0 3 * * 0` (domingo 3h da manhã).

---

## Garantias

- ✅ Log de erro **nunca** quebra a resposta 500 (try/except aninhado).
- ✅ Engine separado — queries de aluno não competem com INSERT de log.
- ✅ Conteúdo da mensagem **não** é logado (LGPD — pode ter código/dados sensíveis).
- ✅ Cada chamada tem timestamp + user + tier + duração — base pra análise de qualidade.

---

## O que NÃO é logado (consciente)

- **Conteúdo da mensagem do aluno** (LGPD, código pode ter dados sensíveis).
- **Resposta completa do tutor** (economia de espaço, contexto fica em `Sessao.historico`).
- **Chave de API** (sanitização automática via `logging.Filter` se necessário no futuro).
- **Headers HTTP completos** (só user-agent se virar relevante pra análise).

Se precisar desses dados no futuro, criar coluna específica com cuidado de privacidade.