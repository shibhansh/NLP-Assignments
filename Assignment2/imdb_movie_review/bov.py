from __future__ import division
import nltk
import numpy as np
import pickle
import sys
import os
import shutil
import gensim

file_train_neg = open("train_neg.txt", "rb")
file_train_pos = open("train_pos.txt", "rb")
file_test_pos = open("test_pos.txt", "rb")
file_test_neg = open("test_neg.txt", "rb")

print "_________________files Opened______________________"

number_of_documents = 10
vocab_size = 30000
number_of_documents = int(raw_input("Input the no. of documents to use in each file (default is 250): "))
#store the docs in a list
document_train_neg = file_train_neg.readlines()[0:number_of_documents]
document_train_pos = file_train_pos.readlines()[0:number_of_documents]
document_test_neg = file_test_neg.readlines()[0:number_of_documents]
document_test_pos = file_test_pos.readlines()[0:number_of_documents]

print "__________________files read______________________"
#removing the extra newline character in every dcoument and word
document_train_neg = [x[:-1] for x in document_train_neg]
document_train_pos = [x[:-1] for x in document_train_pos]
document_test_neg = [x[:-1] for x in document_test_neg]
document_test_pos = [x[:-1] for x in document_test_pos]

corpus = document_train_neg + document_train_pos + document_test_neg + document_test_pos

vocabulary = open("imdb.vocab", "rb")
vocab = vocabulary.readlines()
vocab = [x[:-1] for x in vocab]
vocab = vocab[0:vocab_size]

print "________________now loading self-trained w2v_________________________"
model = gensim.models.Word2Vec.load('imdb_model')
print "_____________________done loading word2vec__________________________"

#making files to save data in
file_train_neg_bov = open("BoV/"+file_train_neg.name+".BoV", "wb") 
file_train_pos_bov = open("BoV/"+file_train_pos.name+".BoV", "wb")
file_test_neg_bov = open("BoV/"+file_test_neg.name+".BoV", "wb")
file_test_pos_bov = open("BoV/"+file_test_pos.name+".BoV", "wb")

files = [file_train_neg_bov, file_train_pos_bov, file_test_neg_bov, file_test_pos_bov]
current_file_number = 0
keys_found = 0
documents_processed = 0
for file in files:
	for doc in corpus[ current_file_number*number_of_documents : (current_file_number+1)*number_of_documents]:
		print "here"
		temp = doc
		# print temp
		doc = nltk.word_tokenize(temp)
		print("Documents Processed %d, remaining %d" % (documents_processed, 4*number_of_documents-documents_processed))
		documents_processed = documents_processed + 1
		current_BoV = [0]*(vocab_size*50)
		for word in doc:
			key_location = 0
			for key in vocab:
				if key == word:
					if word in model.vocab:
						current_BoV[key_location*50:(key_location+1)*50] = model[word]
						keys_found +=1
					break
				key_location = key_location + 1
				if key_location >= vocab_size:
					break
		pickle.dump(current_BoV, file)
	current_file_number += 1