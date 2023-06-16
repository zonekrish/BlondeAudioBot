# BlondeAudioBot
A simple Python script that takes a random 3-second clip from an audio file and adds an image, sending that video file to Twitter. This is currently developed for [@BlondedAudio](https://twitter.com/BlondedAudio)

## Features
- Randomly extracts 3 seconds from an audio file
- Combines a .jpg image to create a .mp4 file
- Can select from multiple audio files
- Only needs two installed libraries

## WARNING:
I am not an expert at programming, which means the way I've coded things might not be the best.

Hence, I've tried my best to make things as plug-and-play as possible. There should be no need for any programming experience to use this.

With that said, any experience in Python *will* help with any errors you may run into. I am not promising that there will be no errors, but regardless if you know Python or not, I will help you with those errors.

This comes with a General Public License. This means you are allowed to use this program essentially however you'd like. I am not liable for anything wrong that happens, nor can I promise any warranty. (But I'd love to help in the case of anything bad happening)

## Usage
Below is a guide on how to use this program for your own needs. This guide is going to be a perpetual work-in-progress, because I may add some things to help smooth the process in using this program.

### Dependencies
- Latest version of Python (3.*)
- [tweepy](https://pypi.org/project/tweepy/)
- [ffmpeg-python](https://pypi.org/project/ffmpeg-python/)
- Twitter API access (free tier is fine)

### API Access
Here's a quick rundown on how to create a Twitter bot

1. Log into [the Twitter Developer site](https://developer.twitter.com)
2. Create yourself [a project and an app](https://developer.twitter.com/en/portal/projects-and-apps)
3. In your app, go to the "Keys and Tokens" section
4. Please save the API key and secret, the bearer token, and the access token and secret with read and write permissions!

### Set up
Now that you have yourself a bot, refer to these steps:

1. Clone this repository into any directory
2. If there isn't one yet, create a folder named exactly: "audio" and put your audio files in there
3. Add the photo you'd like to go with the audio file