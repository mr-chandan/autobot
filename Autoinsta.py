import os
from instagrapi import Client
from RedDownloader import RedDownloader
import time
import random

inst = Client()
inst.login('ID', 'PASSWORD')


def getmemes():
    try:
        post = RedDownloader.DownloadVideosBySubreddit(
            'nextfuckinglevel', 5, flair=None, SortBy="hot", output="downloaded", quality=1080, destination=None, cachefile='Downloaded.txt')
        title = post.GetPostTitles()
    except:
        print("error in redddit api")
    return title


tags = ["#love #art #beautiful #follow #life #makeup #bestoftheday #amazing #lifestyle #beach #vscocam #tagsforlikes #sun #family",
        "#igers #sunset #family #girl #repost #summer #instadaily #style #follow #photography #life #makeup #instagram #love #inspiration",
        "#peace #peaceful #peacefull #peacefulday #satisfying #satisfyingvideos #satisfyingsounds #satisfyingasmr #satisfyingcleaning #satisfyingslimevideo",
        "#tagsforlikes #photographer #hair #motivation #smile #instalike #science #sciencefiction #sciencememes #technology #technologynews #informationtechnology",
        "#technologyfacts #technologyisawesome #memes #mamas #timepass #passingtime #passtime #passeggiatatime #passingthetime #follow4like #pleasefollow #tambahfollowers",
        "#reelsvideo #instareels #reelsindia #reelit #reeltoreel #reellife #instagramreels #spamforfollow #followlike #followforafollow #cashfollowtrain #followbacknow #followersrealindo"]

while True:
    title = getmemes()
    for i in range(1, (len(title)+1)):
        try:
            inst.video_upload(
                "downloaded/downloaded"+str(i)+".mp4",
                title[i-1] + "  " + random.choice(tags))
        except:
            print("error")
        os.remove("downloaded/downloaded"+str(i)+".mp4")
        os.remove("downloaded/downloaded"+str(i)+".mp4.jpg")
        print("sleaping............... "+str(i))
        time.sleep(7200)
    title.clear()
