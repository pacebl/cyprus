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
import progbar
import os

class CopyProgress:
	def __init__(self, src, dest, buffersize=1024*1024, **kwargs):
		self.length = 77
		self.src = src
		self.dest = dest
		self.buffersize = buffersize
		self.limit = os.path.getsize(self.src) / buffersize
		self.prog = progbar.ProgressBar(0, self.limit, self.length, **kwargs)
	
	def copy(self):
		if not hasattr(self.src, 'read'):
			self.src = open(self.src, 'rb')
		if not hasattr(self.dest, 'write'):
			self.dest = open(self.dest, 'wb')

		oldprog = str(self.prog)
		for i in xrange(self.limit + 1):
			copy_buffer = self.src.read(self.buffersize)
			if copy_buffer:
				self.dest.write(copy_buffer)
			self.prog.increment_amount()
			if oldprog != str(self.prog):
				print self.prog, '\r',
				sys.stdout.flush()
				oldprog = str(self.prog)
		print '\n'
