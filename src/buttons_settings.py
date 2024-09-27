import sys

from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QPushButton

from data import cv


button_img_size = cv.button_size - 5
window_widgets_width = 500
right_side_max_x_pos = cv.window_widgets_width - cv.button_size_sett_win - cv.button_pos_gap_sett_win
pos_y = 20


class MyButtonSettings(QPushButton):
    def __init__(self, pos_x, is_button):
        super().__init__(parent=cv.window_widgets)
        self.setIconSize(QSize(button_img_size, button_img_size))
        self.setFlat(True)
        self.setStyleSheet(f"background-color: white;")
        self.setGeometry(pos_x, pos_y, cv.button_size_sett_win, cv.button_size_sett_win)
        self.clicked.connect(lambda: self.button_clicked())
        if is_button:
            self.setIcon(QIcon("docs/icons/window_icon.png"))

    
    def mousePressEvent(self, event):   
        self.mouse_press_pos = None
        self.mouse_move_pos = None
        if event.button() == Qt.MouseButton.LeftButton:
            self.mouse_press_pos = event.globalPosition().toPoint()
            self.mouse_move_pos = event.globalPosition().toPoint()
        return super().mousePressEvent(event)
     

    def mouseMoveEvent(self, event):
        current_pos = self.mapToGlobal(self.pos())
        global_pos = event.globalPosition().toPoint()
        pos_diff = global_pos - self.mouse_move_pos
        pos_diff.setY(0)    # only vertical, no horizontal movement
        new_pos = self.mapFromGlobal(current_pos + pos_diff)

        # Keep the button in the frame
        if new_pos.x() < cv.button_pos_gap_sett_win:
            new_pos.setX(cv.button_pos_gap_sett_win)
        if new_pos.x() > right_side_max_x_pos:
            new_pos.setX(right_side_max_x_pos)

        self.move(new_pos)
        self.mouse_move_pos = global_pos    
        return super().mouseMoveEvent(event)


    def mouseReleaseEvent(self, event):
        '''
            Used to control how much movement needed
            for triggering the button`s clicked signal
        '''
        if self.mouse_move_pos != None:
            moved = event.globalPosition().toPoint() - self.mouse_press_pos
            if moved.manhattanLength() > 3:
                event.ignore()
                return
        return super(MyButtonSettings, self).mouseReleaseEvent(event)


    def button_clicked(self):
        print('Button clicked')
