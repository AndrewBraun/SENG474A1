# This corresponds to hash function h in the lecture notes.

from fnv import *
import uuid

class MinHashFunction():

	hash_table = {}
	a = uuid.uuid4().int & (1<<64)-1
	b = uuid.uuid4().int & (1<<64)-1
	p = 15373875993579943603
	
		"""Maps a string to an integer and hashes it into the table."""
	def hash_string(self, string):
		string = string.encode('utf-8')
		x = hash(string, bits=64)
		hashcode = (self.a*x + self.b) % self.p
		print(hashcode)