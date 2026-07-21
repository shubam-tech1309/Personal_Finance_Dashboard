from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QAbstractItemView,
    QFrame,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QHeaderView,
)


class TransactionTable(QFrame):
    """
    Displays all finance transactions.
    Database integration will be implemented in a later feature.
    """

    HEADERS = [
        "ID",
        "Date",
        "Type",
        "Category",
        "Description",
        "Amount",
        "Created At",
    ]

    def __init__(self):
        super().__init__()

        self.setup_ui()

    def setup_ui(self):
        self.setObjectName("TransactionTable")

        self.setStyleSheet("""
        QFrame#TransactionTable{
            background:white;
            border:1px solid #E5E7EB;
            border-radius:14px;
        }

        QLabel{
            border:none;
            background:transparent;
        }
        """)

        main_layout = QVBoxLayout(self)

        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(16)

        header_layout = QHBoxLayout()

        title = QLabel("Transactions")

        title.setStyleSheet("""
            font-size:16px;
            font-weight:700;
            color:#111827;
        """)

        header_layout.addWidget(title)

        header_layout.addStretch()

        self.refresh_button = QPushButton("Refresh")

        header_layout.addWidget(self.refresh_button)

        main_layout.addLayout(header_layout)

        self.table = QTableWidget()

        self.table.setColumnCount(len(self.HEADERS))
        self.table.setHorizontalHeaderLabels(self.HEADERS)

        self.table.setAlternatingRowColors(True)

        self.table.setSelectionBehavior(
            QAbstractItemView.SelectRows
        )

        self.table.setSelectionMode(
            QAbstractItemView.SingleSelection
        )

        self.table.setEditTriggers(
            QAbstractItemView.NoEditTriggers
        )

        self.table.setSortingEnabled(True)

        self.table.setShowGrid(False)

        self.table.verticalHeader().setVisible(False)

        header = self.table.horizontalHeader()

        header.setSectionResizeMode(QHeaderView.Stretch)

        self.table.setMinimumHeight(350)

        main_layout.addWidget(self.table)

    def clear_table(self):
        self.table.setRowCount(0)

    def load_data(self, records):
        """
        records should be a list of tuples from SQLite.

        Example:
        [
            (
                id,
                date,
                type,
                category,
                description,
                amount,
                created_at
            )
        ]
        """

        self.table.setSortingEnabled(False)

        self.table.setRowCount(0)

        for row_number, record in enumerate(records):

            self.table.insertRow(row_number)

            for column, value in enumerate(record):

                if column == 5:
                    text = f"₹ {float(value):,.2f}"
                else:
                    text = str(value)

                item = QTableWidgetItem(text)

                item.setTextAlignment(
                    Qt.AlignCenter
                    if column != 4
                    else Qt.AlignLeft | Qt.AlignVCenter
                )

                self.table.setItem(
                    row_number,
                    column,
                    item,
                )

        self.table.setSortingEnabled(True)

    def selected_transaction_id(self):
        row = self.table.currentRow()

        if row < 0:
            return None

        item = self.table.item(row, 0)

        if item is None:
            return None

        return int(item.text())