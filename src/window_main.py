from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon, QResizeEvent
from PyQt6.QtWidgets import QWidget

from .data import cv


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(QSize(cv.window_main_width, cv.window_main_height))
        self.setMinimumSize(cv.WINDOW_MAIN_MIN_WIDTH, cv.button_size + cv.button_pos_gap * 2)
        self.setWindowIcon(QIcon('docs/icons/window_icon.png'))
        self.setWindowTitle("App Launcher")
    
    def resizeEvent(self, a0: QResizeEvent):
        if cv.window_main_width != self.width():
            cv.window_main_width = self.width()
            cv.button_move_to_pos_func()
        return super().resizeEvent(a0)