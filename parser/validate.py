import abc
import os
from exception import *

class abstractValidator(object):
	__metaclass__ = abc.ABCMeta
	@abc.abstractmethod
	def validate(self, to_be_validated):
		pass

class InputFileValidator(abstractValidator):
	def __init__ (self, to_be_validated):
		self.filename = to_be_validated
	
	def validate(self):
		if not self._is_string():
			raise NotAString()
		if not self._file_exist():
			raise NotSuchFile()
	
	def _is_string(self):
		return isinstance(self.filename, str)
	
	def _file_exist(self):
		return os.path.isfile(self.filename)
