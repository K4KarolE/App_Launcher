'''
At the early stage I was thinking using a PyGame and a Tkinter
window to support the app launching window dynamic nature, 
resizing the window -> the buttons automatically repositioning 
to a new row, if necessary (PyGame),
and settings window`s user input / add-remove-reorder
buttons capability (Tkinter)

Working:
- Clicking on the buttons launching the relevant python, excel, exe,.. app
- From JSON:
    "app_launcher": "py" -> python app launching with terminal
    "app_launcher": "pyw" -> python app launching without terminal
- Resizing the main window -> the button automatically repositioning
to a new row if necessary 
- 1st settings button: while it is active, the buttons app
launching functions are disabled
- 2nd settings button: launching the settings window
closing the main window

Saving for later
'''


import pygame
from pathlib import Path
import os
import subprocess
import sys

from src import (
    cv,
    WORKING_DIRECTORY,
    PATH_WINDOW_SETTINGS,
    DB
)


''' -- PYGAME -- '''
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((cv.window_main_width, cv.window_main_height), pygame.RESIZABLE)
pygame.display.set_caption('App Launcher')
screen.fill(cv.background_color)


''' WINDOW ICON '''
window_icon_path = Path(WORKING_DIRECTORY, 'docs/icons/window_icon.png')
window_icon = pygame.image.load(window_icon_path)
pygame.display.set_icon(window_icon)


buttons_dic = {}
for button_number in DB['buttons']:
    buttons_dic[button_number] = {}
    buttons_dic[button_number]['clicked'] = False


def generate_button(number):
    icon_path = Path(DB['buttons'][number]['icon_path'])
    buttons_dic[number]['image'] = pygame.image.load(icon_path).convert_alpha()
    buttons_dic[number]['image'] = pygame.transform.scale(buttons_dic[number]['image'], (cv.button_size_px, cv.button_size_px))
    buttons_dic[number]['rect'] = buttons_dic[number]['image'].get_rect()
    buttons_dic[number]['rect'].center = buttons_pos_x + int(cv.button_size_px/2), buttons_pos_y + int(cv.button_size_px/2)
    buttons_dic[number]['pos_x'] = buttons_pos_x
    buttons_dic[number]['pos_y'] = buttons_pos_y
    buttons_dic[number]['not_empty'] = True
    return buttons_dic[number]['image'], buttons_dic[number]['rect']

def generate_empty_button(number):
    buttons_dic[number]['rect'] = pygame.draw.rect(screen, cv.background_color, (buttons_pos_x, buttons_pos_y, cv.button_size_px, cv.button_size_px))
    buttons_dic[number]['not_empty'] = False



SETTINGS_WINDOW_IMG_PATH = Path(WORKING_DIRECTORY, 'docs/icons/settings_window_img.png')
SETTINGS_MAIN_IMG_PATH = Path(WORKING_DIRECTORY, 'docs/icons/settings_main_img.png')

def generate_settings_button(opacity, size_px, x_coord, y_coord, image_path):
    img = pygame.image.load(image_path).convert_alpha()
    img = pygame.transform.scale(img, (size_px, size_px))
    img.set_alpha(opacity)
    img_rect = img.get_rect()
    img_rect.center = x_coord + int(size_px/2), y_coord + int(size_px/2)
    return img, img_rect
    


''' -- LOOP -- '''
run = True
settings_wind_button_clicked = False
settings_main_button_clicked = False
settings_main_button_clicked_counter = 1
sett_main_button_opacity = 50
settings_main_active = False
while run:
    screen.fill(cv.background_color)
    current_window_width, current_window_height = pygame.display.get_surface().get_size()
    cursor_coord_x, cursor_coord_y = pygame.mouse.get_pos()
    # print(cursor_coord_x, cursor_coord_y) # to test


    ''' BUTTONS / ICONS '''
    buttons_counter = 0
    buttons_pos_y = 20
    BUTTONS_POS_X_BASE = 20
    BUTTONS_POS_X_GAP = 10
    BUTTONS_CLICKED_GAP = 0
    for button_number in DB['buttons']:
        buttons_pos_x = BUTTONS_POS_X_BASE + buttons_counter * (cv.button_size_px + BUTTONS_POS_X_GAP)
        
        # DISPLAY THE ICON IN A NEW ROW IF NECESSARY
        if buttons_pos_x >= current_window_width - cv.button_size_px:
            buttons_counter = 0
            buttons_pos_x = BUTTONS_POS_X_BASE + buttons_counter * (cv.button_size_px + BUTTONS_POS_X_GAP)
            buttons_pos_y += cv.button_size_px + BUTTONS_POS_X_GAP
        
        # CLICKED BUTTON ANIMATION
        if (buttons_dic[button_number]['clicked'] and
            buttons_dic[button_number]['not_empty'] and
            not settings_main_active):
            
            BUTTONS_CLICKED_GAP = 3
            buttons_dic[button_number]['rect'].move_ip(BUTTONS_CLICKED_GAP, BUTTONS_CLICKED_GAP)
            pygame.draw.rect(screen, cv.button_clicked_bd_color, buttons_dic[button_number]['rect'])
            
        # DISPLAY BUTTONS
        if DB['buttons'][button_number]['app_path']:
            image = generate_button(button_number)[0]
            screen.blit(image, (buttons_pos_x + BUTTONS_CLICKED_GAP, buttons_pos_y + BUTTONS_CLICKED_GAP))
        else:
            generate_empty_button(button_number)
            
        buttons_counter += 1
        BUTTONS_CLICKED_GAP = 0


    ''' SETTINGS BUTTON '''
    GAP_FROM_RB_CORNER = 30
    SETTING_BUTTONS_GAP = 30
    sett_wind_button_pos = (current_window_width - GAP_FROM_RB_CORNER, current_window_height - GAP_FROM_RB_CORNER)
    sett_main_button_pos = (current_window_width - GAP_FROM_RB_CORNER - SETTING_BUTTONS_GAP, current_window_height - GAP_FROM_RB_CORNER)
    
    # SETTINGS WINDOW
    if settings_wind_button_clicked:
        sett_button_clicked_gap = 3
        sett_wind_button_pos = (sett_wind_button_pos[0] + sett_button_clicked_gap, sett_wind_button_pos[1] + sett_button_clicked_gap)
        pygame.draw.rect(screen, cv.button_clicked_bd_color, settings_wind_button_rect)
    
    settings_wind_button, settings_wind_button_rect = generate_settings_button(100, 20, sett_wind_button_pos[0], sett_wind_button_pos[1], SETTINGS_WINDOW_IMG_PATH)
    screen.blit(settings_wind_button, sett_wind_button_pos)

    # SETTINGS MAIN
    if settings_main_button_clicked:
        sett_button_clicked_gap = 3
        sett_main_button_pos = (sett_main_button_pos[0] + sett_button_clicked_gap, sett_main_button_pos[1] + sett_button_clicked_gap)
        pygame.draw.rect(screen, cv.button_clicked_bd_color, settings_main_button_rect)
   
    settings_main_button, settings_main_button_rect = generate_settings_button(sett_main_button_opacity, 20, sett_main_button_pos[0], sett_main_button_pos[1], SETTINGS_MAIN_IMG_PATH)
    screen.blit(settings_main_button, sett_main_button_pos)

    

    ''' EVENT HANDLING '''
    for event in pygame.event.get():

            # MOUSEBUTTONDOWN
            if event.type == pygame.MOUSEBUTTONDOWN:
                # TO TEST RECT COMPARED TO THE IMAGE LOCATION 
                # pygame.draw.rect(screen, 'red', buttons_dic[number]['rect'])
                for number in buttons_dic:
                    if buttons_dic[number]['rect'].collidepoint(cursor_coord_x, cursor_coord_y):
                        buttons_dic[number]['clicked'] = True
                
                # SETTINGS BUTTON CLICKED
                if settings_wind_button_rect.collidepoint(cursor_coord_x, cursor_coord_y):
                    settings_wind_button_clicked = True
                
                elif settings_main_button_rect.collidepoint(cursor_coord_x, cursor_coord_y):
                    settings_main_button_clicked = True
                        
    
            # MOUSEBUTTONUP - APP LAUNCH 
            elif event.type == pygame.MOUSEBUTTONUP:
                for number in buttons_dic:
                    if buttons_dic[number]['clicked'] and buttons_dic[number]['not_empty'] and not settings_main_active:

                        app_launcher = DB['buttons'][number]['app_launcher']
                        app_path = DB['buttons'][number]['app_path']
                        app_dir = os.path.dirname(app_path)
                        os.chdir(app_dir)
                        
                        if 'py' in app_launcher:
                            subprocess.Popen(f'{app_launcher} "{app_path}"')
                        else:
                            os.startfile(app_path)
                        
                        os.chdir(WORKING_DIRECTORY)
                    buttons_dic[number]['clicked'] = False
                
                # SETTINGS BUTTONS - UNCLICKED
                if settings_wind_button_rect.collidepoint(cursor_coord_x, cursor_coord_y):
                    settings_wind_button_clicked = False
                    subprocess.Popen(f'{cv.py_launcher_settings_window} "{PATH_WINDOW_SETTINGS}"')
                    sys.exit()
                
                elif settings_main_button_rect.collidepoint(cursor_coord_x, cursor_coord_y):
                    settings_main_button_clicked = False
                    
                    if settings_main_active:
                        settings_main_active = False
                        sett_main_button_opacity = 50
                    else:
                        settings_main_active = True
                        sett_main_button_opacity = 100

            # QUIT
            elif event.type == pygame.QUIT:
                run = False
    
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()