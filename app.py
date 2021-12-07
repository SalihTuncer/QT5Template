from PyQt5.QtWidgets import QMainWindow, QAction, QDesktopWidget

from gui import Gui


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Edge Configurator'
        self.width = 640
        self.height = 480
        self.setWindowTitle(self.title)
        self.resize(self.width, self.height)

        self._gui = Gui()
        self.setCentralWidget(self._gui)

        # we put multiple actions which change the resolution into a list
        resolutions = []
        res_800x600 = self.add_action('&800x600', lambda: self.change_res(800, 600))
        resolutions.append(res_800x600)
        res_960x720 = self.add_action('&960x720', lambda: self.change_res(960, 720))
        resolutions.append(res_960x720)
        res_1024x768 = self.add_action('&1024x768', lambda: self.change_res(1024, 768))
        resolutions.append(res_1024x768)
        # and give them to the menu bar as actions to choose from
        self.add_menu_bar('&Resolution', resolutions)
        self.show()

    def add_action(self, name, fct, shortcut=None):
        action = QAction(name, self)
        if shortcut:
            action.setShortcut(shortcut)
        action.triggered.connect(fct)
        return action

    def add_menu_bar(self, name, actions):
        menu_bar = self.menuBar()
        resolution_menu = menu_bar.addMenu(name)
        for action in actions:
            resolution_menu.addAction(action)

    def change_res(self, x, y):
        self.resize(x, y)
        # we want the window always in the middle of the screen
        self.center_window()

    def center_window(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
