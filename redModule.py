

def getNew(argSubreddit):
    import requests
    getHeaders = {'user-agent': 'futbottool'}
    try:
        html = requests.get("https://www.reddit.com/r/" + argSubreddit + "/new.json", headers = getHeaders)
        data = html.json()["data"]["children"]
        return data
    except:
        print("exception with json: on %s!" % html)
        return None
