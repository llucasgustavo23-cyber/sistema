from main import telakm
from PySide6.QtWidgets import QApplication, QMainWindow
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = telakm()
    window.show()
    app.exec()