import requests
import os 
import base64 
import json 
import time
# host = "192.168.1.134"
# port = 8550
# url = f'http://{host}:{port}/recognition'

# url = "http://hhaiasr.vip.cpolar.cn/recognition"
url = "http://47.96.15.141:1234/recognition"


def asr(file_path):
      files = {'file':open(file_path, 'rb').read()}
      s = time.time()
      response = requests.post(url, files=files)
      cost_all_seconds = time.time() - s
      result = "",
      cost = []
      if response.status_code == 200:
            code = int(response.headers.get("code"))
            cost_load_audio_seconds = float(response.headers.get("cost_load_audio_seconds"))
            cost_asr_seconds = float(response.headers.get("cost_asr_seconds"))
            cost_transport_seconds = cost_all_seconds - cost_load_audio_seconds - cost_asr_seconds
            print("[cost_all_seconds]",cost_all_seconds)
            print("[cost_load_audio_seconds]",cost_load_audio_seconds)
            print("[cost_asr_seconds]",cost_asr_seconds)
            print("[cost_transport_seconds]",cost_transport_seconds)
            result = response.content.decode("utf-8")
            cost = [cost_all_seconds,cost_load_audio_seconds,cost_asr_seconds,cost_transport_seconds]
            # print("[result]",result)
      else:
            print("Failed")
      return result,cost


if __name__ == "__main__":

    res = asr("/root/data/client.mp3")
    print(res)

                
