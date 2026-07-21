from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QAbstractItemView,
    QFrame,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QMessageBox,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QHeaderView,
)


class TransactionTable(QFrame):
    """
    Displays saved transactions.

    Provides:
    - Refresh
    - Delete selected transaction
    """


    def __init__(self):

        super().__init__()

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


        top = QHBoxLayout()


        title = QLabel(
            "Transactions"
        )


        title.setStyleSheet(
            """
            font-size:16px;
            font-weight:700;
            """
        )


        top.addWidget(
            title
        )


        top.addStretch()


        self.refresh_button = QPushButton(
            "Refresh"
        )


        self.delete_button = QPushButton(
            "Delete"
        )


        top.addWidget(
            self.refresh_button
        )


        top.addWidget(
            self.delete_button
        )


        layout.addLayout(
            top
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


        self.table.setAlternatingRowColors(
            True
        )


        self.table.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )


        layout.addWidget(
            self.table
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


        self.table.setRowCount(
            0
        )


        for row, record in enumerate(records):


            self.table.insertRow(
                row
            )


            for column, value in enumerate(record):


                if column == 5:

                    value = f"₹ {float(value):,.2f}"


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
                "Please select a transaction first."
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