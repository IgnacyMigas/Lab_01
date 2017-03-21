#!/usr/bin/pyhon2.7.9

from validate import *
import logging

class WordCounter:
	def __init__ (self, *input_files):
		self.files = input_files
		fileLogName = 'wc.log'
		if os.path.exists(fileLogName):
			os.remove(fileLogName)
		logging.basicConfig(filename=fileLogName,level=logging.INFO)

	def countWord (self):
		words = 0
		lines = 0
		size = 0
		for filename in self.files:
			validator = InputFileValidator(filename)
			validator.validate()
			with open(filename) as pl:
				for line in pl.readlines():
					lines += 1
					words += len(line.split())
					size += len(line)
			logging.info("  %d  %d  %d  %s",lines, words, size, filename)

def main():
	WC = WordCounter("test.txt", "baseline_BdJPsiKs_MagD.log", "DR_BdJPsiKs_MagD_1k.log", "DR_NE_BdJPsiKs_MagD.log", "DR_NE_BdJPsiKs_MagD_1k.log")
	WC.countWord()

if __name__ == "__main__":
	main()
