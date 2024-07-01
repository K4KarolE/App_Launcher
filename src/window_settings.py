
import sys
import os

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QKeySequence, QResizeEvent, QShortcut, QIcon, QFont
from PyQt6.QtWidgets import (
    QApplication,
    QFrame,
    QHBoxLayout,
    QPushButton,
    QSplitter,
    QVBoxLayout,
    QWidget
    )

from .cons_and_vars import cv, settings
# from cons_and_vars import cv, settings



# app = QApplication(sys.argv)


# class MyWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.resize(QSize(cv.window_main_width, cv.window_main_height))
#         self.setMinimumSize(cv.window_main_min_width, cv.button_size_px + cv.button_pos_gap * 2)
#         self.setWindowIcon(QIcon('docs/icons/window_icon.png'))
#         self.setWindowTitle("App Launcher")
#         if cv.window_main_always_on_top:
#             self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
    

# window = MyWindow()

# window.show()
# sys.exit(app.exec())