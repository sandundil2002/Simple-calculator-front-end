from PyQt5.QtWidgets import QApplication, QMainWindow
from view.frontEnd import Ui_MainWindow

class CalculatorApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication([])
    window = CalculatorApp()
    window.show()
    app.exec_()
