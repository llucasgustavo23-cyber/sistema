# app/mainwindow.py
from PySide6.QtWidgets import QMainWindow, QStackedWidget, QApplication, QMessageBox
from PySide6.QtCore import Slot

from .views.login import Login
from .views.telainicial import TelaInicial
from .views.relatorio import Relatorio
from .views.menu import menu
from .views.cadastro import Cadastro
from .views.telakm import telakm
# CORREÇÃO: Modificar agora é QDialog — não vai mais para o stack
from .views.modificar import Modificar
from .views.listardados import listardados
from .views.sugestoes import SugestoesProvider, DTOBase
from .views.usuario import usuario
from .database import Database


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("SCT")

        self._sugestoes = SugestoesProvider()
        self.db = Database()

        self._stack = QStackedWidget(self)
        self.setCentralWidget(self._stack)

        # Widgets do stack (apenas QWidgets, não QDialogs)
        self.telainicial = TelaInicial()
        self.relatorio   = Relatorio()
        self.menu_widget = menu()         # renomeado internamente para evitar conflito
        self.telakm      = telakm()
        self.listardados = listardados()
        self.cadastro    = Cadastro()
        # CORREÇÃO: Modificar saiu do stack — é aberto como QDialog por listardados

        self._stack.addWidget(self.telainicial)
        self._stack.addWidget(self.relatorio)
        self._stack.addWidget(self.cadastro)
        self._stack.addWidget(self.telakm)
        self._stack.addWidget(self.menu_widget)
        self._stack.addWidget(self.listardados)

        # Tela inicial
        if hasattr(self.telainicial, "gotoLogin"):
            self.telainicial.gotoLogin.connect(self._abrir_login)

        # Menu → navegação
        # CORREÇÃO: btnModificarAmb agora vai para listardados (não para show_modificar)
        if hasattr(self.menu_widget, "gotoCadastro"):
            self.menu_widget.gotoCadastro.connect(self.show_cadastro)
        if hasattr(self.menu_widget, "gotomodificar"):
            self.menu_widget.gotomodificar.connect(self.show_listardados)   # <-- corrigido
        if hasattr(self.menu_widget, "gotoRelatorio"):
            self.menu_widget.gotoRelatorio.connect(self.show_relatorio)
        if hasattr(self.menu_widget, "gototelakm"):
            self.menu_widget.gototelakm.connect(self.show_telakm)
        if hasattr(self.menu_widget, "gotolistardados"):
            self.menu_widget.gotolistardados.connect(self.show_listardados)
        # CORREÇÃO: era "gotoinicio" (typo) → "gotoInicio"
        if hasattr(self.menu_widget, "gotoInicio"):
            self.menu_widget.gotoInicio.connect(self.show_telainicial)

        # Telas → voltar ao menu
        for tela in (self.cadastro, self.relatorio, self.telakm, self.listardados):
            if hasattr(tela, "gotomenu"):
                tela.gotomenu.connect(self.show_menu)

        # CORREÇÃO: listardados.gotomenu não estava conectado
        # (já coberto pelo loop acima, mas deixo explícito para clareza)

        # Botão "Cadastrar Usuário" no menu
        if hasattr(self.menu_widget, "gotousuario"):
            self.menu_widget.gotousuario.connect(self._abrir_usuario)

        # Sugestões
        self._conectar_provider_ao_fluxo()

        self._usuario      = None
        self._autenticado  = False
        self._role         = "visualizador"

        self.show_telainicial()
        self.resize(1280, 800)
        self.setMinimumSize(1000, 650)
        self.center_on_screen()

    # --------------------------------------------------------
    # CENTER
    # --------------------------------------------------------
    def center_on_screen(self) -> None:
        screen = self.screen() or QApplication.primaryScreen()
        if not screen:
            return
        geo = self.frameGeometry()
        geo.moveCenter(screen.availableGeometry().center())
        self.move(geo.topLeft())

    # --------------------------------------------------------
    # LOGIN
    # --------------------------------------------------------
    def _abrir_login(self) -> None:
        dialog = Login(self)
        dialog.loggedIn.connect(self._on_logged_in)

        if dialog.exec():
            self._autenticado = True
            self._usuario     = dialog.usuario_logado
            self._role        = getattr(dialog, "role", "visualizador")
            self._aplicar_permissoes_menu()
            self.show_menu()

    @Slot(str)
    def _on_logged_in(self, nome: str):
        self._usuario     = nome
        self._autenticado = True

    # --------------------------------------------------------
    # PROTEÇÃO
    # --------------------------------------------------------
    def _require_login(self) -> bool:
        if self._autenticado:
            return True
        self._abrir_login()
        return self._autenticado

    def _deny(self, msg: str = "Acesso negado para seu perfil.") -> None:
        QMessageBox.warning(self, "Permissão", msg)

    def _require_role(self, allowed: set[str]) -> bool:
        if getattr(self, "_role", "visualizador") in allowed:
            return True
        self._deny()
        return False

    # --------------------------------------------------------
    # NAVEGAÇÃO
    # --------------------------------------------------------
    @Slot()
    def show_telainicial(self) -> None:
        self._stack.setCurrentWidget(self.telainicial)

    @Slot()
    def show_relatorio(self) -> None:
        if not self._require_login():
            return
        self._stack.setCurrentWidget(self.relatorio)

    @Slot()
    def show_telakm(self) -> None:
        if not self._require_login():
            return
        if not self._require_role({"admin", "operador"}):
            return
        self._stack.setCurrentWidget(self.telakm)

    @Slot()
    def show_menu(self) -> None:
        if not self._require_login():
            return
        self._stack.setCurrentWidget(self.menu_widget)

    @Slot()
    def show_cadastro(self) -> None:
        if not self._require_login():
            return
        if not self._require_role({"admin"}):
            return
        self._stack.setCurrentWidget(self.cadastro)

    @Slot()
    def show_listardados(self) -> None:
        if not self._require_login():
            return
        self._stack.setCurrentWidget(self.listardados)

    # CORREÇÃO: show_modificar removido do stack.
    # Modificar é aberto como QDialog diretamente em listardados._on_modificar().

    # --------------------------------------------------------
    # DIALOG USUÁRIO
    # --------------------------------------------------------
    @Slot()
    def _abrir_usuario(self) -> None:
        if not self._require_login():
            return
        if not self._require_role({"admin"}):
            return
        dlg = usuario(self)
        dlg.submitted.connect(self._on_usuario_cadastrado)
        dlg.exec()

    @Slot(str, str, str)
    def _on_usuario_cadastrado(self, usuario_txt: str, senha_txt: str, role: str):
        try:
            self.db.criar_usuario(usuario_txt, senha_txt, role)
            QMessageBox.information(
                self, "Usuários",
                f"Usuário '{usuario_txt}' criado com perfil '{role}'."
            )
        except Exception as e:
            QMessageBox.critical(self, "Usuários", f"Falha ao criar usuário: {e}")

    # --------------------------------------------------------
    # RBAC: habilitar/desabilitar botões do menu
    # --------------------------------------------------------
    def _aplicar_permissoes_menu(self) -> None:
        role = getattr(self, "_role", "visualizador")

        btns = {
            "cadastro_amb": getattr(self.menu_widget, "btnCadastroAmb",   None),
            "modificar":    getattr(self.menu_widget, "btnModificarAmb",  None),
            "relatorio":    getattr(self.menu_widget, "btnRelatorio",      None),
            "inserir":      getattr(self.menu_widget, "btnInserirDados",   None),
            "lista":        getattr(self.menu_widget, "pushButton_2",      None),
            "usuario":      getattr(self.menu_widget, "pushButton",        None),
        }

        def set_allowed(allowed_keys: set) -> None:
            for key, btn in btns.items():
                if btn:
                    btn.setEnabled(key in allowed_keys)

        if role == "admin":
            set_allowed(set(btns.keys()))
        elif role == "operador":
            set_allowed({"modificar", "relatorio", "inserir", "lista"})
        else:  # visualizador
            set_allowed({"relatorio", "lista"})

    # --------------------------------------------------------
    # PROVIDER DE SUGESTÕES
    # --------------------------------------------------------
    def _conectar_provider_ao_fluxo(self) -> None:
        if hasattr(self.cadastro, "submitted"):
            self.cadastro.submitted.connect(self._on_cadastrou_ambulancia)
        if hasattr(self.relatorio, "excluida"):
            self.relatorio.excluida.connect(self._on_excluiu_ambulancia)

    @Slot(object)
    def _on_cadastrou_ambulancia(self, dto):
        try:
            self._sugestoes.on_cadastrada(
                DTOBase(dto.placa, dto.chassi, dto.cnes, dto.denominacao)
            )
        except Exception as e:
            print("[Sugestões] Falha:", e)

    @Slot(object)
    def _on_excluiu_ambulancia(self, _id):
        print("Ambulância excluída")