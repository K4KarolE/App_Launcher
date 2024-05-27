
import pygame
from pathlib import Path
from json import load, dump
import sys
import os



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
DB = open_json(PATH_JSON_DB)


# LOAD DB
background_color = DB['background_color']
window_width = DB['window_width']
window_height = DB['window_height']
icons_size_px = DB['icons_size_px']




''' -- PYGAME -- '''
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE)
pygame.display.set_caption('Py App Launcher')


buttons_dic = {}
def generate_button(number, icons_size_px, x_coord, y_coord):
    icon_path = Path(DB['buttons'][number]['icon_path'])
    buttons_dic[number] = {}
    buttons_dic[number]['image'] = pygame.image.load(icon_path).convert_alpha()
    buttons_dic[number]['image'] = pygame.transform.scale(buttons_dic[number]['image'], (icons_size_px, icons_size_px))
    buttons_dic[number]['rect'] = buttons_dic[number]['image'].get_rect()
    buttons_dic[number]['rect'].center = x_coord + int(icons_size_px/2), y_coord + int(icons_size_px/2)
    return buttons_dic[number]['image'], buttons_dic[number]['rect']
    


buttons_counter = 0
BUTTONS_POS_Y = 20
BUTTONS_POS_X_BASE = 20
BUTTONS_POS_X_GAP = 30
for button_number in DB['buttons']:
    buttons_pos_x = BUTTONS_POS_X_BASE + buttons_counter * (icons_size_px + BUTTONS_POS_X_GAP)
    image, image_rect = generate_button(button_number, icons_size_px, buttons_pos_x, BUTTONS_POS_Y)
    screen.blit(image, (buttons_pos_x, BUTTONS_POS_Y))
    buttons_counter += 1



''' -- LOOP -- '''
run = True
while run:
    cursor_coord_x, cursor_coord_y = pygame.mouse.get_pos()
    # print(cursor_coord_x, cursor_coord_y)
    
    for event in pygame.event.get():

            # MOUSEBUTTONDOWN
            if event.type == pygame.MOUSEBUTTONDOWN:

                # Click on the icons
                for number in buttons_dic:
                    # TO TEST RECT COMPARED TO THE IMAGE LOCATION 
                    # pygame.draw.rect(screen, 'red', buttons_dic[number]['rect'])
                    
                    if buttons_dic[number]['rect'].collidepoint(cursor_coord_x, cursor_coord_y):
                        print(cursor_coord_x, cursor_coord_y)

    
            # QUIT
            elif event.type == pygame.QUIT: 
                run = False
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()