from __future__ import division
import nltk
import gensim
import sys
import numpy as np
import pickle

if len(sys.argv) < 2:
	print "Please input file name"
	sys.exit(0)
if len(sys.argv) > 3:
	print "Too many arguments"
	sys.exit(0)

file_name = sys.argv[1]
print file_name

file = open(file_name, "rb")
print "_________________________imported file_____________________________"

lines_file = file.readlines()
print "____________________saved one doc per line__________________________"


w2v_file = open("w2v/"+file_name+".w2v", "wb")
print "___________________created file for each w2v________________________"

print "_____________________now loading google w2v_________________________"
model = gensim.models.Word2Vec.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)
print "_____________________done loading word2vec__________________________"

w2v_represenations = []
for line in lines_file:
	current_doc_word_count = 0
	temp = np.zeros(300)
	for word in line:
		# add the representaion of each word to the document
 		if word in model.vocab:
			temp = temp + model[word]
			current_doc_word_count = current_doc_word_count+1
	# average over all the words of the document
	temp = temp/current_doc_word_count
	w2v_represenations.append(temp)
# write this in file
pickle.dump(w2v_represenations, w2v_file)

# 		# To read:
# 		# with open(the_filename, 'rb') as file:
# 		# my_list = pickle.load(file)	