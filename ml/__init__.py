from wavio import read
import tic_tac_toe.common as tic


def speech_recognition(path):
    data = read(path)
    data_after_squeezing = data.data.squeeze().astype('float32')
    fs = data.rate
    feats = tic.PROCESSOR(data_after_squeezing, sampling_rate=fs, return_tensors='pt', padding=True)  # .to('cuda')
    out = tic.MODEL(input_values=feats.input_values)
    sent1 = tic.DECODER.decode(out.logits.cpu().detach().numpy()[0])
    print('You said: ', sent1)
    return sent1

