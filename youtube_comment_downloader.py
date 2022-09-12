#Import module for work with iterators
from itertools import islice
#Import module for work with comments
from youtube_comment_downloader import *

#Create downloader object
downloader = YoutubeCommentDownloader()
# Download comments by link to YouTube video
comments = downloader.get_comments_from_url('https://www.youtube.com/watch?v=qwA6MmbeGNo&t=4300s', sort_by=SORT_BY_POPULAR)
# Print first 10 comments one by one
for comment in islice(comments, 10):
    print(comment)
