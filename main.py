import sys

from PySide6.QtWidgets import QApplication

from PySide6.QtCore import Qt

from PySide6.QtGui import (
    QKeySequence,
    QShortcut,
)


from ui.main_window import (
    MainWindow
)


from config.settings import (
    APP_NAME,
)


from styles.app_style import (
    APP_STYLE
)



class FinanceApplication(QApplication):


    def __init__(
        self,
        args
    ):

        super().__init__(
            args
        )


        self.setApplicationName(
            APP_NAME
        )


        self.setStyle(
            "Fusion"
        )


        self.setStyleSheet(
            APP_STYLE
        )



def setup_global_shortcuts(
    window
):


    shortcuts = [

        (
            "Alt+A",
            window.open_add_transaction
        ),

        (
            "Ctrl+S",
            window.save_current_transaction
        ),

        (
            "Ctrl+L",
            window.clear_transaction_form
        ),

        (
            "Ctrl+F",
            window.focus_search
        ),

        (
            "F5",
            window.load_transactions
        ),

        (
            "Ctrl+E",
            window.export_excel
        ),

        (
            "Ctrl+I",
            window.import_excel
        ),

        (
            "Delete",
            window.delete_selected_transaction
        ),

    ]



    for key, function in shortcuts:


        shortcut = QShortcut(

            QKeySequence(key),

            window

        )


        shortcut.activated.connect(
            function
        )



def main():


    app = FinanceApplication(
        sys.argv
    )


    window = MainWindow()


    setup_global_shortcuts(
        window
    )


    window.show()



    # Prevent first field focus

    window.clearFocus()

    window.setFocus(
        Qt.OtherFocusReason
    )



    sys.exit(
        app.exec()
    )



if __name__ == "__main__":

    main()