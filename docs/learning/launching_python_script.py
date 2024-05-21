''' Launching a Python file from a Python script '''

import os
from pathlib import Path

file_path = Path('D:\_DEV\Python\Video_Downloader\main.py')
python_keyword = 'py'

os.system(f'{python_keyword} {file_path}')