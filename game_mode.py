class GameMode:
    MENU = 0
    REGULAR_TTT = 1
    ULTIMATE_TTT = 2
    OPTIONS = 3

    current_mode = MENU

    @classmethod
    def change_mode(cls, mode):

        cls.current_mode = mode

    @classmethod
    def get_mode(cls):
        return cls.current_mode
