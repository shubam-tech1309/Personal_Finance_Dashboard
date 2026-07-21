from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton


class Sidebar(QWidget):
    def __init__(self):
        super().__init__()

        # Sidebar width
        self.setFixedWidth(220)

        # Main Layout
        layout = QVBoxLayout()
        layout.setContentsMargins(15, 20, 15, 20)
        layout.setSpacing(12)

        # Title
        title = QLabel("Personal Finance")
        title.setAlignment(Qt.AlignCenter)

        title.setStyleSheet("""
            color: white;
            font-size: 18px;
            font-weight: bold;
            margin-bottom: 20px;
        """)

        layout.addWidget(title)

        # Navigation Buttons
        menu_items = [
            "Dashboard",
            "Income",
            "Expenses",
            "Transactions",
            "Settings"
        ]

        for item in menu_items:
            button = QPushButton(item)

            button.setFixedHeight(45)

            button.setStyleSheet("""
                QPushButton{
                    background-color:#334155;
                    color:white;
                    border:none;
                    border-radius:8px;
                    text-align:left;
                    padding-left:15px;
                    font-size:14px;
                }

                QPushButton:hover{
                    background-color:#2563EB;
                }
            """)

            layout.addWidget(button)

        # Push everything to top
        layout.addStretch()

        self.setLayout(layout)

        self.setStyleSheet("""
            background-color:#1E293B;
        """)