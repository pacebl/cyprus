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

import unittest

import movie

class TestMovie(unittest.TestCase):
    def setUp(self):
        self.mov = movie.Movie("Inception.mkv")

    def test_lookup(self):
        self.mov.lookup()
        self.mov.select_result(0)
        self.assertEqual("Inception (2010)", self.mov.title)

    def test_select_result(self):
        print self.mov.title
        self.mov.lookup()
        length = len(self.mov.results)
        self.assertTrue(self.mov.select_result(length - 1))
        self.assertFalse(self.mov.select_result(length))

if __name__ == '__main__':
    unittest.main()
