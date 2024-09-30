
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

    # WINDOW MAIN
    window: object = None   
    window_main_height: int = db['window_main']['window_height']
    window_main_min_width: int = db['window_main']['window_min_width']
    window_main_width: int = db['window_main']['window_width']
    
    bg_color: str = db['window_main']['bg_color']
    bg_img_path: str = db['window_main']['bg_img_path']
    bg_img_size: str = db['window_main']['bg_img_size']
    
    button_bd_color: str = db['window_main']['button_bd_color']
    button_clicked_bd_color: str = db['window_main']['button_clicked_bd_color']
    button_move_to_pos: object = None
    button_pos_gap: int = db['window_main']['button_pos_gap']
    button_size: int = db['window_main']['button_size']
    buttons_dic = {}
     
    
    # WINDOW SETTINGS
    window_settings_height: int = db['window_settings']['window_height']
    window_settings_width: int = db['window_settings']['window_width']
    window_settings_active: bool = db['window_settings']['window_active']
    py_launcher_settings_window: str = db['window_settings']['py_launcher_window_settings']

    selected_button: int = 0
    button_window: object = None
    button_size_sett_win: int = db['window_settings']['button_size_sett_win']
    button_pos_gap_sett_win: int = db['window_settings']['button_pos_gap_sett_win']
    button_size_and_gap_sett_win: int = button_size_sett_win + button_pos_gap_sett_win
    button_window_width: int = button_pos_gap_sett_win + (button_size_and_gap_sett_win) * len(db['buttons'])
    button_window_button_list = []   # [ [button obj], [button obj], ..] / MyButtonSettings class

    button_window_scroll_area_height: int = 100
    button_window_height: int = button_window_scroll_area_height - 20
    button_window_button_pos_y = 20



cv = Data()