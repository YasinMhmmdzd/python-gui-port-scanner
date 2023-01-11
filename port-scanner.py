from socket import *
from PyQt6.QtWidgets import QApplication , QWidget , QLabel , QPushButton , QLineEdit
import sys
from PyQt6.QtGui import QIcon , QFont
import time
started_time = time.time()
app = QApplication(sys.argv)
class MainPortScannerWindow(QWidget):
    def __init__(self):
        super(MainPortScannerWindow, self).__init__()
        self.setWindowTitle("پورت اسکنر")
        self.setWindowIcon(QIcon("logo.png"))

window = MainPortScannerWindow()
window.show()
sys.exit(app.exec())