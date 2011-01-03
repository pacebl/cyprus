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

import ConfigParser
import os

"""
Config module, reads from ~/.cyprus/config or creates a basic config if one
does not exist.
"""
class Config:
	def __init__(self):
		configfile = '~/.cyprus/config'
		self.configfile = os.path.expanduser(configfile)
		self.config = ConfigParser.ConfigParser()
		(self.path, self.filename) = os.path.split(self.configfile)

	"""
	Make sure configuration file and directory exists, reads library location
	and creates library directories if they do not exist. Must be called once
	before accessing configuration
	"""
	def check_config(self):
		if not os.path.exists(self.path):
			os.makedirs(self.path)
		if not os.path.exists(self.configfile):
			self.config.add_section('basic')
			self.config.set('basic', 'library', '~/CyprusLib')
			configsocket = open(self.configfile, 'wb')
			self.config.write(configsocket)

		self.config.read(self.configfile)

		# Make sure whatever library directory is specified exists
		librarydir = os.path.expanduser(self.config.get('basic', 'library'))
		if not os.path.exists(librarydir):
			os.makedirs(librarydir)

	"""
	Returns location of library directory
	"""
	def get_librarydir(self):
		self.config.read(self.configfile)
		return os.path.expanduser(self.config.get('basic', 'library'))
