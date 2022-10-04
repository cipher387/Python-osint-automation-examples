#Remember to install the library before running the script (run code below in command line)
#pip install duckduckgo_search



from duckduckgo_search import ddg_news

keywords = "osint"
results = ddg_news(keywords, region='wt-wt', safesearch='Off', time='d', max_results=3)

print(*results, sep='\n')
