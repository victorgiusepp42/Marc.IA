"""
Modelos SQLAlchemy do Marc.IA.

Gamificação removida do MVP em 2026-07-06 (ADR-011) — XP, níveis e
progresso gamificado ficaram fora do escopo. Sessao agora guarda só
o histórico de mensagens do aluno.

Ver backlog/gamificacao.md pra reativação futura com critérios definidos.
"""

import json
from datetime import datetime, timezone

from src.database import db

# Limite máximo de mensagens no histórico
MAX_HISTORICO = 200


class Sessao(db.Model):
    """Sessão do aluno — persiste histórico em SQLite via SQLAlchemy."""

    __tablename__ = "sessoes"

    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.String(128), unique=True, nullable=False, index=True)
    historico_json = db.Column(db.Text, default="[]")
    # === NOVO (2026-07-08): histórico segregado por tópico da trilha ===
    # Estrutura JSON:
    #   { "py-variaveis": [{"role":"user","content":"...","timestamp":"2026-07-08T..."}, ...],
    #     "alg-condicionais": [...], ... }
    # Permite ao aluno reabrir histórico salvo de qualquer aula do curso e dá
    # completude ("minha conversa sobre vetores está guardada"). Substitui o
    # `historico_json` legado quando o aluno navega — mas o legado continua
    # existindo por compatibilidade.
    historico_por_topico_json = db.Column(db.Text, default="{}")
    disciplina_ativa = db.Column(db.String(128), nullable=True)
    topico_ativo = db.Column(db.String(128), nullable=True)
    # Linguagem escolhida pelo aluno pro tópico ativo (visualg/portugol/python).
    # Persistido por sessão pra sobreviver F5 e troca de aba.
    linguagem_topico = db.Column(db.String(32), nullable=True)
    criado_em = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    atualizado_em = db.Column(
        db.DateTime,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )

    # --- Propriedade para acessar histórico como lista Python ---

    @property
    def historico(self) -> list[dict]:
        """Deserializa histórico do JSON armazenado."""
        try:
            return json.loads(self.historico_json or "[]")
        except (json.JSONDecodeError, TypeError):
            return []

    @historico.setter
    def historico(self, valor: list[dict]) -> None:
        """Serializa histórico para JSON."""
        self.historico_json = json.dumps(valor, ensure_ascii=False)

    @property
    def historico_por_topico(self) -> dict:
        """Deserializa histórico segregado por tópico. Retorna {topico_id: [msgs]}."""
        try:
            data = json.loads(self.historico_por_topico_json or "{}")
            return data if isinstance(data, dict) else {}
        except (json.JSONDecodeError, TypeError):
            return {}

    @historico_por_topico.setter
    def historico_por_topico(self, valor: dict) -> None:
        """Serializa histórico segregado por tópico."""
        # Garante que seja dict[str, list] — defesa contra keys inválidas
        safe = {}
        if isinstance(valor, dict):
            for k, v in valor.items():
                if isinstance(k, str) and isinstance(v, list):
                    safe[k] = v
        self.historico_por_topico_json = json.dumps(safe, ensure_ascii=False)

    # --- Métodos de negócio ---

    def adicionar_mensagem(self, role: str, content: str) -> None:
        """Adiciona mensagem ao histórico."""
        if role not in ("user", "assistant"):
            return
        if not content:
            return
        hist = self.historico
        hist.append({"role": role, "content": content})
        if len(hist) > MAX_HISTORICO:
            hist = hist[-MAX_HISTORICO:]
        self.historico = hist

    def adicionar_mensagem_topico(self, role: str, content: str, topico_id: str) -> None:
        """Adiciona mensagem AO HISTÓRICO DO TÓPICO ESPECÍFICO.

        Usado pelo /chat pra segregar conversas por aula. Cada tópico
        mantém sua própria lista; quando o aluno volta nele, pode carregar
        tudo via GET /sessao/topico/<id>.
        """
        if role not in ("user", "assistant"):
            return
        if not content or not topico_id:
            return
        todos = self.historico_por_topico
        msgs = todos.get(topico_id, [])
        msgs.append({
            "role": role,
            "content": content,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        })
        # Cap em 200 mensagens por tópico (memória de detalhe da aula)
        if len(msgs) > MAX_HISTORICO:
            msgs = msgs[-MAX_HISTORICO:]
        todos[topico_id] = msgs
        self.historico_por_topico = todos

    def historico_topico(self, topico_id: str) -> list[dict]:
        """Retorna mensagens salvas de um tópico específico (lista vazia se nada)."""
        return self.historico_por_topico.get(topico_id, [])

    def listar_topicos_com_historico(self) -> list[dict]:
        """Retorna lista de tópicos com mensagens salvas, ordenada por mais recente.

        Cada item: {"topico_id": str, "qtd_mensagens": int, "ultimo_timestamp": str}.
        """
        resultado = []
        for topico_id, msgs in self.historico_por_topico.items():
            if not msgs:
                continue
            ts = msgs[-1].get("timestamp", "")
            resultado.append({
                "topico_id": topico_id,
                "qtd_mensagens": len(msgs),
                "ultimo_timestamp": ts,
            })
        # Mais recente primeiro
        resultado.sort(key=lambda x: x["ultimo_timestamp"], reverse=True)
        return resultado

    # --- Factory: carrega ou cria sessão ---

    @classmethod
    def carregar_ou_criar(cls, usuario_id: str) -> "Sessao":
        """Busca sessão existente ou cria uma nova."""
        usuario_id = cls._sanitizar_id(usuario_id)
        sessao = cls.query.filter_by(usuario_id=usuario_id).first()
        if sessao is None:
            sessao = cls(
                usuario_id=usuario_id,
                historico_json="[]",
                historico_por_topico_json="{}",
            )
            db.session.add(sessao)
        return sessao

    def salvar(self) -> None:
        """Persiste alterações no banco."""
        db.session.commit()

    @staticmethod
    def _sanitizar_id(usuario_id: str) -> str:
        """Remove caracteres perigosos do ID."""
        sanitizado = "".join(c for c in usuario_id if c.isalnum() or c == "-")
        return sanitizado or "anonimo"

    def __repr__(self) -> str:
        return f"<Sessao {self.usuario_id}>"


class AlunoPerfil(db.Model):
    """Perfil de continuidade do aluno.

    Design: NÃO é diagnóstico de habilidade (fraco em X, forte em Y).
    É memória de continuidade — o tutor sabe o contexto recente sem julgar
    nem forçar tópicos. O aluno decide o que quer conversar; o tutor só
    não esquece o que já rolou.

    Inspirado no padrão 1 do Hermes Agent (vide memorial_hermes_referencia.md).
    Implementado em 2026-07-05.
    """

    __tablename__ = "alunos_perfil"

    usuario_id = db.Column(db.String(128), primary_key=True)
    topico_atual = db.Column(db.String(256), nullable=True)
    estilo_comunicacao = db.Column(db.String(32), default="auto")  # formal|informal|auto
    preferencias_explicitas = db.Column(db.Text, default="[]")  # JSON list[str]
    topicos_ja_explicados = db.Column(db.Text, default="[]")  # JSON list[str]
    nivel_percebido = db.Column(db.String(256), nullable=True)
    resumo_ultima_sessao = db.Column(db.Text, nullable=True)
    criado_em = db.Column(
        db.DateTime, default=lambda: datetime.now(timezone.utc)
    )
    atualizado_em = db.Column(
        db.DateTime,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )

    @property
    def preferencias(self) -> list[str]:
        try:
            return json.loads(self.preferencias_explicitas or "[]")
        except (json.JSONDecodeError, TypeError):
            return []

    @preferencias.setter
    def preferencias(self, valor: list[str]) -> None:
        # Trim para últimas 20 — evita crescimento ilimitado
        self.preferencias_explicitas = json.dumps(valor[-20:], ensure_ascii=False)

    @property
    def topicos_explicados(self) -> list[str]:
        try:
            return json.loads(self.topicos_ja_explicados or "[]")
        except (json.JSONDecodeError, TypeError):
            return []

    @topicos_explicados.setter
    def topicos_explicados(self, valor: list[str]) -> None:
        # Trim para últimos 50
        self.topicos_ja_explicados = json.dumps(valor[-50:], ensure_ascii=False)

    def atualizar_topico(self, topico: str) -> None:
        """Atualiza o tópico atual da conversa (se diferente)."""
        if topico and topico != self.topico_atual:
            self.topico_atual = topico

    def adicionar_preferencia(self, pref: str) -> None:
        """Adiciona preferência explícita (sem duplicar)."""
        prefs = self.preferencias
        if pref and pref not in prefs:
            prefs.append(pref)
            self.preferencias = prefs

    def registrar_topico_explicado(self, topico: str) -> None:
        """Adiciona tópico à lista do que o tutor já explicou."""
        if topico:
            tops = self.topicos_explicados
            tops.append(topico)
            self.topicos_explicados = tops

    def resumo_para_prompt(self) -> str:
        """Gera string curta pra injetar no system prompt (~200 tokens max)."""
        partes = []
        if self.topico_atual:
            partes.append(f"Tópico atual: {self.topico_atual}")
        if self.estilo_comunicacao and self.estilo_comunicacao != "auto":
            partes.append(f"Aluno prefere tom: {self.estilo_comunicacao}")
        if self.preferencias:
            partes.append(
                f"Preferências declaradas: {', '.join(self.preferencias[-3:])}"
            )
        if self.topicos_explicados:
            tops = self.topicos_explicados[-5:]
            partes.append(f"Tópicos já explicados: {', '.join(tops)}")
        if self.resumo_ultima_sessao:
            partes.append(f"Última sessão: {self.resumo_ultima_sessao}")
        return "\n".join(partes) if partes else ""

    @classmethod
    def carregar_ou_criar(cls, usuario_id: str) -> "AlunoPerfil":
        """Busca perfil existente ou cria um novo."""
        usuario_id = Sessao._sanitizar_id(usuario_id)
        perfil = cls.query.get(usuario_id)
        if perfil is None:
            perfil = cls(usuario_id=usuario_id)
            db.session.add(perfil)
        return perfil

    def salvar(self) -> None:
        """Persiste alterações no banco."""
        db.session.commit()

    def __repr__(self) -> str:
        return f"<AlunoPerfil {self.usuario_id} topico={self.topico_atual}>"


class LogExecucao(db.Model):
    """Registro de cada chamada HTTP bem-sucedida ao /chat.

    Engine separado (data/logs.db) via SQLAlchemy BIND_KEYS.
    Permite queries SQL pra análise de uso, qualidade, performance.

    Schema detalhado em data/kb_ip/00_meta/LOGGING.md.
    """

    __tablename__ = "execucoes"
    __bind_key__ = "logs"

    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(
        db.DateTime,
        default=lambda: datetime.now(timezone.utc),
        index=True,
        nullable=False,
    )
    usuario_id = db.Column(db.String(128), nullable=False, index=True)
    mensagem_chars = db.Column(db.Integer, nullable=False)
    codigo_chars = db.Column(db.Integer, default=0)
    linguagem = db.Column(db.String(16))
    complexidade = db.Column(db.String(16))
    tier = db.Column(db.String(32), nullable=False, index=True)
    perfil_topico = db.Column(db.String(256))
    perfil_preferencias = db.Column(db.Integer, default=0)
    perfil_topicos_explicados = db.Column(db.Integer, default=0)
    duracao_ms = db.Column(db.Integer)
    kb_chunks_usados = db.Column(db.Integer, default=0)

    def __repr__(self) -> str:
        return f"<LogExecucao {self.id} {self.usuario_id} tier={self.tier}>"


class LogErro(db.Model):
    """Registro de cada erro capturado em qualquer endpoint.

    Engine separado (data/logs.db). Traceback completo + contexto JSON.
    """

    __tablename__ = "erros"
    __bind_key__ = "logs"

    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(
        db.DateTime,
        default=lambda: datetime.now(timezone.utc),
        index=True,
        nullable=False,
    )
    usuario_id = db.Column(db.String(128))
    endpoint = db.Column(db.String(64))
    erro_tipo = db.Column(db.String(64), nullable=False, index=True)
    erro_mensagem = db.Column(db.String(500))
    traceback = db.Column(db.Text)
    contexto_json = db.Column(db.Text)

    def __repr__(self) -> str:
        return f"<LogErro {self.id} {self.erro_tipo}>"


class Feedback(db.Model):
    """Like/dislike do aluno em uma resposta do tutor (FRO-06 / MET-01).

    Engine separado (data/logs.db). Cada click registra 1 linha.
    `mensagem_idx` é o índice da resposta do tutor em `Sessao.historico`
    (posições ímpares: 1, 3, 5, …).
    """

    __tablename__ = "feedbacks"
    __bind_key__ = "logs"

    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(
        db.DateTime,
        default=lambda: datetime.now(timezone.utc),
        index=True,
        nullable=False,
    )
    usuario_id = db.Column(db.String(128), nullable=False, index=True)
    sessao_id = db.Column(db.Integer, index=True)  # nullable: historico pode ter sido limpo
    topico_id = db.Column(db.String(64), index=True)
    mensagem_idx = db.Column(db.Integer, nullable=False)
    # 'like' | 'dislike'
    tipo = db.Column(db.String(16), nullable=False, index=True)

    def __repr__(self) -> str:
        return f"<Feedback {self.id} {self.tipo} user={self.usuario_id!r}>"


class Metrica(db.Model):
    """NPS + Sean Ellis + outras métricas pontuais (FRO-06 / MET-02).

    Engine separado (data/logs.db). `valor` é polimórfico (int pra NPS,
    string pra Sean Ellis). `tipo` discrimina.
    """

    __tablename__ = "metricas"
    __bind_key__ = "logs"

    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(
        db.DateTime,
        default=lambda: datetime.now(timezone.utc),
        index=True,
        nullable=False,
    )
    usuario_id = db.Column(db.String(128), nullable=False, index=True)
    # 'nps' | 'sean_ellis'
    tipo = db.Column(db.String(32), nullable=False, index=True)
    # int (0-10) pra nps; string ('muito' | 'um_pouco' | 'indiferente') pra sean_ellis
    valor = db.Column(db.String(32), nullable=False)

    def __repr__(self) -> str:
        return f"<Metrica {self.id} {self.tipo}={self.valor!r} user={self.usuario_id!r}>"
