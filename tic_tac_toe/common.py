from datetime import date


# date support
def get_date(data_format):
    return date.today().strftime(data_format)


def get_today():
    data_format = "%m-%d-%Y"
    return get_date(data_format)


def get_current_time():
    data_format = "%H:%M:%S"
    return get_date(data_format)


# game settings
PLAYER_X = 'X'
PLAYER_O = '0'
PLAYERS = (PLAYER_X, PLAYER_O)

# recording settings
FREQUENCY = 16000
DURATION = 5
CHANNELS = 1
PATH_LIVE_RECORD = "recordings/live/" + get_today() + "/"
RECORDING_FORMAT = ".wav"


class OccupiedExceptions(Exception):
    pass
