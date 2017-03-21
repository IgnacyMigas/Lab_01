#!/usr/bin/pyhon2.7.9

from validate import *

class LogParser:
	def __init__ (self, string_to_be_found, *input_file):
		self.file = input_file
		self.string = string_to_be_found
	
	def parse_log (self, string_to_be_found, input_file):
		with open(input_file) as pl:
			for line in pl.readlines():
				if (string_to_be_found in line):
					print(line)
	
	def parse (self):
		for pl in self.file:
			validator = InputFileValidator(pl)
			validator.validate()
			self.parse_log(self.string, pl)

def main():
	print("Log parser")
	string = "PrChecker.Downs"
	parser = LogParser(string, "baseline_BdJPsiKs_MagD.log", "DR_BdJPsiKs_MagD_1k.log", "DR_NE_BdJPsiKs_MagD.log", "DR_NE_BdJPsiKs_MagD_1k.log", "test")
	parser.parse()

if __name__ == "__main__":
	main()
