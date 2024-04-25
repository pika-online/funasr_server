from funasr_onnx import Paraformer,ContextualParaformer,SeacoParaformer
from pathlib import Path
import time 

with open("hotwords.txt", 'r', encoding='utf-8') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines if len(line.strip())<=10]
hotwords = ' '.join(lines)
# hotword = ""
print(hotwords)


# model_dir = "damo/speech_paraformer-large_asr_nat-zh-cn-16k-common-vocab8404-pytorch"
# model = Paraformer(model_dir, batch_size=1, quantize=True)
# wav_path = "/root/data/client.mp3"
# s = time.perf_counter()
# result = model(wav_path)
# print("cost",time.perf_counter()-s)
# print(result)
# del model 

model_dir = "damo/speech_paraformer-large-contextual_asr_nat-zh-cn-16k-common-vocab8404"
model = ContextualParaformer(model_dir, batch_size=1,quantize=True)
wav_path = "/root/data/client.mp3"
s = time.perf_counter()
result = model(wav_path, hotwords)
print("cost",time.perf_counter()-s)
print(result)
del model 

model_dir = "damo/speech_seaco_paraformer_large_asr_nat-zh-cn-16k-common-vocab8404-pytorch"
model = SeacoParaformer(model_dir, batch_size=1,quantize=True)
wav_path = "/root/data/client.mp3"
s = time.perf_counter()
result = model(wav_path, hotwords)
print("cost",time.perf_counter()-s)
print(result)
del model 


