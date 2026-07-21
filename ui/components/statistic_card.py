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
    Reusable dashboard statistic card.
    """


    def __init__(
        self,
        title,
        value,
        subtitle,
        accent,
    ):

        super().__init__()

        self.accent = accent

        self.setup_ui(
            title,
            value,
            subtitle
        )



    def setup_ui(
        self,
        title,
        value,
        subtitle
    ):


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


        layout = QHBoxLayout(
            self
        )


        layout.setContentsMargins(
            CARD_PADDING,
            CARD_PADDING,
            CARD_PADDING,
            CARD_PADDING
        )


        # Accent line

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


        layout.addWidget(
            accent_bar
        )


        content = QVBoxLayout()


        self.title_label = QLabel(
            title
        )


        self.title_label.setStyleSheet(
            f"""
            color:{TEXT_SECONDARY};
            font-size:11pt;
            font-weight:600;
            """
        )


        self.value_label = QLabel(
            value
        )


        self.value_label.setStyleSheet(
            f"""
            color:{TEXT_PRIMARY};
            font-size:{VALUE_SIZE}px;
            font-weight:700;
            """
        )


        self.subtitle_label = QLabel(
            subtitle
        )


        self.subtitle_label.setStyleSheet(
            f"""
            color:{TEXT_SECONDARY};
            font-size:9pt;
            """
        )


        content.addWidget(
            self.title_label
        )


        content.addWidget(
            self.value_label
        )


        content.addWidget(
            self.subtitle_label
        )


        layout.addLayout(
            content
        )


        layout.addStretch()



    def update_value(
        self,
        value
    ):
        """
        Updates the displayed amount.
        """

        self.value_label.setText(
            value
        )