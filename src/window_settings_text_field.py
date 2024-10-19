from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QLineEdit

from data import cv


class MyTextLine(QLineEdit):
    def __init__(self, field_type, pos_x, pos_y):
        super().__init__()
        self.setParent(cv.window_settings_main)
        self.setCursor(Qt.CursorShape.IBeamCursor)
        self.setFont(QFont(cv.TEXT_FIELD_FONT_STYLE, cv.TEXT_FIELD_FONT_SIZE, 600))
        self.setStyleSheet(
                        "qproperty-cursorPosition: 0;"  # text length > field length
                        f"background-color: {cv.FIELD_BG_COLOR};"
                        "border-radius: 2px;"
                        "border: 1px solid white;"
                        f"color: {cv.TEXT_FIELD_FONT_COLOR};"
                        )
        self.setGeometry(pos_x, pos_y, 200, 30)
        cv.TEXT_FIELDS_DIC[field_type] = self
 