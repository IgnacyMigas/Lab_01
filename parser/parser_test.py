#!/usr/bin/pyhon2.7.9

import unittest

from parser import LogParser
from exception import *

class LogParser_test(unittest.TestCase):
	def test_with_no_file(self):
		filename = "test.dat"
		string = "PrChecker.Downs"
		parser = LogParser(string, filename)
		self.assertRaises(NotSuchFile, parser.parse)
	
	def test_division_by_zero(self):
		filename = 1.3
		string = "PrChecker.Downs"
		parser = LogParser(string, filename)
		self.assertRaises(NotAString, parser.parse)

if __name__ == "__main__":
	unittest.main()
