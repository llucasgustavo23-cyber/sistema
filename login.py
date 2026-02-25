from PySide6.QtWidgets import QApplication, QMainWindow
from main import login
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = login()
    window.show()
    app.exec()