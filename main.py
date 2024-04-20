import pygame
import pygame_menu
import menu
from advanced_board import AdvancedBoard
from basic_board import BasicBoard
from menu import MainMenu
from game_mode import GameMode
import random

pygame.init()
screen = pygame.display.set_mode((900, 800))  # Width, Height
clock = pygame.time.Clock()



running = True
pygame.display.set_caption('Ultimate Tic-Tac-Toe')  # Sets the title of application
main_menu = MainMenu(screen)
regular_ttt = BasicBoard(screen)
ultimate_ttt = AdvancedBoard(screen)
mode = 0
# 0 = Menu, 1 = Regular TTT, 2 =  Ultimate, 3 = Options

while running:
    current_mode = GameMode.get_mode()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_focused() and current_mode == 1:
            regular_ttt.click_detection(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])



    # RENDER YOUR GAME HERE
    screen.fill((228, 100, 36))
    if current_mode == 0:
        main_menu.display_menu()
    elif current_mode == 1:
        regular_ttt.draw_basic_board()
    elif current_mode == 2:
        ultimate_ttt.draw_ultimate_board()
    elif current_mode == 3:
        print("Options Mode")
    else:
        print("Warning!")



    pygame.display.flip()
    clock.tick(60)

pygame.quit()

