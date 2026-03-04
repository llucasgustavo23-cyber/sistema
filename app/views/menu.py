from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal
from .ui_menu import Ui_menu


class menu(QWidget, Ui_menu):
   
    gotoCadastro = Signal()
    gotoRelatorio = Signal()
    gotomodificar = Signal()
    gototelakm = Signal()
    gotoInicio = Signal()

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Tela inicial do sistema")
        self._wire()

    def _wire(self):
        
        if hasattr(self, "btnCadastroAmb"):
            self.btnCadastroAmb.clicked.connect(self.gotoCadastro.emit)
        else:
            print("[menu] Aviso: btnCadastroAmb não encontrado na UI")

        if hasattr(self, "btnModificarAmb"):
            self.btnModificarAmb.clicked.connect(self.gotomodificar.emit)
        else:
            print("[menu] Aviso: btnModificarAmb não encontrado na UI")

        if hasattr(self, "btnInserirDados"):
            self.btnInserirDados.clicked.connect(self.gototelakm.emit)
        else:
            print("[menu] Aviso: btnInserirDados não encontrado na UI")

        if hasattr(self, "btnRelatorio"):
            self.btnRelatorio.clicked.connect(self.gotoRelatorio.emit)
        else:
            print("[menu] Aviso: btnRelatorio não encontrado na UI")

        if hasattr(self, "btnInicio"):
             self.btnInicio.clicked.connect(self.gotoInicio.emit)
