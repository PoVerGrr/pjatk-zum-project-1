import torch
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
from wavio import read
from pyctcdecode import build_ctcdecoder
import warnings
warnings.filterwarnings("ignore")

processor = Wav2Vec2Processor.from_pretrained('facebook/wav2vec2-base-10k-voxpopuli-ft-pl') #TODO przerzucić do common
model = Wav2Vec2ForCTC.from_pretrained('facebook/wav2vec2-base-10k-voxpopuli-ft-pl')  # .to('cuda')
tokens = [x[0] for x in sorted(processor.tokenizer.get_vocab().items(), key=lambda x: x[1])]
decoder = build_ctcdecoder(tokens, 'model_jezyka.arpa', alpha=2.0, beta=-1.0)
def speech_recognition(path):
    data = read(path)
    data_after_squeezing = data.data.squeeze().astype('float32')
    fs = data.rate
   # feats = processor(data_after_squeezing, sampling_rate=fs, return_tensors='pt', padding=True)  # .to('cuda')
   # out = model(input_values=feats.input_values)
   # predicted_ids = torch.argmax(out.logits, dim=-1)
  #  sent = processor.batch_decode(predicted_ids)[0]




    feats = processor(data_after_squeezing, sampling_rate=fs, return_tensors='pt', padding=True)  # .to('cuda')
    out = model(input_values=feats.input_values)
    sent1 = decoder.decode(out.logits.cpu().detach().numpy()[0])
    print('You said: ', sent1)


    return sent1

