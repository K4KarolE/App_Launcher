
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
    WINDOW_MAIN_MIN_WIDTH: int = db['window_main']['window_min_width']
    window_main_width: int = db['window_main']['window_width']
    
    bg_color: str = db['window_main']['bg_color']
    bg_img_path: str = db['window_main']['bg_img_path']
    bg_img_size: str = db['window_main']['bg_img_size']
    
    button_bd_color: str = db['window_main']['button_bd_color']
    button_clicked_bd_color: str = db['window_main']['button_clicked_bd_color']
    BUTTON_MOVE_TO_POS_FUNC: object = None
    button_pos_gap: int = db['window_main']['button_pos_gap']
    button_size: int = db['window_main']['button_size']
    buttons_dic = {}
     
    
    # WINDOW SETTINGS
    window_settings_main: object = None  
    WINDOW_SETTINGS_HEIGHT: int = db['window_settings']['window_height']
    WINDOW_SETTINGS_WIDTH: int = db['window_settings']['window_width']
    window_settings_active: bool = db['window_settings']['window_active']
    py_launcher_settings_window: str = db['window_settings']['py_launcher_window_settings']

    button_window: object = None
    BUTTON_SIZE_SETT_WIN: int = db['window_settings']['button_size_sett_win']
    BUTTON_POS_GAP_SETT_WIN: int = db['window_settings']['button_pos_gap_sett_win']
    BUTTON_SIZE_AND_GAP_SETT_WIN: int = BUTTON_SIZE_SETT_WIN + BUTTON_POS_GAP_SETT_WIN
    button_window_width: int = BUTTON_POS_GAP_SETT_WIN + (BUTTON_SIZE_AND_GAP_SETT_WIN) * len(db['buttons'])
    button_window_button_list = []   # [ [button obj], [button obj], ..] / MyButtonSettings class
    selected_button_index: int = 0

    BUTTON_WINDOW_SCROLL_AREA_HEIGHT: int = 100
    BUTTON_WINDOW_HEIGHT: int = BUTTON_WINDOW_SCROLL_AREA_HEIGHT - 20
    BUTTON_WINDOW_BUTTON_POS_Y = 20

    BG_COLOR_WIN_SETT: str = db['window_settings']['bg_color_win_sett']
    FIELD_BG_COLOR: str = db['window_settings']['field_bg_color']
    TEXT_FIELD_FONT_STYLE: str = db['window_settings']['text_field_font_style']
    TEXT_FIELD_FONT_SIZE: int = db['window_settings']['text_field_font_size']
    TEXT_FIELD_FONT_COLOR: str = db['window_settings']['text_field_font_color']
    TEXT_FIELDS_DIC = {
        'title': object,
        'app_path': object
    }



cv = Data()