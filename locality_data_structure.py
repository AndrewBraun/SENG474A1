# Andrew Braun and Himmat Singh Tiwana
# Consulted Stephen Scinocca and Austin Beauchamp

# This data structure holds the s hash tables needed for the locality algorithm.
# This corresponds to data structure D in the lecture notes.

from hash_table import *

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
			
			
	"""Gets a list of all questions that are similar to the given question."""
	def find_similar_questions(self, question):
	
		similar_questions = []
		
		for hash_table in self.hash_tables:
			retrieved_questions = hash_table.get_similar_questions(question)
						
			"""Remove duplicates and original question id."""
			for retrieved_question in retrieved_questions:
				if retrieved_question not in similar_questions and retrieved_question is not question:
					similar_questions.append(retrieved_question)
		
		return similar_questions