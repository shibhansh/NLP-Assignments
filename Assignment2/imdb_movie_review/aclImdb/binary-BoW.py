from __future__ import division
import nltk
# import gensim
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

#store the docs in a list
document = file.readlines()
#removing the extra newline character in every dcoument and word
document = [x[:-1] for x in document]

vocabulary = open("imdb.vocab", "rb")
vocab = vocabulary.readlines()
vocab = [x[:-1] for x in vocab]

stop_words = vocab[0:100]
# for doc in document:
# 	for word in doc:
# 		if word.lower() not in stop_words:

count = 0

bBoW_file = open("bBoW/"+file_name+".bBoW", "wb")

number_of_documents = len(document)
#creating vector representations for documents
for doc in document:
	document[count] = nltk.word_tokenize(doc)
	doc = document[count]
	print("Documents Processed %d, remaining %d" % (count, number_of_documents-count))
	count = count + 1
	current_BoW = [0]*30000
	for word in doc:
		if word in stop_words:
			continue
		key_location = 0
		for key in vocab:
			if key == word:
				current_BoW[key_location] = 1
				break
			key_location = key_location + 1
			if key_location >= 30000:
				break
	pickle.dump(current_BoW, bBoW_file)

# accuracy: 0.861709