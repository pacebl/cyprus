import unittest

from cypruslib import config_test, movie_test

tl = unittest.TestLoader()

movietests = tl.loadTestsFromTestCase(movie_test.MovieTest)
configtests = tl.loadTestsFromTestCase(config_test.ConfigTest)

tests = [movietests, configtests]

suite = unittest.TestSuite()
suite.addTests(tests)

unittest.TextTestRunner(verbosity=2).run(suite)
