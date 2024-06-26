import pygame
import pygame_menu
import sys
from basic_board import BasicBoard
from game_mode import GameMode


class MainMenu:
    def __init__(self, screen):
        self.active = True
        self.screen = screen
        self.mode = 0

        self.color_themes = [()]
        self.menu_theme = pygame_menu.Theme(background_color=(144, 55, 73),
                                            # 71, 79, 122
                                            title_background_color=(43, 46, 74),
                                            title_font_shadow=True,
                                            title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_ADAPTIVE,
                                            title_font_color=(255, 255, 255),  # Title Text Color

                                            widget_padding=25,
                                            widget_font_color=(0, 0, 0),  # Button Text Color
                                            widget_font_size=35

                                            )

        self.main_menu = pygame_menu.Menu('Ultimate Tic Tac Toe', 900, 800, theme=pygame_menu.themes.THEME_ORANGE)

        # Button Setup
        self.ultimate_ttt_start = self.main_menu.add.button('Ultimate Tic Tac Toe', self.start_ultimate)
        self.normal_ttt_start = self.main_menu.add.button('Normal Tic Tac Toe', self.normal_ttt_start)
        self.options_button = self.main_menu.add.button('Options', self.options_button_press)
        self.exit_button = self.main_menu.add.button('Exit', self.end_program)

    def start_ultimate(self):
        self.main_menu.disable()
        self.active = False
        GameMode.change_mode(2)

    def normal_ttt_start(self):
        self.main_menu.disable()
        self.active = False
        GameMode.change_mode(1)


    def options_button_press(self):
        print("Clicked on Options menu")
        GameMode.change_mode(3)

    @staticmethod
    def end_program():
        sys.exit()

    def display_menu(self):
        self.main_menu.enable()
        self.main_menu.mainloop(self.screen)
