from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QAbstractItemView,
    QComboBox,
    QFrame,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QMessageBox,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QHeaderView,
)


class TransactionTable(QFrame):
    """
    Transaction table with:

    - Search
    - Type filter
    - Refresh
    - Delete
    """


    def __init__(self):

        super().__init__()


        self.all_records = []

        self.delete_callback = None

        self.refresh_callback = None


        self.setup_ui()



    def setup_ui(self):


        self.setObjectName(
            "TransactionTable"
        )


        self.setStyleSheet(
            """
            QFrame#TransactionTable
            {
                background:white;
                border:1px solid #E5E7EB;
                border-radius:14px;
            }
            """
        )


        layout = QVBoxLayout(
            self
        )


        layout.setContentsMargins(
            20,
            20,
            20,
            20
        )


        # ----------------------------
        # Header
        # ----------------------------


        header = QHBoxLayout()


        title = QLabel(
            "Transactions"
        )


        title.setStyleSheet(
            """
            font-size:16px;
            font-weight:700;
            """
        )


        header.addWidget(
            title
        )


        header.addStretch()


        self.refresh_button = QPushButton(
            "Refresh"
        )


        self.delete_button = QPushButton(
            "Delete"
        )


        header.addWidget(
            self.refresh_button
        )


        header.addWidget(
            self.delete_button
        )


        layout.addLayout(
            header
        )


        # ----------------------------
        # Search Area
        # ----------------------------


        search_layout = QHBoxLayout()


        self.search_box = QLineEdit()


        self.search_box.setPlaceholderText(
            "Search description or category..."
        )


        self.type_filter = QComboBox()


        self.type_filter.addItems(
            [
                "All",
                "Income",
                "Expense"
            ]
        )


        search_layout.addWidget(
            self.search_box
        )


        search_layout.addWidget(
            self.type_filter
        )


        layout.addLayout(
            search_layout
        )


        # ----------------------------
        # Table
        # ----------------------------


        self.table = QTableWidget()


        headers = [

            "ID",
            "Date",
            "Type",
            "Category",
            "Description",
            "Amount",
            "Created"

        ]


        self.table.setColumnCount(
            len(headers)
        )


        self.table.setHorizontalHeaderLabels(
            headers
        )


        self.table.setSelectionBehavior(
            QAbstractItemView.SelectRows
        )


        self.table.setEditTriggers(
            QAbstractItemView.NoEditTriggers
        )


        self.table.verticalHeader().setVisible(
            False
        )


        self.table.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )


        layout.addWidget(
            self.table
        )


        # Connections


        self.search_box.textChanged.connect(
            self.apply_filter
        )


        self.type_filter.currentTextChanged.connect(
            self.apply_filter
        )


        self.refresh_button.clicked.connect(
            self.refresh_clicked
        )


        self.delete_button.clicked.connect(
            self.delete_clicked
        )



    def load_data(
        self,
        records
    ):

        self.all_records = records

        self.display_records(
            records
        )



    def display_records(
        self,
        records
    ):


        self.table.setRowCount(
            0
        )


        for row, record in enumerate(records):


            self.table.insertRow(
                row
            )


            for column, value in enumerate(record):


                if column == 5:

                    value = (
                        f"₹ {float(value):,.2f}"
                    )


                item = QTableWidgetItem(
                    str(value)
                )


                item.setTextAlignment(
                    Qt.AlignCenter
                )


                self.table.setItem(
                    row,
                    column,
                    item
                )



    def apply_filter(self):


        search_text = (
            self.search_box
            .text()
            .lower()
        )


        selected_type = (
            self.type_filter
            .currentText()
        )


        filtered = []


        for record in self.all_records:


            text_match = (

                search_text in
                str(record[3]).lower()

                or

                search_text in
                str(record[4]).lower()

            )


            type_match = (

                selected_type == "All"

                or

                record[2] == selected_type

            )


            if text_match and type_match:

                filtered.append(
                    record
                )


        self.display_records(
            filtered
        )



    def selected_id(self):

        row = self.table.currentRow()


        if row < 0:

            return None


        item = self.table.item(
            row,
            0
        )


        if item:

            return int(
                item.text()
            )


        return None



    def delete_clicked(self):


        transaction_id = (
            self.selected_id()
        )


        if transaction_id is None:

            QMessageBox.warning(
                self,
                "No Selection",
                "Select a transaction first."
            )

            return



        confirm = QMessageBox.question(
            self,
            "Confirm",
            "Delete this transaction?"
        )


        if confirm == QMessageBox.Yes:


            if self.delete_callback:

                self.delete_callback(
                    transaction_id
                )



    def refresh_clicked(self):

        if self.refresh_callback:

            self.refresh_callback()