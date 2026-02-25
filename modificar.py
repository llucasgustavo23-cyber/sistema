from PySide6.QtWidgets import QApplication, QMainWindow
from main import modificar
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = modificar()
    window.show()
    app.exec()