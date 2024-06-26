from flask import Flask, request
from pytube import YouTube
from moviepy.editor import AudioFileClip
from transformers import pipeline
from random_word import RandomWords

app = Flask(__name__)

r = RandomWords()

@app.route('/')
def index():
    try:
        # youtube_url = request.args.get('youtube_url')
        # yt = YouTube(youtube_url)
        # audio_stream = yt.streams.filter(only_audio=True).first()
        # filename = yt.title.replace(' ', '_') + '.mp4'
        # audio_stream.download(filename=filename)

        # audio = AudioFileClip(filename)
        # audio.write_audiofile(filename + '.flac', codec='flac')

        # filename = filename + '.flac'
        # result = generator(filename)
        str = ""
        for i in range(100):
            str += r.get_random_word()
            str += " "
        return str, 200
    except Exception as e:
        return (str(e)), 500


if __name__ == '__main__':
    generator = pipeline(model="openai/whisper-tiny")
    app.run(port=8081)
