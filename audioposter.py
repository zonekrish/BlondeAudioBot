# Install needed dependencies
import tweepy
import ffmpeg
import os
import random
import math
from mysecrets import credentials, config

# Log into API + create client
auth = tweepy.OAuth1UserHandler(
    credentials["twitter"]["API_KEY"],
    credentials["twitter"]["API_KEY_SECRET"],
    credentials["twitter"]["ACCESS_TOKEN"],
    credentials["twitter"]["ACCESS_TOKEN_SECRET"],
)
api = tweepy.API(auth)

client = tweepy.Client(
    credentials["twitter"]["BEARER_TOKEN"],
    credentials["twitter"]["API_KEY"],
    credentials["twitter"]["API_KEY_SECRET"],
    credentials["twitter"]["ACCESS_TOKEN"],
    credentials["twitter"]["ACCESS_TOKEN_SECRET"],
)

# Remove clips if they're in the directory
try:
    os.remove("clip.mp3")
except:
    pass

try:
    os.remove("temp.mp4")
except:
    pass

# Get random song from audio file + its duration
rand = random.randint(0, len(os.listdir("audio"))-1)
song = "audio/" + os.listdir("audio")[rand]
songLength = math.floor(float(ffmpeg.probe(song)["format"]["duration"]))

# Get random time for clip to start
while True:
    time = random.randint(0, songLength-1)
    
    # Make sure clip doesn't start less than 3 seconds before end of song
    if not(time + 3 > songLength):
        break

# Get song name + human time for reply
reply = config["song_list"][rand]

minutes = math.floor(time / 60)
seconds = math.floor((time / 60 - minutes) * 60)
time = str(minutes).zfill(2) + ":" + str(seconds).zfill(2)

reply += ", " + time

# Extract clip with ffmpeg
audio = ffmpeg.input(song, ss=time, t=3)
audio = ffmpeg.output(audio, "clip.mp3")
ffmpeg.run(audio)

# Add album cover to clip
clip = ffmpeg.input("clip.mp3")
cover = ffmpeg.input(config["cover_file"])

clip = ffmpeg.concat(cover, clip, v=1, a=1)
clip = ffmpeg.output(clip, "temp.mp4")
ffmpeg.run(clip)

# Post to Twitter
vid = api.media_upload("temp.mp4")
tweet = api.update_status("", media_ids=[vid.media_id])
client.create_tweet(text=reply, in_reply_to_tweet_id=tweet.id)

# Finally, remove files
os.remove("clip.mp3")
os.remove("temp.mp4")