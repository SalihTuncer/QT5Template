from PyQt5.QtWidgets import QPushButton, QComboBox, QLabel, QWidget, QGridLayout, QLineEdit, \
    QMessageBox, QRadioButton, QCheckBox

from PyQt5.QtCore import pyqtSlot


class Gui(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Edge Configurator'
        self.drops = []
        self.init_ui()

    def init_ui(self):

        b1 = self.add_button(self.on_click)

        d1 = self.add_dropdown(self.selection)
        d2 = self.add_dropdown(self.selection)

        c1 = self.add_check_box(self.click_box)
        c2 = self.add_check_box(self.click_box)

        e1 = QLineEdit('localhost')
        e2 = QLineEdit('8080')

        r1 = QRadioButton("&intern")
        r1.setChecked(True)
        r2 = QRadioButton("&extern")

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

        layout.addWidget(b1, 4, 2)
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

    def selection(self, i):
        print("Current index", self.drops[i].currentIndex(), "selected element", self.drops[i].currentText())

    # normal button where you can define what to do if its is clicked or where it should be placed
    def add_button(self, fct, name="Confirm", tooltip=None):
        button = QPushButton(name, self)
        if tooltip:
            button.setToolTip(tooltip)
        button.clicked.connect(fct)
        return button

    @pyqtSlot()
    def on_click(self):
        QMessageBox.about(self, self.title, "Configuration applied")

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
