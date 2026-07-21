import sys

from PySide6.QtWidgets import QApplication

from styles.theme import APP_STYLE
from ui.main_window import MainWindow
from utils.database import DatabaseManager


def main():
    database = DatabaseManager()
    database.initialize()

    app = QApplication(sys.argv)

    app.setStyleSheet(APP_STYLE)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()