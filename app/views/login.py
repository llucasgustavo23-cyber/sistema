
from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Signal
from .ui_teladelogin import Ui_login  

class Login(QDialog, Ui_login):
    gotoTelaInicial = Signal()
    gotoCadastro = Signal()
    loggedIn = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)  

        self.setWindowTitle("Login")
        self.setModal(True)  

        self._wire()

    def _wire(self):
        self.btnEntrar.clicked.connect(self._on_entrar)
        if hasattr(self, "btnCadastrar"):
            self.btnCadastrar.clicked.connect(self.gotoCadastro.emit)

    def _on_entrar(self):
        usuario = self.txtUsuario.text().strip()
        senha   = self.txtSenha.text().strip()

        if not usuario or not senha:
            self.lblMensagem.setText("Preencha usuário e senha.")
            return

        if self._auth(usuario, senha):
            self.lblMensagem.setText("Login realizado.")
            self.loggedIn.emit(usuario)

            self.accept()
        else:
            self.lblMensagem.setText("Usuário ou senha inválidos.")

    def _auth(self, usuario: str, senha: str) -> bool:
        return usuario == "admin" and senha == "123"

