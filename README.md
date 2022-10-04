# Python OSINT automation examples
In this repository, I will collect quick and simple code examples that use Python to automate various #osint tasks.



## [](#table-of-contents) Table of contents
- [How to run this scripts?](#how-to-run-this-scripts) 
     - [Variant #1](#variant-1) 
     - [Variant #2](#variant-2) 
     - [Variant #3](#variant-3) 
- [Packages using examples from my Twitter account](#packages-using-examples-from-my-twitter-account-cyb_detective)
     - [YouTubeSearch](#youtubesearch-httpspypiorgprojectyoutube-search-python) 
     - [YouTube Comments Downloader](#-youtube-comment-downloader-httpspypiorgprojectyoutube-comment-downloader) 
     - [Whois](#whois-httpspypiorgprojectpython-whois)
     - [DuckDuckGo search](#duckduckgo) 
- [HINTS](#hints)

## [](#how-to-run-this-scripts)How to run this scripts?



![image](https://github.com/cipher387/Python-osint-automation-examples/blob/main/images/run_python_script.png)

Copy file to your computer/server/online IDE and run in command line:

python filename.py

For example:

python youtube_video_search.py



If you haven't used Python before, you have several ways to get started:

###  [](#variant1)Variant 1

![image](https://github.com/cipher387/Python-osint-automation-examples/blob/main/images/real_python.png)

Install Python in your computer using this instruction https://realpython.com/installing-python/


###  [](#variant2)Variant 2

![image](https://github.com/cipher387/Python-osint-automation-examples/blob/main/images/gitpod.png)

Open this repository in Gitpod https://gitpod.io#https://github.com/cipher387/Python-osint-automation-examples

(To run it for the first time, you need to log in to your Github, Gitlab, or Bitbucket account)


###  [](#variant3)Variant 3

![image](https://github.com/cipher387/Python-osint-automation-examples/blob/main/images/tsurigi.png)


Install a Linux VM with Python preinstalled.

If you are doing OSINT, I recommend you start with Tsurugi Acquire https://archive.org/download/tsurugi_acquire_2021.1/tsurugi_acquire_2021.1.iso

For launch VM in Windows and old MacBooks you may use Virtual Box https://www.virtualbox.org

For new MacBooks with M1 — UTM https://mac.getutm.app

(if your computer has modest technical resources, you can specify in the VM settings for Tsurugi Linux Acquire 2-4 GB of RAM, but run it only in text mode)


##  [](#usingexamples)Packages using examples from my Twitter account [@cyb_detective](https://twitter.com/cyb_detective)


### [](#youtubesearch)YouTubeSearch (https://pypi.org/project/youtube-search-python/)


Twitter thread:

https://twitter.com/cyb_detective/status/1567170268937723905


Source code files (example of results in the pictures):

![image](https://github.com/cipher387/Python-osint-automation-examples/blob/main/images/youtube_search.jpeg)

https://github.com/cipher387/Python-osint-automation-examples/blob/main/youtube_video_search.py

![image](https://github.com/cipher387/Python-osint-automation-examples/blob/main/images/youtube_search_2.jpeg)

https://github.com/cipher387/Python-osint-automation-examples/blob/main/youtube_channel_search.py

![image](https://github.com/cipher387/Python-osint-automation-examples/blob/main/images/youtube_search_3.jpeg)

https://github.com/cipher387/Python-osint-automation-examples/blob/main/youtube_search_videos_in_channel.py


### [](#youtubecommentsdownloader) YouTube Comment Downloader (https://pypi.org/project/youtube-comment-downloader/)


Twitter thread:

https://twitter.com/cyb_detective/status/1569147434248376321

Source code files (example of results in the pictures):


![image](https://github.com/cipher387/Python-osint-automation-examples/blob/main/images/youtube_comment_downloader.png)

https://github.com/cipher387/Python-osint-automation-examples/blob/main/youtube_comment_downloader.py


### [](#whois)WHOIS https://pypi.org/project/python-whois/

Twitter thread:

https://twitter.com/cyb_detective/status/1569500433827385344


Source code files (example of results in the pictures):


![image](https://github.com/cipher387/Python-osint-automation-examples/blob/main/images/whois_python.png)


https://github.com/cipher387/Python-osint-automation-examples/blob/main/whois.py


### [](#duckduckgo)DuckDuckGo search https://pypi.org/project/duckduckgo-search/

Twitter thread:

Source code files (example of results in the pictures):


## [](#hints)HINTS


### Saving results to .txt file

If you want to save the results to a text file, add "filename.txt" after the command to run the script

(view pic)

![image](https://github.com/cipher387/Python-osint-automation-examples/blob/main/images/results_to_file.png)

