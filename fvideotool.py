# By Bilal Aloui @ 12/06/2021 @ 
import requests
import re

# Don't use a samrtphone browser user-agent (i'm using firefox for windows user-agent)
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0"}
# Send an http request using GET 
r =requests.get('https://www.facebook.com/DimaRapTV/videos/moro-khofiatan/305658944351064/?_rdc=1&_rdr',headers=headers)
# Save response data as text
html = r.text 

# Search and print html page title
title = re.search('<title id=\"pageTitle\">(.*?)</title>', html)
if title is not None:
 print('Title : '+title.group(1))
 
# Search and print video thumbnail url
thum_url = re.search('.thumbnailUrl.:"(.*?)"', html)
if thum_url is not None:
 print('Thumbnail Url : '+thum_url.group(1).replace("\/","/"))

# Search and print SD video url
sd_url = re.search('sd_src:"(.*?)",', html)
if sd_url is not None:
 print('SD : '+sd_url.group(1))

# Search and print HD video url
hd_url = re.search('hd_src:"(.*?)",', html)
if hd_url is not None:
 print('HD : '+hd_url.group(1))

# Search and print audio url (Download video as audio)
audio_url = re.search('audio:..url:"(.*?)"', html)
if audio_url is not None:
 print('audio : '+audio_url.group(1))
 
# Search and print 144p video url (Without audio)
v_144 = re.search('144p.*?>.x3CBaseURL>(.*?).x3C/', html)
if v_144 is not None:
 print('144p : '+v_144.group(1).replace("&amp;","&"))

# Search and print 240p video url (Without audio)
v_240 = re.search('240p.*?>.x3CBaseURL>(.*?).x3C/', html)
if v_240 is not None:
 print('240p : '+v_240.group(1).replace("&amp;","&"))
 
# Search and print 360p video url (Without audio)
v_360 = re.search('360p.*?>.x3CBaseURL>(.*?).x3C/', html)
if v_360 is not None:
 print('360p : '+v_360.group(1).replace("&amp;","&"))

# Search and print 480p video url (Without audio)
v_480 = re.search('480p.*?>.x3CBaseURL>(.*?).x3C/', html)
if v_480 is not None:
 print('480p : '+v_480.group(1).replace("&amp;","&"))

# Search and print 720p video url (Without audio)
v_720 = re.search('720p.*?>.x3CBaseURL>(.*?).x3C/', html)
if v_720 is not None:
 print('720p : '+v_720.group(1).replace("&amp;","&"))

# Search and print 1080p video url (Without audio)
v_1080 = re.search('1080p.*?>.x3CBaseURL>(.*?).x3C/', html)
if v_1080 is not None:
 print('1080p : '+v_1080.group(1).replace("&amp;","&"))

# Hope this code is useful and clear
