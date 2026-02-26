from PySide6.QtWidgets import QWidget
from app.views.ui_menu import Ui_menu


class menu (QWidget, Ui_menu ):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)  # nome sempre é setupUi
        self.setWindowTitle("Tela inicial do sistema")
