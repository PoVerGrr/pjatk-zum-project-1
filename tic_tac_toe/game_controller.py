import common
import tic_tac_toe
import voice_to_file as voice
import re


def get_coordinates(current_game):
    try:
        voice_file_path = voice.get_voice_file()
        transcription = ml.get_transcription(voice_file_path)  # TODO: ML
        position = get_values_from_voice(transcription, current_game)
        return position

    except ValueError:
        print('You should enter two numbers from 1 to 3 separated by white space.')
        get_coordinates(current_game)
    except common.OccupiedExceptions:
        print('This cell is occupied. Choose another one.')
        get_coordinates(current_game)
    except IndexError:
        print('Coordinates should be from 1 to 3.')
        get_coordinates(current_game)


def get_values_from_voice(transcription, game):
    x, y = valid_transcription(transcription)
    position = y + (3 * x)
    if game.state[position] in common.PLAYERS:
        raise common.OccupiedExceptions
    return position


def valid_transcription(transcription):
    pattern = r'\d'
    match = re.search(pattern, transcription)
    if match:
        x = int(match.group())
        y = int(match.group())
    else:
        raise ValueError
    if (2 < x or x < 0) or (y > 2 or y < 0):
        raise IndexError
    return x, y


def start_full_game():
    game = tic_tac_toe.Game()
    game.start_game()
    while input('Do you want to play again? (y/n) >> ') == 'y':
        game = tic_tac_toe.Game()
        game.start_game()

# https://softwareengineering.stackexchange.com/questions/308972/python-file-naming-convention
