# Discorddit Webhook
A script to post the newest submissions of a given subreddit to a discord webhook. The script will check every five minutes for new posts. 

[![MIT](https://img.shields.io/github/license/mashape/apistatus.svg?style=flat-square)](https://opensource.org/licenses/MIT) 

## Contents

- [Installation](#installation)	
- [Dependencies](#dependencies)
- [Using Discorddit](#using-discorddit)
- [Licence](#licence)


## Installation
Just download the script and run Discorddit.py! The script is a infinite loop.

## Dependencies
Discorddit requires Python 3.5+, and the Python Library "Requests". 
This can be installed by executing `pip install -r /path/to/requirements.txt`. 
Well done, you have now installed everything you need for Discorddit!

## Using Discorddit
To start using, you will need to setup the config.ini file. The one provided looks something like this:

```
[Required]
webhooksurl: https://discordapp.com/api/reallynicewebhookurl
subreddits: ["sr1", "sr2"]
colors: [16744192, 65407]
time: 300

[Optional]
footerimg: 
```

You will need to replace the webhook url and subreddits fields with the ones needed for your discord server. You can get the url from the webhooks menu. The subreddit name is just the name of the subreddit. The colors are decimal versions of the hex code for the color you want to use. A footer image is optional. If you don't have/need one, leave this section blank.

The webhook has three types of posts. Self text posts where plain text is posted, a link posts where a preview in unavaliable so a URL is posted, and a link post where preview is avaliable so both the preview and the URL are posted. 

The script will also post reddit threads that were created in the period (default 5 min) before the bot was started, so if you increase this value it could post many threads.

![Preview](http://i.imgur.com/NcxWOCY.png)

## Licence
[MIT Licence](https://github.com/RainbowDinoaur/Reddit-Discord-Webhook/blob/master/LICENSE)
