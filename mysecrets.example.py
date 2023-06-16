# Here is where you'll put some information about your Twitter bot and other configuration stuff
# Before touching this file, please rename this to "mysecrets.py"!!
# This part is for configurating your program
# For "cover_file", you want to add the file name for the image you want to use here (ex: "cover.jpg")
# For "song_list", add the names of your songs you've added into the audio folder

# Ex: If I have 3 songs in the audio folder, mine would like this:
# "song_list": sorted(["Nikes", "Ivy", "Pink + White"])

config = {
    "cover_file": "[insert file name here]",
    "song_list": sorted([])
}

# This is for the Twitter bot credentials
# If you're planning on just retrieving audio/video files, you don't have to worry about this
# DO NOT SHARE THE INFO HERE WITH ANYBODY
# DO NOT PUSH THE FINAL "mysecrets.py" FILE INTO THE REPOSITORY
# ("mysecrets.py" is in gitignore for a reason)

# Remove the hard brackets [] when putting in your values
credentials = {
    "BEARER_TOKEN": r"[insert bearer token here]",
    "API_KEY": "[insert API key here]",
    "API_KEY_SECRET": "[insert API key secret here]",
    "ACCESS_TOKEN": "[insert access token here]",
    "ACCESS_TOKEN_SECRET": "[insert access token secret here]"
}