from PySide6.QtWidgets import (
    QWidget,
    QMainWindow,
    QHBoxLayout,
    QVBoxLayout
)

from ui.sidebar import Sidebar
from ui.header import Header
from ui.cards import DashboardCards


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Personal Finance Dashboard")

        self.resize(1200,750)

        self.setMinimumSize(1000,650)

        central_widget = QWidget()

        self.setCentralWidget(central_widget)

        main_layout = QHBoxLayout()

        main_layout.setContentsMargins(0,0,0,0)

        main_layout.setSpacing(0)

        sidebar = Sidebar()

        content = QWidget()

        content_layout = QVBoxLayout()

        content_layout.setContentsMargins(20,20,20,20)

        content_layout.setSpacing(20)

        header = Header()

        cards = DashboardCards()

        content_layout.addWidget(header)

        content_layout.addWidget(cards)

        content_layout.addStretch()

        content.setLayout(content_layout)

        main_layout.addWidget(sidebar)

        main_layout.addWidget(content,1)

        central_widget.setLayout(main_layout)