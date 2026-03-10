# app/database.py
from __future__ import annotations

import os
import base64
import hmac
from hashlib import pbkdf2_hmac
from secrets import token_bytes
from typing import Optional, Dict, List, Any
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

    # ========== Usuários ==========

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

    # ---------- lookups ----------
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
        """
        FIX: a tabela no schema é 'for_aquisicao' com PK 'id_forma_aquisicao'.
        O código antigo usava 'forma_aquisicao' (nome errado).
        """
        forma_texto = (forma_texto or "").strip()
        if not forma_texto:
            raise ValueError("Forma de aquisição não pode ser vazia.")
        name_col = self._descobrir_coluna_texto_principal("for_aquisicao")
        sql = f"SELECT id_forma_aquisicao AS id FROM for_aquisicao WHERE {name_col}=%s LIMIT 1"
        conn = self._get_conn()
        try:
            with conn.cursor() as cur:
                cur.execute(sql, (forma_texto,))
                row = cur.fetchone()
                if not row:
                    raise ValueError(f"Forma de aquisição '{forma_texto}' não encontrada em 'for_aquisicao'.")
                return int(row["id"])
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
        """FIX: tabela correta é 'for_aquisicao', não 'forma_aquisicao'."""
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
        """Lista todos os CNES cadastrados."""
        sql = "SELECT DISTINCT cnes FROM ambulancia WHERE cnes IS NOT NULL AND cnes <> '' ORDER BY cnes"
        conn = self._get_conn()
        try:
            with conn.cursor() as cur:
                cur.execute(sql)
                return [r["cnes"] for r in (cur.fetchall() or []) if r.get("cnes")]
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

    def obter_ambulancia_por_chassi(self, chassi_ref: str) -> Optional[Dict[str, Any]]:
        """
        FIX: Tabela de forma é 'for_aquisicao'.
        Retorna dict com os dados da ambulância.
        """
        nome_modelo = self._descobrir_coluna_texto_principal("modelo")
        nome_forma = self._descobrir_coluna_texto_principal("for_aquisicao")

        sql = f"""
            SELECT
                a.id_ambulancia,
                a.placa,
                a.chassi,
                a.id_modelo,
                m.{nome_modelo} AS modelo_nome,
                a.id_forma_aquisicao,
                f.{nome_forma} AS forma_nome,
                a.data_aquisicao,
                a.uso_oficial,
                a.cnes
            FROM ambulancia a
            LEFT JOIN modelo m ON m.id_modelo = a.id_modelo
            LEFT JOIN for_aquisicao f ON f.id_forma_aquisicao = a.id_forma_aquisicao
            WHERE a.chassi = %s
            LIMIT 1
        """
        conn = self._get_conn()
        try:
            with conn.cursor() as cur:
                cur.execute(sql, [chassi_ref.strip()])
                row = cur.fetchone()
                return row
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
    ) -> bool:
        """"""
        cnes_final = (cnes or "").strip() if uso_oficial else None
        if uso_oficial and not cnes_final:
            raise ValueError("CNES é obrigatório para viatura oficial.")

        sets = [
            "id_modelo=%s",
            "id_forma_aquisicao=%s",
            "data_aquisicao=%s",
            "uso_oficial=%s",
            "cnes=%s",          
        ]
        vals: List[Any] = [int(id_modelo), int(id_forma_aquisicao), data_aquisicao, bool(uso_oficial), cnes_final]

        if placa:
            sets.append("placa=%s")
            vals.append(placa.strip())
        if chassi:
            sets.append("chassi=%s")
            vals.append(chassi.strip())

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
    ) -> bool:
        """
        FIX: obter_id_ambulancia_por_chassi retorna int (não dict),
        então o .get("id_ambulancia") que estava aqui causava AttributeError.
        """
        id_amb = self.obter_id_ambulancia_por_chassi(chassi_ref)
        if not id_amb:
            raise ValueError("Não encontrei ambulância com esse chassi.")

        return self.atualizar_ambulancia_por_id(
            int(id_amb),          # FIX: era id_amb["id_ambulancia"]
            id_modelo=id_modelo,
            id_forma_aquisicao=id_forma_aquisicao,
            data_aquisicao=data_aquisicao,
            uso_oficial=uso_oficial,
            cnes=cnes,
            placa=placa,
            chassi=novo_chassi,
        )

    # ------------------ CADASTRO ------------------
    def cadastrar_ambulancia(
        self,
        *,
        placa: str,
        chassi: str,
        modelo_texto: Optional[str] = None,
        forma_aquisicao_texto: Optional[str] = None,
        id_modelo: Optional[int] = None,
        id_forma_aquisicao: Optional[int] = None,
        data_aquisicao: date,
        uso_oficial: bool,
        cnes: Optional[str] = None,
        ano: Optional[int] = None,
        denominacao: Optional[str] = None,
    ) -> int:
        """
        FIX:
        - 
        - 'ano' e 'denominacao' só são inseridos se a coluna existir no banco,
          evitando erro caso o ALTER TABLE ainda não tenha sido rodado.
        """
        if not placa or not chassi:
            raise ValueError("Placa e chassi são obrigatórios.")

        if self._placa_existe(placa):
            raise ValueError("Já existe ambulância com esta placa.")
        if self._chassi_existe(chassi):
            raise ValueError("Já existe ambulância com este chassi.")

        if id_modelo is None:
            if not modelo_texto:
                raise ValueError("Informe 'id_modelo' ou 'modelo_texto'.")
            id_modelo = self._get_modelo_id_por_texto(modelo_texto)

        if id_forma_aquisicao is None:
            if not forma_aquisicao_texto:
                raise ValueError("Informe 'id_forma_aquisicao' ou 'forma_aquisicao_texto'.")
            id_forma_aquisicao = self._get_forma_id_por_texto(forma_aquisicao_texto)

        cnes_final = (cnes or "").strip() if uso_oficial else None
        if uso_oficial and not cnes_final:
            raise ValueError("CNES é obrigatório para viatura oficial.")

        # Colunas e valores base (sempre presentes)
        colunas = [
            "placa", "chassi", "id_modelo", "id_forma_aquisicao",
            "data_aquisicao", "uso_oficial", "cnes",   
        ]
        valores: List[Any] = [
            placa.strip(),
            chassi.strip(),
            int(id_modelo),
            int(id_forma_aquisicao),
            data_aquisicao,
            bool(uso_oficial),
            cnes_final,
        ]

        # FIX: 'ano' e 'denominacao' só inseridos se a coluna existir
        if ano is not None and self._tabela_tem_coluna("ambulancia", "ano"):
            colunas.append("ano")
            valores.append(ano)

        if denominacao is not None and self._tabela_tem_coluna("ambulancia", "denominacao"):
            colunas.append("denominacao")
            valores.append(denominacao)

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

    # ------------------ LISTAGEM COMPLETA ------------------
    def listar_ambulancias(self) -> List[Dict[str, Any]]:
        """
        Retorna todas as ambulâncias com nome do modelo e forma de aquisição.
        Usado por listardados para preencher a tabela.
        """
        nome_modelo = self._descobrir_coluna_texto_principal("modelo")
        nome_forma  = self._descobrir_coluna_texto_principal("for_aquisicao")

        # Inclui 'ano' e 'denominacao' apenas se existirem na tabela
        col_ano  = ", a.ano"         if self._tabela_tem_coluna("ambulancia", "ano")         else ", NULL AS ano"
        col_den  = ", a.denominacao" if self._tabela_tem_coluna("ambulancia", "denominacao") else ", NULL AS denominacao"

        sql = f"""
            SELECT
                a.id_ambulancia,
                a.placa,
                a.chassi,
                a.id_modelo,
                m.{nome_modelo}  AS modelo_nome,
                a.id_forma_aquisicao,
                f.{nome_forma}   AS forma_nome,
                a.data_aquisicao,
                a.uso_oficial,
                a.cnes
                {col_ano}
                {col_den}
            FROM ambulancia a
            LEFT JOIN modelo       m ON m.id_modelo           = a.id_modelo
            LEFT JOIN for_aquisicao f ON f.id_forma_aquisicao = a.id_forma_aquisicao
            ORDER BY a.id_ambulancia DESC
        """
        conn = self._get_conn()
        try:
            with conn.cursor() as cur:
                cur.execute(sql)
                return list(cur.fetchall() or [])
        finally:
            conn.close()

    # ------------------ EXCLUSÃO ------------------
    def excluir_ambulancia_por_chassi(self, chassi: str) -> bool:
        """Remove a ambulância e seus registros de uso vinculados."""
        chassi = (chassi or "").strip()
        if not chassi:
            raise ValueError("Chassi não pode ser vazio.")

        id_amb = self.obter_id_ambulancia_por_chassi(chassi)
        if not id_amb:
            return False

        conn = self._get_conn()
        try:
            with conn.cursor() as cur:
                # 1) Remove registros de uso vinculados (respeita a FK)
                cur.execute("DELETE FROM registro_uso WHERE id_ambulancia = %s", (id_amb,))
                # 2) Remove a ambulância
                cur.execute("DELETE FROM ambulancia WHERE id_ambulancia = %s", (id_amb,))
                ok = cur.rowcount > 0
            conn.commit()
            return ok
        except Exception:
            conn.rollback()
            raise
        finally:
            conn.close()
    
    # ------------------ REGISTRO DE USO ------------------
    def inserir_registro_uso(
        self,
        *,
        total_km: int,
        motivo: Optional[str],
        data: date,
        rodou: str,
        id_ambulancia: Optional[int] = None,
        placa: Optional[str] = None,
        km_inicial: Optional[int] = None,
        km_final: Optional[int] = None,
    ) -> int:
        if id_ambulancia is None and placa:
            id_ambulancia = self.obter_id_ambulancia_por_placa(placa.strip())

        sql = """
            INSERT INTO registro_uso (total_km, rodou, motivo, data, id_ambulancia, km_inicial, km_final)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        conn = self._get_conn()
        try:
            with conn.cursor() as cur:
                cur.execute(sql, (total_km, rodou, motivo, data, id_ambulancia, km_inicial, km_final))
                new_id = cur.lastrowid
            conn.commit()
            return int(new_id)
        except Exception:
            conn.rollback()
            raise
        finally:
            conn.close()

    def listar_registros_uso(
        self,
        *,
        mes: Optional[int] = None,
        ano: Optional[int] = None,
        id_ambulancia: Optional[int] = None,
        placa: Optional[str] = None,
    ) -> List[Dict[str, Any]]:
        if id_ambulancia is None and placa:
            id_ambulancia = self.obter_id_ambulancia_por_placa(placa.strip())

        conditions = []
        params = []

        if mes is not None:
            conditions.append("MONTH(data) = %s")
            params.append(mes)
        if ano is not None:
            conditions.append("YEAR(data) = %s")
            params.append(ano)
        if id_ambulancia is not None:
            conditions.append("id_ambulancia = %s")
            params.append(id_ambulancia)

        where = f"WHERE {' AND '.join(conditions)}" if conditions else ""
        sql = f"""
            SELECT idRegistro_uso, total_km, rodou, motivo, data, id_ambulancia, km_inicial, km_final
            FROM registro_uso
            {where}
            ORDER BY data ASC
        """
        conn = self._get_conn()
        try:
            with conn.cursor() as cur:
                cur.execute(sql, params)
                return list(cur.fetchall() or [])
        finally:
            conn.close()