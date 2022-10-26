PLAYER_X = 'X'
PLAYER_O = '0'
PLAYERS = (PLAYER_X, PLAYER_O)


def coordinates_to_position_in_state(x, y):
    if (2 < x or x < 0) or (y > 2 or y < 0):
        raise IndexError
    return y + (3 * x)
'''
elif x == 0:
    return y
elif x == 1:
    return y + 3
elif x == 2:
    return y + 6
'''

class OccupiedExceptions(Exception):
    pass
