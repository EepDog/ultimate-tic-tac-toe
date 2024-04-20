import pygame
import sys
import random
import game_mode


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
        self.player_turn = random.randint(1, 2)

        self.board_cells = [0, 1, 2,
                            3, 4, 5,
                            6, 7, 8]

        self.win_conditions = [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]
        self.winning_player = None
        self.mode = 1

    def board_reset(self):
        self.active = True
        self.board_cells = [0, 1, 2,
                            3, 4, 5,
                            6, 7, 8]
        self.winning_player = None

    def win_scan(self):
        print("Scanning for win...")
        for condition in self.win_conditions:
            if all(self.board_cells[tile] == "X" for tile in condition):
                self.winning_player = "X"
                return True, "X"  # X Player wins
            elif all(self.board_cells[tile] == "O" for tile in condition):
                self.winning_player = "O"
                return True, "O"  # O Player wins
        if all(cell in ["X", "O"] for cell in self.board_cells):
            return True, "Draw"
        return False, None  # No winner yet

    def draw_basic_board(self):
        width_amount = 10  # This sets how thick the board lines are
        margin = self.board_size[1] / 12  # Sets up empty space on sides of board
        playable_board_x = self.board_size[0] - margin * 2
        playable_board_y = self.board_size[1] - margin * 2

        tile_width = playable_board_x / 3
        tile_height = playable_board_y / 3

        # Board Setup
        for row in range(1, 3):
            pygame.draw.line(self.screen, self.board_color,  # Horizontal line creator
                             start_pos=(margin, row * (playable_board_y / 3) + margin),
                             end_pos=(self.board_size[0] - margin, row * (playable_board_y / 3) + margin),
                             width=width_amount)
            pygame.draw.line(self.screen, self.board_color,  # Vertical line creator
                             start_pos=(row * (playable_board_x / 3) + margin, margin),
                             end_pos=(row * (playable_board_x / 3) + margin, self.board_size[1] - margin),
                             width=width_amount)

        # Text Setup
        self.change_text_color()
        player1_text = self.font.render("Player 1", True, self.player_1_text_color)
        player2_text = self.font.render("Player 2", True, self.player_2_text_color)

        player1_rect = player1_text.get_rect(center=(0 + 80, 25))
        player2_rect = player2_text.get_rect(center=(self.screen.get_size()[0] - 80, 25))

        self.screen.blit(player1_text, player1_rect)
        self.screen.blit(player2_text, player2_rect)

        symbol_font = pygame.font.Font(None, int(tile_width / 1.25))

        for index, cell in enumerate(self.board_cells):
            row = index // 3
            column = index % 3

            if cell in ["O", "X"]:
                symbol_x = margin + column * tile_width + tile_width / 2
                symbol_y = margin + row * tile_height + tile_height / 2

                symbol_text = symbol_font.render(cell, True, self.board_color)
                symbol_rect = symbol_text.get_rect(center=(symbol_x, symbol_y))
                self.screen.blit(symbol_text, symbol_rect)

        if not self.active and self.mode == 1:
            center_x = self.board_size[0] // 2
            center_y = self.board_size[1] // 2

            winner_font = pygame.font.Font(None, int(playable_board_x * 0.15))
            if self.winning_player == "Draw":
                winner_text = winner_font.render(f'Draw!', True, [0, 0, 0])
            else:
                winner_text = winner_font.render(f'The winner is {self.winning_player}!', True, [0, 0, 0])

            w_text_rect = winner_text.get_rect()
            w_text_rect.center = (center_x, center_y)
            self.screen.blit(winner_text, w_text_rect)
            pygame.display.flip()

            pygame.time.wait(3000)
            game_mode.GameMode.change_mode(0)
            self.board_reset()

    def change_text_color(self):
        # The player's name will turn white to display that it's their turn
        if self.player_turn == 1:
            self.player_1_text_color = (255, 255, 255)
            self.player_2_text_color = (0, 0, 0)
        elif self.player_turn == 2:
            self.player_2_text_color = (255, 255, 255)
            self.player_1_text_color = (0, 0, 0)

    def click_detection(self, click_x, click_y):
        if self.active:
            margin = self.board_size[1] / 12

            playable_board_x = self.board_size[0] - margin * 2
            playable_board_y = self.board_size[1] - margin * 2

            tile_width = playable_board_x / 3
            tile_height = playable_board_y / 3

            row = int((click_y - margin) // tile_height)
            col = int((click_x - margin) // tile_width)

            if not row < 0 and not row >= 3 and not col < 0 and not col >= 3:
                print(f"\nColumn: {col}\n"
                      f"Row: {row}")
                self.board_check(col=col, row=row)
                result = self.win_scan()
                if result[0]:
                    self.active = False
                    winning_symbol = result[1]
                    if winning_symbol == "Draw":
                        self.winning_player = "Draw"
                    print(f"The winner is {winning_symbol}")
                    pygame.display.flip()

    def board_symbol_logic(self, col, row):
        if self.player_turn == 1:
            self.board_cells[row * 3 + col] = "X"  # The symbol for Player 1 is X
            self.player_turn = 2
        elif self.player_turn == 2:
            self.board_cells[row * 3 + col] = "O"  # The symbol for Player 2 is O
            self.player_turn = 1

    def board_check(self, col, row):
        selected_tile = self.board_cells[row * 3 + col]
        print(f"Board Check Selected Tile Value: {selected_tile}")
        if selected_tile != "O" and selected_tile != "X":
            print("This move was valid")
            self.board_symbol_logic(col=col, row=row)
        else:
            print(f"This slot is already taken with ${selected_tile}, try again")
