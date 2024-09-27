from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QLabel

from .data import cv


class MyImage(QLabel):
    def __init__(self):
        super().__init__()
        self.resize_bg_img()
        self.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.setParent(cv.window)
    
    def resize_bg_img(self):
        self.image = QPixmap(cv.bg_img_path).scaledToWidth(cv.bg_img_size, Qt.TransformationMode.SmoothTransformation)
        self.setPixmap(self.image)
