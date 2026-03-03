# app/views/telainicial.py
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal
from .ui_telainicia import Ui_telainicia  

class TelaInicial(QWidget, Ui_telainicia):
    gotoLogin = Signal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self._wire()

    def Atributo(self):
        # Conecte aqui os sinais dos botões que existem no seu .ui.
        # Exemplo: se no Designer o botão 'Voltar/Logout' chama-se 'homeBtn',
        # conectamos ao sinal gotoLogin. Se houver outro botão para Relatório,
        # conecte ao gotoRelatorio.
        # Botão que você mencionou:
        if hasattr(self, "homeBtn"):
            self.homeBtn.clicked.connect(self.gotoLogin.emit)
        if hasattr(self, "btnRelatorio"):
            self.btnRelatorio.clicked.connect(self.gotoRelatorio.emit)
        if hasattr(self, "btnSair"):
            self.btnSair.clicked.connect(self.gotoLogin.emit)

    # Se precisar receber dados do Login (ex.: usuário logado):
    def seu_usuario(self, nome: str):
        if hasattr(self, "lblUsuario"):
            self.lblUsuario.setText(f"Bem-vindo, {nome}")

    
# hasattr Ela serve para verificar se um objeto possui um atributo específico (como uma variável interna ou método).

