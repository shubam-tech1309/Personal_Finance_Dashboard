from PySide6.QtWidgets import (
    QWidget,
    QMainWindow,
    QHBoxLayout,
    QLabel
)

from PySide6.QtCore import Qt

from ui.sidebar import Sidebar


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

        # Placeholder Content Area
        content = QLabel("Dashboard Area")
        content.setAlignment(Qt.AlignCenter)

        content.setStyleSheet("""
            background:#F5F7FA;
            font-size:24px;
            color:#555555;
        """)

        # Add Widgets
        main_layout.addWidget(sidebar)
        main_layout.addWidget(content, 1)

        central_widget.setLayout(main_layout)