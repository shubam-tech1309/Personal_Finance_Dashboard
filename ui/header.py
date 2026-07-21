from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QHBoxLayout,
    QVBoxLayout
)

from PySide6.QtCore import Qt


class Header(QWidget):

    def __init__(self):
        super().__init__()

        self.setFixedHeight(80)

        layout = QHBoxLayout()

        layout.setContentsMargins(25, 15, 25, 15)

        # Left Side
        left_layout = QVBoxLayout()

        title = QLabel("Dashboard")

        title.setStyleSheet("""
            font-size:24px;
            font-weight:bold;
            color:#111827;
        """)

        subtitle = QLabel("Welcome to your Personal Finance Dashboard")

        subtitle.setStyleSheet("""
            color:#6B7280;
            font-size:13px;
        """)

        left_layout.addWidget(title)
        left_layout.addWidget(subtitle)

        # Right Side
        profile = QLabel("Shubam")

        profile.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

        profile.setStyleSheet("""
            font-size:14px;
            font-weight:bold;
            color:#111827;
        """)

        layout.addLayout(left_layout)

        layout.addStretch()

        layout.addWidget(profile)

        self.setLayout(layout)

        self.setStyleSheet("""
            background:white;
            border-bottom:1px solid #E5E7EB;
        """)