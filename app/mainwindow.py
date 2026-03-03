from PySide6.QtWidgets import QMainWindow, QStackedWidget, QApplication
from PySide6.QtCore import Slot

# Views normais
from .views.login import Login              # QDialog
from .views.telainicial import TelaInicial
from .views.relatorio import Relatorio
from .views.menu import menu
from .views.cadastro import Cadastro
from .views.telakm import telakm
from .views.modificar import Modificar


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Meu Sistema")

        # --- Stack ---
        self._stack = QStackedWidget(self)
        self.setCentralWidget(self._stack)

        # --- Instanciar telas ---
        self.telainicial = TelaInicial()
        self.relatorio = Relatorio()
        self.cadastro = Cadastro()
        self.menu = menu()
        self.telakm = telakm()
        self.modificar = Modificar()

        # --- Adiciona ao stack ---
        self._stack.addWidget(self.telainicial)
        self._stack.addWidget(self.relatorio)
        self._stack.addWidget(self.cadastro)
        self._stack.addWidget(self.telakm)
        self._stack.addWidget(self.modificar)
        self._stack.addWidget(self.menu)

        # --- Conectar sinal do botão Login da TelaInicial ---
        # Quando clicar no botão de login → abre o QDialog Login
        if hasattr(self.telainicial, "gotoLogin"):
            self.telainicial.gotoLogin.connect(self._abrir_login)

        # --- Conectar sinais do menu ---
        if hasattr(self.menu, "gotoCadastro"):
            self.menu.gotoCadastro.connect(self.show_cadastro)
        if hasattr(self.menu, "gotomodificar"):
            self.menu.gotomodificar.connect(self.show_modificar)
        if hasattr(self.menu, "gotoRelatorio"):
            self.menu.gotoRelatorio.connect(self.show_relatorio)
        if hasattr(self.menu, "gototelakm"):
            self.menu.gototelakm.connect(self.show_telakm)

        # --- Conectar sinais para voltar ao Menu ---
        if hasattr(self.cadastro, "gotomenu"):
            self.cadastro.gotomenu.connect(self.show_menu)
        if hasattr(self.modificar, "gotomenu"):
            self.modificar.gotomenu.connect(self.show_menu)
        if hasattr(self.telakm, "gotomenu"):
            self.telakm.gotomenu.connect(self.show_menu)
        if hasattr(self.relatorio, "gotomenu"):
            self.relatorio.gotomenu.connect(self.show_menu)

        # --- Estado de login ---
        self._usuario = None
        self._autenticado = False

        # --- MOSTRAR TELA INICIAL PRIMEIRO ---
        self.show_telainicial()

        # ========= Opção 1: tamanho inicial + centralizar + tamanho mínimo =========
        self.resize(1280, 800)          # tamanho inicial ao abrir
        self.setMinimumSize(1000, 650)  # evita janela minúscula
        self.center_on_screen()         # centraliza na tela
        # ==========================================================================

    # --------------------------- Utilitário para centralizar ---------------------------
    def center_on_screen(self) -> None:
        """
        Centraliza a MainWindow na tela atual.
        """
        screen = self.screen() or QApplication.primaryScreen()
        if not screen:
            return
        geo = self.frameGeometry()
        geo.moveCenter(screen.availableGeometry().center())
        self.move(geo.topLeft())

    # ======================================================
    #                 ↙️  MÉTODOS DE LOGIN  ↘️
    # ======================================================
    def _abrir_login(self) -> None:
        """Abre o QDialog somente quando o usuário clicar em Login."""
        dialog = Login(self)
        if hasattr(dialog, "loggedIn"):
            dialog.loggedIn.connect(self._on_logged_in)

        result = dialog.exec()  # bloqueia até fechar

        if result:
            self._autenticado = True
            # Se o seu Login define self.usuario_logado, use-o:
            usuario_nome = getattr(dialog, "usuario_logado", None)
            # Caso contrário, tente 'usuario' como fallback:
            self._usuario = usuario_nome or getattr(dialog, "usuario", None)
            self.show_menu()  # Vá para o menu depois do login
        else:
            # Login cancelado → fica na TelaInicial
            pass

    @Slot(str)
    def _on_logged_in(self, nome: str):
        self._usuario = nome
        self._autenticado = True

    # ======================================================
    #                 ↙️  PROTEÇÃO DE TELAS  ↘️
    # ======================================================
    def _require_login(self) -> bool:
        """Protege as telas — só acessa se estiver logado."""
        if self._autenticado:
            return True
        self._abrir_login()
        return self._autenticado

    # ======================================================
    #                 ↙️  MÉTODOS DE NAVEGAÇÃO  ↘️
    # ======================================================
    @Slot()
    def show_telainicial(self) -> None:
        self._stack.setCurrentWidget(self.telainicial)

    @Slot()
    def show_relatorio(self) -> None:
        if not self._require_login():
            return
        self._stack.setCurrentWidget(self.relatorio)

    @Slot()
    def show_modificar(self) -> None:
        if not self._require_login():
            return
        self._stack.setCurrentWidget(self.modificar)

    @Slot()
    def show_telakm(self) -> None:
        if not self._require_login():
            return
        self._stack.setCurrentWidget(self.telakm)

    @Slot()
    def show_menu(self) -> None:
        if not self._require_login():
            return
        self._stack.setCurrentWidget(self.menu)

    @Slot()
    def show_cadastro(self) -> None:
        if not self._require_login():
            return
        self._stack.setCurrentWidget(self.cadastro)
