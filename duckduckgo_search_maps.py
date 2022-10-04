#Remember to install the library before running the script (run code below in command line)
#pip install duckduckgo_search


from duckduckgo_search import ddg_maps

keywords = 'detective'
city ='New York'
radius=1
results = ddg_maps(keywords, city, radius)

print(results)
