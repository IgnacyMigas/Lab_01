#!/usr/bin/pyhon2.7.9

import unittest
import math

from WC import WordCounter
from exception import *

class WordCounter_test(unittest.TestCase):
	def test_with_no_file(self):
		filename = "test.dat"
		wc = WordCounter(filename)
		self.assertRaises(NotSuchFile, wc.countWord)
	
	def test_division_by_zero(self):
		filename = 1.3
		wc = WordCounter(filename)
		self.assertRaises(NotAString, wc.countWord)

if __name__ == "__main__":
	unittest.main()
