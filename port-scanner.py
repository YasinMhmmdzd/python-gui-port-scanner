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
        self.ip_address.setStyleSheet("border:1px solid #668df7;border-radius:5px;padding:10px;")
        self.t_IP = gethostbyname(self.ip_address.text())
        self.first_label_range = QLabel("جستجو از پورت : ", self)
        self.first_label_range.move(520 , 200)
        self.first_label_range.setFont(QFont("irancell" , 12))
        self.first_range = QLineEdit(self)
        self.first_range.setGeometry(420 , 190 , 100 , 45)
        self.first_range.setStyleSheet("border:1px solid #668df7;border-radius:5px;padding:10px;")
        self.second_label_range = QLabel(" تا پورت : ", self)
        self.second_label_range.move(350 , 200)
        self.second_label_range.setFont(QFont("irancell" , 12))
        self.second_range = QLineEdit(self)
        self.second_range.setGeometry(250 , 190 , 100 , 45)
        self.second_range.setStyleSheet("border:1px solid #668df7;border-radius:5px;padding:10px;")
        self.start_button = QPushButton("اسکن" , self)
        self.start_button.setGeometry(50 , 190 , 180 , 50)
        self.start_button.setStyleSheet("background-color:#0650af;color:white;border:1px solid #0650af; border-radius:5px;")
        self.start_button.clicked.connect(self.start_scan)
    def start_scan(self):
        for port in range(int(self.first_range) , int(self.second_range)):
            server = socket(AF_INET , SOCK_STREAM)
            connection = server.connect_ex(self.t_IP, port)
            if connection == 0:
                self.port_label = QLabel(f"{port}این پورت باز است : " , self)
                self.port_label.move(500 , 250)
                server.close()
window = MainPortScannerWindow()
window.show()
sys.exit(app.exec())