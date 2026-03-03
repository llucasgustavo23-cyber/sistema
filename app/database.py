import pymysql
from pymysql.cursors import DictCursor

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "sistema",
    "charset": "utf8mb4",
    "cursorclass": DictCursor,
    "autocommit": False,
}

class Database:
    def __init__(self):
        self.connection = None

    def conectar(self):
        if not self.connection:
            self.connection = pymysql.connect(**DB_CONFIG)
        return self.connection

    # ---------------------------
    # INSERIR USUÁRIO (admin cria)
    # ---------------------------
    def insert_user(self, usuario, senha):
        cursor = None
        try:
            self.conectar()
            cursor = self.connection.cursor()

            sql = """
                INSERT INTO funcionarios (usuario, senha)
                VALUES (%s, %s)
            """
            cursor.execute(sql, (usuario, senha))
            self.connection.commit()
            return True

        except Exception as e:
            if self.connection:
                self.connection.rollback()
            print("Erro ao inserir usuário:", e)
            return False

        finally:
            if cursor:
                cursor.close()

    # ---------------------------
    # VERIFICAR USUÁRIO (login)
    # ---------------------------
    def checar_usuario(self, usuario, senha):
        cursor = None
        try:
            self.conectar()
            cursor = self.connection.cursor()

            sql = """
                SELECT usuario
                FROM funcionarios
                WHERE usuario= %s AND senha = %s
                LIMIT 1
            """
            cursor.execute(sql, (usuario, senha))
            result = cursor.fetchone()

            return result  # Ex.: {"name": "Lucas Souza", "user": "lucas"} ou None

        except Exception as e:
            print("Erro ao consultar usuário:", e)
            return None

        finally:
            if cursor:
                cursor.close()

    # ---------------------------
    # CADASTRAR AMBULÂNCIA
    # ---------------------------
    def cadastra_ambulan(self, chassi, placa, ano, data_aquisicao):
        cursor = None
        try:
            self.conectar()
            cursor = self.connection.cursor()

            sql = """
                INSERT INTO ambulancia (chassi, placa, ano, data_aquisicao)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(sql, (chassi, placa, ano, data_aquisicao))
            self.connection.commit()
            return True

        except Exception as e:
            if self.connection:
                self.connection.rollback()
            print("Erro ao inserir ambulância:", e)
            return False

        finally:
            if cursor:
                cursor.close()

    # ---------------------------
    # ATUALIZAR AMBULÂNCIA
    # ---------------------------
    def update_ambulancia(self, chassi, placa=None, ano=None, data_aquisicao=None):
        """
        Atualiza campos da ambulância identificada por 'chassi'.
        Só atualiza os campos que não forem None.
        """
        if not any([placa, ano, data_aquisicao]):
            return False

        cursor = None
        try:
            self.conectar()
            cursor = self.connection.cursor()

            sets = []
            params = []

            if placa is not None:
                sets.append("placa = %s")
                params.append(placa)

            if ano is not None:
                sets.append("ano = %s")
                params.append(ano)

            if data_aquisicao is not None:
                sets.append("data_aquisicao = %s")
                params.append(data_aquisicao)

            params.append(chassi)

            sql = f"""
                UPDATE ambulancia
                SET {', '.join(sets)}
                WHERE chassi = %s
            """

            rows = cursor.execute(sql, params)
            self.connection.commit()
            return rows > 0

        except Exception as e:
            if self.connection:
                self.connection.rollback()
            print("Erro ao atualizar ambulância:", e)
            return False

        finally:
            if cursor:
                cursor.close()


#Estabelecer os butoes



#tela inicial


#login


#menu


#cadastro

#modificar

#relatório


#telakm


