import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QFont, QIcon, QResizeEvent 
from PyQt6.QtWidgets import (
    QApplication,
    QPushButton,
    QWidget
    )

from src import (
    cv,
    settings
    )



class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(QSize(cv.window_main_width, cv.window_main_height))
        self.setMinimumSize(cv.window_main_min_width, cv.button_size_px + cv.button_pos_gap * 2)
        self.setWindowIcon(QIcon('docs/icons/window_icon.png'))
        self.setWindowTitle("App Launcher")
        if cv.window_main_always_on_top:
            self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
    
    def resizeEvent(self, a0: QResizeEvent):
        if cv.window_main_width != self.width():
            cv.window_main_width = self.width()
            button_move_to_pos()
        return super().resizeEvent(a0)
    


class MyButton(QPushButton):
    def __init__(self, button_number):
        super().__init__()
        self.setParent(window)
        self.resize(cv.button_size_px, cv.button_size_px)
        self.button_number = str(button_number)
        self.button = settings['buttons'][self.button_number]
        if self.button['title']:
            self.setToolTip(self.button['title'])
            self.setToolTipDuration(1500)
            self.setFont(QFont('Times', 9, 600))
            self.setIcon(QIcon(self.button['icon_path']))
            button_icon_diff = 10
            self.setIconSize(QSize(cv.button_size_px-button_icon_diff, cv.button_size_px-button_icon_diff))




app = QApplication(sys.argv)
window = MyWindow()



def button_move_to_pos():
    BUTTON_POS_BASE_X = 30
    BUTTON_POS_BASE_Y = 30
    buttons_counter = 0
    button_pos_y = BUTTON_POS_BASE_Y

    for button_number in cv.buttons_dic:
        button_pos_x = BUTTON_POS_BASE_X + buttons_counter * (cv.button_size_px + cv.button_pos_gap)
        # PLACE BUTTON TO A NEW ROW IF NECESSARY
        if button_pos_x >= cv.window_main_width - cv.button_size_px - BUTTON_POS_BASE_X:
            buttons_counter = 0
            button_pos_x = BUTTON_POS_BASE_X + buttons_counter * (cv.button_size_px + cv.button_pos_gap)
            button_pos_y += cv.button_size_px + cv.button_pos_gap
        cv.buttons_dic[button_number].move(button_pos_x, button_pos_y)
        buttons_counter += 1


# BUTTON CREATION & PLACEMENT
for button_number in settings['buttons']:
    cv.buttons_dic[button_number] = MyButton(button_number)
    if settings['buttons'][button_number]['title']:
        button_move_to_pos()
    else:
        cv.buttons_dic[button_number].hide()


window.show()
sys.exit(app.exec())