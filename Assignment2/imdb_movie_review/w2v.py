from __future__ import division
import nltk
import gensim
import sys
import numpy as np
import pickle

file_name = raw_input("Input the name file_name:       ")
model_to_use = raw_input('Please input weather to use self or "google" or "self" w2v:         ')

file = open(file_name, "rb")
print "_________________________imported file_____________________________"

lines_file = file.readlines()
print "____________________saved as one doc per line_______________________"

if model_to_use == "google":
	print "_____________________now loading google w2v_________________________"
	model = gensim.models.Word2Vec.load_word2vec_format('~/Desktop/GoogleNews-vectors-negative300.bin', binary=True)
	print "_____________________done loading word2vec__________________________"
	w2v_type = "google"
	dimensions_w2v = 300

if model_to_use == "self":
	print "________________now loading self-trained w2v_________________________"
	model = gensim.models.Word2Vec.load('imdb_model')
	print "_____________________done loading word2vec__________________________"
	w2v_type = "self"
	dimensions_w2v = 50

w2v_file = open("w2v_"+w2v_type+"/"+file_name+".w2v_"+w2v_type, "wb")
print "___________________created file for each w2v________________________"

for line in lines_file:
	current_doc_word_count = 0
	temp = np.zeros(dimensions_w2v)
	for word in line:
		# add the representaion of each word to the document
 		if word in model.vocab:
			temp = temp + model[word]
			current_doc_word_count = current_doc_word_count+1
	# average over all the words of the document
	temp = temp/current_doc_word_count
	pickle.dump(temp, w2v_file)

# accuracy: 0.587063 using google
# accuracy: 0.591527 using self