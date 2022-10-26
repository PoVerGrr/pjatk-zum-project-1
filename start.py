from pathlib import Path
from tqdm import tqdm
import torch
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
from pyctcdecode import build_ctcdecoder
from wavio import read
import jiwer
import arpa
processor=Wav2Vec2Processor.from_pretrained('facebook/wav2vec2-base-10k-voxpopuli-ft-pl')
model=Wav2Vec2ForCTC.from_pretrained('facebook/wav2vec2-base-10k-voxpopuli-ft-pl') #.to('cuda')


#nagrania -----------------------------------------------------------------------------------------------------
import soundfile as sf
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

# Sampling frequency
freq = 16000

# Recording duration
duration = 5

# Start recorder with the given values
# of duration and sample frequency
print('recording')
recording = sd.rec(int(duration * freq), samplerate=freq, channels=1)

# Record audio for the given number of seconds
sd.wait()

# This will convert the NumPy array to an audio
# file with the given sampling frequency
#write("nagrania/recording0.wav", freq, recording)

# Convert the NumPy array to audio file
wv.write("nagrania/recording1.wav", recording, freq, sampwidth=2)

print('end of recording')
ob = sf.SoundFile('recording1.wav')
print('Sample rate: {}'.format(ob.samplerate))
print('Channels: {}'.format(ob.channels))
print('Subtype: {}'.format(ob.subtype))

#-----------------------------------------------------------------------------------------------------------------------


files={}
for f in Path('nagrania').glob('*.wav'):
  data=read(str(f))
  files[f.stem]=data.data.squeeze().astype('float32')
  print('done')

Fs=data.rate
for name,d in files.items():
  print(f'{name}: {d.size/Fs:0.2f}s')


trans={}
for name,data in tqdm(files.items()):
  feats=processor(data,sampling_rate=Fs,return_tensors='pt',padding=True)  #.to('cuda')
  out=model(input_values=feats.input_values)
  predicted_ids=torch.argmax(out.logits,dim=-1)
  sent=processor.batch_decode(predicted_ids)[0]
  trans[name]=sent

print(trans)