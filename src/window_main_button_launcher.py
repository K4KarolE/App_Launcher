import os
import subprocess

from PyQt6.QtCore import QSize
from PyQt6.QtGui import QFont, QIcon
from PyQt6.QtWidgets import QPushButton

from .data import cv, db, WORKING_DIRECTORY


class MyButton(QPushButton):
    def __init__(self, button_number):
        super().__init__()
        self.setParent(cv.window)
        self.resize(cv.button_size, cv.button_size)
        self.button_number = str(button_number)
        self.button = db['buttons'][self.button_number]
        if self.button['title']:
            self.setToolTip(self.button['title'])
            self.setToolTipDuration(1500)
            self.setFont(QFont('Times', 9, 600))
            self.setIcon(QIcon(self.button['icon_path']))
            button_icon_diff = 5
            self.setIconSize(QSize(cv.button_size-button_icon_diff, cv.button_size-button_icon_diff))
            self.set_style_playlist_buttons()
            self.clicked.connect(self.button_clicked_action)
    

    def set_style_playlist_buttons(self):
        self.setStyleSheet(
                        "QPushButton"
                            "{"
                            # "background-color: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 white, stop: 0.2 #F0F0F0, stop: 0.8 #F0F0F0, stop: 1 #C2C2C2);"
                            f"background-color: {cv.button_bd_color};"
                            # "color: grey;"   # font
                            # "border: 1px solid grey;"
                            "border-radius: 2px;"
                            # "margin: 3 px;" # 3 px != 3px
                            "}"
                        "QPushButton::pressed"
                            "{"
                            "background-color : #C2C2C2;"
                            "}"
                        )
    
    def button_clicked_action(self):
        '''
        os.chdir(app_dir) / os.chdir(WORKING_DIRECTORY):
            be able to launch pyhton applications
            one after another
        '''

        app_launcher = db['buttons'][self.button_number]['app_launcher']
        app_path = db['buttons'][self.button_number]['app_path']
        app_dir = os.path.dirname(app_path)
        os.chdir(app_dir)
        
        if 'py' in app_launcher:
            '''
            app_launcher =  
            'py' -> terminal
            'pyw' -> no terminl
            '''
            subprocess.Popen(f'{app_launcher} "{app_path}"')
        else:
            os.startfile(app_path)
        
        os.chdir(WORKING_DIRECTORY)