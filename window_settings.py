from pathlib import Path
from tkinter import *

from src import (
    cv,
    save_json,
    WORKING_DIRECTORY,
    DB
)


# WINDOW
window = Tk()
window.title('Settings')
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry(f'{cv.window_settings_width}x{cv.window_settings_height}+%d+%d' % (screen_width/2-275, screen_height/2-125))    #   position to the middle of the screen
window.resizable(0,0)   # locks the main window
window.configure(background=cv.background_color)
# ICON
path_icon = Path(WORKING_DIRECTORY, 'docs/icons/window_settings_icon.ico') 
window.iconbitmap(path_icon)





window.mainloop()

# AFTER CLOSING THE SETTINGS WINDOW
DB['window_settings_active'] = False
save_json()