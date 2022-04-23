import json
import os
import random
import requests
from pydub import AudioSegment


def get_picture(pictures):
    pic = random.choice(pictures)
    return pic


def get_audio(pathes):
    AudioSegment.converter = "C:\\FFmpeg\\bin\\ffmpeg.exe"
    AudioSegment.ffmpeg = "C:\\FFmpeg\\bin\\ffmpeg.exe"
    AudioSegment.ffprobe = "C:\\FFmpeg\\bin\\ffprobe.exe"
    result_sound = AudioSegment.empty()
    for path in pathes:
        little_sound = AudioSegment.from_mp3(path)
        result_sound += little_sound
        result_sound.export(os.getcwd() + "\\result_audio.mp3", format="mp3")


def get_audio_url():
    url = "http://httpbin.org/post"  # Адрес загрузки файла на сервер ВКонтакте
    file_path = os.getcwd() + "\\result_audio.mp3"
    response = requests.post(url, files={"audio": open(file_path, 'rb')})
    json_response = response.json()
    audio = json_response['files']['audio']
    return audio


def _get_json_verbs():
    """Получаем список аудио из файла жсон"""
    with open('data/verb.json', encoding='utf-8') as f:
        audios = json.load(f)
        if audios:
            return audios
        return []

def _get_json_nouns():
    """Получаем список аудио из файла жсон"""
    with open('data/noun.json', encoding='utf-8') as f:
        audios = json.load(f)
        if audios:
            return audios
        return []

def get_audio_pathes():
    audios_verb = _get_json_verbs()
    audios_noun = _get_json_nouns()
    verb_1 = random.choice(audios_verb)
    noun = random.choice(audios_noun)
    while True:
        verb_2 = random.choice(audios_verb)
        if verb_1 != verb_2:
            break
    audio_pathes = []
    words = []
    audio_pathes.append(verb_1["audio_path"])
    words.append(verb_1['word'])
    audio_pathes.append(noun["audio_path"])
    words.append(noun['word'])
    audio_pathes.append(verb_2["audio_path"])
    words.append(verb_2['word'])

    return audio_pathes, words



