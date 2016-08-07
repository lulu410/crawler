import urllib
import re
import sys
import socket
import Queue

class BloomFilter(object):
	def __init__(self,capacity,errorRate):
		return None

	def __contains__(self,key):
		return "unimplemented"
	
	def add(self,key):
		return "unimplemented"

f = BloomFilter(capacity=10000, errorRate=0.001)

initial = raw_input("Please enter a initial web page\n") 
k = initial.rfind("/")
header = initial[:(k+1)]
print "header ", header, "\n"
initial_page = initial
seen = {}

def merge_lists(x, y):
	if x == None:
		copy = dict(x)
		copy.update(y)
		return copy
	else:
		return dict(x)

def extract_url(webpage, pairs):
	try:
		htmlfile = urllib.urlopen(webpage)
		htmltext = htmlfile.read()
		urls = re.findall(r'(?i)href=[\'"]?([^\'" >]+)', htmltext)
		regex = '<[\aA][^>]*>(.*?)</[\aA]>'
		names_pattern = re.compile(regex)
		names = re.findall(names_pattern, htmltext)
		return merge_lists(dict(zip(urls, names)).items(), pairs.items())
	except Exception:
		pass

links =  extract_url(initial_page, {})
while (len(links) > 0):
	key, value = links.popitem()
	if not (f.contains(key)):
		new_links = extract_url(header + key, links)
		links = merge_lists(links, new_links)
	f.add(key)
	print f
	
