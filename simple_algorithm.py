# Andrew Braun
# V00851919

# This is the simple algorithm for finding similarity.
from common_code import *

def main():
	questions = read_input_file()
		
	similarity_table = SimilarityTable()
	
	# Adding every question ID to similarity table
	for question in questions:
		similarity_table.add_question_id(question.get_question_id())
		
	for i in range(0, len(questions)):
	
		question1 = questions[i]
	
		for j in range(i+1, len(questions)):
		
			question2 = questions[j]
			
			similarity = jaccard_similarity(question1.get_words(), question2.get_words())
				
			if (similarity >= 0.6):
				similarity_table.add_similar_item(question1.get_question_id(), question2.get_question_id())
					
	output_to_file(questions, similarity_table)

if __name__ == '__main__':
	main()