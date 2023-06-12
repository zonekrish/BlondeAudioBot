import ffmpeg

audio = ffmpeg.input("selfcontrol.mp4", ss=43, t=3)
audio = ffmpeg.output(audio, "clip.mp4")
ffmpeg.run(audio)