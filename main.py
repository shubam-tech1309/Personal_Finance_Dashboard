import sys

from PySide6.QtWidgets import QApplication

from ui.main_window import MainWindow

from database.database import DatabaseManager


def main():

    app = QApplication(sys.argv)

    database = DatabaseManager()

    window = MainWindow()

    window.show()

    exit_code = app.exec()

    database.close()

    sys.exit(exit_code)


if __name__ == "__main__":

    main()