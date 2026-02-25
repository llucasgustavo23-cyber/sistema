from PySide6.QtWidgets import QApplication, QMainWindow
from ui_telainicia import Ui_telainicial
from ui_menu import Ui_menu
from ui_relatorio import Ui_relatorio
from ui_teladecadastro import Ui_cadastro
from ui_teladelogin import Ui_login
from ui_telademodifica import Ui_modificar
from ui_telakm import Ui_telakm

import sys

class TelaInicial(QMainWindow, Ui_telainicial):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)  # nome sempre é setupUi
        self.setWindowTitle("Tela inicial do sistema")
        
class menu (QMainWindow, Ui_menu ):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)  # nome sempre é setupUi
        self.setWindowTitle("Tela inicial do sistema")

class relatorio(QMainWindow, Ui_relatorio):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)  # nome sempre é setupUi
        self.setWindowTitle("Tela inicial do sistema")

class cadastro(QMainWindow,Ui_cadastro):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)  # nome sempre é setupUi
        self.setWindowTitle("Tela inicial do sistema")

class modificar(QMainWindow,Ui_modificar ):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)  # nome sempre é setupUi
        self.setWindowTitle("Tela inicial do sistema")

class login(QMainWindow,Ui_login ):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)  # nome sempre é setupUi
        self.setWindowTitle("Tela inicial do sistema")

class telakm(QMainWindow,Ui_telakm):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)  # nome sempre é setupUi
        self.setWindowTitle("Tela inicial do sistema")
 