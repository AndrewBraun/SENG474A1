import uuid
from fnv import *

class HashTable():

	dict = {}
	a = uuid.uuid4().int & (1<<64)-1
	b = uuid.uuid4().int & (1<<64)-1
	p = 15373875993579943603
	
	"""Hashes a question into the hash table."""
	def insert_question(self, question):
		minhash_signature = get_hash_signature(question)
		
		if !dict.has_key(minhash_signature):
			dict[minhash_signature] = []
		
		dict[minhash_signature].append(question.get_question_id())
	
	"""Maps a string to an integer and hashes it into the table."""
	def hash_string(self, string):
		string = string.encode('utf-8')
		x = hash(string, bits=64)
		hashcode = (self.a*x + self.b) % self.p
		print(hashcode)
		
	"""Gets a MinHash signature for a question."""
	def get_hash_signature(self, question):
		minhash_signature = []
		# TODO: implement hashing stuff
		return minhash_signature
	
	"""Gets a list of similar question IDs, or an empty list if none are found."""
	def get_similar_question_ids(self, question):
		
		similar_question_ids = dict[get_hash_signature(question)]
		similar_question_ids.remove(question.get_question_id())
		
		return similar_question_ids