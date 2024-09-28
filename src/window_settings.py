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
# BUTTONS - window_scroll_area
for index, item in enumerate(db['buttons']):
    MyButtonSettings(
        index,
        db['buttons'][item]['title'],
        db['buttons'][item]['app_path'],
        db['buttons'][item]['app_launcher'],
        db['buttons'][item]['icon_path']
        )


window_main.show()
sys.exit(app.exec())