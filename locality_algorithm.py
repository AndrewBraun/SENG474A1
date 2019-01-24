# Andrew Braun and Himmat Singh Tiwana
# Consulted Stephen Scinocca and Austin Beauchamp

# This is the locality sensitive hashing algorithm for calculating similarity

from locality_data_structure import *
from common_code import *

def main():

	questions = read_input_file()
		
	similarity_table = SimilarityTable()
	
	# Adding every question ID to similarity table
	for question in questions:
		similarity_table.add_question_id(question.get_question_id())
	
	locality_data_structure = LocalityDataStructure()
	
	for question in questions:
		locality_data_structure.insert_question(question)
	
	for question in questions:
	
		#Get all similar question IDs from all hash tables
		similar_question_ids = locality_data_structure.find_similar_questions(question)
		
		for similar_question_id in similar_question_ids:
			
			# Get a question object by its question ID
			question2 = next(question for question in questions if question.get_question_id() == similar_question_id)
			
			# Only add question IDs that have a verified Jaccard similarity (no false positives)
			
			if jaccard_similarity(question.get_words(), question2.get_words()) >= 0.6:
			
				similarity_table.add_similar_item(question.get_question_id(), similar_question_id)
		
	output_to_file(questions, similarity_table)

if __name__ == '__main__':
	main()