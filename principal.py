# import pymysql

# DB_CONFIG = {
#     "host": "localhost",
#     "user": "root",
#     "password": "",
#     "database": "LUCAS",
#     "charset": "utf8mb4",
#     "cursorclass": pymysql.cursors.Cursor,
#     "autocommit": False
# }

# # Função para conectar ao banco
# def conectar():
#     print('Concluido')
#     return pymysql.connect(**DB_CONFIG)

# db_mysql.py
import pymysql
from pymysql.cursors import DictCursor
from tkinter import messagebox

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "sistema",
    "charset": "utf8mb4",
    "cursorclass": DictCursor,  # retorna dict nas consultas
    "autocommit": False,        # melhor controle transacional
}

def conectar():
    """Abre e retorna uma conexão com o MySQL usando PyMySQL."""
    # Evite prints aqui; deixe a função só conectar.
    return pymysql.connect(**DB_CONFIG)

def testar_conexao(verbose: bool = True) -> bool:
    """
    Testa a conexão de ponta a ponta:
    - Abre a conexão
    - Dá ping (reconnect=True)
    - Executa SELECT 1
    - Fecha a conexão
    Retorna True/False.
    """
    try:
        conn = conectar()
        # Confirma que o socket está ok; reconecta se necessário
        conn.ping(reconnect=True)

        with conn.cursor() as cur:
            cur.execute("SELECT 1;")
            _ = cur.fetchone()

        conn.close()
        if verbose:
            print("✔ Conexão com MySQL OK!")
        return True
    except Exception as e:
        if verbose:
            print("❌ Falha na conexão com MySQL:", repr(e))
        return False

def executar(sql: str, params: tuple | dict = None, commit: bool = False) -> int:
    """
    Executa INSERT/UPDATE/DELETE. Retorna número de linhas afetadas.
    Use params para evitar SQL injection.
    """
    conn = None
    try:
        conn = conectar()
        with conn.cursor() as cur:
            cur.execute(sql, params)
        if commit:
            conn.commit()
        return cur.rowcount
    except Exception:
        if conn:
            conn.rollback()
        raise
    finally:
        if conn:
            conn.close()

def consultar(sql: str, params: tuple | dict = None) -> list[dict]:
    """
    Executa SELECT e retorna lista de dicionários (com DictCursor).
    """
    conn = None
    try:
        conn = conectar()
        with conn.cursor() as cur:
            cur.execute(sql, params)
            return list(cur.fetchall())
    finally:
        if conn:
            conn.close()



#Estabelecer os butoes



#tela inicial


#login


#menu


#cadastro

#modificar

#relatório


#telakm


