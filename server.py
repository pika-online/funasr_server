from flask import Flask, request, Response,make_response,send_file
from funasr import AutoModel
from funasr_onnx import Paraformer,ContextualParaformer,SeacoParaformer
from read_audio import ffmpeg_read
import time 
import numpy as np
# 加载热词
with open("hotwords.txt", 'r', encoding='utf-8') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines if len(line.strip())<=10]
hotword = ' '.join(lines)
# hotword = ""
print(hotword)

# 加载模型
mode = "onnx"
# model_path = "damo/speech_paraformer-large_asr_nat-zh-cn-16k-common-vocab8404-pytorch"
model_path = "damo/speech_paraformer-large-contextual_asr_nat-zh-cn-16k-common-vocab8404"
# model_path = "damo/speech_seaco_paraformer_large_asr_nat-zh-cn-16k-common-vocab8404-pytorch"
if mode == 'torch':
    model = AutoModel(model=model_path,
                    disable_pbar=True,
                    disable_log=True)
if mode == 'onnx':
    # model = Paraformer(model_path, batch_size=1, quantize=True)
    model = ContextualParaformer(model_path, batch_size=1,quantize=True)
    # model = SeacoParaformer(model_path, batch_size=1,quantize=True)





app = Flask(__name__)


@app.route('/recognition', methods=['POST'])
def recognition():
    response = Response("")
    response.content_type = "text/plain"

    ip = request.remote_addr
    print("client ip:",ip)
    file = request.files['file']
    audio_bytes = file.read()
    pcm_bytes,cost = ffmpeg_read(audio_bytes)
    print("load audio cost:",cost)
    response.headers["cost_load_audio_seconds"] = cost

    s = time.perf_counter()
    if mode=='torch':
        res = model.generate(input=pcm_bytes, 
                            hotword=hotword)
        res = res[0]["text"].replace(" ","").encode("utf-8")
    if mode=='onnx':
        pcm_data = np.frombuffer(pcm_bytes,dtype=np.int16)
        res = model(pcm_data, hotword)
        res = res[0]["preds"][0].replace(" ","").encode("utf-8")
    cost = time.perf_counter()-s
    print(res)
    
    print("asr cost:",cost)
    response.headers["cost_asr_seconds"] = cost
    response.headers['code'] = 0
    
    response.set_data(res)
    return response

if __name__ == '__main__':

    app.run(host="0.0.0.0",port=1234,debug=False)