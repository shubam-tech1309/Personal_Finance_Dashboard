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

        self.refresh_dashboard()



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


        self.transaction_table.delete_callback = (
            self.delete_transaction
        )


        self.transaction_table.refresh_callback = (
            self.load_transactions
        )


        self.transaction_table.table.doubleClicked.connect(
            self.edit_selected_transaction
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


        layout.addWidget(
            splitter
        )



    def save_transaction(
        self,
        data,
        edit_id=None
    ):


        if edit_id:


            self.database.update_transaction(

                edit_id,

                data["date"],

                data["type"],

                data["category"],

                data["description"],

                data["amount"]

            )


            message = "Transaction updated successfully."


        else:


            self.database.add_transaction(

                data["date"],

                data["type"],

                data["category"],

                data["description"],

                data["amount"]

            )


            message = "Transaction added successfully."



        QMessageBox.information(
            self,
            "Success",
            message
        )


        self.load_transactions()

        self.refresh_dashboard()



    def edit_selected_transaction(
        self
    ):


        transaction_id = (
            self.transaction_table.selected_id()
        )


        records = (
            self.database
            .get_all_transactions()
        )


        for record in records:

            if record[0] == transaction_id:

                self.transaction_form.load_transaction(
                    record
                )

                break



    def delete_transaction(
        self,
        transaction_id
    ):


        self.database.delete_transaction(
            transaction_id
        )


        self.load_transactions()

        self.refresh_dashboard()



    def load_transactions(self):

        records = (
            self.database
            .get_all_transactions()
        )


        self.transaction_table.load_data(
            records
        )



    def refresh_dashboard(self):

        stats = (
            self.database
            .get_statistics()
        )


        self.dashboard_cards.update_statistics(

            stats["balance"],

            stats["income"],

            stats["expense"],

            stats["savings"]

        )