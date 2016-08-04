import urllib
import re
import socket
import Queue

initial_page = "file:///Users/madison/Desktop/simple-html/index.html"

htmlfile = urllib.urlopen(initial_page)
htmltext = htmlfile.read()
urls = re.findall(r'href=[\'"]?([^\'" >]+)', htmltext)
regex = '<a[^>]*>(.*?)</a>'
#regex = '<head>(.+?)</head>'
names_pattern = re.compile(regex)
names = re.findall(names_pattern, htmltext)
pairs = dict(zip(names, urls))
print pairs
#url_queue = Queue.Queue()
#seen = set()
#seen.insert(initial_page)
#url_queue.put(initial_page)
#while(True): 
#	if url_queue.size()>0:
#		urrent_url = url_queue.get()    
#		store(current_url)               
#		for next_url in extract_urls(current_url): 
#		seen.put(next_url)
#		url_queue.put(next_url)
#	else:
#		break

#urls = ["http://google.com", "http://nytimes.com", "http://CNN.com"]
#regex = '<title>(.+?)</title>'
#pattern = re.compile(regex)
#i = 0
#while i < len(urls):
#	htmlfile = urllib.urlopen(urls[i])
#	htmltext = htmlfile.read()
#	titles = re.findall(pattern, htmltext)
#	print titles
#	i+=1
