import sys

# Class that represents a question. Has a question ID and a set of words.
class Question():
	
	def __init__(self):
		self.question_id = None
		self.words = None
		
	def __init__(self, question_id):
		self.question_id = question_id
		self.words = None
	
	def __init__(self, question_id, words):
		self.question_id = question_id
		self.words = words
		
	def set_question_id(self, question_id):
		self.question_id = question_id
		
	def get_question_id(self):
		return self.question_id
		
	def set_words(self, words):
		self.words = words
		
	def get_words(self):
		return self.words

# Dictionary that holds the similarities of all questions. The key is a question ID, and the value is the list of similar question IDs.
class SimilarityTable():

	dict = {}
		
	"""Add a question ID to the similarity table."""
	def add_question_id(self, question_id):
		self.dict[question_id] = []
	
	"""Adds each question ID as similar to each other."""
	def add_similar_item(self, question_id1, question_id2):
		if question_id2 not in self.dict[question_id1]:
			self.dict[question_id1].append(question_id2)
			
		if question_id1 not in self.dict[question_id2]:
			self.dict[question_id2].append(question_id1)
		
	"""Removes each question ID from the similarity table."""
	def remove_similar_item(self, question_id1, question_id2):
		if question_id2 in self.dict[question_id1]:
			self.dict[question_id1].remove(question_id2)
			
		if question_id1 in self.dict[question_id2]:
			self.dict[question_id2].remove(question_id1)
		
	"""Gets the question IDs similar to the incoming question."""
	def get_similar_question_ids(self, question_id):
		return self.dict[question_id]
	
	"""Converts a question ID in the similarity table to a TSV string."""
	def get_entry_as_string(self, question_id):
		return str(question_id) + "	" + ",".join(self.get_similar_question_ids(question_id))

#Reads the input file and puts all the questions into a list
def read_input_file():

	# If no file is specified, this program quits.
	if len(sys.argv) < 2:
		print("Error: no file specified.")
		sys.exit();
		
	try:
		input_file = open(sys.argv[1], encoding='utf8')
	except Exception as e:
		print(str(e))
		sys.exit();
	
	questions = [line.rstrip('\n') for line in input_file]
	input_file.close()
	
	# Remove the header line from the questions
	del questions[0]
	
	# Convert the list of strings into Question objects
	for i in range(0, len(questions)):
	
		question_data = questions[i].strip().split('\t')
		
		# Only convert a string into a Question object if the string is valid.
		if len(question_data) >= 2:
			questions[i] = Question(question_data[0], set(question_data[1].split(' ')))
			
		else: questions[i] = None
	
	# If the question is not formatted properly, remove it
	questions = [question for question in questions if question is not None]
	
	return questions

def output_to_file(questions, similarity_table):
	with open("question_sim" + sys.argv[1][8:],"w") as output_file:
		output_file.write("qid	similar-qids\n")
		
		for question in questions:
			output_file.write(similarity_table.get_entry_as_string(question.get_question_id()) + "\n")
			
# Returns a float represent the Jaccard similarity
# based on the two given sets
def jaccard_similarity(a, b):

	intersect_length = len(set(a).intersection(b))
	union_length = len(set(a).union(b))
	
	if (union_length > 0):
		return float(intersect_length) / float(union_length)
	else:
		return 0.0