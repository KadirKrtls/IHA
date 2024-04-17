import sys
from PyQt5.QtWidgets import *
from ekran import Ui_MainWindow

class Pencere(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ekran=Ui_MainWindow()
        self.ekran.setupUi(self)

uygulama=QApplication(sys.argv)
Baslat=Pencere()
Baslat.show()
sys.exit(uygulama.exec_())