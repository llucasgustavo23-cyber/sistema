# app/mainwindow.py
from PySide6.QtWidgets import QMainWindow, QStackedWidget, QApplication, QMessageBox
from PySide6.QtCore import Slot

# Views normais
from .views.login import Login
from .views.telainicial import TelaInicial
from .views.relatorio import Relatorio
from .views.menu import menu
from .views.cadastro import Cadastro
from .views.telakm import telakm
from .views.modificar import Modificar
from .views.listardados import listardados
from .views.sugestoes import SugestoesProvider, DTOBase
from .views.usuario import usuario  
from .database import Database


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("SCT")

        # Provider
        self._sugestoes = SugestoesProvider()

        # DB compartilhado
        self.db = Database()

        # Stack
        self._stack = QStackedWidget(self)
        self.setCentralWidget(self._stack)

        # Instanciar telas do STACK (QWidgets)
        self.telainicial = TelaInicial()
        self.relatorio = Relatorio()
        self.menu = menu()
        self.telakm = telakm()
        self.listardados = listardados()
        self.modificar = Modificar(self._sugestoes)
        self.cadastro = Cadastro()


        # ADICIONAR APENAS WIDGETS (não QDialogs!)
        self._stack.addWidget(self.telainicial)
        self._stack.addWidget(self.relatorio)
        self._stack.addWidget(self.cadastro)
        self._stack.addWidget(self.telakm)
        self._stack.addWidget(self.modificar)
        self._stack.addWidget(self.menu)
        self._stack.addWidget(self.listardados)

        # Conectar tela inicial
        if hasattr(self.telainicial, "gotoLogin"):
            self.telainicial.gotoLogin.connect(self._abrir_login)

        # Conectar menu -> navegação
        if hasattr(self.menu, "gotoCadastro"):
            self.menu.gotoCadastro.connect(self.show_cadastro)
        if hasattr(self.menu, "gotomodificar"):
            self.menu.gotomodificar.connect(self.show_modificar)
        if hasattr(self.menu, "gotoRelatorio"):
            self.menu.gotoRelatorio.connect(self.show_relatorio)
        if hasattr(self.menu, "gototelakm"):
            self.menu.gototelakm.connect(self.show_telakm)
        if hasattr(self.menu, "gotolistardados"):
            self.menu.gotolistardados.connect(self.show_listardados)
        if hasattr(self.menu, "gotoinicio"):
            self.menu.gotoInicio.connect(self.show_telainicial)

        if hasattr(self.modificar, "gotomenu"):
            self.modificar.gotomenu.connect(self.show_menu)
        if hasattr(self.cadastro, "gotomenu"):
            self.cadastro.gotomenu.connect(self.show_menu)
        if hasattr(self.relatorio, "gotomenu"):
            self.relatorio.gotomenu.connect(self.show_menu)
        if hasattr(self.telakm, "gotomenu"):
            self.telakm.gotomenu.connect(self.show_menu)

        # Botão “Cadastrar Usuário” -> abre QDialog usuario
        if hasattr(self.menu, "gotousuario"):
            self.menu.gotousuario.connect(self._abrir_usuario)
        

        # SUGESTÕES
        self._conectar_provider_ao_fluxo()

        self._usuario = None
        self._autenticado = False
        self._role = "visualizador"  

        # Inicial
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
            self._usuario = dialog.usuario_logado
            self._role = getattr(dialog, "role", "visualizador")
            self._aplicar_permissoes_menu()
            self.show_menu()

    @Slot(str)
    def _on_logged_in(self, nome: str):
        self._usuario = nome
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
        role = getattr(self, "_role", "visualizador")
        if role in allowed:
            return True
        self._deny()
        return False

    # --------------------------------------------------------
    # NAVEGAÇÃO — WIDGETS NO STACK (com RBAC)
    # --------------------------------------------------------
    @Slot()
    def show_telainicial(self) -> None:
        self._stack.setCurrentWidget(self.telainicial)

    @Slot()
    def show_relatorio(self) -> None:
        if not self._require_login(): return
        # liberado para todos os perfis
        self._stack.setCurrentWidget(self.relatorio)

    @Slot()
    def show_modificar(self) -> None:
        if not self._require_login(): return
        # admin e operador
        if not self._require_role({"admin", "operador"}): return
        self._stack.setCurrentWidget(self.modificar)

    @Slot()
    def show_telakm(self) -> None:
        if not self._require_login(): return
        # admin e operador
        if not self._require_role({"admin", "operador"}): return
        self._stack.setCurrentWidget(self.telakm)

    @Slot()
    def show_menu(self) -> None:
        if not self._require_login(): return
        self._stack.setCurrentWidget(self.menu)

    @Slot()
    def show_cadastro(self) -> None:
        if not self._require_login(): return
        # somente admin
        if not self._require_role({"admin"}): return
        self._stack.setCurrentWidget(self.cadastro)

    @Slot()
    def show_listardados(self) -> None:
        if not self._require_login(): return
        # liberado para todos os perfis
        self._stack.setCurrentWidget(self.listardados)

    # --------------------------------------------------------
    # QDIALOG DE USUÁRIO (cadastro com perfil)
    @Slot()
    def _abrir_usuario(self) -> None:
        if not self._require_login():
            return
        if not self._require_role({"admin"}):
            return

        dlg = usuario(self)
        dlg.submitted.connect(self._on_usuario_cadastrado)

        # Mantém modal, porém NÃO navega para menu após fechar
        dlg.exec()

    

    @Slot(str, str, str)
    def _on_usuario_cadastrado(self, usuario_txt: str, senha_txt: str, role: str):
        try:
            self.db.criar_usuario(usuario_txt, senha_txt, role)
            QMessageBox.information(self, "Usuários",
                                    f"Usuário '{usuario_txt}' criado com perfil '{role}'.")
        except Exception as e:
            QMessageBox.critical(self, "Usuários", f"Falha ao criar usuário: {e}")
        # ❌ Não navega para o menu aqui
    

    # --------------------------------------------------------
    # RBAC: Habilitar/Desabilitar botões do menu conforme o perfil
    # --------------------------------------------------------
    def _aplicar_permissoes_menu(self) -> None:
 
        role = getattr(self, "_role", "visualizador")

        # Mapear botões do menu (checar existência por segurança)
        btns = {
            "cadastro_amb": getattr(self.menu, "btnCadastroAmb", None),
            "modificar":    getattr(self.menu, "btnModificarAmb", None),
            "relatorio":    getattr(self.menu, "btnRelatorio", None),
            "inserir":      getattr(self.menu, "btnInserirDados", None),
            "lista":        getattr(self.menu, "pushButton_2", None),  
            "usuario":      getattr(self.menu, "pushButton", None),   
        }

        def set_allowed(allowed_keys: set[str]) -> None:
            for key, btn in btns.items():
                if btn:
                    btn.setEnabled(key in allowed_keys)

        if role == "admin":
            # tudo habilitado
            set_allowed(set(btns.keys()))
            return

        if role == "operador":
            allowed = {"modificar", "relatorio", "inserir", "lista"}
            set_allowed(allowed)
            return

        # visualizador
        allowed = {"relatorio", "lista"}
        set_allowed(allowed)

    
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