from PyQt5.QtWidgets import QPushButton, QComboBox, QLabel, QWidget, QGridLayout, QLineEdit, \
    QMessageBox, QRadioButton, QCheckBox, QListWidget, QListWidgetItem

from PyQt5.QtCore import pyqtSlot
import random


class Gui(QWidget):

    def __init__(self, title):
        super().__init__()
        self.title = title
        self.drops = []
        self.init_ui()

    def init_ui(self):

        b1 = self.add_button(self.on_click, 'Configuration applied')

        d1 = self.add_dropdown(self.selection)
        d2 = self.add_dropdown(self.selection)

        c1 = self.add_check_box(self.click_box)
        c2 = self.add_check_box(self.click_box)

        e1 = QLineEdit('localhost')
        e2 = QLineEdit('8080')

        r1 = QRadioButton("&intern")
        r1.setChecked(True)
        r2 = QRadioButton("&extern")

        l1 = self.add_list()

        layout = QGridLayout()

        layout.addWidget(QLabel("Language:"), 0, 0)
        layout.addWidget(d1, 0, 1)
        layout.addWidget(d2, 0, 2)

        layout.addWidget(QLabel("Domain:"), 1, 0)
        layout.addWidget(e1, 1, 1)
        layout.addWidget(e2, 1, 2)

        layout.addWidget(QLabel("Scope:"), 2, 0)
        layout.addWidget(r1, 2, 1)
        layout.addWidget(r2, 2, 2)

        layout.addWidget(QLabel("Chess:"), 3, 0)
        layout.addWidget(c1, 3, 1)
        layout.addWidget(c2, 3, 2)

        layout.addWidget(l1, 4, 0)

        layout.addWidget(b1, 5, 2)
        self.setLayout(layout)

    def add_dropdown(self, fct, items=None):
        if items is None:
            items = ['Java', 'Python', 'R']
        dropdown = QComboBox(self)
        self.drops.append(dropdown)
        dropdown.addItems(items)
        i = len(self.drops) - 1
        dropdown.currentIndexChanged.connect(lambda: fct(i))
        return dropdown

    @pyqtSlot()
    def selection(self, i):
        print("Current index", self.drops[i].currentIndex(), "selected element", self.drops[i].currentText())

    # normal button where you can define what to do if its is clicked or where it should be placed
    def add_button(self, fct, message_text, name="Confirm", tooltip=None):
        button = QPushButton(name, self)
        if tooltip:
            button.setToolTip(tooltip)
        button.clicked.connect(lambda: fct(message_text))
        return button

    @pyqtSlot()
    def on_click(self, text):
        msg = QMessageBox(self)
        msg.setWindowTitle(self.title)
        msg.setText(text)
        msg.setIcon(QMessageBox.Information)
        msg.exec_()

    def add_check_box(self, fct, name='Check Mate'):
        cb = QCheckBox(name, self)
        cb.stateChanged.connect(lambda: fct(cb))
        return cb

    @pyqtSlot()
    def click_box(self, cb):
        if cb.isChecked():
            print('Checked')
        else:
            print('Unchecked')

    def add_list(self, items=None):
        if items is None:
            items = ['Java', 'Python', 'R'] * 10
        random.shuffle(items)

        list_widget = QListWidget(self)
        for item in items:
            list_widget.addItem(QListWidgetItem(item))

        list_widget.itemClicked.connect(lambda: self.on_list_click(list_widget))
        list_widget.setGeometry(50, 70, 50, 80)
        list_widget.setDragDropMode(3)
        list_widget.setAutoScroll(True)
        list_widget.setAutoScrollMargin(3)
        list_widget.setWordWrap(True)
        return list_widget

    @pyqtSlot()
    def on_list_click(self, list_widget):
        print(list_widget.currentItem().text())
