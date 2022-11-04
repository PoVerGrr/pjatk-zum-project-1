from datetime import datetime


# date support
def get_date():
    date_format = "%Y-%m-%d--%H-%M-%S"
    return datetime.now().strftime(date_format)

def get_word_from_transcription(word):
    if word == "jeden":
        return 1
    elif word == "dwa":
        return 2
    elif word == "trzy":
        return 3
    else:
        raise Exception("Application error")


# game settings
PLAYER_X = 'X'
PLAYER_O = '0'
PLAYERS = (PLAYER_X, PLAYER_O)


# recording settings
FREQUENCY = 16000
DURATION = 6
CHANNELS = 1
PATH_LIVE_RECORD = "recordings/live/rec-"
RECORDING_FORMAT = ".wav"


class OccupiedExceptions(Exception):
    pass
