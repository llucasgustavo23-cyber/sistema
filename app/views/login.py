# app/views/login.py
from PySide6.QtWidgets import QWidget, QMainWindow, QVBoxLayout
from PySide6.QtCore import Signal
from .ui_teladelogin import Ui_login  # GERADO A PARTIR DE MAIN WINDOW

class Login(QWidget):
    gotoTelaInicial = Signal()
    gotoCadastro = Signal()
    loggedIn = Signal(str)

    def __init__(self):
        super().__init__()

        # Monta o .ui em um QMainWindow temporário
        temp = QMainWindow()
        self.ui = Ui_login()
        self.ui.setupUi(temp)              # aqui tudo funciona, pois é QMainWindow
        from PySide6.QtWidgets import QWidget
        children = [c for c in self.findChildren(QWidget)]
        print(f"[DEBUG {self.__class__.__name__}] filhos QWidget:", len(children))
        for c in children[:5]:
            print("  -", c.objectName(), type(c).__name__)
        # Extrai o centralWidget do temp e coloca dentro deste QWidget
        cw = temp.centralWidget()
        temp.setCentralWidget(None)

        
        self._wire()

    def _wire(self):
        self.ui.btnEntrar.clicked.connect(self._on_entrar)
       
    def _on_entrar(self):
        usuario = self.ui.txtUsuario.text().strip()
        senha = self.ui.txtSenha.text()
        if not usuario or not senha:
            self.ui.lblMensagem.setText("Preencha usuário e senha.")
            return
        if self._auth(usuario, senha):
            self.ui.lblMensagem.setText("Login realizado.")
            self.loggedIn.emit(usuario)
            self.gotoTelaInicial.emit()
        else:
            self.ui.lblMensagem.setText("Usuário ou senha inválidos.")

    def _on_cancelar(self):
        self.ui.txtSenha.clear()
        self.ui.lblMensagem.clear()

    def _auth(self, usuario, senha) -> bool:
        return usuario == "admin" and senha == "123"
