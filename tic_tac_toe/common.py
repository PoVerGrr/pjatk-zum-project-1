from datetime import datetime
import torch
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
from pyctcdecode import build_ctcdecoder

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

#speech recognitions settings
PROCESSOR = Wav2Vec2Processor.from_pretrained('facebook/wav2vec2-base-10k-voxpopuli-ft-pl')
MODEL = Wav2Vec2ForCTC.from_pretrained('facebook/wav2vec2-base-10k-voxpopuli-ft-pl')  # .to('cuda')
tokens = [x[0] for x in sorted(PROCESSOR.tokenizer.get_vocab().items(), key=lambda x: x[1])]
DECODER = build_ctcdecoder(tokens, 'model_jezyka.arpa', alpha=2.0, beta=-1.0)


class OccupiedExceptions(Exception):
    pass
