from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QSplitter,
)

from PySide6.QtCore import (
    Qt,
    QTimer,
    QTime,
)


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

from utils.excel_manager import (
    ExcelManager
)



class MainWindow(QMainWindow):


    def __init__(self):

        super().__init__()


        self.database = DatabaseManager()


        self.excel = ExcelManager()



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



        self.start_status_timer()



        self.clearFocus()

        self.setFocus(

            Qt.OtherFocusReason

        )




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

            10

        )


        main_layout.setSpacing(

            15

        )



        self.header = Header()


        main_layout.addWidget(

            self.header

        )



        self.dashboard_cards = DashboardCards()



        main_layout.addWidget(

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

            splitter

        )



        shortcut_panel = QLabel(

            """

            Keyboard Shortcuts:

            Alt + A  Add Transaction

            Ctrl + S  Save

            Ctrl + F  Search

            Ctrl + E  Export Excel

            Ctrl + I  Import Excel

            Delete   Delete Selected

            F5       Refresh

            """

        )


        shortcut_panel.setStyleSheet(

            """

            background:white;

            border-radius:12px;

            padding:12px;

            color:#475569;

            """

        )



        main_layout.addWidget(

            shortcut_panel

        )



        self.status_label = QLabel()


        self.status_label.setStyleSheet(

            """

            color:#475569;

            padding:5px;

            """

        )



        self.statusBar().addWidget(

            self.status_label

        )




    # =========================
    # Keyboard Actions
    # =========================


    def open_add_transaction(self):


        self.transaction_form.clear_form()


        self.transaction_form.focus_first_field()



    def save_current_transaction(self):


        self.transaction_form.handle_save()



    def clear_transaction_form(self):


        self.transaction_form.clear_form()



    def focus_search(self):


        self.transaction_table.search_box.setFocus()



    def delete_selected_transaction(self):


        row = (

            self.transaction_table.selected_id()

        )


        if row:

            self.delete_transaction(

                row

            )



    # =========================
    # Database
    # =========================


    def save_transaction(

        self,

        data,

        edit_id=None

    ):


        if edit_id:


            self.database.update_transaction(

                edit_id,

                data

            )


        else:


            self.database.add_transaction(

                data

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


        self.update_status()



    def delete_transaction(

        self,

        transaction_id

    ):


        self.database.delete_transaction(

            transaction_id

        )


        self.load_transactions()


        self.refresh_dashboard()




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




    def update_status(self):


        count = len(

            self.database
            .get_all_transactions()

        )


        self.status_label.setText(

            f"Database Connected ✓     Transactions: {count}"

        )




    def start_status_timer(self):


        timer = QTimer(

            self

        )


        timer.timeout.connect(

            self.update_status

        )


        timer.start(

            5000

        )