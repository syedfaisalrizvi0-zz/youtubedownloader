import requests as re
from bs4 import BeautifulSoup
import youtube_dl
print('Engine start....')
qry  = str(input('Enter the Video name : '))
qry  = qry.replace(' ','+')
data ='https://www.youtube.com/results?search_query='+qry
html = re.get(data)
soup = BeautifulSoup(html.text,'html.parser')
yt_links = soup.find_all("a", class_ = "yt-uix-tile-link")
yt_href = yt_links[0].get("href")
href ='https://www.youtube.com'+yt_href
ydl_opts = {'format': 'bestaudio/best','noplaylist' : True,}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([href])
