from PyQt5.QtWidgets import QMainWindow, QAction, QDesktopWidget

from gui import Gui


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Edge Configurator'
        self.width = 640
        self.height = 320
        self.setWindowTitle(self.title)
        self.resize(self.width, self.height)

        self._gui = Gui(self.title)
        self.setCentralWidget(self._gui)

        # we put multiple actions which change the resolution into a list
        resolutions = []
        res_640x320 = self.add_action('&640x320', lambda: self.change_res(640, 320))
        resolutions.append(res_640x320)
        res_960x480 = self.add_action('&960x480', lambda: self.change_res(960, 480))
        resolutions.append(res_960x480)
        res_1440x720 = self.add_action('&1440x720', lambda: self.change_res(1440, 720))
        resolutions.append(res_1440x720)
        res_2160x1080 = self.add_action('&2160x1080', lambda: self.change_res(2160, 1080))
        resolutions.append(res_2160x1080)
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
