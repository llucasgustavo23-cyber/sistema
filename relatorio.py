from PySide6.QtWidgets import QApplication, QMainWindow
from main import relatorio
import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = relatorio()
    window.show()
    app.exec()
    :