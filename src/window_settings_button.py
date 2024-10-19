from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QPushButton

from data import cv


class MyBaseButtonSettings(QPushButton):
    def __init__(self, text, pos_x, pos_y, func):
        super().__init__()
        self.setParent(cv.window_settings_main)
        self.setGeometry(pos_x, pos_y, 100, 30)
        self.setText(text)
        self.clicked.connect(lambda: func())
        self.setFont(QFont(cv.TEXT_FIELD_FONT_STYLE, cv.TEXT_FIELD_FONT_SIZE, 600))
        self.setStyleSheet(
            "QPushButton"
                "{"
                "border-radius: 2px;"
                "border: 1px solid white;"
                f"background-color: {cv.FIELD_BG_COLOR};"
                f"color: {cv.TEXT_FIELD_FONT_COLOR};"
                "}"
            "QPushButton::pressed"
                "{"
                f"background-color: grey;"
                "}"
                )
 