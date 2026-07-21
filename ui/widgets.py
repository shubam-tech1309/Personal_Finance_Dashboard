from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout,
)


class SummaryCard(QFrame):
    """
    Reusable dashboard summary card.
    """

    def __init__(self, title: str, value: str):
        super().__init__()

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
        layout.setSpacing(8)

        title_label = QLabel(title)
        title_label.setAlignment(Qt.AlignLeft)

        title_label.setStyleSheet("""
            font-size:11pt;
            color:#6B7280;
            font-weight:600;
            background:transparent;
            border:none;
        """)

        value_label = QLabel(value)
        value_label.setAlignment(Qt.AlignLeft)

        value_label.setStyleSheet("""
            font-size:22pt;
            font-weight:700;
            color:#111827;
            background:transparent;
            border:none;
        """)

        layout.addWidget(title_label)
        layout.addStretch()
        layout.addWidget(value_label)