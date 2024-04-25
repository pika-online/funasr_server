import subprocess
import io
import time 

def ffmpeg_read(audio_bytes):
    s = time.perf_counter()
    audio_stream = io.BytesIO(audio_bytes)
    ffmpeg_cmd = [
    'ffmpeg',
    '-i', 'pipe:',  
    '-f', 's16le',
    '-acodec', 'pcm_s16le',
    '-ar', '16k',
    '-ac', '1',
    'pipe:' ]
    with subprocess.Popen(ffmpeg_cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=False) as proc:
        stdout_data, stderr_data = proc.communicate(input=audio_stream.read())
    if stderr_data:
        print(stderr_data,file=open("ffmpeg.log","a+"))
    cost = time.perf_counter()-s
    return stdout_data,cost

if __name__ == "__main__":
    pcm_bytes,cost = ffmpeg_read(open("/root/data/client.mp3","rb").read())
    print(cost)