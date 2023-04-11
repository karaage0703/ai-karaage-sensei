#!/bin/bash

# setup speech_recognition with whisper
sudo apt install -y portaudio19-dev
pip install SpeechRecognition
pip install pyaudio
pip install openai

# setup voicevox
wget https://github.com/VOICEVOX/voicevox_core/releases/download/0.14.3/voicevox_core-0.14.3+cpu-cp38-abi3-linux_x86_64.whl
pip install voicevox_core-0.14.3+cpu-cp38-abi3-linux_x86_64.whl

# download onnxruntime for voicevox
wget https://github.com/microsoft/onnxruntime/releases/download/v1.13.1/onnxruntime-linux-x64-1.13.1.tgz
tar xvzf onnxruntime-linux-x64-1.13.1.tgz
mv onnxruntime-linux-x64-1.13.1/lib/libonnxruntime.so.1.13.1 ./

# download dictionary for voicevox
wget http://downloads.sourceforge.net/open-jtalk/open_jtalk_dic_utf_8-1.11.tar.gz
tar xvzf open_jtalk_dic_utf_8-1.11.tar.gz

# setup playsound for play .wav
pip install playsound

# install library for GUI
pip install pillow
pip install PySimpleGUI
