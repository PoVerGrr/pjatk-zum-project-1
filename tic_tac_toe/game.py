import common
from game_controller import get_coordinates


class Game:
    def __init__(self, initial_state="         "):
        self.state = initial_state.replace('_', " ")
        self.empty_nb = self.state.count(' ')
        self.x_nb = self.state.count(common.PLAYER_X)
        self.o_nb = self.state.count(common.PLAYER_O)
        self.rows = [initial_state[0:3], initial_state[3:6], initial_state[6:9]]
        self.columns = [initial_state[0:7:3], initial_state[1:8:3], initial_state[2:9:3]]
        self.left_diagonal, self.right_diagonal = initial_state[0:9:4], initial_state[2:7:2]
        self.winning_combinations = self.rows + self.columns + [self.right_diagonal, self.left_diagonal]

    def change_state(self, character_number, value):
        self.state = self.state[:character_number] + value + self.state[character_number + 1:]
        self.__init__(self.state)
        print(self)

    def __str__(self):
        matrix_to_display = '---------\n' + \
                            '| ' + " ".join(self.state[0:3]) + ' |\n' + \
                            '| ' + " ".join(self.state[3:6]) + ' |\n' + \
                            '| ' + " ".join(self.state[6:9]) + ' |\n' + \
                            '---------'
        return matrix_to_display

    def is_identical_in_row(self, character, nb_in_row=3):
        return character * nb_in_row in self.winning_combinations

    def check_game_state(self):
        x_in_row = self.is_identical_in_row(common.PLAYER_X)
        o_in_row = self.is_identical_in_row(common.PLAYER_O)
        game_state = True

        if x_in_row and o_in_row:
            print('Impossible')
        elif abs(self.x_nb - self.o_nb) > 1:
            print('Impossible')
        elif x_in_row:
            print(common.PLAYER_X, 'wins')
            game_state = False
        elif o_in_row:
            print(common.PLAYER_O, 'wins')
            game_state = False
        elif (not x_in_row) and (not o_in_row):
            if self.empty_nb != 0:
                pass
            else:
                print('Draw')
                game_state = False
        return game_state

    def start_game(self):
        print("Game has been started! Good Luck!")
        print(self)
        i = 0
        while self.check_game_state():
            player = common.PLAYERS[i % 2]
            position = get_coordinates(self)
            self.change_state(position, player)
            i += 1
        print("End of the game.")
