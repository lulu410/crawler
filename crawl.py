import urllib
import re
import socket
import Queue

header = "file:///Users/madison/Desktop/simple-html/"
initial_page = header + "index.html"
seen = {}

def merge_lists(x, y):
	copy = dict(x)
	copy.update(y)
	return copy

def extract_url(webpage, pairs):
	htmlfile = urllib.urlopen(webpage)
	htmltext = htmlfile.read()
	urls = re.findall(r'href=[\'"]?([^\'" >]+)', htmltext)
	regex = '<a[^>]*>(.*?)</a>'
	names_pattern = re.compile(regex)
	names = re.findall(names_pattern, htmltext)
	return merge_lists(dict(zip(urls, names)).items(), pairs.items())

links =  extract_url(initial_page, {})
while (len(links) > 0):
	key, value = links.popitem()
	if not (key in seen):
		new_links = extract_url(header + key, links)
		links = merge_lists(links, new_links)
	seen[key] = value
	print seen
	
