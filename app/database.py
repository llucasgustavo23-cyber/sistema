# app/database.py
from __future__ import annotations

import os
import base64
import hmac
from hashlib import pbkdf2_hmac
from secrets import token_bytes
from typing import Optional, Dict, List, Any

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


def _verify_password(password: str, algo: str, salt_b64: str, iterations: int, hash_b64: str) -> bool:
   
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

                ok = _verify_password(
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
        """
        Lista usuários (sem retornar salt/hash por segurança).
        """
        sql = "SELECT idfuncionarios, usuario, role, created_at FROM funcionarios ORDER BY id DESC"
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


#tela inicial


#login


#menu


#cadastro

#modificar

#relatório


#telakm


