from PySide6.QtWidgets import QMainWindow, QStackedWidget
from PySide6.QtCore import Slot
from .views.login import Login
from .views.telainicial import TelaInicial
from .views.relatorio import Relatorio

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

        self._stack.addWidget(self.login)      # index 0
        self._stack.addWidget(self.telaincial)       # index 1
        self._stack.addWidget(self.relatorio)  # index 2

        # Conexões diretas entre sinais das telas e slots da MainWindow
        self.login.gotoTelaInicial.connect(self.show_telainicial)
        self.telaincial.gotoRelatorio.connect(self.show_relatorio)
        self.telaincial.gotoLogin.connect(self.show_login)
        self.relatorio.gotoTelaInicial.connect(self.show_telainicial)

        self.show_login()

    # ----- Navegação controlada pela MainWindow -----
    @Slot()
    def show_login(self) -> None:
        self._stack.setCurrentWidget(self.login)

    @Slot()
    def show_telainicial(self) -> None:
        # exemplo: se precisar enviar dados para Home, chame um método
        # self.home.set_usuario_logado(self.login.user())
        self._stack.setCurrentWidget(self.telaincial)

    @Slot()
    def show_relatorio(self) -> None:
        # exemplo: atualizar a tela antes de mostrar
        # self.relatorio.carregar_dados()
        self._stack.setCurrentWidget(self.relatorio)