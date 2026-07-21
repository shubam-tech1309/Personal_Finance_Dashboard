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
    Transaction table component.

    Features:
    - Display transactions
    - Search
    - Filter
    - Refresh
    - Delete
    - Export Excel
    - Import Excel
    """


    def __init__(self):

        super().__init__()


        self.all_records = []


        self.delete_callback = None

        self.refresh_callback = None

        self.export_callback = None

        self.import_callback = None


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


        main_layout = QVBoxLayout(
            self
        )


        main_layout.setContentsMargins(
            20,
            20,
            20,
            20
        )


        main_layout.setSpacing(
            15
        )



        header_layout = QHBoxLayout()



        title = QLabel(
            "Transactions"
        )


        title.setStyleSheet(
            """
            font-size:16px;
            font-weight:700;
            """
        )


        header_layout.addWidget(
            title
        )


        header_layout.addStretch()



        self.refresh_button = QPushButton(
            "Refresh"
        )


        self.delete_button = QPushButton(
            "Delete"
        )


        self.export_button = QPushButton(
            "Export Excel"
        )


        self.import_button = QPushButton(
            "Import Excel"
        )



        header_layout.addWidget(
            self.refresh_button
        )


        header_layout.addWidget(
            self.delete_button
        )


        header_layout.addWidget(
            self.export_button
        )


        header_layout.addWidget(
            self.import_button
        )


        main_layout.addLayout(
            header_layout
        )



        filter_layout = QHBoxLayout()



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



        filter_layout.addWidget(
            self.search_box
        )


        filter_layout.addWidget(
            self.type_filter
        )


        main_layout.addLayout(
            filter_layout
        )



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


        main_layout.addWidget(
            self.table
        )



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


        self.export_button.clicked.connect(
            self.export_clicked
        )


        self.import_button.clicked.connect(
            self.import_clicked
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


        text = (
            self.search_box
            .text()
            .lower()
            .strip()
        )


        selected = (
            self.type_filter
            .currentText()
        )


        filtered = []


        for record in self.all_records:


            text_match = (

                text in str(record[3]).lower()

                or

                text in str(record[4]).lower()

            )


            type_match = (

                selected == "All"

                or

                record[2] == selected

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


        transaction_id = self.selected_id()


        if transaction_id is None:

            QMessageBox.warning(
                self,
                "No Selection",
                "Select a transaction first."
            )

            return



        confirm = QMessageBox.question(
            self,
            "Confirm Delete",
            "Delete selected transaction?"
        )



        if confirm == QMessageBox.Yes:


            if self.delete_callback:

                self.delete_callback(
                    transaction_id
                )



    def refresh_clicked(self):


        if self.refresh_callback:

            self.refresh_callback()



    def export_clicked(self):


        if self.export_callback:

            self.export_callback()



    def import_clicked(self):


        if self.import_callback:

            self.import_callback()