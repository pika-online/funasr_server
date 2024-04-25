from funasr import AutoModel
import time 
wav_path = "/root/data/client.mp3"

model_path = "damo/speech_paraformer-large_asr_nat-zh-cn-16k-common-vocab8404-pytorch"
model = AutoModel(model=model_path,
                  disable_pbar=False,
                  disable_log=True)
s = time.perf_counter()
res = model.generate(input=wav_path)
print("cost",time.perf_counter()-s)
print(res[0]["text"])
del model

model_path = "damo/speech_paraformer-large-contextual_asr_nat-zh-cn-16k-common-vocab8404"
model = AutoModel(model=model_path,
                  disable_pbar=False,
                  disable_log=True)
s = time.perf_counter()
res = model.generate(input=wav_path)
print("cost",time.perf_counter()-s)
print(res[0]["text"])
del model

model_path = "damo/speech_seaco_paraformer_large_asr_nat-zh-cn-16k-common-vocab8404-pytorch"
model = AutoModel(model=model_path,
                  disable_pbar=False,
                  disable_log=True)
s = time.perf_counter()
res = model.generate(input=wav_path)
print("cost",time.perf_counter()-s)
print(res[0]["text"])
del model