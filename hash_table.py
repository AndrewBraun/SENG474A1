# Andrew Braun and Himmat Singh Tiwana
# Consulted Stephen Scinocca and Austin Beauchamp

# This corresponds to Hash Table H in the lecture notes.
from minhash_function import *

class HashTable():
	
	def __init__(self):
	
		self.hash_table = {}
		self.minhash_signature_hash_table = {}
		self.minhash_functions = []
	
		for i in range(0, 6):
			self.minhash_functions.append(MinHashFunction())
	
	"""Hashes a question into the hash table."""
	def insert_question(self, question):
		minhash_signature = self.get_hash_signature(question)
		
		if not minhash_signature in self.hash_table:
			self.hash_table[minhash_signature] = []
		
		self.hash_table[minhash_signature].append(question)
		
	"""Gets a MinHash signature for a question."""
	def get_hash_signature(self, question):
		minhash_signature = ""
		question_id = question.get_question_id()
		
		if question_id in self.minhash_signature_hash_table:
			minhash_signature = self.minhash_signature_hash_table[question_id]
		
		else:
			for minhash_function in self.minhash_functions:
				minhash_signature += str(minhash_function.get_minhash(question)) + ","
			self.minhash_signature_hash_table[question_id] = minhash_signature
			
		return minhash_signature
	
	"""Gets a list of similar questions, or an empty list if none are found."""
	def get_similar_questions(self, question):
		
		return self.hash_table[self.get_hash_signature(question)]