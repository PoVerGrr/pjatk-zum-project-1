import re

from .common import OccupiedExceptions, PLAYERS
import voice_to_file as voice


def get_coordinates(current_game):
    try:
        voice_file_path = voice.get_voice_file()
        transcription = "12"

        position = get_values_from_voice(transcription, current_game)

        return position

    except ValueError:
        print('You should enter two numbers from 1 to 3 separated by white space.')
        get_coordinates(current_game)
    except OccupiedExceptions:
        print('This cell is occupied. Choose another one.')
        get_coordinates(current_game)
    except IndexError:
        print('Coordinates should be from 1 to 3.')
        get_coordinates(current_game)
#TODO add default exception


def get_values_from_voice(transcription, game):
    x, y = valid_transcription(transcription)
    position = y + (3 * x)
    if game.state[position] in PLAYERS:
        raise OccupiedExceptions
    return position


def valid_transcription(transcription):
    #TODO: add pattern realated to 'jeden' 'dwa' trzy'
    pattern = r'\d'
    match = re.search(pattern, transcription)
    print(transcription)
    if match:
        x = int(match.group())
        y = int(match.group())
        print("X=",str(x),"y=",str(y))
    else:
        raise ValueError
    if (2 < x or x < 0) or (y > 2 or y < 0):
        raise IndexError
    return x, y
