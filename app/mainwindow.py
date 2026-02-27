from PySide6.QtWidgets import QMainWindow, QStackedWidget
from PySide6.QtCore import Slot
from .views.login import Login
from .views.telainicial import TelaInicial
from .views.relatorio import Relatorio
# from .views.menu import menu
# from .views.cadastro import cadastro
# from .views.telakm import telakm
# from .views.modificar import modificar
# from .views.principal import *

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Meu Sistema")

        self._stack = QStackedWidget(self)
        self.setCentralWidget(self._stack)

        # Instancia as telas uma vez (ou poderia ser lazy)
        self.login = Login()
        self.telaincial = TelaInicial()
        self.relatorio = Relatorio()
        # self.cadastro = cadastro()
        # self.menu = menu()
        # self.telakm = telakm()
        # self.modificar = modificar()

        self._stack.addWidget(self.login)     
        self._stack.addWidget(self.telaincial)       
        self._stack.addWidget(self.relatorio)
        # self._stack.addWidget(self.menu)   
        # self._stack.addWidget(self.cadastro)  
        # self._stack.addWidget(self.telakm)  
        # self._stack.addWidget(self.modificar)  

        # Conexões diretas entre sinais das telas e slots da MainWindow
        self.telaincial.gotoLogin.connect(self.show_login)
        # self.menu.gotocadastro.connect(self.show_cadastro)
        # self.menu.gotomodificar.connect(self.show_modificar)
        # self.menu.gotoRelatorio.connect(self.show_relatorio)
        # self.menu.gototelakm.connect(self.show_telakm)
        # self.login.gotomenu.connect(self.show_menu)

        self.show_telainicial()

    
    def show_login(self):
        dialog = Login(self)   
        dialog.loggedIn.connect(self._usuario_logado)

        resultado = dialog.exec()  
        if resultado:
            print("Login OK")
        else:
            print("Login cancelado ou inválido")

    def _usuario_logado(self, usuario):
        print(f"Usuário autenticado: {usuario}")
        self.show_telainicial()  

    
    def show_telainicial(self) -> None:
        # exemplo: se precisar enviar dados para Home, chame um método
        # self.home.set_usuario_logado(self.login.user())
        self._stack.setCurrentWidget(self.telaincial)


    def show_relatorio(self) -> None:
        # exemplo: atualizar a tela antes de mostrar
        # self.relatorio.carregar_dados()
        self._stack.setCurrentWidget(self.relatorio)

    # def show_menu(self) -> None:
    #     self._stack.setCurrentWidget(self.menu)

    # def show_cadastro(self) -> None:
    #     self._stack.setCurrentWidget(self.cadastro)

    # def show_modificart(self) ->None:
    #     self._stack.setCurrentWidget(self.modificar)

    # def show_telakm(self) -> None:
    #     self._stack.setCurrentWidget(self.telakm)    


