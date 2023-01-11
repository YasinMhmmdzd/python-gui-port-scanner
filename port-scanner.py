from socket import *
from PyQt6.QtWidgets import QApplication , QWidget , QLabel , QPushButton , QLineEdit
import sys
from PyQt6.QtGui import QIcon , QFont , QPixmap
import time
started_time = time.time()
app = QApplication(sys.argv)
class MainPortScannerWindow(QWidget):
    def __init__(self):
        super(MainPortScannerWindow, self).__init__()
        self.setWindowTitle("پورت اسکنر")
        self.top_header_label = QLabel("پورت اسکنر" , self)
        self.setFont(QFont("irancell" , 20))
        self.top_header_label.setStyleSheet("color:#0650af;")
        self.top_header_label.move(425 , 5)
        self.setWindowIcon(QIcon("logo.png"))
        self.setFixedSize(1000 , 500)
        self.app_logo = QLabel(self)
        logo = QPixmap("logo.png")
        self.app_logo.setPixmap(logo)
        self.app_logo.move(425, 50)
        self.ip_address = QLineEdit(self)
        self.ip_address.setPlaceholderText("آدرس ip مورد نظر را تایپ کنید...")
        self.ip_address.setFont(QFont("irancell" , 14))
        self.ip_address.setGeometry(650 , 190 , 300 , 45)
        self.ip_address.setStyleSheet("border:1px solid #bbb;border-radius:5px;padding:10px;")

window = MainPortScannerWindow()
window.show()
sys.exit(app.exec())