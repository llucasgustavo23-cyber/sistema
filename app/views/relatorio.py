# app/views/relatorio.py
from PySide6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from PySide6.QtCore import Signal, QDate
from .ui_relatorio import Ui_relatorio
class Relatorio(QWidget, Ui_relatorio):
    gotomenu = Signal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Estado interno simples (atual seleção)
        self._ambulancia_selecionada = None
        self._data_ref: QDate = self.dateEdit.date()

        # Fio dos sinais -> slots
        self._wire()

        # Carrega UI inicial
        self._setup_inicial()

    # ---------------------------------------------------------------------
    # Conexões dos botões e widgets
    # ---------------------------------------------------------------------
    def _wire(self):
      
        if hasattr(self, "btnVoltar"):
            self.btnVoltar.clicked.connect(self.gotomenu.emit)

        
        # if hasattr(self, "btnGerar"):
        #      self.btnGerar.clicked.connect(self._carregar)

        
        # if hasattr(self, "btnExportarPDF"):
        #     self.btnExportarPDF.clicked.connect(self._exportar_pdf)
        # if hasattr(self, "btnExportarExcel"):
        #     self.btnExportarExcel.clicked.connect(self._exportar_excel)
        # if hasattr(self, "btnImprimir"):
        #     self.btnImprimir.clicked.connect(self._imprimir)

        
        # if hasattr(self, "comboAmbulancia"):
        #     self.comboAmbulancia.currentIndexChanged.connect(self._on_change_filtros)
        # if hasattr(self, "dateEdit"):
        #     self.dateEdit.dateChanged.connect(self._on_change_filtros)

    # ---------------------------------------------------------------------
    # Configuração inicial de widgets
    # ---------------------------------------------------------------------
    def _setup_inicial(self):
        if hasattr(self, "tableDiario"):
            self.tableDiario.setRowCount(0)

