from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal
from ui_telademodifica import Ui_modificar


class modificar(QWidget,Ui_modificar ):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)  # nome sempre é setupUi
        self.setWindowTitle("Tela inicial do sistema")
