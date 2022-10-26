class MyExceptions(Exception):
    pass

class SimpleTicTakToe:

    def __init__(self, initial_state):
        self.state = initial_state.replace('_'," ")
        self.empty_nb = self.state.count(' ')
        self.x_nb = self.state.count('X')
        self.o_nb = self.state.count('O')
        self.rows = [initial_state[0:3], initial_state[3:6], initial_state[6:9]]
        self.columns = [initial_state[0:7:3], initial_state[1:8:3], initial_state[2:9:3]]
        self.left_diagonal, self.right_diagonal = initial_state[0:9:4], initial_state[2:7:2]
        self.winning_combinations = self.rows + self.columns + [self.right_diagonal, self.left_diagonal]

    def coordinates_to_position_in_state(self, x, y):
        if (2 < x or x < 0) or (y > 2 or y < 0):
            raise IndexError
        elif x == 0:
            return y
        elif x == 1:
            return y + 3
        elif x == 2:
            return y + 6

    def change_state(self, character_number, value):
        self.state = self.state[:character_number]+value+self.state[character_number+1:]
        self.__init__(self.state)
        print(self)

    def __str__(self):
        matrix_to_display = '---------\n' + \
                       '| ' + " ".join(self.state[0:3]) + ' |\n' +\
                       '| ' + " ".join(self.state[3:6]) + ' |\n' +\
                       '| ' + " ".join(self.state[6:9]) + ' |\n' +\
                       '---------'
        return matrix_to_display

    def check_if_identical_in_row(self, character, nb_in_row=3):
        if character*nb_in_row in self.winning_combinations:
            return True
        else:
            return False

    def check_game_state(self):
        x_in_row = self.check_if_identical_in_row('X')
        o_in_row = self.check_if_identical_in_row('O')
        game_state = True

        if x_in_row and o_in_row:
            print('Impossible')
        elif abs(self.x_nb - self.o_nb)> 1:
            print('Impossible')
        elif x_in_row:
            print('X wins')
            game_state = False
        elif o_in_row:
            print('O wins')
            game_state = False
        elif (not x_in_row) and (not o_in_row):
            if self.empty_nb != 0:
                #print('Game not finished')
                pass
            else:
                print('Draw')
                game_state = False
        return game_state

    def input_coordinates(self, player):
        while(True):
            try:
                first, second = input('Enter the coordinates >>').split(' ')
                first = int(first) - 1
                second = int(second) - 1
                position = self.coordinates_to_position_in_state(first, second)
                if self.state[position] in ['X', 'O']:
                    raise MyExceptions
                self.change_state(position, player)
                break
            except ValueError:
                print('You should enter two numbers from 1 to 3 separated by white space.')
                continue
            except MyExceptions:
                print('This cell is occupied. Choose another one.')
                continue
            except IndexError:
                print('Coordinates should be from 1 to 3.')
                continue





while(True):
    game = SimpleTicTakToe("         ")
    print(game)
    characters = ['X', 'O']
    conuter = 0
    while(game.check_game_state()):
        game.input_coordinates(characters[conuter % 2])
        conuter += 1
    decision = input('Do you want to play again? (y/n) >> ')
    if decision == 'y':
        continue
    else:
        break