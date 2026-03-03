# app/views/login.py
from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtCore import Signal

# importa sua UI gerada pelo Qt Designer
from app.views.ui_login import Ui_login
# importa sua classe de banco (pymysql)
from app.database import Database


class Login(QDialog, Ui_login):
    """
    QDialog de Login que usa:
      - UI do Qt Designer (Ui_login) com os seguintes widgets:
          * QLineEdit de usuário  -> self.lineEdit
          * QLineEdit de senha    -> self.lineEdit_2
          * QPushButton Entrar    -> self.btnEntrar
          * (Opcional) QPushButton Cadastrar -> self.btnCadastrar (não usado aqui)
      - Validação no MySQL via Database.checar_usuario(usuario, senha)
    """
    loggedIn = Signal(str)  # emite o "name" do usuário (para MainWindow)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)                 # monta a UI do Designer
        self.setWindowTitle("Login")

        self.db = Database()
        self.usuario_logado = None

        # Assegura que o campo de senha está como Password (já está no UI, mas reforçamos):
        try:
            self.lineEdit_2.setEchoMode(self.lineEdit_2.EchoMode.Password)
        except Exception:
            pass

        # Conexões dos botões
        self.btnEntrar.clicked.connect(self._tentar_login)

        # Se quiser fechar/ocultar a opção de "Cadastrar" (não há cadastro no app)
        # você pode ocultar o botão:
        # self.btnCadastrar.hide()
        # ou, se preferir, desconectar qualquer uso:
        # self.btnCadastrar.clicked.disconnect()

        # Enter no campo de senha efetua login
        self.lineEdit_2.returnPressed.connect(self._tentar_login)

    # ----------------------------------------------------
    #                    LÓGICA DE LOGIN
    # ----------------------------------------------------
    def _tentar_login(self):
        usuario = self.lineEdit.text().strip()
        senha = self.lineEdit_2.text().strip()

        # validações simples de preenchimento
        if not usuario:
            self._mostrar_erro("Informe o usuário.")
            self.lineEdit.setFocus()
            return

        if not senha:
            self._mostrar_erro("Informe a senha.")
            self.lineEdit_2.setFocus()
            return

        # consulta no banco (MySQL) usando sua classe Database
        try:
            result = self.db.checar_usuario(usuario, senha)
        except Exception as e:
            self._mostrar_erro("Falha ao consultar o banco de dados.")
            # Se quiser logar o erro no console:
            print("[Login] Erro ao checar usuário:", e)
            return

        if result:
            # result deve ter: {"name": "...", "user": "..."}
            nome_real = result.get("name") or result.get("user") or usuario
            self.usuario_logado = nome_real
            self.loggedIn.emit(nome_real)
            self.accept()  # fecha o QDialog com Accepted
        else:
            self._mostrar_erro("Usuário ou senha inválidos.")

    # ----------------------------------------------------
    #                      HELPERS UI
    # ----------------------------------------------------
    def _mostrar_erro(self, mensagem: str):
        """
        Exibe um aviso de erro. Você pode:
          - Usar QMessageBox, OU
          - Reaproveitar o lblSubtitulo para feedback visual.
        Abaixo, uso as duas abordagens (comente a que não quiser).
        """

        # 1) Opção: feedback inline no lblSubtitulo
        try:
            self.lblSubtitulo.setText(mensagem)
            self.lblSubtitulo.setStyleSheet("color: #ff6b6b; font-weight: 600;")
        except Exception:
            pass

        # 2) Opção: popup modal
        # QMessageBox.warning(self, "Login", mensagem)