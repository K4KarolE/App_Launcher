import sys

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QScrollArea,
    QMainWindow
    )

from buttons_settings import MyButtonSettings
from window_settings_text_field import MyTextLine
from window_settings_button import MyBaseButtonSettings
from data import cv, db




''' APP '''
app = QApplication(sys.argv)


'''
WINDOW MAIN <-- QSCROLLAREA WINDOW <-- QWIDGET WINDOW <-- QWIDGETS
'''

# MAIN WINDOW
cv.window_settings_main = QWidget()
cv.window_settings_main.resize(cv.window_settings_width, cv.window_settings_height)
cv.window_settings_main.setWindowTitle("Settings")
cv.window_settings_main.setStyleSheet(f"background-color: {cv.BG_COLOR_WIN_SETT};")
cv.window_settings_main.setWindowIcon(QIcon('docs/icons/settings_main_img.png'))


# QSCROLL AREA WINDOW
BASE_X = 20
button_window_scroll_area_width = cv.window_settings_width - BASE_X*2
button_window_scroll_area = QScrollArea(cv.window_settings_main)
button_window_scroll_area.setGeometry(
                                    20,
                                    30,
                                    button_window_scroll_area_width,
                                    cv.button_window_scroll_area_height
                                    )
button_window_scroll_area.setStyleSheet(f"background-color: {cv.BG_COLOR_WIN_SETT};")

# QWIDGET WINDOW
cv.button_window = QMainWindow()
cv.button_window.setStyleSheet(f"background-color: {cv.BG_COLOR_WIN_SETT};")
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



button_add = MyBaseButtonSettings("Add", BASE_X, 150, add_new_button)

button_remove = MyBaseButtonSettings("Remove", BASE_X + 120, 150, remove_button)


text_line_title = MyTextLine("title", BASE_X, 200)
















''' Sort before apply/save '''
def get_seq_number(e):
        return e.seq_number

def sort_button_list():
    cv.button_window_button_list.sort(key=get_seq_number)


cv.window_settings_main.show()
sys.exit(app.exec())