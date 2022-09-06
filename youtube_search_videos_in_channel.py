#Don't forget install package before start (launch next line in command line before first start).   
#pip3 install youtube-search-python

#Import packages for channel search and json formatting
from youtubesearchpython import ChannelSearch
import json


#Start search in channel by keyword in ID (copy it from link to the YouTube video)
search = ChannelSearch("osint", "UCMBPtmmDDhzy3nndMd2pJBA")

#Print results
print(json.dumps(search.result(),indent=4))
