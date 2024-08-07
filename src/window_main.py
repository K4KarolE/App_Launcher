from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QIcon, QResizeEvent
from PyQt6.QtWidgets import QWidget

from src import cv


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(QSize(cv.window_main_width, cv.window_main_height))
        self.setMinimumSize(cv.window_main_min_width, cv.button_size_px + cv.button_pos_gap * 2)
        self.setWindowIcon(QIcon('docs/icons/window_icon.png'))
        self.setWindowTitle("App Launcher")
    
    def resizeEvent(self, a0: QResizeEvent):
        if cv.window_main_width != self.width():
            cv.window_main_width = self.width()
            cv.button_move_to_pos()
        return super().resizeEvent(a0)