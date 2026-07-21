from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QSplitter,
)
from PySide6.QtCore import Qt

from config.settings import (
    APP_NAME,
    APP_VERSION,
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
)

from ui.header import Header
from ui.components.dashboard_cards import DashboardCards
from ui.transaction_form import TransactionForm
from ui.transaction_table import TransactionTable


class MainWindow(QMainWindow):
    """
    Main application window.

    Controls the complete dashboard layout.
    """

    def __init__(self):
        super().__init__()

        self.setWindowTitle(
            f"{APP_NAME} v{APP_VERSION}"
        )

        self.resize(
            WINDOW_WIDTH,
            WINDOW_HEIGHT,
        )

        self.setup_ui()


    def setup_ui(self):

        central = QWidget()

        self.setCentralWidget(
            central
        )


        main_layout = QVBoxLayout(
            central
        )


        main_layout.setContentsMargins(
            20,
            20,
            20,
            20,
        )


        main_layout.setSpacing(
            20
        )


        # -----------------------------
        # Header
        # -----------------------------

        self.header = Header()

        main_layout.addWidget(
            self.header
        )


        # -----------------------------
        # Dashboard Statistics
        # -----------------------------

        self.dashboard_cards = DashboardCards()

        main_layout.addWidget(
            self.dashboard_cards
        )


        # -----------------------------
        # Content Area
        # -----------------------------

        splitter = QSplitter(
            Qt.Horizontal
        )


        splitter.setChildrenCollapsible(
            False
        )


        splitter.setHandleWidth(
            8
        )


        # -----------------------------
        # Transaction Form
        # -----------------------------

        self.transaction_form = (
            TransactionForm()
        )


        # -----------------------------
        # Transaction Table
        # -----------------------------

        self.transaction_table = (
            TransactionTable()
        )


        splitter.addWidget(
            self.transaction_form
        )


        splitter.addWidget(
            self.transaction_table
        )


        splitter.setSizes(
            [
                380,
                900
            ]
        )


        main_layout.addWidget(
            splitter,
            1
        )