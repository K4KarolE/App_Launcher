import sys

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QScrollArea,
    QMainWindow
    )

from buttons_settings import MyButtonSettings
from data import cv, db




''' APP '''
app = QApplication(sys.argv)


'''
WINDOW MAIN <-- QSCROLLAREA WINDOW <-- QWIDGET WINDOW <-- QWIDGETS
'''

# MAIN WINDOW
window_main = QWidget()
window_main.resize(500, 300)
window_main.setWindowTitle("Grab & move a button")


# QSCROLL AREA WINDOW
window_scroll_area = QScrollArea(window_main)
window_scroll_area.setGeometry(50, 50, 400, 100)
window_scroll_area.setStyleSheet(f"background-color: green;")

# QWIDGET WINDOW
cv.window_widgets = QMainWindow()
cv.window_widgets.setStyleSheet(f"background-color: grey;")
cv.window_widgets.setGeometry(0, 0, cv.window_widgets_width, 80)
window_scroll_area.setWidget(cv.window_widgets)


# WIDGET
for index, item in enumerate(db['buttons']):
    pos_x = cv.button_pos_gap + (cv.button_size_sett_win + cv.button_pos_gap_sett_win) * index
    if db['buttons'][item]['title'] != "":
        is_button = True
    else:
        is_button = False
    MyButtonSettings(pos_x, is_button)


window_main.show()
sys.exit(app.exec())