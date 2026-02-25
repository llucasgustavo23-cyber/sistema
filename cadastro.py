from PySide6.QtWidgets import QApplication, QMainWindow
from main import cadastro
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = cadastro()
    window.show()
    app.exec()