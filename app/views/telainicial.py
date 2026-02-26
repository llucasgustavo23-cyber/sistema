# app/views/telainicial.py
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal
from .ui_telainicia import Ui_telainicia  # GERADO A PARTIR DE FORM "Widget"

class TelaInicial(QWidget, Ui_telainicia):
    gotoRelatorio = Signal()
    gotoLogin = Signal()

    def __init__(self):
        super().__init__()
        # Monta a UI criada no Designer dentro deste QWidget
        self.setupUi(self)
        self._wire()

    def _wire(self):
        """
        Conecte aqui os sinais dos botões que existem no seu .ui.
        Exemplo: se no Designer o botão 'Voltar/Logout' chama-se 'homeBtn',
        conectamos ao sinal gotoLogin. Se houver outro botão para Relatório,
        conecte ao gotoRelatorio.
        """
        # Botão que você mencionou:
        if hasattr(self, "homeBtn"):
            self.homeBtn.clicked.connect(self.gotoLogin.emit)

        # Exemplos de outros botões (ajuste os nomes conforme o seu .ui):
        if hasattr(self, "btnRelatorio"):
            self.btnRelatorio.clicked.connect(self.gotoRelatorio.emit)
        if hasattr(self, "btnSair"):
            self.btnSair.clicked.connect(self.gotoLogin.emit)

    # Se precisar receber dados do Login (ex.: usuário logado):
    def set_usuario(self, nome: str):
        if hasattr(self, "lblUsuario"):
            self.lblUsuario.setText(f"Bem-vindo, {nome}")