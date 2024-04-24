import pygame
from basic_board import BasicBoard


class AdvancedBoard:
    def __init__(self, screen):
        self.color = 'Black'
        self.screen = screen
        self.board_size = screen.get_size()
        self.active = True


    def draw_ultimate_board(self):
        margin = self.board_size[1] / 12

    def board_reset(self):
        print("Board Reset")

