import base64

import requests
import json
import time
from pydub import AudioSegment
from pydub.playback import play
import pyaudio
import wave
import io

API_KEY = ""
SECRET_KEY = ""


def getID(t):
    url = "https://aip.baidubce.com/rpc/2.0/ernievilg/v1/txt2imgv2?access_token=" + get_access_token()

    payload = json.dumps({
        "prompt": t,
        "version": "v2",
        "width": 1024,
        "height": 1024
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.json())

    return response.json()["data"]["task_id"]


def getPic(t):
    url = "https://aip.baidubce.com/rpc/2.0/ernievilg/v1/getImgv2?access_token=" + get_access_token()
    picID = getID(t)
    payload = json.dumps({
        "task_id": picID
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    while response.json()["data"]["task_status"] == 'RUNNING':
        time.sleep(0.8)
        response = requests.request("POST", url, headers=headers, data=payload)
    # print(response.json())
    # print(response.json()["data"]["sub_task_result_list"][0]["final_image_list"][0]["img_url"])
    return response.json()["data"]["sub_task_result_list"][0]["final_image_list"][0]["img_url"]


def say(ss):
    url = "https://aip.baidubce.com/rpc/2.0/tts/v1/create?access_token=" + get_access_token()

    payload = json.dumps({
        "text": ss,
        "lang": "zh"
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
    sayId = response.json()["task_id"]

    url = "https://aip.baidubce.com/rpc/2.0/tts/v1/query?access_token=" + get_access_token()

    payload = json.dumps({"task_ids": [sayId]})
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    while response.json()["tasks_info"][0]["task_status"] == "Running":
        time.sleep(0.5)
        response = requests.request("POST", url, headers=headers, data=payload)
    output_url = response.json()["tasks_info"][0]["task_result"]["speech_url"]

    with open("output.mp3", "wb") as f:
        f.write(requests.get(output_url).content)
    f.close()
    audio_data = AudioSegment.from_file("output.mp3", format="mp3")
    play(audio_data)


def getListen():
    # 聆听
    listen()
    # 获取base64编码
    # PCM 文件名
    FILE_NAME = 'input.pcm'

    # 读取 PCM 文件
    with open(FILE_NAME, 'rb') as pcm_file:
        pcm_data = pcm_file.read()

    # 计算 PCM 数据的长度并打印
    pcm_len = len(pcm_data)

    # 将 PCM 数据进行 base64 编码并打印
    base64_data = base64.b64encode(pcm_data).decode('utf-8')

    url = "https://vop.baidu.com/server_api"

    # speech 可以通过 get_file_content_as_base64("C:\fakepath\input.pcm",False) 方法获取
    payload = json.dumps({
        "format": "pcm",
        "rate": 16000,
        "channel": 1,
        "cuid": "test111",
        "token": get_access_token(),
        "speech": base64_data,
        "len": pcm_len
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
    return response.json()["result"][0]


def listen():
    # 配置录音参数
    CHANNELS = 1  # 声道数
    FORMAT = pyaudio.paInt16  # 采样位数
    RATE = 16000  # 采样频率
    CHUNK = 1024  # 缓冲区大小，以数据块为单位
    RECORD_SECONDS = 5  # 录音时长，单位为秒
    WAVE_OUTPUT_FILENAME = "input.pcm"  # 录音文件名

    # 创建PyAudio对象
    p = pyaudio.PyAudio()

    # 打开音频数据流
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("开始录音...")

    frames = []

    # 录音逻辑
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK, exception_on_overflow=False)
        frames.append(data)

    print("录音结束...")

    # 关闭音频数据流
    stream.stop_stream()
    stream.close()
    p.terminate()

    # 保存录音数据为pcm格式文件
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))


# if __name__ == '__main__':
#     getListen()
#     say("你好，我是小爱同学")

