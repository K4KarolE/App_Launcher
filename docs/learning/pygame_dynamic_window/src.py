from dataclasses import dataclass
from pathlib import Path
from json import load, dump

def open_json():
    with open(PATH_JSON_DB) as f:
        json_dic = load(f)
    return json_dic

def save_json():
    with open(PATH_JSON_DB, 'w') as f:
        dump(DB, f, indent=2)
    return


WORKING_DIRECTORY = Path().resolve()
PATH_JSON_DB = Path(WORKING_DIRECTORY, 'settings.json')
PATH_WINDOW_SETTINGS = Path(Path(__file__).parent, 'window_settings.py')
DB = open_json()

@dataclass
class Data:
    background_color = DB['bg_color']

    window_main_width = DB['window_main_width']
    window_main_height = DB['window_main_height']
    window_settings_width = DB['window_settings_width']
    window_settings_height = DB['window_settings_height']

    button_size_px = DB['button_size_px']
    button_clicked_bd_color = DB['button_clicked_bd_color']
    py_launcher_settings_window = DB['window_settings']['py_launcher_window_settings']

cv = Data()