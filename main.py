
import pygame
from pathlib import Path
from json import load
import os
import subprocess



def open_json(path_json):
    with open(path_json) as f:
        json_dic = load(f)
    return json_dic


# LOAD DB
WORKING_DIRECTORY = Path().resolve()
PATH_JSON_DB = Path(WORKING_DIRECTORY, 'database.json')
PATH_WINDOW_SETTINGS = Path(WORKING_DIRECTORY, 'window_settings.py')
DB = open_json(PATH_JSON_DB)

background_color = DB['background_color']
window_width = DB['window_width']
window_height = DB['window_height']
button_size_px = DB['button_size_px']
button_clicked_bd_color = DB['button_clicked_bd_color']




''' -- PYGAME -- '''
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE)
pygame.display.set_caption('App Launcher')
screen.fill(background_color)


''' WINDOW ICON '''
window_icon_path = Path(WORKING_DIRECTORY, 'docs/icons/window_icon.png')
window_icon = pygame.image.load(window_icon_path)
pygame.display.set_icon(window_icon)


buttons_dic = {}
for button_number in DB['buttons']:
    buttons_dic[button_number] = {}
    buttons_dic[button_number]['clicked'] = False


def generate_button(number, button_size_px, x_coord, y_coord):
    icon_path = Path(DB['buttons'][number]['icon_path'])
    buttons_dic[number]['image'] = pygame.image.load(icon_path).convert_alpha()
    buttons_dic[number]['image'] = pygame.transform.scale(buttons_dic[number]['image'], (button_size_px, button_size_px))
    buttons_dic[number]['rect'] = buttons_dic[number]['image'].get_rect()
    buttons_dic[number]['rect'].center = x_coord + int(button_size_px/2), y_coord + int(button_size_px/2)
    buttons_dic[number]['pos_x'] = x_coord
    buttons_dic[number]['pos_y'] = y_coord
    return buttons_dic[number]['image'], buttons_dic[number]['rect']


SETTINGS_IMG_PATH = Path(WORKING_DIRECTORY, 'docs/icons/settings.png')
def generate_settings_button(size_px, x_coord, y_coord):
    img = pygame.image.load(SETTINGS_IMG_PATH).convert_alpha()
    img = pygame.transform.scale(img, (size_px, size_px))
    img_rect = img.get_rect()
    img_rect.center = x_coord + int(size_px/2), y_coord + int(size_px/2)
    return img, img_rect
    


''' -- LOOP -- '''
run = True
settings_button_clicked = False
while run:
    screen.fill(background_color)
    current_window_width, current_window_height = pygame.display.get_surface().get_size()
    cursor_coord_x, cursor_coord_y = pygame.mouse.get_pos()
    # print(cursor_coord_x, cursor_coord_y) # to test


    ''' BUTTONS / ICONS '''
    buttons_counter = 0
    BUTTONS_POS_Y = 20
    BUTTONS_POS_X_BASE = 20
    BUTTONS_POS_X_GAP = 30
    BUTTONS_CLICKED_GAP = 0
    for button_number in DB['buttons']:
        buttons_pos_x = BUTTONS_POS_X_BASE + buttons_counter * (button_size_px + BUTTONS_POS_X_GAP)
        
        # DISPLAY THE ICON IN A NEW ROW IF NECESSARY
        if buttons_pos_x >= current_window_width - button_size_px:
            buttons_counter = 0
            buttons_pos_x = BUTTONS_POS_X_BASE + buttons_counter * (button_size_px + BUTTONS_POS_X_GAP)
            BUTTONS_POS_Y += button_size_px + BUTTONS_POS_X_GAP
        
        # CLICKED BUTTON ANIMATION
        if buttons_dic[button_number]['clicked']:
            BUTTONS_CLICKED_GAP = 3
            buttons_dic[button_number]['rect'].move_ip(BUTTONS_CLICKED_GAP, BUTTONS_CLICKED_GAP)
            pygame.draw.rect(screen, button_clicked_bd_color, buttons_dic[button_number]['rect'])
            
        # DISPLAY BUTTONS
        image = generate_button(button_number, button_size_px, buttons_pos_x, BUTTONS_POS_Y)[0]
        screen.blit(image, (buttons_pos_x + BUTTONS_CLICKED_GAP, BUTTONS_POS_Y + BUTTONS_CLICKED_GAP))
        buttons_counter += 1
        BUTTONS_CLICKED_GAP = 0


    ''' SETTINGS BUTTON '''
    GAP_FROM_RB_CORNER = 30
    sett_button_pos = (current_window_width - GAP_FROM_RB_CORNER, current_window_height - GAP_FROM_RB_CORNER)
    
    if settings_button_clicked:
        sett_button_clicked_gap = 3
        sett_button_pos = (current_window_width - GAP_FROM_RB_CORNER + sett_button_clicked_gap, current_window_height - GAP_FROM_RB_CORNER + sett_button_clicked_gap)
        pygame.draw.rect(screen, button_clicked_bd_color, settings_button_rect)
    
    settings_button, settings_button_rect = generate_settings_button(20, sett_button_pos[0], sett_button_pos[1])
    screen.blit(settings_button, sett_button_pos)

    

    ''' EVENT HANDLING '''
    for event in pygame.event.get():

            # MOUSEBUTTONDOWN
            if event.type == pygame.MOUSEBUTTONDOWN:
                # TO TEST RECT COMPARED TO THE IMAGE LOCATION 
                # pygame.draw.rect(screen, 'red', buttons_dic[number]['rect'])
                for number in buttons_dic:
                    if buttons_dic[number]['rect'].collidepoint(cursor_coord_x, cursor_coord_y):
                        buttons_dic[number]['clicked'] = True
                
                if settings_button_rect.collidepoint(cursor_coord_x, cursor_coord_y):
                    settings_button_clicked = True
                        
    
            # MOUSEBUTTONUP - APP LAUNCH 
            elif event.type == pygame.MOUSEBUTTONUP:
                for number in buttons_dic:
                    if buttons_dic[number]['clicked']:
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
                
                if settings_button_rect.collidepoint(cursor_coord_x, cursor_coord_y):
                    settings_button_clicked = False
                    subprocess.Popen(f'py "{PATH_WINDOW_SETTINGS}"')


            # QUIT
            elif event.type == pygame.QUIT: 
                run = False
    
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()