from .game import Game


def start_full_game():
    Game().start_game()
    while input('Do you want to play again? (y/n) >> ') == 'y':
        Game().start_game()

