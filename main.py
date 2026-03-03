import sys
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UI_DIR = os.path.join(BASE_DIR, "app", "views")
if UI_DIR not in sys.path:
    sys.path.insert(0, UI_DIR)

from PySide6.QtWidgets import QApplication
from app.mainwindow import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
