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

    def _wire(self):
        if hasattr(self, "homeBtn"):
            self.btnCadastroAmb.clicked.connect(self.gotoCadastro.emit)
        if hasattr(self, "homeBtn"):
            self.btnModificarAmb.clicked.connect(self.gotomodificar.emit)
        if hasattr(self, "homeBtn"):
            self.btnInserirDados.clicked.connect(self.gototelakm.emit)
        if hasattr(self, "homeBtn"):
            self.btnRelatorio.clicked.connect(self.gotoRelatorio.emit)
