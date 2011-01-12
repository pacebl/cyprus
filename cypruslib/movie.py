# This file is part of Cyprus.
#
# Cyprus is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Cyprus is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Cyprus.  If not, see <http://www.gnu.org/licenses/>.

import os
import sys
import config
import urllib
import copy

try:
	import imdb
except:
	print 'You must install the IMDbPY package.'
	sys.exit(1)

"""
Movie class, holds file information and metadata, is responsible for
low level moving and writing metadata
"""
class Movie:
	def __init__(self, fullpath):
		self.fullpath = fullpath
		(self.path, self.filename) = os.path.split(fullpath)
		self.splitname = self.filename.split('.')
		self.query = self.splitname[0]
		self.config = config.Config()
		self.imdb = imdb.IMDb()
		self.result = None
		self.search_results = None
		self.title = None
	
	def lookup(self):
		try:
			self.search_results = self.imdb.search_movie(self.query)
		except imdb.IMDbError, e:
			print "Probably no connection to the internet. Full error follows:"
			print e
			sys.exit(3)
		
		if not self.search_results == []:
			self.result = self.search_results[0]
			self.imdb.update(self.result)
			self.title = self.result['long imdb canonical title']
	
	def get_searchterm(self):
		return self.splitname[0]
	
	def get_other_results(self, values):
		if len(self.search_results) >= values:
			for i in range(values):
				print (i + 1), self.search_results[i]
		else:
			for i in range(0, len(self.search_results)):
				print (i + 1), self.search_results[i]

	def select_other_result(self, value):
		self.result = self.search_results[value - 1]
		self.imdb.update(self.result)
		self.title = self.result['long imdb canonical title']
	
	def set_query(self, newquery):
		self.query = newquery

	def move_to_library(self):
		path = self.config.get_librarydir() + '/' + self.title
		if not os.path.exists(path):
			os.makedirs(path)
		filename = path + '/' + self.title + '.' + self.splitname[-1]

		copier = copy.CopyProgress(self.fullpath, filename, mode='fixed')
		copier.copy()

		coverurl = self.result['full-size cover url']
		urllib.urlretrieve(coverurl, path + '/' + self.title + '.tbn')
	
	def print_metadata(self):
		print "Title: ", self.title
		print "Filetype: ", self.splitname[-1]
		print self.config.get_librarydir()

	def summarize(self):
		return self.result.summary()
