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

    def __init__(self):

        super().__init__()

        self.save_callback = None

        self.edit_id = None

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
            "Transaction"
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


        buttons = QHBoxLayout()


        self.save_button = QPushButton(
            "Save Transaction"
        )


        self.clear_button = QPushButton(
            "Clear"
        )


        buttons.addWidget(
            self.save_button
        )


        buttons.addWidget(
            self.clear_button
        )


        layout.addLayout(
            buttons
        )


        self.save_button.clicked.connect(
            self.handle_save
        )


        self.clear_button.clicked.connect(
            self.clear_form
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
                data,
                self.edit_id
            )



        self.clear_form()



    def load_transaction(
        self,
        record
    ):

        self.edit_id = record[0]


        self.date_edit.setDate(
            QDate.fromString(
                record[1],
                "yyyy-MM-dd"
            )
        )


        self.type_combo.setCurrentText(
            record[2]
        )


        self.category_combo.setCurrentText(
            record[3]
        )


        self.description_input.setText(
            record[4]
        )


        self.amount_input.setValue(
            float(record[5])
        )



    def clear_form(self):

        self.edit_id = None

        self.description_input.clear()

        self.amount_input.setValue(
            0
        )