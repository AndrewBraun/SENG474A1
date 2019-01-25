# Andrew Braun and Himmat Singh Tiwana
# Consulted Stephen Scinocca and Austin Beauchamp

# This data structure holds the s hash tables needed for the locality algorithm.
# This corresponds to data structure D in the lecture notes.

from hash_table import *
import time

class LocalityDataStructure():

	hash_tables = []

	def __init__(self):
		for i in range(0,14):
			self.hash_tables.append(HashTable())

	"""Insert every question into the hash tables."""
	def insert_questions(self, questions):
		for hash_table in self.hash_tables:
			for question in questions:
				hash_table.insert_question(question)
			
			
	"""Gets a list of all question IDs that are similar to the given question."""
	def find_similar_questions(self, question):
	
		similar_question_ids = []
		
		for hash_table in self.hash_tables:
			retrieved_question_ids = hash_table.get_similar_question_ids(question)
						
			"""Remove duplicates and original question id."""
			for retrieved_question_id in retrieved_question_ids:
				if retrieved_question_id not in similar_question_ids and retrieved_question_id is not question.get_question_id():
					similar_question_ids.append(retrieved_question_id)
		
		return similar_question_ids