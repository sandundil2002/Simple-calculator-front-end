from PyQt5.QtWidgets import QApplication, QMainWindow

from view import frontEnd
from view.frontEnd import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

    def button_clicked(self):
        frontEnd.Ui_MainWindow.retranslateUi(self, MainWindow)