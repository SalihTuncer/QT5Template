import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QComboBox, QHBoxLayout
from PyQt5.QtCore import pyqtSlot


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Edge Configurator'
        self.width = 600
        self.height = 400
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.resize(self.width, self.height)

        self.boxes = []

        self.add_button(450, 100, self.on_click)
        self.add_button(450, 150, self.on_click)
        self.add_button(450, 200, self.on_click)

        self.add_QComboBox(50, 100, self.selectionchange)
        self.add_QComboBox(50, 150, self.selectionchange)
        self.add_QComboBox(50, 200, self.selectionchange)

        self.show()

    def add_QComboBox(self, x, y, fct, item='C', items=['Java', 'C#', 'Python']):
        q_combo_box = QComboBox(self)
        self.boxes.append(q_combo_box)
        q_combo_box.move(x, y)
        q_combo_box.addItem(item)
        q_combo_box.addItems(items)
        i = len(self.boxes) - 1
        q_combo_box.currentIndexChanged.connect(lambda: fct(i))

    def selectionchange(self, i):
        print("Items in the list are :")

        for count in range(self.boxes[i].count()):
            print(self.boxes[i].itemText(count))
        print("Current index", i, "selection changed ", self.boxes[i].currentText())

    # normal button where you can define what to do if its is clicked or where it should be placed
    def add_button(self, x, y, fct, name="Confirm", tooltip="Button"):
        button = QPushButton(name, self)
        button.setToolTip(tooltip)
        button.move(x, y)
        button.clicked.connect(fct)

    @pyqtSlot()
    def on_click(self):
        print('PyQt5 button click')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
