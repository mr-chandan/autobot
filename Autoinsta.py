import os
from instagrapi import Client
from RedDownloader import RedDownloader
import time

inst = Client()
inst.login('id', 'password')


def getmemes():
    RedDownloader.DownloadVideosBySubreddit(
        'IndianDankMemes', 6, flair=None, SortBy="hot", output="downloaded", quality=360, destination=None, cachefile='Downloaded.txt')


while True:
    title = getmemes()
    for i in range(1, 7):
        try:
            inst.video_upload(
                "/home/mtgodlon/downloaded/downloaded"+str(i)+".mp4",
                "credits to IndianDankMemes")
            os.remove("/home/mtgodlon/downloaded/downloaded"+str(i)+".mp4")
            os.remove("/home/mtgodlon/downloaded/downloaded"+str(i)+".mp4.jpg")
        except:
            print("error")
        print("sleaping...............in_for")
        time.sleep(4680)
    print("sleaping...............in_while")
    time.sleep(3600)
