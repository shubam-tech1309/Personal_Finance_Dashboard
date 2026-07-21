from PySide6.QtCore import QDate, Qt

from PySide6.QtWidgets import (
    QFrame,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QFormLayout,
    QDateEdit,
    QComboBox,
    QLineEdit,
    QDoubleSpinBox,
    QPushButton,
    QMessageBox,
)

from utils.validators import (
    clean_text,
    clean_category,
    clean_description,
    clean_amount,
    validate_transaction,
)



class TransactionForm(QFrame):


    def __init__(self):

        super().__init__()


        self.save_callback = None

        self.edit_id = None


        self.setup_ui()

        self.setup_navigation()



    def setup_ui(self):


        self.setObjectName(
            "TransactionForm"
        )


        self.setStyleSheet(
            """

            QFrame#TransactionForm
            {
                background:#FFFFFF;
                border-radius:14px;
                border:1px solid #E5E7EB;
            }


            QLineEdit,
            QComboBox,
            QDateEdit,
            QDoubleSpinBox
            {
                padding:8px;
                font-size:14px;
                border-radius:8px;
                border:1px solid #D1D5DB;
            }


            QPushButton
            {
                padding:10px;
                border-radius:8px;
                font-weight:600;
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
            "Add Transaction"
        )


        title.setStyleSheet(
            """
            font-size:18px;
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



        self.category_input = QLineEdit()


        self.category_input.setPlaceholderText(
            "Category"
        )



        self.description_input = QLineEdit()


        self.description_input.setPlaceholderText(
            "Description"
        )



        self.amount_input = QDoubleSpinBox()


        self.amount_input.setPrefix(
            "₹ "
        )


        self.amount_input.setMaximum(
            999999999
        )


        self.amount_input.setDecimals(
            2
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
            self.category_input
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
            "Save Transaction  (Ctrl + S)"
        )


        self.clear_button = QPushButton(
            "Clear  (Ctrl + L)"
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



    def setup_navigation(self):


        fields = [

            self.date_edit,

            self.type_combo,

            self.category_input,

            self.description_input,

            self.amount_input,

        ]



        for field in fields:

            field.setFocusPolicy(
                Qt.StrongFocus
            )



        self.date_edit.editingFinished.connect(

            lambda:
            self.type_combo.setFocus()

        )



        self.type_combo.activated.connect(

            lambda:
            self.category_input.setFocus()

        )



        self.category_input.returnPressed.connect(

            lambda:
            self.description_input.setFocus()

        )



        self.description_input.returnPressed.connect(

            lambda:
            self.amount_input.setFocus()

        )



        self.amount_input.lineEdit().returnPressed.connect(

            self.handle_save

        )



    def handle_save(self):


        data = {


            "date":

            self.date_edit
            .date()
            .toString(
                "yyyy-MM-dd"
            ),



            "type":

            clean_text(
                self.type_combo.currentText()
            ),



            "category":

            clean_category(
                self.category_input.text()
            ),



            "description":

            clean_description(
                self.description_input.text()
            ),



            "amount":

            clean_amount(
                self.amount_input.value()
            )

        }



        valid, errors = validate_transaction(
            data
        )



        if not valid:


            QMessageBox.warning(

                self,

                "Check Details",

                "\n".join(errors)

            )

            return



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


        self.category_input.setText(

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


        self.date_edit.setDate(
            QDate.currentDate()
        )


        self.type_combo.setCurrentIndex(
            0
        )


        self.category_input.clear()


        self.description_input.clear()


        self.amount_input.setValue(
            0
        )


        self.date_edit.setFocus()
