from PyQt5 import QtWidgets, uic


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        uic.loadUi('main.ui', self)
        self.button = self.findChild(QtWidgets.QPushButton, 'addRow')
        self.button.clicked.connect(self.add_row)
        self.list = self.findChild(QtWidgets.QListWidget, 'list')
        self.index = 1
        self.show()

    def add_row(self):
        item = QtWidgets.QListWidgetItem()
        item.setText(str(self.index))
        self.list.addItem(item)
        self.index += 1
