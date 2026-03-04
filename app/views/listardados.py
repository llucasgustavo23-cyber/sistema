from PySide6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from PySide6.QtCore import Signal, QDate
from .ui_lista import Ui_listardados 


class listardados(QWidget, Ui_listardados):
    gotomenu = Signal()
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
    def _wire(self) -> None:
        if hasattr(self, "btnvolta") and self.pushButton:
            self.pushButton.clicked.connect(self.gotomenu.emit)
        else:
            print("[listardado] Aviso: pushbutton não encontrado na UI")
