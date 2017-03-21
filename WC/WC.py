#!/usr/bin/pyhon2.7.9

class WordCounter:
	def __init__ (self, *input_file):
		self.file = input_file

	def countWord (self):
		count = 0
		for filename in self.file:
			with open(filename) as pl:
				count = len(pl.read().split())
			print("In "+filename+" are "+str(count)+" words")

WC = WordCounter("test.txt", "baseline_BdJPsiKs_MagD.log", "DR_BdJPsiKs_MagD_1k.log", "DR_NE_BdJPsiKs_MagD.log", "DR_NE_BdJPsiKs_MagD_1k.log")
WC.countWord()
