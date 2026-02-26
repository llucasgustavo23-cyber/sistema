# app/views/relatorio.py
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal
from .ui_relatorio import Ui_relatorio  # GERADO A PARTIR DE FORM "Widget"

class Relatorio(QWidget, Ui_relatorio):
    gotoTelaInicial = Signal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)     # monta a UI do Designer neste QWidget
        self._wire()
        self._carregar()       # opcional: popula dados ao abrir

    def _wire(self):
        # Conecta os botões (só se existirem no .ui)
        if hasattr(self, "btnVoltar"):
            self.btnVoltar.clicked.connect(self.gotoTelaInicial.emit)
        if hasattr(self, "btnAtualizar"):
            self.btnAtualizar.clicked.connect(self._carregar)

    def _carregar(self):
        # Exemplo: popular uma lista, se ela existir no .ui
        if hasattr(self, "listRelatorios"):
            self.listRelatorios.clear()
            self.listRelatorios.addItems([
                "Relatório 01",
                "Relatório 02",
                "Relatório 03",
            ])