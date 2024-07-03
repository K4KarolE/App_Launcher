
from dataclasses import dataclass
from pathlib import Path
from json import load, dump


def open_json(path_json):
    with open(path_json) as f:
        json_dic = load(f)
    return json_dic

def save_json(json_dic, path_json):
    with open(path_json, 'w') as f:
        dump(json_dic, f, indent=2)
    return

WORKING_DIRECTORY = Path().resolve()
PATH_JSON_SETTINGS = Path(WORKING_DIRECTORY, 'settings.json')
settings = open_json(PATH_JSON_SETTINGS)


@dataclass
class Data:

    bg_color = settings['bg_color']
    bg_img_path = settings['bg_img_path']
    bg_img_size = settings['bg_img_size']
    
    button_bd_color = settings['button_bd_color']
    button_clicked_bd_color = settings['button_clicked_bd_color']
    button_move_to_pos = None # obj
    button_pos_gap = settings['button_pos_gap']
    button_size_px = settings['button_size_px']
    buttons_dic = {}
    
    py_launcher_settings_window = settings['window_settings']['py_launcher_window_settings']
    
    window = None   # obj
    window_main_height = settings['window_main_height']
    window_main_min_width = settings['window_main_min_width']
    window_main_width = settings['window_main_width']
    window_settings_height = settings['window_settings_height']
    window_settings_width = settings['window_settings_width']


cv = Data()