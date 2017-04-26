# Discorddit
# /u/xGiBbYv, /u/n4nonuclei

import time
from time import sleep
import optModule
import redModule
import disModule

if __name__ == "__main__":
    configReq = optModule.config("Required");
    configOpt = optModule.config("Optional");
    subreddits = configReq["subreddits"]
    webhookURL = configReq["webhookurl"]
    colors = configReq["colors"]
    sleepTime = int(configReq["time"])

    img = configOpt["footerimg"]
    
    postedPosts = []

    while True:
        for subreddit in subreddits:
            newPosts = redModule.getNew(subreddit)
            if newPosts != None:
                for newPost in reversed(newPosts):
                    if (newPost["data"]["id"] not in postedPosts) and ((time.time() - newPost["data"]["created_utc"]) < sleepTime * 1.5):
                        disModule.postDiscordPost(newPost, webhookURL, img, colors[subreddits.index(subreddit)])
                        postedPosts.append(newPost["data"]["id"])
                        sleep(2)
                print(subreddit + " done")
            else:
                print(subreddit + " error!")

        print("Sleeping for " + str(int(sleepTime / 60)) + " minutes.\n")
        sleep(sleepTime)
        