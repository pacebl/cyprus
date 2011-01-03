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

import sys
import movie
import config
import os
"""
Main class which handles user input sanitization
"""
class Main:
	def __init__(self):
		self.argv = sys.argv
		self.config = config.Config()
		self.config.check_config()
	
	def read_input(self):
		if len(self.argv) != 2:
			print 'Only one argument is required:'
			print '     %s "movie filename"' % self.argv[0]
			sys.exit(2)
		elif not os.path.exists(sys.argv[1]):
			print 'File %s does not exist' % self.argv[1]
		else:
			mov = movie.Movie(sys.argv[1])
			print "Looking up movie %s" % sys.argv[1]
			mov.lookup()
			mov.print_metadata()
			mov.move_to_library()
			#mov.summarize()
