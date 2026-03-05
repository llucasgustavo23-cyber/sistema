# app/database.py
from __future__ import annotations

import os
import base64
import hmac
from hashlib import pbkdf2_hmac
from secrets import token_bytes
from typing import Optional, Dict, List, Any, Tuple
from datetime import date

import pymysql
from pymysql.cursors import DictCursor


# ==========================
# Config & Cripto (interno)
# ==========================

_PBKDF2_ALGO = "sha256"
_PBKDF2_ITERATIONS_DEFAULT = 210_000
_PBKDF2_SALT_LEN = 16   # 128 bits
_PBKDF2_DK_LEN = 32     # 256 bits
_ALLOWED_ROLES = {"admin", "operador", "visualizador"}


def _hash_password(password: str) -> tuple[str, str, int, str]:
    if isinstance(password, str):
        password = password.encode("utf-8")
    salt = token_bytes(_PBKDF2_SALT_LEN)
    dk = pbkdf2_hmac(_PBKDF2_ALGO, password, salt, _PBKDF2_ITERATIONS_DEFAULT, dklen=_PBKDF2_DK_LEN)
    return (
        _PBKDF2_ALGO,
        base64.b64encode(salt).decode("ascii"),
        _PBKDF2_ITERATIONS_DEFAULT,
        base64.b64encode(dk).decode("ascii"),
    )


def verifica_senha(password: str, algo: str, salt_b64: str, iterations: int, hash_b64: str) -> bool:
    if isinstance(password, str):
        password = password.encode("utf-8")
    salt = base64.b64decode(salt_b64)
    expected = base64.b64decode(hash_b64)
    dk = pbkdf2_hmac(algo, password, salt, int(iterations), dklen=len(expected))
    return hmac.compare_digest(dk, expected)


# ==========================
# Classe Database (MySQL)
# ==========================

class Database:

    def __init__(self, ensure_schema: bool = False) -> None:
        self.host = os.getenv("DB_HOST", "localhost")
        self.port = int(os.getenv("DB_PORT", "3306"))
        self.user = os.getenv("DB_USER", "root")
        self.password = os.getenv("DB_PASSWORD", "")
        self.db_name = os.getenv("DB_NAME", "sistema")

        # Cria schema (tabela usuarios) se solicitado
        if ensure_schema:
            try:
                self.create_tables()
            except Exception as e:
                print("[Database] Aviso: falha ao criar schema:", e)

    # --------------- Conexão ---------------

    def _get_conn(self) -> pymysql.Connection:
        return pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.db_name,
            autocommit=False,
            charset="utf8mb4",
            cursorclass=DictCursor,
        )

    # ========== (SEU) gerenciamento de usuários ==========
    def checar_usuario(self, usuario: str, senha: str) -> Optional[Dict[str, Any]]:
        sql = """
            SELECT idfuncionarios, usuario, algo, iterations, salt, pwd_hash, role
              FROM funcionarios
             WHERE usuario = %s
             LIMIT 1
        """
        conn = self._get_conn()
        try:
            with conn.cursor() as cur:
                cur.execute(sql, (usuario,))
                row = cur.fetchone()
                if not row:
                    return None

                ok = verifica_senha(
                    senha,
                    row["algo"],
                    row["salt"],
                    int(row["iterations"]),
                    row["pwd_hash"],
                )
                if not ok:
                    return None

                return {
                    "idfuncionarios": row["idfuncionarios"],
                    "usuario": row["usuario"],
                    "role": row["role"],
                }
        finally:
            conn.close()

    def criar_usuario(self, usuario: str, senha: str, role: str = "visualizador", nome: Optional[str] = None) -> int:
        role = (role or "visualizador").lower()
        if role not in _ALLOWED_ROLES:
            raise ValueError(f"Perfil inválido: {role}. Use um de: {sorted(_ALLOWED_ROLES)}")

        if self._usuario_existe(usuario):
            raise ValueError("Usuário já existe.")

        algo, salt_b64, iterations, hash_b64 = _hash_password(senha)

        sql = """
            INSERT INTO funcionarios (usuario, algo, iterations, salt, pwd_hash, role)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        vals = (usuario, algo, iterations, salt_b64, hash_b64, role)

        conn = self._get_conn()
        try:
            with conn.cursor() as cur:
                cur.execute(sql, vals)
                new_id = cur.lastrowid
            conn.commit()
            return int(new_id)
        except Exception:
            conn.rollback()
            raise
        finally:
            conn.close()

    def alterar_senha(self, usuario: str, nova_senha: str) -> bool:
        if not self._usuario_existe(usuario):
            return False

        algo, salt_b64, iterations, hash_b64 = _hash_password(nova_senha)
        sql = """
            UPDATE funcionarios
               SET algo=%s, iterations=%s, salt=%s, pwd_hash=%s
             WHERE usuario=%s
             LIMIT 1
        """
        conn = self._get_conn()
        try:
            with conn.cursor() as cur:
                cur.execute(sql, (algo, iterations, salt_b64, hash_b64, usuario))
                ok = cur.rowcount > 0
            conn.commit()
            return ok
        except Exception:
            conn.rollback()
            raise
        finally:
            conn.close()

    def alterar_role(self, usuario: str, novo_role: str) -> bool:
        novo_role = (novo_role or "").lower()
        if novo_role not in _ALLOWED_ROLES:
            raise ValueError(f"Perfil inválido: {novo_role}. Use um de: {sorted(_ALLOWED_ROLES)}")

        sql = "UPDATE funcionarios SET role=%s WHERE usuario=%s LIMIT 1"
        conn = self._get_conn()
        try:
            with conn.cursor() as cur:
                cur.execute(sql, (novo_role, usuario))
                ok = cur.rowcount > 0
            conn.commit()
            return ok
        except Exception:
            conn.rollback()
            raise
        finally:
            conn.close()

    def deletar_usuario(self, usuario_ou_id: str | int) -> bool:
        if isinstance(usuario_ou_id, int):
            sql = "DELETE FROM funcionarios WHERE idfuncionarios=%s LIMIT 1"
            params = (usuario_ou_id,)
        else:
            sql = "DELETE FROM funcionarios WHERE usuario=%s LIMIT 1"
            params = (usuario_ou_id,)

        conn = self._get_conn()
        try:
            with conn.cursor() as cur:
                cur.execute(sql, params)
                ok = cur.rowcount > 0
            conn.commit()
            return ok
        except Exception:
            conn.rollback()
            raise
        finally:
            conn.close()

    def listar_usuarios(self) -> List[Dict[str, Any]]:
        sql = "SELECT idfuncionarios, usuario, role, created_at FROM funcionarios ORDER BY idfuncionarios DESC"
        conn = self._get_conn()
        try:
            with conn.cursor() as cur:
                cur.execute(sql)
                return list(cur.fetchall() or [])
        finally:
            conn.close()

    def _usuario_existe(self, usuario: str) -> bool:
        sql = "SELECT 1 FROM funcionarios WHERE usuario=%s LIMIT 1"
        conn = self._get_conn()
        try:
            with conn.cursor() as cur:
                cur.execute(sql, (usuario,))
                return cur.fetchone() is not None
        finally:
            conn.close()

    # =====================================================
    # ====== A PARTIR DAQUI: MÉTODOS PARA AMBULÂNCIA ======
    # =====================================================

    # ---------- util: schema ----------
    def _tabela_tem_coluna(self, tabela: str, coluna: str) -> bool:
        sql = """
            SELECT 1
              FROM INFORMATION_SCHEMA.COLUMNS
             WHERE TABLE_SCHEMA=%s AND TABLE_NAME=%s AND COLUMN_NAME=%s
             LIMIT 1
        """
        conn = self._get_conn()
        try:
            with conn.cursor() as cur:
                cur.execute(sql, (self.db_name, tabela, coluna))
                return cur.fetchone() is not None
        finally:
            conn.close()

    def _descobrir_coluna_texto_principal(self, tabela: str) -> str:
        sql = """
            SELECT COLUMN_NAME
              FROM INFORMATION_SCHEMA.COLUMNS
             WHERE TABLE_SCHEMA = %s
               AND TABLE_NAME   = %s
               AND DATA_TYPE IN ('varchar','char','text','tinytext','mediumtext','longtext')
               AND COLUMN_KEY NOT IN ('PRI')
          ORDER BY
               (COLUMN_NAME LIKE 'nome%%') DESC,
               (COLUMN_NAME LIKE '%%nome%%') DESC,
               (COLUMN_NAME LIKE 'descricao%%') DESC,
               (COLUMN_NAME LIKE '%%descricao%%') DESC,
               (COLUMN_NAME LIKE 'modelo%%') DESC,
               (COLUMN_NAME LIKE '%%modelo%%') DESC,
               (COLUMN_NAME LIKE 'tipo%%') DESC,
               (COLUMN_NAME LIKE '%%tipo%%') DESC,
               ORDINAL_POSITION ASC
             LIMIT 1
        """
        conn = self._get_conn()
        try:
            with conn.cursor() as cur:
                cur.execute(sql, (self.db_name, tabela))
                row = cur.fetchone()
                if not row or not row.get("COLUMN_NAME"):
                    raise RuntimeError(f"Não encontrei coluna textual adequada em '{tabela}'.")
                return row["COLUMN_NAME"]
        finally:
            conn.close()

    # ---------- lookups (buscar sem criar) ----------
    def _get_modelo_id_por_texto(self, modelo_texto: str) -> int:
        modelo_texto = (modelo_texto or "").strip()
        if not modelo_texto:
            raise ValueError("Modelo não pode ser vazio.")
        name_col = self._descobrir_coluna_texto_principal("modelo")
        sql = f"SELECT id_modelo FROM modelo WHERE {name_col}=%s LIMIT 1"
        conn = self._get_conn()
        try:
            with conn.cursor() as cur:
                cur.execute(sql, (modelo_texto,))
                row = cur.fetchone()
                if not row:
                    raise ValueError(f"Modelo '{modelo_texto}' não encontrado na tabela 'modelo'.")
                return int(row["id_modelo"])
        finally:
            conn.close()

    def _get_forma_id_por_texto(self, forma_texto: str) -> int:
        forma_texto = (forma_texto or "").strip()
        if not forma_texto:
            raise ValueError("Forma de aquisição não pode ser vazia.")
        name_col = self._descobrir_coluna_texto_principal("for_aquisicao")  # geralmente 'tipo'
        # PK em for_aquisicao é idFor_aquisicao
        sql = f"SELECT id_forma_aquisicao FROM for_aquisicao WHERE {name_col}=%s LIMIT 1"
        conn = self._get_conn()
        try:
            with conn.cursor() as cur:
                cur.execute(sql, (forma_texto,))
                row = cur.fetchone()
                if not row:
                    raise ValueError(f"Forma de aquisição '{forma_texto}' não encontrada em 'for_aquisicao'.")
                return int(row["id_forma_aquisicao"])
        finally:
            conn.close()

    # ---------- sugestões/autocomplete ----------
    def listar_modelos(self) -> List[Dict[str, Any]]:
        name_col = self._descobrir_coluna_texto_principal("modelo")
        sql = f"SELECT id_modelo, {name_col} AS nome FROM modelo ORDER BY nome"
        conn = self._get_conn()
        try:
            with conn.cursor() as cur:
                cur.execute(sql)
                return list(cur.fetchall() or [])
        finally:
            conn.close()

    def listar_formas_aquisicao(self) -> List[Dict[str, Any]]:
        name_col = self._descobrir_coluna_texto_principal("for_aquisicao")
        sql = f"SELECT id_forma_aquisicao AS id, {name_col} AS nome FROM for_aquisicao ORDER BY nome"
        conn = self._get_conn()
        try:
            with conn.cursor() as cur:
                cur.execute(sql)
                return list(cur.fetchall() or [])
        finally:
            conn.close()

    def listar_placas(self) -> List[str]:
        sql = "SELECT placa FROM ambulancia ORDER BY placa"
        conn = self._get_conn()
        try:
            with conn.cursor() as cur:
                cur.execute(sql)
                return [r["placa"] for r in (cur.fetchall() or []) if r.get("placa")]
        finally:
            conn.close()

    def listar_chassis(self) -> List[str]:
        sql = "SELECT chassi FROM ambulancia ORDER BY chassi"
        conn = self._get_conn()
        try:
            with conn.cursor() as cur:
                cur.execute(sql)
                return [r["chassi"] for r in (cur.fetchall() or []) if r.get("chassi")]
        finally:
            conn.close()

    def listar_cnes(self) -> List[str]:
        sql = "SELECT DISTINCT cnes FROM ambulancia WHERE cnes IS NOT NULL AND cnes <> '' ORDER BY cnes"
        conn = self._get_conn()
        try:
            with conn.cursor() as cur:
                cur.execute(sql)
                return [r["cnes"] for r in (cur.fetchall() or []) if r.get("cnes")]
        finally:
            conn.close()

    def listar_denominacoes(self) -> List[str]:
        if not self._tabela_tem_coluna("ambulancia", "denominacao"):
            return []
        sql = "SELECT DISTINCT denominacao FROM ambulancia WHERE denominacao IS NOT NULL AND denominacao <> '' ORDER BY denominacao"
        conn = self._get_conn()
        try:
            with conn.cursor() as cur:
                cur.execute(sql)
                return [r["denominacao"] for r in (cur.fetchall() or []) if r.get("denominacao")]
        finally:
            conn.close()

    # ---------- unicidade ----------
    def _chassi_existe(self, chassi: str) -> bool:
        sql = "SELECT 1 FROM ambulancia WHERE chassi=%s LIMIT 1"
        conn = self._get_conn()
        try:
            with conn.cursor() as cur:
                cur.execute(sql, (chassi,))
                return cur.fetchone() is not None
        finally:
            conn.close()

    def _placa_existe(self, placa: str) -> bool:
        sql = "SELECT 1 FROM ambulancia WHERE placa=%s LIMIT 1"
        conn = self._get_conn()
        try:
            with conn.cursor() as cur:
                cur.execute(sql, (placa,))
                return cur.fetchone() is not None
        finally:
            conn.close()

    # ---------- recuperação ----------
    def obter_id_ambulancia_por_chassi(self, chassi: str) -> Optional[int]:
        sql = "SELECT id_ambulancia FROM ambulancia WHERE chassi=%s LIMIT 1"
        conn = self._get_conn()
        try:
            with conn.cursor() as cur:
                cur.execute(sql, (chassi,))
                row = cur.fetchone()
                return int(row["id_ambulancia"]) if row else None
        finally:
            conn.close()

    def obter_id_ambulancia_por_placa(self, placa: str) -> Optional[int]:
        sql = "SELECT id_ambulancia FROM ambulancia WHERE placa=%s LIMIT 1"
        conn = self._get_conn()
        try:
            with conn.cursor() as cur:
                cur.execute(sql, (placa,))
                row = cur.fetchone()
                return int(row["id_ambulancia"]) if row else None
        finally:
            conn.close()

    # ---------- atualização ----------
    def atualizar_ambulancia_por_id(
        self,
        id_ambulancia: int,
        *,
        id_modelo: int,
        id_forma_aquisicao: int,
        data_aquisicao: date,
        uso_oficial: bool,
        cnes: Optional[str],
        placa: Optional[str] = None,
        chassi: Optional[str] = None,
        denominacao: Optional[str] = None,
    ) -> bool:
        """
        Atualiza a ambulância pelo ID. Respeita a regra do CNES x Oficial.
        """
        cnes_final = (cnes or "").strip() if uso_oficial else None
        if uso_oficial and not cnes_final:
            raise ValueError("CNES é obrigatório para viatura oficial.")

        tem_denominacao = self._tabela_tem_coluna("ambulancia", "denominacao")

        sets = ["id_modelo=%s", "id_forma_aquisicao=%s", "data_aquisicao=%s", "uso_oficial=%s", "cnes=%s"]
        vals: List[Any] = [int(id_modelo), int(id_forma_aquisicao), data_aquisicao, bool(uso_oficial), cnes_final]

        if placa:
            sets.append("placa=%s")
            vals.append(placa.strip())
        if chassi:
            sets.append("chassi=%s")
            vals.append(chassi.strip())
        if tem_denominacao and (denominacao or "").strip():
            sets.append("denominacao=%s")
            vals.append(denominacao.strip())

        vals.append(int(id_ambulancia))
        sql = f"UPDATE ambulancia SET {', '.join(sets)} WHERE id_ambulancia=%s"

        conn = self._get_conn()
        try:
            with conn.cursor() as cur:
                cur.execute(sql, vals)
                ok = cur.rowcount > 0
            conn.commit()
            return ok
        except Exception:
            conn.rollback()
            raise
        finally:
            conn.close()

    def atualizar_ambulancia_por_chassi(
        self,
        chassi_ref: str,
        *,
        id_modelo: int,
        id_forma_aquisicao: int,
        data_aquisicao: date,
        uso_oficial: bool,
        cnes: Optional[str],
        placa: Optional[str] = None,
        novo_chassi: Optional[str] = None,
        denominacao: Optional[str] = None,
    ) -> bool:
        """
        Atualiza a ambulância localizando pelo CHASSI atual (único).
        """
        id_amb = self.obter_id_ambulancia_por_chassi(chassi_ref)
        if not id_amb:
            raise ValueError("Não encontrei ambulância com esse chassi.")

        return self.atualizar_ambulancia_por_id(
            id_amb,
            id_modelo=id_modelo,
            id_forma_aquisicao=id_forma_aquisicao,
            data_aquisicao=data_aquisicao,
            uso_oficial=uso_oficial,
            cnes=cnes,
            placa=placa,
            chassi=novo_chassi,
            denominacao=denominacao,
        )
    # ------------------ CADASTRO DE AMBULÂNCIA (USANDO FKs EXISTENTES) ------------------
    def cadastrar_ambulancia(
        self,
        *,
        placa: str,
        chassi: str,
        # escolha UMA das duas abordagens abaixo para cada FK:
        # 1) passar o TEXTO e eu converto para id existente (não cria):
        modelo_texto: Optional[str] = None,
        forma_aquisicao_texto: Optional[str] = None,
        # 2) OU passar diretamente os IDs (mais seguro/rápido):
        id_modelo: Optional[int] = None,
        id_forma_aquisicao: Optional[int] = None,   # <- FK em ambulancia
        data_aquisicao: date,
        uso_oficial: bool,
        cnes: Optional[str] = None,
        denominacao: Optional[str] = None,          # grava se a coluna existir
    ) -> int:
        """
        Insere em 'ambulancia' referenciando SOMENTE registros já existentes:
        - modelo (modelo.id_modelo)
        - for_aquisicao (for_aquisicao.idFor_aquisicao) -> FK: ambulancia.id_forma_aquisicao
        Regras:
        - placa/chassi únicos
        - CNES obrigatório se uso_oficial=True; NULL se False
        - 'denominacao' gravada apenas se a coluna existir em 'ambulancia'
        """
        if not placa or not chassi:
            raise ValueError("Placa e chassi são obrigatórios.")

        if self._placa_existe(placa):
            raise ValueError("Já existe ambulância com esta placa.")
        if self._chassi_existe(chassi):
            raise ValueError("Já existe ambulância com este chassi.")

        # Resolver id_modelo
        if id_modelo is None:
            if not modelo_texto:
                raise ValueError("Informe 'id_modelo' ou 'modelo_texto'.")
            id_modelo = self._get_modelo_id_por_texto(modelo_texto)

        # Resolver id_forma_aquisicao (aponta para for_aquisicao.idFor_aquisicao)
        if id_forma_aquisicao is None:
            if not forma_aquisicao_texto:
                raise ValueError("Informe 'id_forma_aquisicao' ou 'forma_aquisicao_texto'.")
            id_forma_aquisicao = self._get_forma_id_por_texto(forma_aquisicao_texto)

        # Regra CNES x Oficial
        cnes_final = (cnes or "").strip() if uso_oficial else None
        if uso_oficial and not cnes_final:
            raise ValueError("CNES é obrigatório para viatura oficial.")

        tem_denominacao = self._tabela_tem_coluna("ambulancia", "denominacao")

        colunas = [
            "placa", "chassi", "id_modelo", "id_forma_aquisicao",
            "data_aquisicao", "uso_oficial", "cnes"
        ]
        valores = [
            placa.strip(), chassi.strip(), int(id_modelo), int(id_forma_aquisicao),
            data_aquisicao, bool(uso_oficial), cnes_final
        ]

        if tem_denominacao and (denominacao or "").strip():
            colunas.append("denominacao")
            valores.append(denominacao.strip())

        placeholders = ", ".join(["%s"] * len(valores))
        sql = f"INSERT INTO ambulancia ({', '.join(colunas)}) VALUES ({placeholders})"

        conn = self._get_conn()
        try:
            with conn.cursor() as cur:
                cur.execute(sql, valores)
                new_id = cur.lastrowid
            conn.commit()
            return int(new_id)
        except Exception:
            conn.rollback()
            raise
        finally:
            conn.close()