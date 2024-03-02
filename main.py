import pygame
import pygame_menu
import menu
from advanced_board import AdvancedBoard
from basic_board import BasicBoard
from menu import MainMenu
from game_mode import GameMode

pygame.init()
screen = pygame.display.set_mode((900, 800))  # Width, Height
clock = pygame.time.Clock()



running = True
pygame.display.set_caption('Ultimate Tic-Tac-Toe')  # Sets the title of application
main_menu = MainMenu(screen)
regular_ttt = BasicBoard(screen)
mode = 0
# 0 = Menu, 1 = Regular TTT, 2 =  Ultimate, 3 = Options

while running:
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("Click Detect")

    # RENDER YOUR GAME HERE
    screen.fill((228, 100, 36))
    current_mode = GameMode.get_mode()
    if current_mode == 0:
        main_menu.display_menu()
    elif current_mode == 1:
        regular_ttt.draw_basic_board()
    else:
        print("Warning! This shouldn't be happening")



    pygame.display.flip()
    clock.tick(60)

pygame.quit()
