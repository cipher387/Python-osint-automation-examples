#Remember to install the library before running the script (run code below in command line)
#pip install duckduckgo_search

from duckduckgo_search import ddg

keywords = 'osint'
results = ddg(keywords, region='us-en', safesearch='Moderate', time='y', max_results=3)
print(*results, sep='\n')
