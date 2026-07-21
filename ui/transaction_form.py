from PySide6.QtCore import QDate
from PySide6.QtWidgets import (
    QComboBox,
    QDateEdit,
    QDoubleSpinBox,
    QFormLayout,
    QFrame,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
)


class TransactionForm(QFrame):
    """
    Transaction entry form.
    Business logic will be added in later features.
    """

    def __init__(self):
        super().__init__()

        self.setup_ui()

    def setup_ui(self):
        self.setObjectName("TransactionForm")

        self.setStyleSheet("""
        QFrame#TransactionForm{
            background:white;
            border:1px solid #E5E7EB;
            border-radius:14px;
        }

        QLabel{
            background:transparent;
            border:none;
        }
        """)

        main_layout = QVBoxLayout(self)

        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(16)

        title = QLabel("New Transaction")

        title.setStyleSheet("""
            font-size:16px;
            font-weight:700;
            color:#111827;
        """)

        main_layout.addWidget(title)

        form = QFormLayout()

        form.setHorizontalSpacing(18)
        form.setVerticalSpacing(14)

        self.date_edit = QDateEdit()

        self.date_edit.setCalendarPopup(True)
        self.date_edit.setDate(QDate.currentDate())

        self.type_combo = QComboBox()

        self.type_combo.addItems([
            "Income",
            "Expense"
        ])

        self.category_combo = QComboBox()

        self.category_combo.addItems([
            "Salary",
            "Business",
            "Food",
            "Transport",
            "Shopping",
            "Bills",
            "Health",
            "Investment",
            "Entertainment",
            "Other"
        ])

        self.description_input = QLineEdit()

        self.description_input.setPlaceholderText(
            "Enter description"
        )

        self.amount_input = QDoubleSpinBox()

        self.amount_input.setMaximum(999999999)

        self.amount_input.setDecimals(2)

        self.amount_input.setPrefix("₹ ")

        self.amount_input.setSingleStep(100)

        form.addRow("Date", self.date_edit)
        form.addRow("Type", self.type_combo)
        form.addRow("Category", self.category_combo)
        form.addRow("Description", self.description_input)
        form.addRow("Amount", self.amount_input)

        main_layout.addLayout(form)

        button_layout = QHBoxLayout()

        button_layout.addStretch()

        self.add_button = QPushButton("Add Transaction")

        self.add_button.setMinimumHeight(40)

        button_layout.addWidget(self.add_button)

        main_layout.addLayout(button_layout)

    def get_transaction_data(self):
        """
        Returns the entered values.
        Database integration will be implemented later.
        """

        return {
            "date": self.date_edit.date().toString("yyyy-MM-dd"),
            "type": self.type_combo.currentText(),
            "category": self.category_combo.currentText(),
            "description": self.description_input.text().strip(),
            "amount": self.amount_input.value(),
        }

    def clear_form(self):
        """
        Resets the form after saving.
        """

        self.date_edit.setDate(QDate.currentDate())

        self.type_combo.setCurrentIndex(0)

        self.category_combo.setCurrentIndex(0)

        self.description_input.clear()

        self.amount_input.setValue(0.00)