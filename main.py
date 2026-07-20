import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QLabel


app = QApplication(sys.argv)

label = QLabel("Welcome to Personal Finance Dashboard!")

label.resize(500,100)

label.show()

app.exec()