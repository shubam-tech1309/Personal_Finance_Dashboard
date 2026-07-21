from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QSplitter,
    QMessageBox,
)
from PySide6.QtCore import Qt


from config.settings import (
    APP_NAME,
    APP_VERSION,
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
)


from ui.header import Header

from ui.components.dashboard_cards import (
    DashboardCards
)

from ui.transaction_form import (
    TransactionForm
)

from ui.transaction_table import (
    TransactionTable
)

from utils.database import (
    DatabaseManager
)



class MainWindow(QMainWindow):


    def __init__(self):

        super().__init__()


        self.database = DatabaseManager()


        self.setWindowTitle(
            f"{APP_NAME} v{APP_VERSION}"
        )


        self.resize(
            WINDOW_WIDTH,
            WINDOW_HEIGHT
        )


        self.setup_ui()


        self.load_transactions()



    def setup_ui(self):


        central = QWidget()


        self.setCentralWidget(
            central
        )


        layout = QVBoxLayout(
            central
        )


        layout.setContentsMargins(
            20,
            20,
            20,
            20
        )


        layout.setSpacing(
            20
        )


        self.header = Header()

        layout.addWidget(
            self.header
        )


        self.dashboard_cards = DashboardCards()

        layout.addWidget(
            self.dashboard_cards
        )


        splitter = QSplitter(
            Qt.Horizontal
        )


        self.transaction_form = TransactionForm()


        self.transaction_form.save_callback = (
            self.save_transaction
        )


        self.transaction_table = TransactionTable()


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


        layout.addWidget(
            splitter
        )



    def save_transaction(
        self,
        data
    ):


        self.database.add_transaction(
            data["date"],
            data["type"],
            data["category"],
            data["description"],
            data["amount"]
        )


        QMessageBox.information(
            self,
            "Success",
            "Transaction added successfully."
        )


        self.load_transactions()



    def load_transactions(self):


        records = (
            self.database
            .get_all_transactions()
        )


        self.transaction_table.load_data(
            records
        )