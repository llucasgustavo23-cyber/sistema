from PySide6.QtWidgets import QWidget, QDialogButtonBox
from PySide6.QtCore import Signal
from ui_teladecadastro import Ui_cadastro

class cadastro(QWidget, Ui_cadastro):
    gotomenu = Signal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Cadastro Ambulância")
        self._wire()

    def atributo(self):
        self.buttonBox = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
            parent=self
        )
        self.buttonBox.accepted.connect(self.ir_para_menu)  
        self.buttonBox.rejected.connect(self.close)         

    def ir_para_menu(self):
        # Se preferir sinal:
        self.gotomenu.emit()
        print("Indo para o menu…")

