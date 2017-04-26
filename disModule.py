def isSelfpost(argData):
    if "reddit.com" in argData["data"]["url"] and not "np.reddit.com" in argData["data"]["url"]:
        return True
    else:
        return False

def isPreview(argData):
    try:
        i = argData["data"]["preview"]
        return True
    except:
        return False

def determineType(argData):
    if isSelfpost(argData):
        return 0
    elif isPreview(argData):
        return 1
    else:
        return 3

def developDiscordPost(argData, argFooterImg, argColor):
    from textwrap import shorten
    from datetime import datetime

    redType = determineType(argData)
    if redType == 0:
        description = shorten(argData["data"]["selftext"], 500)
        imageurl = None
    elif redType == 1:
        description = argData["data"]["url"]
        imageurl = argData["data"]["preview"]["images"][0]["source"]["url"]
    elif redType == 2:
        description = None
        imageurl = argData["data"]["url"]
    elif redtype == 3:
        description = argData["data"]["url"]
        imageurl = None

    strCreated = datetime.utcfromtimestamp(argData["data"]["created_utc"]).strftime("%d/%m/%Y %H:%M:%S UTC")

    message = {
        "embeds": [{
            "color": int(argColor),
            "title": "/u/" + argData["data"]["author"],
            "url": "https://www.reddit.com/u/" + argData["data"]["author"],
            "author": {"name": argData["data"]["title"], "url": "https://reddit.com" + argData["data"]["permalink"]},
            "image": {"url": imageurl},
            "description": description,
            "footer": {"icon_url": argFooterImg, "text": "/r/" + argData["data"]["subreddit"] + "  |  Created " + strCreated}
        }]
    }

    if not imageurl:
        message["embeds"][0].pop("image")
    if not description:
        message["embeds"][0].pop("description")

    return message

def postDiscordPost(argData, argUrl, argImage, argColor):
    import requests
    import json

    message = developDiscordPost(argData, argImage, argColor)
    messageHeaders = {'Content-Type': 'application/json'}
    reqReturn = requests.post(argUrl, data = json.dumps(message), headers = messageHeaders)
    if reqReturn.status_code == 400:
        print("Post Failed, Error 400")
    else:
        print("Posted {}".format(argData["data"]["title"]))
    print("Code " + str(reqReturn.status_code))
    print("")