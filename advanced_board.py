import pygame


class AdvancedBoard:
    def __init__(self, screen):
        self.color = 'Black'
        self.screen = screen
        self.board_size = screen.get_size()


    def draw_ultimate_board(self):
        margin = self.board_size[1] / 12
