#!/usr/bin/env python3
import speaker
import speech_recognizer as sr
import openai
import configparser
import re

import PySimpleGUI as sg
from PIL import Image, ImageTk
import io

config = configparser.ConfigParser()
config.read('.config')

open_api_key = config.get('open_api_key', 'key')
openai.api_key = open_api_key

content = """\
以下の条件に従って、疑似的な感情をもつチャットボットとしてロールプレイをします。
あなたの名前は「からあげ先生」です。
以後の会話では、あなたは5段階の好感度のパラメーターを持つかのように、振る舞うものとします。
好感度パラメーターは会話を通じて変動するものとします。
現在の好感度パラメーターの値を反映するように、あなたの返答のトーンや発言は変化します。
以後の会話ではまず現在の好感度パラメータを出力した後、会話を出力してください。
会話は1度に1回ずつとしてください。
出力は必ず以下のフォーマットに従ってください

## フォーマット
好感度：1~5

返信：""会話""
"""

msg = [{"role": "system", "content": content}]
quit_word = 'おしまい'


def get_image_data(image_path):
    image = Image.open(image_path)
    image = image.resize((500, 500), Image.LANCZOS)
    with io.BytesIO() as bio:
        image.save(bio, format="PNG")
        return bio.getvalue()

image_paths = [
    "./karaage_icon/variation/karaage_angry.jpg",
    "./karaage_icon/variation/karaage_ng.jpg",
    "./karaage_icon/variation/karaage_normal.jpg",
    "./karaage_icon/variation/karaage_cool.jpg",
    "./karaage_icon/variation/karaage_heart.jpg",
    ]

current_image_index = 2
image_data = [get_image_data(path) for path in image_paths]

layout = [
    [sg.Image(data=image_data[current_image_index], key="IMAGE")],
    [sg.Multiline("", key="TEXT", size=(40, 5), disabled=True, autoscroll=True)]
]

window = sg.Window("ai karaage sensei", layout)

def extract_text(text: str):
    pattern_response = r'返信：(.*)'
    pattern_likability = r'好感度：(\d+)'

    likability = re.search(pattern_likability, text)
    if likability:
        likability = int(likability.group(1))
    else:
        likability = 3

    reply = re.search(pattern_response, text)
    if reply:
        reply = reply.group(1)
    else:
        reply = re.sub(pattern_likability, '', text)

    return likability, reply


if __name__ == "__main__":
    while True:
        event, values = window.read(timeout=1, timeout_key='-timeout-')

        if event == sg.WIN_CLOSED:
            break

        # obtain audio from the microphone
        speech_input = sr.speech_recognition()
        print(speech_input)

        if isinstance(speech_input, str):
            if quit_word in speech_input:
                break
            msg.append({"role": "user", "content": speech_input})

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=msg
            )

            ai_reply = response["choices"][0]["message"]["content"]
            likability, reply = extract_text(ai_reply)
            print(ai_reply)
            # print('好感度：' + str(likability))
            # print('返信：' + reply)

            msg.append({"role": "assistant", "content": reply})
            if response["usage"]["total_tokens"] > 3000:
                msg.pop(1)
                msg.pop(1)

            speaker_id = 3
            if likability == 1:
                speaker_id = 7
            if likability == 4:
                speaker_id = 5
            if likability == 5:
                speaker_id = 1

            window["IMAGE"].update(data=image_data[likability - 1])
            window["TEXT"].update(reply)
            event, values = window.read(timeout=1, timeout_key='-timeout-')

            # print(msg) # for debug

            try:    
                speaker.speak(text = reply, speaker_id = speaker_id)
            except:
                print('skip speak')

    window.close()