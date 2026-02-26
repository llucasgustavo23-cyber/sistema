from PySide6.QtWidgets import QWidget
from ui_telakm import Ui_telakm
from PySide6.QtCore import Signal

class telakm(QWidget,Ui_telakm):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)  # nome sempre é setupUi
        self.setWindowTitle("Tela inicial do sistema")
 