import sounddevice as sd
import wavio as wv
from tic_tac_toe.common import DURATION, FREQUENCY, CHANNELS, RECORDING_FORMAT, PATH_LIVE_RECORD, get_date
import time


def get_voice_file():
    recording = sd.rec(int(DURATION * FREQUENCY), samplerate=FREQUENCY, channels=CHANNELS)
    print('RECORDING',end='')
    path = PATH_LIVE_RECORD + get_date() + RECORDING_FORMAT
    for i in range(55):
        time.sleep(0.1)
        print('.', end='')
#    sd.wait()
    wv.write(path, recording, FREQUENCY, sampwidth=2)
#    print("recording save path: " + path)
    print('end of recording')

    return path
