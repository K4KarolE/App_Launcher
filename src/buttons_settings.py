from pathlib import Path

from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QPushButton

from data import cv


button_img_size = cv.button_size - 5
window_widgets_width = 500
right_side_max_x_pos = cv.window_widgets_width - cv.button_size_sett_win - cv.button_pos_gap_sett_win
pos_y = 20


class MyButtonSettings(QPushButton):
    def __init__(self, seq_number, title, app_path, app_launcher, icon_path):
        super().__init__(parent=cv.window_widgets)
        self.seq_number = seq_number
        self.title = title
        self.app_path = app_path
        self.app_launcher = app_launcher
        self.icon_path = icon_path
        self.new_pos = None
        self.setIconSize(QSize(button_img_size, button_img_size))
        self.setFlat(True)
        self.setStyleSheet(f"background-color: white;")
        self.setGeometry(self.get_pos_x(), pos_y, cv.button_size_sett_win, cv.button_size_sett_win)
        self.clicked.connect(lambda: self.button_clicked())
        if self.icon_path:
            if Path(self.icon_path).exists():
                self.setIcon(QIcon(self.icon_path))
            else:
                self.setIcon(QIcon("docs/icons/default_icon.png"))
        cv.button_list_sett_win.append([self.seq_number, self])

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
        self.new_pos = self.mapFromGlobal(current_pos + pos_diff)

        # Keep the button in the frame
        if self.new_pos.x() < cv.button_pos_gap_sett_win:
            self.new_pos.setX(cv.button_pos_gap_sett_win)
        if self.new_pos.x() > right_side_max_x_pos:
            self.new_pos.setX(right_side_max_x_pos)

        self.move(self.new_pos)
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


    def get_pos_x(self):
        return cv.button_pos_gap + cv.button_size_and_gap_sett_win * self.seq_number


    def reposition(self):
        self.move(self.get_pos_x(), pos_y)

    
    def get_seq_number_from_new_pos(self):
        if self.new_pos:
            return round((self.new_pos.x() - cv.button_pos_gap) / cv.button_size_and_gap_sett_win)


    def button_clicked(self):
        print(self.title)
