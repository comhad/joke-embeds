# `joke-embeds`
A flask server no one asked for to makes embeds for discord to rickroll people and other things, well just rick roll people at the moment.
> If you've used Heroku before, you've probably received an email telling you that Heroku are shutting down some free tier products. As you might've guessed, the `joke-embeds` app was designed to run on these free dynos. With the shutdown of these free dynos, I've decided to stop hosting the app on cdn.quotebot.me, since I don't use it anymore, and I don't receive any comments on the blog post or the YouTube video of the app.

# Usage
This server is designed to create embeds in discord by recieving a youtube video ID, and make an embed that disguises the Never Gonna Give You Up youtube video as that video.

You can get a Youtube video ID by going to the video and select everything after `watch?=`.

![A youtube video ID being highlighted](https://github.com/comhad/joke-embeds/blob/main/media/youtube_id.PNG?raw=true)

You need to prefix the URLs, either with the app name (`<appname>.herokuapp.com`) or add your own domain to it, In the examples I've added a `cdn` subdomain of my domain `quotebot.me`, although you can choose any subdomain, or not have one at all. You also need to prefix it with either `https://` or `http://`, if you're using a custom domain, you may have some issues with `https://`, but either will work.

## Youtube style embed
To make a Youtube style embed, do `/yt?video=` followed by your Youtube video ID, and post it to discord, this will create a video embed that looks similar to Youtube's embeds.

![An embed similar to youtube](https://github.com/comhad/joke-embeds/blob/main/media/rickroll1.PNG?raw=true)

## Posted video embed
To make an embed where it looks like the video was uploaded or the raw file was linked from another site, do `/raw/` followed by your Youtube video ID, and post it to discord.

![An embed similar to uploaded videos](https://github.com/comhad/joke-embeds/blob/main/media/rickroll2.PNG?raw=true)

*You can add any extension on the end, it will be ignored by the app.*
