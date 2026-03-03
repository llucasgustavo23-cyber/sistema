from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal
from .ui_telainicia import Ui_telainicia  

class TelaInicial(QWidget, Ui_telainicia):
    gotoLogin = Signal()
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self._wire()

    def _wire(self):
        # Botão "Login" → abre o QDialog de Login via MainWindow
        self.homeBtn.clicked.connect(self.gotoLogin.emit)

    # Se quiser exibir o usuário logado depois:
    def seu_usuario(self, nome: str):
        if hasattr(self, "lblUsuario"):
            self.lblUsuario.setText(f"Bem-vindo, {nome}")
