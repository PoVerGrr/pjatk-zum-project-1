import sounddevice as sd
import wavio as wv

from tic_tac_toe import common as c


def get_voice_file():
    print('recording...')
    recording = sd.rec(int(c.DURATION * c.FREQUENCY), samplerate=c.FREQUENCY, CHANNELS=c.CHANNELS)
    path = c.PATH_LIVE_RECORD + "recording" + c.RECORDING_FORMAT
    sd.wait()
    wv.write(path, recording, c.FREQUENCY, sampwidth=2)
    print('end of recording')

    return path
