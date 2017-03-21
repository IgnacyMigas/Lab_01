#!/usr/bin/pyhon2.7.9

class NotSuchFile(Exception):
	def __str__(self):
		return repr("Not found file")

class NotAString(Exception):
	def __str__(self):
		return repr("Argument is not a string")
