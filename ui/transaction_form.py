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
    QMessageBox,
)

from utils.validators import (
    title_case,
    validate_transaction,
)


class TransactionForm(QFrame):
    """
    Transaction entry form.

    Handles user input and emits saved data.
    """

    def __init__(self):

        super().__init__()

        self.save_callback = None

        self.setup_ui()


    def setup_ui(self):

        self.setObjectName(
            "TransactionForm"
        )


        self.setStyleSheet(
            """
            QFrame#TransactionForm
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


        title = QLabel(
            "New Transaction"
        )


        title.setStyleSheet(
            """
            font-size:16px;
            font-weight:700;
            """
        )


        layout.addWidget(
            title
        )


        form = QFormLayout()


        self.date_edit = QDateEdit()

        self.date_edit.setDate(
            QDate.currentDate()
        )

        self.date_edit.setCalendarPopup(
            True
        )


        self.type_combo = QComboBox()

        self.type_combo.addItems(
            [
                "Income",
                "Expense"
            ]
        )


        self.category_combo = QComboBox()

        self.category_combo.addItems(
            [
                "Salary",
                "Business",
                "Food",
                "Transport",
                "Shopping",
                "Bills",
                "Investment",
                "Other"
            ]
        )


        self.description_input = QLineEdit()

        self.description_input.setPlaceholderText(
            "Example: Monthly salary"
        )


        self.amount_input = QDoubleSpinBox()

        self.amount_input.setMaximum(
            999999999
        )

        self.amount_input.setDecimals(
            2
        )

        self.amount_input.setPrefix(
            "₹ "
        )


        form.addRow(
            "Date",
            self.date_edit
        )

        form.addRow(
            "Type",
            self.type_combo
        )

        form.addRow(
            "Category",
            self.category_combo
        )

        form.addRow(
            "Description",
            self.description_input
        )

        form.addRow(
            "Amount",
            self.amount_input
        )


        layout.addLayout(
            form
        )


        button_layout = QHBoxLayout()

        button_layout.addStretch()


        self.add_button = QPushButton(
            "Add Transaction"
        )


        self.add_button.clicked.connect(
            self.handle_save
        )


        button_layout.addWidget(
            self.add_button
        )


        layout.addLayout(
            button_layout
        )


    def handle_save(self):

        description = title_case(
            self.description_input.text()
        )


        amount = self.amount_input.value()


        valid, message = validate_transaction(
            description,
            amount
        )


        if not valid:

            QMessageBox.warning(
                self,
                "Validation Error",
                message
            )

            return


        data = {

            "date":
            self.date_edit.date().toString(
                "yyyy-MM-dd"
            ),

            "type":
            self.type_combo.currentText(),

            "category":
            self.category_combo.currentText(),

            "description":
            description,

            "amount":
            amount
        }


        if self.save_callback:

            self.save_callback(
                data
            )


        self.clear_form()



    def clear_form(self):

        self.description_input.clear()

        self.amount_input.setValue(
            0
        )