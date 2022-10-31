import sounddevice as sd
import wavio as wv
from tic_tac_toe.common import DURATION, FREQUENCY, CHANNELS, RECORDING_FORMAT, PATH_LIVE_RECORD, get_date


def get_voice_file():
    print('recording...')
    recording = sd.rec(int(DURATION * FREQUENCY), samplerate=FREQUENCY, channels=CHANNELS)
    path = PATH_LIVE_RECORD + get_date() + RECORDING_FORMAT
    sd.wait()
    print(path)
    wv.write(path, recording, FREQUENCY, sampwidth=2)
    print('end of recording')

    return path
