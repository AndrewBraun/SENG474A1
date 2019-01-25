# Andrew Braun and Himmat Singh Tiwana
# Consulted Stephen Scinocca and Austin Beauchamp

# This is the locality sensitive hashing algorithm for calculating similarity

from locality_data_structure import *
from common_code import *
import time

def main():

	questions = read_input_file()
		
	similarity_table = SimilarityTable()
	
	# Adding every question ID to similarity table
	for question in questions:
		similarity_table.add_question_id(question.get_question_id())
	
	locality_data_structure = LocalityDataStructure()
	
	locality_data_structure.insert_questions(questions)
	
	for question in questions:
	
		question_id = question.get_question_id()
		#Get all similar questions from all hash tables
		similar_questions = locality_data_structure.find_similar_questions(question)
		
		for similar_question in similar_questions:
			
			# Get a question object by its question ID
			
			# Only add question IDs that have a verified Jaccard similarity (no false positives)
			similar_question_id = similar_question.get_question_id()
			
			if similar_question_id not in similarity_table.get_similar_question_ids(question_id) and jaccard_similarity(question.get_words(), similar_question.get_words()) >= 0.6:
			
				similarity_table.add_similar_item(question_id, similar_question_id)
		
	output_to_file(questions, similarity_table)

if __name__ == '__main__':
	main()