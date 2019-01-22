# This corresponds to Hash Table H in the lecture notes.
from minhash_function import *

class HashTable():
	
	hash_table = {}
	minhash_functions = []
	
	def __init__(self):
		for i in range(0, 6):
			minhash_functions.append(MinHashFunction())
	
	"""Hashes a question into the hash table."""
	def insert_question(self, question):
		minhash_signature = get_hash_signature(question)
		
		if !hash_table.has_key(minhash_signature):
			hash_table[minhash_signature] = []
		
		hash_table[minhash_signature].append(question.get_question_id())
		
	"""Gets a MinHash signature for a question."""
	def get_hash_signature(self, question):
		minhash_signature = ""
		
		for minhash_function in minhash_funcitons:
			minhash_signature.append(minhash_function.get_minhash(question))
			
		return minhash_signature
	
	"""Gets a list of similar question IDs, or an empty list if none are found."""
	def get_similar_question_ids(self, question):
		
		similar_question_ids = hash_table[get_hash_signature(question)]
		similar_question_ids.remove(question.get_question_id())
		
		return similar_question_ids