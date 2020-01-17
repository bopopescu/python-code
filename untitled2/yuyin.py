import pyaudio
import IPython.display as ipd
import wave
import requests
import json
import base64
import os
import requests
import json
import wave
from pyaudio import PyAudio, paInt16

def play():
    chunk=1024  #2014kb
    wf=wave.open("./1.wav",'rb')
    p=PyAudio()
    stream=p.open(format=p.get_format_from_width(wf.getsampwidth()),channels=wf.getnchannels(),rate=wf.getframerate(),output=True)

    data = wf.readframes(chunk)  # 读取数据

    while True:
        data=wf.readframes(chunk)
        print(len(data))
        if len(data)==0:
            break
        stream.write(data)
    stream.stop_stream()   # 停止数据流
    stream.close()
    p.terminate()  # 关闭 PyAudio
    print('play函数结束！')




def LuYin():
    while 1:
            CHUNK = 2048  # wav文件是由若干个CHUNK组成的，CHUNK我们就理解成数据包或者数据片段。
            FORMAT = pyaudio.paInt16  # 这个参数后面写的pyaudio.paInt16表示我们使用量化位数 16位来进行录音。
            CHANNELS = 1  # 代表的是声道，这里使用的单声道。
            RATE = 16000  # 采样率16k
            RECORD_SECONDS = 2.5  # 采样时间

            p = pyaudio.PyAudio()

            stream = p.open(format=FORMAT,
                            channels=CHANNELS,
                            rate=RATE,
                            input=True,
                            frames_per_buffer=CHUNK)

            print("* 录音开始")
            frames = []
            for i in range(0, 30):
                data = stream.read(CHUNK)
                frames.append(data)

            print("* 录音结束")
            wf = wave.open(r'1.wav', 'w')

            wf.setnchannels(CHANNELS)
            wf.setsampwidth(p.get_sample_size(FORMAT))
            wf.setframerate(RATE)
            wf.writeframes(b''.join(frames))
            wf.close()
            return 1


# play()

