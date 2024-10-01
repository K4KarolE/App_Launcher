import sys

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QScrollArea,
    QMainWindow,
    QPushButton
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
window_main.resize(cv.window_settings_width, cv.window_settings_height)
window_main.setWindowTitle("Settings")
window_main.setStyleSheet(f"background-color: #555555;")
window_main.setWindowIcon(QIcon('docs/icons/settings_main_img.png'))


# QSCROLL AREA WINDOW
BASE_X = 20
button_window_scroll_area_width = cv.window_settings_width - BASE_X*2
button_window_scroll_area = QScrollArea(window_main)
button_window_scroll_area.setGeometry(
                                    20,
                                    30,
                                    button_window_scroll_area_width,
                                    cv.button_window_scroll_area_height
                                    )
button_window_scroll_area.setStyleSheet(f"background-color: #454545;")

# QWIDGET WINDOW
cv.button_window = QMainWindow()
cv.button_window.setStyleSheet("background-color: #454545;")
cv.button_window.setGeometry(0, 0, cv.button_window_width, cv.button_window_height)
button_window_scroll_area.setWidget(cv.button_window)

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


def remove_button():
    if len(cv.button_window_button_list) != 0:
        for button in cv.button_window_button_list:
            if button.seq_number > cv.selected_button_index:
                button.seq_number -= 1
                button.move(button.get_pos_x(), cv.button_window_button_pos_y)
        cv.button_window_button_list[cv.selected_button_index].deleteLater()
        cv.button_window_button_list.pop(cv.selected_button_index)
        
        if cv.selected_button_index != 0:
            if cv.selected_button_index + 1 > len(cv.button_window_button_list):
                cv.selected_button_index -= 1
        if len(cv.button_window_button_list) > 0:
            cv.button_window_button_list[cv.selected_button_index].set_style_selected_button()
        
        resize_button_window()



def add_new_button():
    button_list_length = len(cv.button_window_button_list)

    if cv.selected_button_index + 1 == button_list_length:
        new_button_index = button_list_length
    elif button_list_length == 0:
        new_button_index = 0
    else:
        new_button_index = cv.selected_button_index + 1

    for button in cv.button_window_button_list:
        if button.seq_number >= new_button_index:
            button.seq_number += 1
            button.move(button.get_pos_x(), cv.button_window_button_pos_y)

    new_button = MyButtonSettings(new_button_index)
    layout = cv.button_window.layout()
    layout.addChildWidget(new_button)

    if len(cv.button_window_button_list) == 1:
        cv.button_window_button_list[0].set_style_selected_button()

    resize_button_window()
    sort_button_list()


def resize_button_window():
    cv.button_window_width = (
        cv.button_pos_gap_sett_win
        + cv.button_size_and_gap_sett_win
        * len(cv.button_window_button_list)
        )
    if cv.button_window_width < button_window_scroll_area_width:
        cv.button_window_width = button_window_scroll_area_width
    cv.button_window.resize(cv.button_window_width, cv.button_window_height)





aa = QPushButton(window_main, text="Add")
aa.setGeometry(100, 200, 100, 30)
aa.clicked.connect(lambda: add_new_button())


bb = QPushButton(window_main, text="Remove")
bb.setGeometry(100, 260, 100, 30)
bb.clicked.connect(lambda: remove_button())
















''' Sort before apply/save '''
def get_seq_number(e):
        return e.seq_number

def sort_button_list():
    cv.button_window_button_list.sort(key=get_seq_number)


window_main.show()
sys.exit(app.exec())