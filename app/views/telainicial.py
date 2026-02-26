from PySide6.QtWidgets import QWidget, QMainWindow, QVBoxLayout
from PySide6.QtCore import Signal
from .ui_telainicia import Ui_telainicia  # <-- GERADO DE MAINWINDOW

class TelaInicial(QWidget):
    gotoRelatorio = Signal()
    gotoLogin = Signal()

    def __init__(self):
        super().__init__()

        temp = QMainWindow()
        self.ui = Ui_telainicia()
        self.ui.setupUi(temp)   
        from PySide6.QtWidgets import QWidget
        children = [c for c in self.findChildren(QWidget)]
        print(f"[DEBUG {self.__class__.__name__}] filhos QWidget:", len(children))
        for c in children[:5]:
            print("  -", c.objectName(), type(c).__name__)               # ok: chamada em MainWindow

        cw = temp.centralWidget()      # pega o centralWidget
        temp.setCentralWidget(None)    # desanexa do temp

                   # coloca dentro do seu QWidget

        self._wire()

    def _wire(self):
        self.ui.homeBtn.clicked.connect(self.gotoLogin.emit)
   
