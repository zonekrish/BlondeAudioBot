# Install needed dependencies
import tweepy
import ffmpeg
import os
import random
import math
from mysecrets import credentials

# Log into API + create client
auth = tweepy.OAuth1UserHandler(
    credentials["API_KEY"],
    credentials["API_KEY_SECRET"],
    credentials["ACCESS_TOKEN"],
    credentials["ACCESS_TOKEN_SECRET"],
)
api = tweepy.API(auth)

client = tweepy.Client(
    credentials["BEARER_TOKEN"],
    credentials["API_KEY"],
    credentials["API_KEY_SECRET"],
    credentials["ACCESS_TOKEN"],
    credentials["ACCESS_TOKEN_SECRET"],
)
# Remove clips if they're in the directory
try:
    os.remove("clip.mp3")
    os.remove("temp.mp4")
except:
    pass

# Get random song from audio file + its duration
song = "audio/" + random.choice(os.listdir("audio"))
songLength = math.floor(float(ffmpeg.probe(song)["format"]["duration"]))

# Get random time for clip to start
while True:
    time = random.randint(0, songLength-1)
    
    # Make sure clip doesn't start less than 3 seconds before end of song
    if not(time + 3 > songLength):
        break

# Extract clip with ffmpeg
audio = ffmpeg.input(song, ss=time, t=3)
audio = ffmpeg.output(audio, "clip.mp3")
ffmpeg.run(audio)

# Add album cover to clip
clip = ffmpeg.input("clip.mp3")
cover = ffmpeg.input("cover.jpg")

clip = ffmpeg.concat(cover, clip, v=1, a=1)
clip = ffmpeg.output(clip, "temp.mp4")
ffmpeg.run(clip)

# Post to Twitter
vid = api.media_upload("temp.mov")
client.create_tweet(media_ids=[vid.media_id])