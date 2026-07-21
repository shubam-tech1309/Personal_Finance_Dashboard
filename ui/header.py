from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QHBoxLayout,
    QVBoxLayout,
)


class Header(QFrame):
    """
    Application header displayed at the top of the dashboard.
    """

    def __init__(self):
        super().__init__()

        self.setObjectName("Header")

        self.setStyleSheet("""
        QFrame#Header{
            background:white;
            border:1px solid #E5E7EB;
            border-radius:14px;
        }
        """)

        self.setMinimumHeight(90)

        layout = QHBoxLayout(self)

        layout.setContentsMargins(25, 18, 25, 18)
        layout.setSpacing(20)

        text_layout = QVBoxLayout()
        text_layout.setSpacing(4)

        title = QLabel("Personal Finance Dashboard")
        title.setAlignment(Qt.AlignLeft)

        title.setStyleSheet("""
            font-size:22px;
            font-weight:700;
            color:#111827;
            border:none;
            background:transparent;
        """)

        subtitle = QLabel(
            "Manage your income, expenses, savings and financial reports."
        )

        subtitle.setAlignment(Qt.AlignLeft)

        subtitle.setStyleSheet("""
            font-size:10pt;
            color:#6B7280;
            border:none;
            background:transparent;
        """)

        text_layout.addWidget(title)
        text_layout.addWidget(subtitle)

        layout.addLayout(text_layout)
        layout.addStretch()