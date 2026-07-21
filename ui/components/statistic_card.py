from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QHBoxLayout,
    QVBoxLayout,
)

from styles.palette import (
    CARD,
    TEXT_PRIMARY,
    TEXT_SECONDARY,
    BORDER,
    CARD_HEIGHT,
    CARD_PADDING,
    RADIUS_LARGE,
    VALUE_SIZE,
)


class StatisticCard(QFrame):
    """
    Premium dashboard statistic card.

    Example:

    card = StatisticCard(
        title="Income",
        value="₹50,000",
        subtitle="This Month",
        accent="#22C55E"
    )
    """

    def __init__(
        self,
        title: str,
        value: str,
        subtitle: str,
        accent: str,
    ):
        super().__init__()

        self.title = title
        self.value = value
        self.subtitle = subtitle
        self.accent = accent

        self.setup_ui()


    def setup_ui(self):

        self.setFixedHeight(
            CARD_HEIGHT
        )

        self.setObjectName(
            "StatisticCard"
        )


        self.setStyleSheet(
            f"""
            QFrame#StatisticCard
            {{
                background:{CARD};
                border:1px solid {BORDER};
                border-radius:{RADIUS_LARGE}px;
            }}

            QFrame#StatisticCard:hover
            {{
                border:1px solid {self.accent};
            }}
            """
        )


        main_layout = QHBoxLayout(
            self
        )

        main_layout.setContentsMargins(
            CARD_PADDING,
            CARD_PADDING,
            CARD_PADDING,
            CARD_PADDING,
        )

        main_layout.setSpacing(
            18
        )


        # Accent indicator

        accent_bar = QFrame()

        accent_bar.setFixedWidth(
            6
        )

        accent_bar.setStyleSheet(
            f"""
            background:{self.accent};
            border-radius:3px;
            """
        )


        main_layout.addWidget(
            accent_bar
        )


        # Text section

        text_layout = QVBoxLayout()

        text_layout.setSpacing(
            5
        )


        title_label = QLabel(
            self.title
        )

        title_label.setStyleSheet(
            f"""
            color:{TEXT_SECONDARY};
            font-size:11pt;
            font-weight:600;
            border:none;
            """
        )


        value_label = QLabel(
            self.value
        )

        value_label.setStyleSheet(
            f"""
            color:{TEXT_PRIMARY};
            font-size:{VALUE_SIZE}px;
            font-weight:700;
            border:none;
            """
        )


        subtitle_label = QLabel(
            self.subtitle
        )

        subtitle_label.setStyleSheet(
            f"""
            color:{TEXT_SECONDARY};
            font-size:9pt;
            border:none;
            """
        )


        text_layout.addWidget(
            title_label
        )

        text_layout.addWidget(
            value_label
        )

        text_layout.addWidget(
            subtitle_label
        )


        main_layout.addLayout(
            text_layout
        )

        main_layout.addStretch()


    def update_value(
        self,
        value: str
    ):
        """
        Update displayed value dynamically.
        """

        self.value = value