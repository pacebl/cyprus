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
import copy
import os

# Number of other results to give if the first found movie is incorrect
NUM_OTHER_RESULTS = 5

"""
Main class which handles user input and sanitization
"""
class Main:
    def __init__(self):
        self.argv = sys.argv
        self.config = config.Config()
        self.config.check_config()
        self.mov = None
    
    def read_input(self):
        if len(self.argv) != 2:
            print 'Only one argument is required:'
            print '     %s "movie filename"' % self.argv[0]
            sys.exit(2)
        elif not os.path.exists(sys.argv[1]):
            print 'File %s does not exist' % self.argv[1]
        else:
            self.mov = movie.Movie(sys.argv[1])
            print 'Looking up file %s...' % self.argv[1]
            print 'Search term: ' + self.mov.query + '\n'
            self.mov.lookup()
            self.mov.select_result(0)
            self.check_movie()

    def check_movie(self):
        if self.mov.results == []:
            print 'No movies found in search.'
            self.manual_search()
            return

        summary = self.mov.summarize()
        print summary + '\n'
        correct = raw_input('Is this movie correct? Y/N: ')
        if correct == 'Y' or correct == 'y':
            print 'Movie is correct. Copying to library...'
            self.mov.move_to_library()
        else:
            self.extended_search()

    def extended_search(self):
        print '\nPrinting other results: '
        if len(self.mov.results) >= NUM_OTHER_RESULTS:
            for i in range(0, NUM_OTHER_RESULTS):
                print i + 1, self.mov.results[i]
        else:
            for i in range(0, len(self.mov.results)):
                print i + 1, self.mov.results[i]
                
        while True:
            other_movie = raw_input('Correct movie (or N for none): ')
            
            if other_movie == 'n' or other_movie == 'N':
                self.manual_search()
                return
            try:
                other_movie = int(other_movie)
            except ValueError, e:
                print 'Whoops, that value seems to not be valid.'
                print e

            if other_movie > 0 and other_movie <= NUM_OTHER_RESULTS:
                print '\nPicking other movie.'
                self.mov.select_result(other_movie - 1)
                self.check_movie()
                return

    def manual_search(self):
        newquery = raw_input('Please provide new search term: ')
        print 'Searching for new movie %s: \n' % newquery
        self.mov.query = newquery
        self.mov.lookup()
        self.mov.select_result(0)
        self.check_movie()
