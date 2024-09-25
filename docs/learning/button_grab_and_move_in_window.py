import sys

from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import (
    QApplication,
    QPushButton,
    QWidget,
    QScrollArea,
    QMainWindow
    )

button_size = 40
button_img_size = button_size - 5
window_widgets_width = 500
distance_from_side = 20
right_side_max_x_pos = window_widgets_width - button_size - distance_from_side


class MyButton(QPushButton):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.setIcon(QIcon("docs/icons/window_icon.png"))
        self.setIconSize(QSize(button_img_size, button_img_size))
        self.setFlat(True)

    
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
        if new_pos.x() < distance_from_side:
            new_pos.setX(distance_from_side)
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
        return super(MyButton, self).mouseReleaseEvent(event)



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
window_widgets = QMainWindow()
window_widgets.setStyleSheet(f"background-color: grey;")
window_widgets.setGeometry(0, 0, window_widgets_width, 80)
window_scroll_area.setWidget(window_widgets)


# WIDGET
def button_clicked():
    print('Button clicked')

button = MyButton(window_widgets)
button.setStyleSheet(f"background-color: white;")
button.setGeometry(20, 20, button_size, button_size)
button.clicked.connect(button_clicked)


window_main.show()
sys.exit(app.exec())