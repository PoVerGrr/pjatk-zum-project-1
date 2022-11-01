import re

from .common import OccupiedExceptions, PLAYERS, get_word_from_transcription
import voice_to_file as voice


def get_coordinates(current_game):
    try:
        voice_file_path = voice.get_voice_file()
        transcription = "trzytrzy" #TODO: get from ML
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


def get_values_from_voice(transcription, game):
    x, y = valid_transcription(transcription)
    position = y + (3 * x)
    if game.state[position] in PLAYERS:
        raise OccupiedExceptions
    return position


def valid_transcription(transcription):
    pattern = 'jeden|dwa|trzy'
    match = re.findall(pattern, transcription)
    if len(match) >= 2:
        x = int(get_word_from_transcription(match[0])) - 1
        y = int(get_word_from_transcription(match[1])) - 1
    else:
        raise ValueError
    if (2 < x or x < 0) or (y > 2 or y < 0):
        raise IndexError
    return x, y
