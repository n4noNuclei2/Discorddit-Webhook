# Discorddit Webhook
A script to post the newest submissions of a given subreddit to a discord webhook. The script will check every five minutes for new posts. 

[![MIT](https://img.shields.io/github/license/mashape/apistatus.svg?style=flat-square)](https://opensource.org/licenses/MIT) [![Say Thanks](https://img.shields.io/badge/say-thanks-ff69b4.svg)](https://saythanks.io/to/RainbowDinoaur)

## Contents

- [Installation](#installation)	
- [Dependencies](#dependencies)
- [Using Discorddit](#using-discorddit)
- [Licence](#licence)


## Installation
Just download the script and run main.py! The script is a infinite loop for ease of use.

## Dependencies
Discorddit requires Python 3.5. Discorddit the Python Library "Requests". This will be installed by executing `pip install -r /path/to/requirements.txt`. Well done, you have now installed everything you need for Discorddit.

## Using Discorddit
To start using, you will need to setup the config.ini file. The one provided looks like this:

```
[Required]
url: https://discordapp.com/api/reallynicewebhookurl
subreddit: greatestsubredditofalltime
colour: 16744192

[Optional]
footerimg: https://i.imgur.com/coolfooterimage
```

You will need to replace the url and subreddit fields with the ones needed for your discord server. You can get the url from the webhooks menu. The subreddit name is just the name of the subreddit. Colour is a decimal version of the hex code for the colour you want to use. A footer image is optional. If you don't have/need one, leave this section blank.

The webhook has three types of posts. Self text posts where plain text is posted, a link posts where a preview in unavaliable so a URL is posted, and a link post where preview is avaliable so both the preview and the URL are posted. 

Be careful running the script for the first time or after periods of inactivity, it will post 25 messages at once to load up the ids.

![Preview](http://i.imgur.com/NcxWOCY.png)

## Licence
[MIT Licence](https://github.com/RainbowDinoaur/Reddit-Discord-Webhook/blob/master/LICENSE)
