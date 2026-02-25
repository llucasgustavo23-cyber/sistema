from main import TelaInicial
from PySide6.QtWidgets import QApplication, QMainWindow
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TelaInicial()
    window.show()
    app.exec()