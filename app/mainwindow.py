from PySide6.QtWidgets import QMainWindow, QStackedWidget, QApplication
from PySide6.QtCore import Slot

# Views normais
from .views.login import Login 
from .views.telainicial import TelaInicial
from .views.relatorio import Relatorio
from .views.menu import menu
from .views.cadastro import Cadastro
from .views.telakm import telakm
from .views.modificar import Modificar

# 👉 importa o provider central
from .views.sugestoes import SugestoesProvider, DTOBase


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Meu Sistema")

        # --- Provider central de sugestões (uma instância para o app inteiro)
        self._sugestoes = SugestoesProvider()

        # --- Stack ---
        self._stack = QStackedWidget(self)
        self.setCentralWidget(self._stack)

        # --- Instanciar telas ---
        self.telainicial = TelaInicial()
        self.relatorio = Relatorio()
        self.menu = menu()
        self.telakm = telakm()
        # 👉 Passa o provider para a tela Modificar
        self.modificar = Modificar(self._sugestoes)
        self.cadastro = Cadastro()

        # --- Adiciona ao stack ---
        self._stack.addWidget(self.telainicial)
        self._stack.addWidget(self.relatorio)
        self._stack.addWidget(self.cadastro)
        self._stack.addWidget(self.telakm)
        self._stack.addWidget(self.modificar)
        self._stack.addWidget(self.menu)

        # --- Conectar sinal do botão Login da TelaInicial ---
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

        # --- (Opcional) Conectar cadastro/exclusão ao provider ---
        self._conectar_provider_ao_fluxo()

        self._usuario = None
        self._autenticado = False

        # --- MOSTRAR TELA INICIAL PRIMEIRO ---
        self.show_telainicial()
        self.resize(1280, 800)
        self.setMinimumSize(1000, 650)
        self.center_on_screen()

    # --------------------------- Utilitário para centralizar ---------------------------
    def center_on_screen(self) -> None:
        screen = self.screen() or QApplication.primaryScreen()
        if not screen:
            return
        geo = self.frameGeometry()
        geo.moveCenter(screen.availableGeometry().center())
        self.move(geo.topLeft())

    # ======================================================
    #                 MÉTODOS DE LOGIN  
    # ======================================================
    def _abrir_login(self) -> None:
        dialog = Login(self)
        if hasattr(dialog, "loggedIn"):
            dialog.loggedIn.connect(self._on_logged_in)

        result = dialog.exec()
        if result:
            self._autenticado = True
            usuario_nome = getattr(dialog, "usuario_logado", None)
            self._usuario = usuario_nome or getattr(dialog, "usuario", None)
            self.show_menu()

    @Slot(str)
    def _on_logged_in(self, nome: str):
        self._usuario = nome
        self._autenticado = True

    # ======================================================
    #                 ↙ PROTEÇÃO DE TELAS  
    # ======================================================
    def _require_login(self) -> bool:
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

    # ======================================================
    #       Provider ↔️ fluxo de cadastro/exclusão
    # ======================================================
    def _conectar_provider_ao_fluxo(self) -> None:
        """
        Conecta sinais de cadastro/exclusão ao provider de sugestões.
        Ajuste os nomes dos sinais conforme sua tela de cadastro.
        """
        # 1) Ao cadastrar uma ambulância, alimenta o provider incrementalmente
        if hasattr(self.cadastro, "submitted"):
            self.cadastro.submitted.connect(self._on_cadastrou_ambulancia)

        # 2) Ao excluir, recarrega tudo do DAO (evita remover valores ainda usados)
        #    Se sua tela de relatório/menu expõe um sinal 'excluida' com o id, conecte aqui:
        if hasattr(self.relatorio, "excluida"):
            self.relatorio.excluida.connect(self._on_excluiu_ambulancia)

        # 3) (Opcional) Carrega sugestões na inicialização a partir do DAO
        try:
            dao = getattr(self, "dao", None) or getattr(self, "_dao", None)
            if dao and hasattr(dao, "listar_todas"):
                todas = dao.listar_todas()
                self._sugestoes.load_from(
                    DTOBase(a.placa, a.chassi, a.cnes, a.denominacao) for a in todas
                )
        except Exception as e:
            print("[Sugestões] Aviso: não foi possível carregar sugestões iniciais:", e)

    @Slot(object)
    def _on_cadastrou_ambulancia(self, dto):
        """dto deve ter atributos: placa, chassi, cnes, denominacao"""
        try:
            self._sugestoes.on_cadastrada(DTOBase(dto.placa, dto.chassi, dto.cnes, dto.denominacao))
        except Exception as e:
            print("[Sugestões] Falha ao adicionar sugestão após cadastro:", e)

    @Slot(object)
    def _on_excluiu_ambulancia(self, _id):
        """
        Após excluir no banco, recarrega o provider a partir do DAO.
        Ajuste para chamar seu DAO real.
        """
        try:
            dao = getattr(self, "dao", None) or getattr(self, "_dao", None)
            if dao and hasattr(dao, "listar_todas"):
                todas = dao.listar_todas()
                self._sugestoes.on_excluida_recarregar(
                    DTOBase(a.placa, a.chassi, a.cnes, a.denominacao) for a in todas
                )
        except Exception as e:
            print("[Sugestões] Falha ao recarregar sugestões após exclusão:", e)