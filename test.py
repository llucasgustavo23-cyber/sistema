from PySide6.QtWidgets import QApplication, QMainWindow
from app.views.ui_telainicia import Ui_telainicial
from app.views.ui_menu import Ui_menu
from app.views.ui_relatorio import Ui_relatorio
from app.views.ui_teladecadastro import Ui_cadastro
from app.views.ui_teladelogin import Ui_login
from app.views.ui_telademodifica import Ui_modificar
from app.views.ui_telakm import Ui_telakm

import sys




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
 