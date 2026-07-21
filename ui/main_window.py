from PySide6.QtWidgets import (
    QWidget,
    QMainWindow,
    QHBoxLayout,
    QVBoxLayout,
    QLabel
)

from PySide6.QtCore import Qt

from ui.sidebar import Sidebar
from ui.header import Header


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Personal Finance Dashboard")

        self.resize(1200, 750)

        self.setMinimumSize(1000, 650)

        # Central Widget
        central_widget = QWidget()

        self.setCentralWidget(central_widget)

        # Main Horizontal Layout
        main_layout = QHBoxLayout()

        main_layout.setContentsMargins(0, 0, 0, 0)

        main_layout.setSpacing(0)

        # Sidebar
        sidebar = Sidebar()

        # Content Area
        content = QWidget()

        content_layout = QVBoxLayout()

        content_layout.setContentsMargins(0, 0, 0, 0)

        content_layout.setSpacing(0)

        # Header
        header = Header()

        # Body
        body = QLabel("Dashboard Content Coming Soon")

        body.setAlignment(Qt.AlignCenter)

        body.setStyleSheet("""
            background:#F5F7FA;
            font-size:22px;
            color:#6B7280;
        """)

        content_layout.addWidget(header)

        content_layout.addWidget(body)

        content.setLayout(content_layout)

        # Add Everything
        main_layout.addWidget(sidebar)

        main_layout.addWidget(content)

        central_widget.setLayout(main_layout)