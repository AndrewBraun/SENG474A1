# This data structure holds the s hash tables needed for the locality algorithm.
# This corresponds to data structure D in the lecture notes.

from hash_table import *

class LocalityDataStructure():

	hash_tables = {}

	def __init__(self):
		for i in range(0,14):
			self.hash_tables.append(HashTable())

	"""Hashes a question into every hash table."""
	def insert_question(self, question):
		for hash_table in self.hash_tables:
			hash_table.insert_question(question)
			
	"""Gets a list of all question IDs that are similar to the given question."""
	def find_similar_questions(self, question):
	
		similar_question_ids = []
		
		for hash_table in hash_tables:
			retrieved_question_ids = hash_table.get_similar_question_ids(question)
			
			for retrieved_question_id in retrieved_question_ids:
				if retrieved_question_id not in similar_question_ids:
					similar_question_ids.append(retrieved_question_id)
		
		return similar_question_ids