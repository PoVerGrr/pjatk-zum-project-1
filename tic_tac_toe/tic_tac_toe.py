import common as s


# https://softwareengineering.stackexchange.com/questions/308972/python-file-naming-convention


class TicTakToe:

    def __init__(self, initial_state):
        self.state = initial_state.replace('_', " ")
        self.empty_nb = self.state.count(' ')
        self.x_nb = self.state.count(s.PLAYER_X)
        self.o_nb = self.state.count(s.PLAYER_O)
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
        x_in_row = self.is_identical_in_row(s.PLAYER_X)
        o_in_row = self.is_identical_in_row(s.PLAYER_O)
        game_state = True

        if x_in_row and o_in_row:
            print('Impossible')
        elif abs(self.x_nb - self.o_nb) > 1:
            print('Impossible')
        elif x_in_row:
            print(s.PLAYER_X, 'wins')
            game_state = False
        elif o_in_row:
            print(s.PLAYER_O, 'wins')
            game_state = False
        elif (not x_in_row) and (not o_in_row):
            if self.empty_nb != 0:
                # print('Game not finished')
                pass
            else:
                print('Draw')
                game_state = False
        return game_state

    # TODO: this method should only concetrate on puting x and y into right place
    def input_coordinates(self, player, x, y):
        # TODO: while and validation should be on higer lvl
        while True:
            try:
                # TODO: change it to x,y in param
                first, second = input('Enter the coordinates >>').split(' ')
                first = int(first) - 1
                second = int(second) - 1

                position = s.coordinates_to_position_in_state(x, y)
                if self.state[position] in s.PLAYERS:
                    raise s.OccupiedExceptions
                self.change_state(position, player)
                break

                # TODO: exctract valitaion to higher lvl
            except ValueError:
                print('You should enter two numbers from 1 to 3 separated by white space.')
                continue
            except s.OccupiedExceptions:
                print('This cell is occupied. Choose another one.')
                continue
            except IndexError:
                print('Coordinates should be from 1 to 3.')
                continue


# TODO: probably not here
def start_game():
    while True:
        game = TicTakToe("         ")
        print(game)
        characters = s.PLAYERS
        conuter = 0
        while game.check_game_state():
            game.input_coordinates(characters[conuter % 2])
            conuter += 1
        decision = input('Do you want to play again? (y/n) >> ')
        if decision == 'y':
            continue
        else:
            break
