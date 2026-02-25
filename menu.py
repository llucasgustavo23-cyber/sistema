from PySide6.QtWidgets import QApplication, QMainWindow
from main import menu
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = menu()
    window.show()
    app.exec()