import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import pyqtSlot


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Edge Configurator'
        self.width = 800
        self.height = 500
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.resize(self.width, self.height)

        self.add_button(600, 100, self.on_click)
        self.add_button(600, 200, self.on_click)
        self.add_button(600, 300, self.on_click)

        self.show()

    @pyqtSlot()
    def on_click(self):
        print('PyQt5 button click')

    def add_button(self, x, y, fct, name="PyQt5 button", tooltip="This is a button"):
        button = QPushButton(name, self)
        button.setToolTip(tooltip)
        button.move(x, y)
        button.clicked.connect(fct)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
