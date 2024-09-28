
from dataclasses import dataclass
from pathlib import Path
from json import load, dump


def get_path_json():
    path_json = Path(WORKING_DIRECTORY, 'database.json')
    return path_json

def open_db():
    f = open(PATH_JSON)
    json_dictionary = load(f)
    return json_dictionary

def save_db():
    with open(PATH_JSON, 'w') as f:
        dump(db, f, indent=2)


WORKING_DIRECTORY = Path().resolve()
PATH_JSON = get_path_json()
db = open_db()


@dataclass
class Data:

    bg_color: str = db['bg_color']
    bg_img_path: str = db['bg_img_path']
    bg_img_size: str = db['bg_img_size']
    
    button_bd_color: str = db['button_bd_color']
    button_clicked_bd_color: str = db['button_clicked_bd_color']
    button_move_to_pos: object = None
    button_pos_gap: int = db['button_pos_gap']
    button_size: int = db['button_size']
    buttons_dic = {}
    
    py_launcher_settings_window: str = db['window_settings']['py_launcher_window_settings']
    
    window: object = None   
    window_main_height: int = db['window_main_height']
    window_main_min_width: int = db['window_main_min_width']
    window_main_width: int = db['window_main_width']
    window_settings_height: int = db['window_settings_height']
    window_settings_width: int = db['window_settings_width']

    window_widgets: object = None
    window_widgets_width: int = (button_size + button_pos_gap) * len(db['buttons']) + button_pos_gap

    # WINDOW SETTINGS
    button_size_sett_win: int = db['window_settings']['button_size_sett_win']
    button_pos_gap_sett_win: int = db['window_settings']['button_pos_gap_sett_win']
    button_size_and_gap_sett_win: int = button_size_sett_win + button_pos_gap_sett_win
    button_list_sett_win = []   # [ [1, button obj], [2, button obj], ..] / MyButtonSettings class


cv = Data()