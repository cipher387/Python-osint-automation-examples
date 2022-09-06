#Don't forget install package before start (launch next line in command line before first start).    
#pip3 install youtube-search-python


#Import package for YouTube search
from youtubesearchpython import VideosSearch
#Import package for JSON formatting
import json


#Start search (in limit specify the desired number of results)
videosSearch = VideosSearch('osint', limit = 1)


#Print results (with json formatting)
print(json.dumps(videosSearch.result(), indent=4))
