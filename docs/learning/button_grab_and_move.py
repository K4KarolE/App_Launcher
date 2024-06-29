'''
Grab and move a button

Cheers jdi!:
https://stackoverflow.com/questions/12219727/dragging-moving-a-qpushbutton-in-pyqt
'''


import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QPushButton,
    QWidget
    )


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 300)
        self.setWindowTitle("Grab & move a button")


class MyButton(QPushButton):
    def __init__(self, text, parent):
        super().__init__(text=text, parent=parent)
        self.setGeometry(200, 135, 100, 30)
    

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
        new_pos = self.mapFromGlobal(current_pos + pos_diff)
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



app = QApplication(sys.argv)
window = MyWindow()

def button_clicked():
    print('Button clicked')

button = MyButton('Test Button', window)
button.clicked.connect(button_clicked)

window.show()
sys.exit(app.exec())