import requests
import urllib
from PIL import Image
import pytesseract

urlIndex = "http://hoidienvannghe.oceanbank.vn/Binhchon.aspx?location=MB"

# get header -> userid, sessionid
r = requests.get(urlIndex)
sessionId = r.headers['Set-Cookie'].split(';')[0].split('=')[1]
userId = r.headers['Set-Cookie'].split(';')[4].split('=')[1]

# set url to download captcha
urlCaptcha = "http://hoidienvannghe.oceanbank.vn/GetCapchar.aspx?user_id="+userId+"&ms=121"
print sessionId
print urlCaptcha

# download captcha file
f = open('captcha.jpg', 'wb')
f.write(urllib.urlopen(urlCaptcha).read())
f.close()

# read captcha
text = pytesseract.image_to_string(Image.open('captcha.jpg'))
captcha = text.split(',')[0]

# submit vote
urlUpvote = "http://hoidienvannghe.oceanbank.vn/UpdateVote.aspx?user_id=" + \
    userId + "&vp_id=121&capchar=" + captcha

re = requests.get(urlUpvote)
print re.content
