from PySide6.QtWidgets import QMainWindow


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Personal Finance Dashboard")

        self.resize(1200, 750)

        self.setMinimumSize(1000, 650)