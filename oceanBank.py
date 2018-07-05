import requests
import urllib
from PIL import Image
import pytesseract
import time
from random import randint


def upvote(ms):
    urlIndex = "http://hoidienvannghe.oceanbank.vn/Binhchon.aspx?location=MB"
    # get header -> userid, sessionid
    r = requests.get(urlIndex)
    sessionId = r.headers['Set-Cookie'].split(';')[0].split('=')[1]
    userId = r.headers['Set-Cookie'].split(';')[4].split('=')[1]
    # set url to download captcha
    urlCaptcha = "http://hoidienvannghe.oceanbank.vn/GetCapchar.aspx?user_id=" + \
        userId+"&ms="+str(ms)
    # download captcha file
    capImg = "captcha"+str(ms)+".jpg"
    f = open(capImg, 'wb')
    f.write(urllib.urlopen(urlCaptcha).read())
    f.close()
    # read captcha
    text = pytesseract.image_to_string(Image.open(capImg))
    captcha = text.split(',')[0]
    # submit vote
    urlUpvote = "http://hoidienvannghe.oceanbank.vn/UpdateVote.aspx?user_id=" + \
        userId + "&vp_id="+str(ms)+"&capchar=" + captcha
    re = requests.get(urlUpvote)
    print re.content


if __name__ == "__main__":
    while True:
        upvote(121)
        upvote(120)
        sleeptime = (randint(10, 20))
        time.sleep(sleeptime)
        print "Sleep for: "+str(sleeptime)
