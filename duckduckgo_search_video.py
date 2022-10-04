#Remember to install the library before running the script (run code below in command line)
#pip install duckduckgo_search


from duckduckgo_search import ddg_videos

keywords = 'osint'
results = ddg_videos(keywords="osint", region='wt-wt', safesearch='Off', time=None, resolution=None,
               duration=None, license_videos=None, max_results=3, output=None)
print(*results, sep='\n')
