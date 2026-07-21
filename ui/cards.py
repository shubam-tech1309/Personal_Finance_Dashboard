from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QFrame,
    QGridLayout,
    QVBoxLayout
)

from PySide6.QtCore import Qt


class DashboardCards(QWidget):

    def __init__(self):
        super().__init__()

        grid = QGridLayout()

        grid.setSpacing(20)

        cards = [

            ("Total Income", "₹25,000"),

            ("Total Expense", "₹10,500"),

            ("Current Balance", "₹14,500"),

            ("Savings", "₹5,000")

        ]

        positions = [

            (0,0),

            (0,1),

            (1,0),

            (1,1)

        ]

        for position, data in zip(positions, cards):

            title, value = data

            card = self.create_card(title, value)

            grid.addWidget(card, *position)

        self.setLayout(grid)

    def create_card(self, title, value):

        frame = QFrame()

        frame.setMinimumHeight(140)

        frame.setStyleSheet("""

            QFrame{

                background:white;

                border-radius:12px;

                border:1px solid #E5E7EB;

            }

        """)

        layout = QVBoxLayout()

        layout.setContentsMargins(20,20,20,20)

        heading = QLabel(title)

        heading.setStyleSheet("""

            font-size:15px;

            color:#6B7280;

        """)

        amount = QLabel(value)

        amount.setAlignment(Qt.AlignLeft)

        amount.setStyleSheet("""

            font-size:28px;

            font-weight:bold;

            color:#111827;

        """)

        layout.addWidget(heading)

        layout.addStretch()

        layout.addWidget(amount)

        frame.setLayout(layout)

        return frame