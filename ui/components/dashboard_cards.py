from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QFrame,
    QVBoxLayout,
    QLabel,
)

from PySide6.QtCore import Qt



class DashboardCard(QFrame):


    def __init__(
        self,
        title
    ):

        super().__init__()


        self.setObjectName(
            "DashboardCard"
        )


        self.setStyleSheet(
            """

            QFrame#DashboardCard
            {

                background:white;

                border-radius:16px;

                border:1px solid #E5E7EB;

            }


            QLabel
            {

                color:#111827;

            }

            """
        )



        layout = QVBoxLayout(
            self
        )


        layout.setContentsMargins(
            18,
            18,
            18,
            18
        )



        self.title_label = QLabel(
            title
        )


        self.title_label.setStyleSheet(
            """
            font-size:13px;
            color:#64748B;
            """
        )



        self.value_label = QLabel(
            "₹ 0.00"
        )


        self.value_label.setStyleSheet(
            """
            font-size:24px;
            font-weight:700;
            """
        )



        layout.addWidget(
            self.title_label
        )


        layout.addWidget(
            self.value_label
        )



    def update_value(
        self,
        value
    ):


        self.value_label.setText(

            f"₹ {value:,.2f}"

        )





class DashboardCards(QWidget):


    def __init__(self):

        super().__init__()


        self.setup_ui()



    def setup_ui(self):


        layout = QHBoxLayout(
            self
        )


        layout.setSpacing(
            15
        )


        self.balance_card = DashboardCard(

            "Current Balance"

        )


        self.income_card = DashboardCard(

            "Total Income"

        )


        self.expense_card = DashboardCard(

            "Total Expense"

        )


        self.savings_card = DashboardCard(

            "Savings"

        )



        cards = [

            self.balance_card,

            self.income_card,

            self.expense_card,

            self.savings_card

        ]



        for card in cards:

            layout.addWidget(
                card
            )



    def update_statistics(

        self,

        balance,

        income,

        expense,

        savings

    ):


        self.balance_card.update_value(

            balance

        )


        self.income_card.update_value(

            income

        )


        self.expense_card.update_value(

            expense

        )


        self.savings_card.update_value(

            savings

        )