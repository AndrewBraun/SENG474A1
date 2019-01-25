# Andrew Braun and Himmat Singh Tiwana
# Consulted Stephen Scinocca and Austin Beauchamp

# This corresponds to hash function h in the lecture notes.

import fnv
import uuid

class MinHashFunction():

	p = 15373875993579943603
	
	def __init__(self):
		self.dict = {}
		self.a = uuid.uuid4().int & (1<<64)-1
		self.b = uuid.uuid4().int & (1<<64)-1
	
	"""Takes as input a set of words and returns the smallest index of the words."""
	def get_minhash(self, question):
		index = None
		
		for word in question.get_words():
		
			word_index = self.get_index_of_word(word)
			if index is None or word_index < index:
				index = word_index
			
		return index
	
	"""Takes as input a word (string), converts it to an integer via FNV, and then converts the integer into a hash value."""
	def get_index_of_word(self, word):
		hash = None
		
		if (word in self.dict):
			hash = self.dict[word]
			
		else:
			hash_input_int = fnv.hash(word.encode('utf-8'), bits=64)
			hash = (self.a * hash_input_int + self.b) % self.p
			self.dict[word] = hash
			
		return hash