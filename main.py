import sys
from PyQt5.QtWidgets import QApplication, QWidget
from window import Window

app = QApplication(sys.argv)
window = Window()
app.exec_()

