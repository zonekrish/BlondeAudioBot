import ffmpeg
import os

try:
    os.remove("clip.mp3")
except:
    pass

audio = ffmpeg.input("selfcontrol.mp3", ss=43, t=3)
audio = ffmpeg.output(audio, "clip.mp3")
ffmpeg.run(audio)