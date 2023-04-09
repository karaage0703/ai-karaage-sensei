#!/usr/bin/env python3
import speaker
import speech_recognizer as sr
import openai
import configparser

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
以後の会話ではまず現在の好感度パラメータを出力し、その後に会話を出力してください。
会話は1度に1回ずつとしてください。
出力は以下の形式としてください。

""
好感度：1~5

返信：""会話""
""
"""

msg = [{"role": "system", "content": content}]
quit_word = 'おしまい'

while True:
    # obtain audio from the microphone
    speech_input = sr.speech_recognition()
    print(speech_input)

    msg.append({"role": "user", "content": speech_input})
    if quit_word in speech_input:
        break
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=msg
    )

    ai_reply = response["choices"][0]["message"]["content"]
    print(ai_reply)
    msg.append({"role": "assistant", "content": ai_reply})
    if response["usage"]["total_tokens"] > 3000:
        msg.pop(1)
        msg.pop(1)
    speaker.speak(text = ai_reply, speaker_id = 4)
