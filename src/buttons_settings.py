'''
    LEARNED:
    - At startup widgets will be added to the parent window
    - Once the app running, the new widget has to be added to
      the window`s layout, otherwise it will not be visible
    "
     new_button = MyButtonSettings(seq_number_new)
     layout = cv.button_window.layout()
     layout.addChildWidget(new_button)
    "
'''

from pathlib import Path

from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QPushButton

from data import cv

button_img_size = cv.button_size - 5


class MyButtonSettings(QPushButton):

    def __init__(
            self,
            seq_number = 0,
            title = None,
            app_path = None,
            app_launcher = None,
            icon_path = None):
        super().__init__(parent=cv.button_window)
        self.seq_number = seq_number
        self.title = title
        self.app_path = app_path
        self.app_launcher = app_launcher
        self.icon_path = icon_path
        self.new_pos = None
        self.new_seq_number = self.seq_number
        self.setParent(cv.button_window)
        self.setIconSize(QSize(button_img_size, button_img_size))
        self.setGeometry(
            self.get_pos_x(),
            cv.button_window_button_pos_y,
            cv.button_size_sett_win,
            cv.button_size_sett_win
            )
        self.clicked.connect(lambda: self.button_clicked())
        # self.setText(str(self.seq_number))
        if self.icon_path:
            if Path(self.icon_path).exists():
                self.setIcon(QIcon(self.icon_path))
            else:
                self.setIcon(QIcon("docs/icons/default_icon.png"))
        cv.button_window_button_list.append(self)
        # Flat >> BG is visible once the button is clicked
        self.setFlat(True)
        self.setStyleSheet("background-color: white;")
        


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
        right_side_max_x_pos = cv.button_window_width - cv.button_size_and_gap_sett_win
        if self.new_pos.x() < cv.button_pos_gap_sett_win:
            self.new_pos.setX(cv.button_pos_gap_sett_win)
        if self.new_pos.x() > right_side_max_x_pos:
            self.new_pos.setX(right_side_max_x_pos)
        self.move(self.new_pos)
        self.mouse_move_pos = global_pos    
        return super().mouseMoveEvent(event)


    def mouseReleaseEvent(self, event):
        if self.mouse_press_pos != self.mouse_move_pos: # movement, not just click
            self.move_unselected_buttons()
            self.move_selected_button()
        cv.selected_button_index =  self.seq_number
        self.set_style_selected_button()
        return super(MyButtonSettings, self).mouseReleaseEvent(event)


    def get_pos_x(self):
        return cv.button_pos_gap + cv.button_size_and_gap_sett_win * self.seq_number

    
    def get_seq_number_from_new_pos(self):
        return round((self.new_pos.x() - cv.button_pos_gap) / cv.button_size_and_gap_sett_win)


    def move_unselected_buttons(self):
        if self.new_pos:
            self.new_seq_number = self.get_seq_number_from_new_pos()
            
            if self.new_seq_number < self.seq_number:
                for button in cv.button_window_button_list:
                    if self.new_seq_number <= button.seq_number < self.seq_number:
                        button.seq_number += 1
                        button.move(button.get_pos_x(), cv.button_window_button_pos_y)
            
            if self.new_seq_number > self.seq_number:
                for button in cv.button_window_button_list:
                    if self.new_seq_number >= button.seq_number > self.seq_number:
                        button.seq_number -= 1
                        button.move(button.get_pos_x(), cv.button_window_button_pos_y)


    def move_selected_button(self):
        ''' 
            Called after the rest of the buttons
            already moved and the self.new_seq_number
            is generated
        '''
        if self.new_pos:
            self.seq_number = self.new_seq_number
            self.move(self.get_pos_x(), cv.button_window_button_pos_y)
            self.new_pos = None
            self.sort_button_list()
    

    def set_style_selected_button(self):
        for button in cv.button_window_button_list:
            button.setFlat(True)
        self.setFlat(False)    


    def get_seq_number(self, e):
        return e.seq_number

    def sort_button_list(self):
        cv.button_window_button_list.sort(key=self.get_seq_number)


    
    def button_clicked(self):
        # self.setText(str(self.seq_number))
        print(self.title)