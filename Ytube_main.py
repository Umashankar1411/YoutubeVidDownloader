from pytube import *

url="https://www.youtube.com/watch?v=lQzC4eouzFk"
path_to_save_video="C:\\Users\\HP\\Desktop"
#creating youtube object with url
ob=YouTube(url)
strms=ob.streams.all()
for s in strms:
    print(s)

#strm=ob.streams.first()
##print(strm)
#print(strm.filesize)
#print(strm.title)