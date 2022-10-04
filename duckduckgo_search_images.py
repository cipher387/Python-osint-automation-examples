#Remember to install the library before running the script (run code below in command line)
#pip install duckduckgo_search


from duckduckgo_search import ddg_images


keywords = 'osint'
results = ddg_images(keywords, region='wt-wt', safesearch='Off', size=None,
               color='Monochrome', type_image=None, layout=None, license_image=None, max_results=3)
print(*results, sep='\n')
