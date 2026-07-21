from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFrame,
    QGridLayout,
    QLabel,
    QVBoxLayout,
)


class SummaryCard(QFrame):
    """
    Reusable dashboard card.
    """

    def __init__(self, title: str, value: str):
        super().__init__()

        self.title_label = QLabel(title)
        self.value_label = QLabel(value)

        self.setup_ui()

    def setup_ui(self):
        self.setMinimumHeight(120)

        self.setStyleSheet("""
        QFrame{
            background:white;
            border:1px solid #E5E7EB;
            border-radius:14px;
        }
        """)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 18, 20, 18)
        layout.setSpacing(10)

        self.title_label.setAlignment(Qt.AlignLeft)

        self.title_label.setStyleSheet("""
            font-size:11pt;
            font-weight:600;
            color:#6B7280;
            border:none;
            background:transparent;
        """)

        self.value_label.setAlignment(Qt.AlignLeft)

        self.value_label.setStyleSheet("""
            font-size:24px;
            font-weight:700;
            color:#111827;
            border:none;
            background:transparent;
        """)

        layout.addWidget(self.title_label)
        layout.addStretch()
        layout.addWidget(self.value_label)

    def set_value(self, value: str):
        self.value_label.setText(value)


class SummaryCards(QFrame):
    """
    Container holding all dashboard summary cards.
    """

    def __init__(self):
        super().__init__()

        self.balance_card = SummaryCard(
            "Current Balance",
            "₹0.00"
        )

        self.income_card = SummaryCard(
            "Total Income",
            "₹0.00"
        )

        self.expense_card = SummaryCard(
            "Total Expenses",
            "₹0.00"
        )

        self.savings_card = SummaryCard(
            "Savings",
            "₹0.00"
        )

        self.setup_ui()

    def setup_ui(self):
        self.setStyleSheet("""
        QFrame{
            background:transparent;
            border:none;
        }
        """)

        layout = QGridLayout(self)

        layout.setHorizontalSpacing(18)
        layout.setVerticalSpacing(18)

        layout.addWidget(self.balance_card, 0, 0)
        layout.addWidget(self.income_card, 0, 1)
        layout.addWidget(self.expense_card, 1, 0)
        layout.addWidget(self.savings_card, 1, 1)

    def update_cards(
        self,
        balance,
        income,
        expense,
        savings,
    ):
        self.balance_card.set_value(f"₹{balance:,.2f}")
        self.income_card.set_value(f"₹{income:,.2f}")
        self.expense_card.set_value(f"₹{expense:,.2f}")
        self.savings_card.set_value(f"₹{savings:,.2f}")