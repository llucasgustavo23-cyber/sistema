# app/views/relatorio.py
from PySide6.QtWidgets import QWidget, QMainWindow, QVBoxLayout
from PySide6.QtCore import Signal
from .ui_relatorio import Ui_relatorio  # <-- GERADO A PARTIR DE MAINWINDOW

class Relatorio(QWidget):
    gotoTelaInicial = Signal()

    def __init__(self):
        super().__init__()

        temp = QMainWindow()
        self.ui = Ui_relatorio()
        self.ui.setupUi(temp)             # ok: é MainWindow
        from PySide6.QtWidgets import QWidget
        children = [c for c in self.findChildren(QWidget)]
        print(f"[DEBUG {self.__class__.__name__}] filhos QWidget:", len(children))
        for c in children[:5]:
            print("  -", c.objectName(), type(c).__name__)
        cw = temp.centralWidget()         # extrai o centralWidget
        temp.setCentralWidget(None)

           # encaixa no seu QWidget

        # self._wire()
        # self._carregar()

    # def _wire(self):
    #     self.ui.btnVoltar.clicked.connect(self.gotoTelaInicial.emit)
