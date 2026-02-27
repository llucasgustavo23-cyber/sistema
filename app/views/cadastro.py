from PySide6.QtWidgets import QWidget
from ui_teladecadastro import Ui_cadastro
from PySide6.QtCore import Signal


class cadastro(QWidget,Ui_cadastro):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)  # nome sempre é setupUi
        self.setWindowTitle("Tela inicial do sistema")     