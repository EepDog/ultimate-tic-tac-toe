import pygame
import sys


class BasicBoard:
    def __init__(self, screen):
        self.color = "Black"
        self.active = False
        self.screen = screen
        self.screen_size = screen.get_size()  # 900-Width 800-Height
        self.font = pygame.font.Font(None, 50)
        self.player_1_text_color = (0, 0, 0)
        self.player_2_text_color = (0, 0, 0)
        self.board_color = (255, 255, 255)

    def draw_basic_board(self):
        width_amount = 3
        current_y = 200
        current_x_horizontal = 250
        margin = 100  # Assuming a margin of 100 pixels on each side

        # Board Setup
        for index in range(3):  # Horizontal Lines
            pygame.draw.line(self.screen, self.board_color,
                             start_pos=(0 + 100, current_y),
                             end_pos=(self.screen_size[0] - 100, current_y),
                             width=width_amount)
            current_y += 200

        drawable_width = 700  # Subtract margins from both sides

        for i in range(1, 3):  # Draw two vertical lines
            current_x_vertical = margin + (drawable_width * i // 3)
            pygame.draw.line(self.screen, self.board_color,
                             start_pos=(current_x_vertical, 50),  # Starting Y a bit lower than the top
                             end_pos=(current_x_vertical, self.screen_size[1] - 50),
                             # Ending Y a bit higher than the bottom
                             width=width_amount)

        # Text Setup
        player1_text = self.font.render("Player 1", True, self.player_1_text_color)
        player2_text = self.font.render("Player 2", True, self.player_2_text_color)

        player1_rect = player1_text.get_rect(center=(0 + 80, 25))
        player2_rect = player2_text.get_rect(center=(self.screen_size[0] - 80, 25))

        self.screen.blit(player1_text, player1_rect)
        self.screen.blit(player2_text, player2_rect)

    def change_text_color(self, active_player):
        # The player's name will turn red to display that it's their turn
        if active_player == 1:
            self.player_1_text_color = (255, 0, 0)
            self.player_2_text_color = (0, 0, 0)
        elif active_player == 2:
            self.player_2_text_color = (255, 0, 0)
            self.player_1_text_color = (0, 0, 0)
