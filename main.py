import sys

from PyQt6.QtWidgets import (
    QApplication
    )

from src import (
    MyImage,
    MyButton,
    MyWindow,
    cv,
    db
    )



app = QApplication(sys.argv)
cv.window = MyWindow()


img = MyImage()



def button_move_to_pos():
    BUTTON_POS_BASE_X = 30
    BUTTON_POS_BASE_Y = 30
    buttons_counter = 0
    button_pos_y = BUTTON_POS_BASE_Y

    for button_number in cv.buttons_dic:
        button_pos_x = BUTTON_POS_BASE_X + buttons_counter * (cv.button_size + cv.button_pos_gap)
        # PLACE BUTTON TO A NEW ROW IF NECESSARY
        if button_pos_x >= cv.window_main_width - cv.button_size - BUTTON_POS_BASE_X:
            buttons_counter = 0
            button_pos_x = BUTTON_POS_BASE_X + buttons_counter * (cv.button_size + cv.button_pos_gap)
            button_pos_y += cv.button_size + cv.button_pos_gap
        cv.buttons_dic[button_number].move(button_pos_x, button_pos_y)
        buttons_counter += 1
cv.button_move_to_pos = button_move_to_pos


# BUTTON CREATION & PLACEMENT
for button_number in db['buttons']:
    cv.buttons_dic[button_number] = MyButton(button_number)
    if db['buttons'][button_number]['title']:
        button_move_to_pos()
    else:
        cv.buttons_dic[button_number].hide()



cv.window.show()
sys.exit(app.exec())