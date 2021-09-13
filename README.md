# `joke-embeds`
A flask server no one asked for to makes embeds for discord to rickroll people and other things, well just rick roll people at the moment.

# Usage
This server is designed to create embeds in discord by recieving a youtube video ID, and make an embed that disguises the Never Gonna Give You Up youtube video as that video.

You need to prefix the URLs, either with the app name (`<appname>.herokuapp.com`) or add your own domain to it, In the examples I've added a `cdn` subdomain of my domain `quotebot.me`, although you can choose any subdomain, or not have one at all.

## Youtube style embed
To make a Youtube style embed, do `/yt?video=` followed by your Youtube video ID, and post it to discord, this will create a video embed that looks similar to Youtube's embeds.

![An embed similar to youtube](https://github.com/comhad/joke-embeds/blob/main/media/rickroll1.PNG?raw=true)

## Posted video embed
To make an embed where it looks like the video was uploaded or the raw file was linked from another site, do `/raw/` followed by your Youtube video ID, and post it to discord.

![An embed similar to uploaded videos](https://github.com/comhad/joke-embeds/blob/main/media/rickroll2.PNG?raw=true)

*You can add any extension on the end, it will be ignored by the app.*