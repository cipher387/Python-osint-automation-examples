#Remember to install the library before running the script (run code below in command line)
#pip install duckduckgo_search


from duckduckgo_search import ddg_translate

keywords = "Hello, friends!"
results = ddg_translate(keywords, to='fr')


print(results)
