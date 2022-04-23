from flask import Flask, render_template

from utils import get_picture, get_audio_url, get_audio, get_audio_pathes

from data.pictures import pictures

app = Flask('Zhirinovsky')


@app.route("/")
def page_index():
    picture = get_picture(pictures=pictures)
    audio_pathes, words = get_audio_pathes()
    phrase = ' '.join(words)
    get_audio(audio_pathes)
    audio = get_audio_url()
    return render_template("index.html", picture=picture, phrase=phrase, audio=audio)


if __name__ == "__main__":
    app.run()
