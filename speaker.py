from pathlib import Path
import voicevox_core
from voicevox_core import AccelerationMode, AudioQuery, VoicevoxCore
from playsound import playsound

open_jtalk_dict_dir = './open_jtalk_dic_utf_8-1.11'
out = Path('output.wav')
acceleration_mode = AccelerationMode.AUTO

def speak(text = 'これはテストです', speaker_id = 2) -> None:
    core = VoicevoxCore(
        acceleration_mode=acceleration_mode, open_jtalk_dict_dir=open_jtalk_dict_dir
    )
    core.load_model(speaker_id)
    audio_query = core.audio_query(text, speaker_id)
    wav = core.synthesis(audio_query, speaker_id)
    out.write_bytes(wav)
    playsound(out)


if __name__ == "__main__":
    speak(text = 'テスト', speaker_id = 4)
