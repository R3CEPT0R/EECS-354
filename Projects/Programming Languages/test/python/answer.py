#!/usr/bin/python

'''
Python is a language with many great strengths.  Perhaps the only one that really matters in this class is it's extensive standard library, which can be used as something of a swiss army knife.  This means that python scripts can do a lot of heavy lifting in very few lines of code.

Subclass the provided class (Downloadable) with a class named "Downloader" whose constructor takes, in addition to any other arguments, an argument called hash representing the MD5 hash of the content at Downloadable's url.  Downloader should have at least the following functions:
* download : Retrieves the contents of Downloadable's url and stores them internally. (Don't worry about error handling)
* hash     : Returns the md5 hash (as a string of a hexadecimal number) of the downloaded content (for comparison with the hash passed to Downloader's constructor).
* encode   : Returns the content encoded in base 64.
* isValid  : Returns true if the the hash of the internal content matches the hash passed to the constructor.
'''

class Downloadable:
	def __init__(self, url):
		self.url = url
