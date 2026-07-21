from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
)

from ui.components.statistic_card import StatisticCard

from styles.palette import (
    PRIMARY,
    SUCCESS,
    DANGER,
    PURPLE,
)


class DashboardCards(QWidget):
    """
    Container for dashboard financial statistics.

    This widget controls all summary cards.
    Later it will receive live data from SQLite.
    """

    def __init__(self):
        super().__init__()

        self.setup_ui()


    def setup_ui(self):

        layout = QHBoxLayout(
            self
        )

        layout.setContentsMargins(
            0,
            0,
            0,
            0
        )

        layout.setSpacing(
            18
        )


        self.balance_card = StatisticCard(
            title="Current Balance",
            value="₹0.00",
            subtitle="Available funds",
            accent=PRIMARY,
        )


        self.income_card = StatisticCard(
            title="Total Income",
            value="₹0.00",
            subtitle="This month",
            accent=SUCCESS,
        )


        self.expense_card = StatisticCard(
            title="Total Expenses",
            value="₹0.00",
            subtitle="This month",
            accent=DANGER,
        )


        self.savings_card = StatisticCard(
            title="Savings",
            value="₹0.00",
            subtitle="Financial growth",
            accent=PURPLE,
        )


        layout.addWidget(
            self.balance_card
        )

        layout.addWidget(
            self.income_card
        )

        layout.addWidget(
            self.expense_card
        )

        layout.addWidget(
            self.savings_card
        )


    def update_statistics(
        self,
        balance,
        income,
        expenses,
        savings,
    ):
        """
        Updates dashboard values.

        Database connection will be added later.
        """

        self.balance_card.update_value(
            f"₹{balance:,.2f}"
        )

        self.income_card.update_value(
            f"₹{income:,.2f}"
        )

        self.expense_card.update_value(
            f"₹{expenses:,.2f}"
        )

        self.savings_card.update_value(
            f"₹{savings:,.2f}"
        )