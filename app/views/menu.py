from PySide6.QtWidgets import QWidget
from app.views.ui_menu import Ui_menu
from PySide6.QtCore import Signal


class menu (QWidget, Ui_menu ):
    gotoCadastro = Signal()
    gotoRelatorio = Signal()
    gotomodificar = Signal
    gototelakm = Signal()

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self) 
        self.setWindowTitle("Tela inicial do sistema")
        self._wire()