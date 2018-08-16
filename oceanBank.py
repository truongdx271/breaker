import requests
import urllib
from PIL import Image
import pytesseract
import time
from random import randint
from faker import Factory

fake_generator = Factory.create()

def get_random_ip():
    return fake_generator.ipv4()

def set_header(ip,sessionId):
    return {
    "Host": "hoidienvannghe.oceanbank.vn",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
    "Accept": "*/*",
    "Referer": "http://hoidienvannghe.oceanbank.vn/Binhchon.aspx?location=MB",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "X-Forwarded-For": ip,
    "X-Requested-With": "XMLHttpRequest",
    "Cookie": "ASP.NET_SessionId="+sessionId,
    "Connection": "close"
    }


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
    captcha = text.replace('\'','').replace(',','').replace('s','5').replace('.','').replace(' ','')
    print captcha
    # submit vote
    urlUpvote = "http://hoidienvannghe.oceanbank.vn/UpdateVote.aspx?user_id=" + \
        userId + "&vp_id="+str(ms)+"&capchar=" + captcha
    re = requests.get(urlUpvote,headers=set_header(get_random_ip(),sessionId))
    print re.status_code


if __name__ == "__main__":
    #while True:
    #    upvote(121)
    #    sleeptime = (randint(10, 20))
    #    time.sleep(sleeptime)
    #    print "Sleep for: "+str(sleeptime)
    upvote(121)
