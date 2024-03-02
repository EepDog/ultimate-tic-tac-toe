import pygame
import sys



class BasicBoard:
    def __init__(self, screen):
        self.color = "Black"
        self.active = True
        self.screen = screen
        self.board_size = screen.get_size()  # 900-Width 800-Height
        self.font = pygame.font.Font(None, 50)
        self.player_1_text_color = (0, 0, 0)
        self.player_2_text_color = (0, 0, 0)
        self.board_color = (255, 255, 255)

    def draw_basic_board(self):
        width_amount = 10  # This sets how thick the board lines are
        margin = self.board_size[1] / 12  #
        playable_board_x = self.board_size[0] - margin * 2
        playable_board_y = self.board_size[1] - margin * 2

        # Board Setup
        for i in range(1, 3):  # Horizontal lines
            print(self.board_size)

            pygame.draw.line(self.screen, self.board_color,  # Horizontal line creator
                             start_pos=(margin, i * (playable_board_y / 3) + margin),
                             end_pos=(self.board_size[0] - margin, i * (playable_board_y / 3) + margin),
                             width=width_amount)
            pygame.draw.line(self.screen, self.board_color,  # Vertical creator
                             start_pos=(i * (playable_board_x / 3) + margin, margin),
                             end_pos=(i * (playable_board_x / 3) + margin, self.board_size[1] - margin),
                             width=width_amount)

        # Text Setup
        player1_text = self.font.render("Player 1", True, self.player_1_text_color)
        player2_text = self.font.render("Player 2", True, self.player_2_text_color)

        player1_rect = player1_text.get_rect(center=(0 + 80, 25))
        player2_rect = player2_text.get_rect(center=(self.screen.get_size()[0] - 80, 25))

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
