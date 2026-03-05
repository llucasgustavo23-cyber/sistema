from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal
from .ui_menu1 import Ui_menu


class menu(QWidget, Ui_menu):
    
    gotoCadastro = Signal()
    gotoRelatorio = Signal()
    gotomodificar = Signal()
    gototelakm = Signal()
    gotoInicio = Signal()
    gotolistardados = Signal()
    gotousuario = Signal()

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Tela inicial do sistema")

        self.btnlistadados = getattr(self, "pushButton_2", None)  
        self.btnusuario = getattr(self, "pushButton", None)       

        self._wire()


   
    def _wire(self) -> None:
        # CADASTRO DE AMBULÂNCIA (botão grande na grade)
        if hasattr(self, "btnCadastroAmb") and self.btnCadastroAmb:
            self.btnCadastroAmb.clicked.connect(self.gotoCadastro.emit)
        else:
            print("[menu] Aviso: btnCadastroAmb não encontrado na UI")

        # MODIFICAR AMBULÂNCIA (botão grande na grade)
        if hasattr(self, "btnModificarAmb") and self.btnModificarAmb:
            self.btnModificarAmb.clicked.connect(self.gotomodificar.emit)
        else:
            print("[menu] Aviso: btnModificarAmb não encontrado na UI")

        # INSERIR DADOS (tela KM) (botão grande na grade)
        if hasattr(self, "btnInserirDados") and self.btnInserirDados:
            self.btnInserirDados.clicked.connect(self.gototelakm.emit)
        else:
            print("[menu] Aviso: btnInserirDados não encontrado na UI")

        # RELATÓRIO (botão grande na grade)
        if hasattr(self, "btnRelatorio") and self.btnRelatorio:
            self.btnRelatorio.clicked.connect(self.gotoRelatorio.emit)
        else:
            print("[menu] Aviso: btnRelatorio não encontrado na UI")

        # INÍCIO (menu lateral)
        if hasattr(self, "btnInicio") and self.btnInicio:
            self.btnInicio.clicked.connect(self.gotoInicio.emit)
        else:
            print("[menu] Aviso: btnInicio não encontrado na UI")

        # DADOS AMBULÂNCIAS (menu lateral) -> lista de dados
        if hasattr(self, "pushButton_2") and self.pushButton_2:
            self.pushButton_2.clicked.connect(self.gotolistardados.emit)
        elif getattr(self, "btnlistadados", None):
            self.btnlistadados.clicked.connect(self.gotolistardados.emit)
        else:
            print("[menu] Aviso: botão 'Dados Ambulâncias' (pushButton_2) não encontrado na UI")

        # CADASTRAR USUÁRIO (menu lateral)
        if hasattr(self, "pushButton") and self.pushButton:
            self.pushButton.clicked.connect(self.gotousuario.emit)
        elif getattr(self, "btnusuario", None):
            self.btnusuario.clicked.connect(self.gotousuario.emit)
        else:
            print("[menu] Aviso: botão 'Cadastrar Usuário' (pushButton) não encontrado na UI")

        # Opcional: btnConfig existe na UI, mas você não definiu um sinal específico
        # Se quiser reagir a ele, crie um Signal (ex.: gotoConfig) e conecte aqui.
        if hasattr(self, "btnConfig") and self.btnConfig:
            # Exemplo de log para lembrar de implementar quando necessário:
            self.btnConfig.clicked.connect(lambda: print("[menu] Clique em Ajuste (btnConfig)"))
