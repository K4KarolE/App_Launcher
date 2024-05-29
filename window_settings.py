from pathlib import Path
from json import load, dump
from tkinter import *

def open_json(path_json):
    with open(path_json) as f:
        json_dic = load(f)
    return json_dic

def save_json(json_dic, path_json):
    with open(path_json, 'w') as f:
        dump(json_dic, f, indent=2)
    return



WORKING_DIRECTORY = Path().resolve()
PATH_JSON_DB = Path(WORKING_DIRECTORY, 'database.json')
PATH_WINDOW_SETTINGS = Path(WORKING_DIRECTORY, 'window_settings.py')
DB = open_json(PATH_JSON_DB)

background_color = DB['background_color']
window_width = DB['window_settings_width']
window_height = DB['window_settings_height']
button_clicked_bd_color = DB['button_clicked_bd_color']

# WINDOW
window = Tk()
window.title('Settings')
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry(f'{window_width}x{window_height}+%d+%d' % (screen_width/2-275, screen_height/2-125))    #   position to the middle of the screen
window.resizable(0,0)   # locks the main window
window.configure(background=background_color)
# ICON
path_icon = Path(WORKING_DIRECTORY, 'docs/icons/window_settings_icon.ico') 
window.iconbitmap(path_icon)

# CANVAS
# canvas_color = 'black'
# canvas_frame_color = 'grey'
# canvas = Canvas(window, width=window_width, height=window_length, background = 'grey')
# canvas.create_rectangle(5-1, 5+2, window_width-5, window_length-5, outline=canvas_frame_color, fill=canvas_color)
# canvas.pack()





window.mainloop()