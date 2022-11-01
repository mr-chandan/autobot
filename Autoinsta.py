import os
from instagrapi import Client
from RedDownloader import RedDownloader
import time

title = []
cl = Client()
cl.login('memes.pst', '123321123zxc')


def getmemes():
    post = RedDownloader.DownloadVideosBySubreddit(
        'IndianDankMemes', 5, flair=None, SortBy="hot", quality=1080, output="downloaded", destination=None, cachefile='Downloaded.txt')
    title = post.GetPostTitles()
    return title

while True:
    title = getmemes()
    for i in range(1, 7):
        cl.video_upload(
            "downloaded\downloaded"+str(i)+".mp4",
            title[i] + "  credits to IndianDankMemes")
        os.remove("downloaded\downloaded"+str(i)+".mp4")
        os.remove("downloaded\downloaded"+str(i)+".mp4.jpg")
        print("sleaping...............in_for")
        time.sleep(1800)
    title = []
    print("sleaping...............in_while")
    time.sleep(21600)
