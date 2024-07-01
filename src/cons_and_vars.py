
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

    background_color = settings['background_color']

    window_main_always_on_top = settings['window_main_always_on_top']
    window_main_width = settings['window_main_width']
    window_main_height = settings['window_main_height']
    window_main_min_width = settings['window_main_min_width']

    window_settings_width = settings['window_settings_width']
    window_settings_height = settings['window_settings_height']

    buttons_dic = {}
    button_size_px = settings['button_size_px']
    button_pos_gap = settings['button_pos_gap']
    button_clicked_bd_color = settings['button_clicked_bd_color']
    py_launcher_settings_window = settings['window_settings']['py_launcher_window_settings']

cv = Data()