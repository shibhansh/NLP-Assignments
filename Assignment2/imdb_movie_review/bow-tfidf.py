import numpy as np
import pickle
import sys
import os
import shutil
from sklearn.decomposition import PCA
from sklearn.feature_extraction.text import TfidfVectorizer

file_train_neg = open("train_neg.txt", "rb")
file_train_pos = open("train_pos.txt", "rb")
file_test_pos = open("test_pos.txt", "rb")
file_test_neg = open("test_neg.txt", "rb")

print "_________________files Opened______________________"

documents_to_use = 500
#store the docs in a list
document_train_neg = file_train_neg.readlines()[0:documents_to_use]
document_train_pos = file_train_pos.readlines()[0:documents_to_use]
document_test_neg = file_test_neg.readlines()[0:documents_to_use]
document_test_pos = file_test_pos.readlines()[0:documents_to_use]

print "__________________files read______________________"

#removing the extra newline character in every dcoument and word
document_train_neg = [x[:-1] for x in document_train_neg]
document_train_pos = [x[:-1] for x in document_train_pos]
document_test_neg = [x[:-1] for x in document_test_neg]
document_test_pos = [x[:-1] for x in document_test_pos]

document = document_train_neg + document_train_pos + document_test_neg + document_test_pos

vocabulary = open("imdb.vocab", "rb")
vocab = vocabulary.readlines()
vocab = [x[:-1] for x in vocab]
vocab = vocab[0:30000]

print "_______________converting to tf-idf_______________"

vect = TfidfVectorizer(sublinear_tf=True, max_df=0.5, analyzer='word', stop_words='english', vocabulary=vocab)
document_tf_idf = vect.fit_transform(document)
document_tf_idf = document_tf_idf.toarray()

print "_________________saving in files_________________"

file_train_neg_bow = open("BoW/"+file_train_neg.name+".BoW", "wb") 
file_train_pos_bow = open("BoW/"+file_train_pos.name+".BoW", "wb")
file_test_neg_bow = open("BoW/"+file_test_neg.name+".BoW", "wb")
file_test_pos_bow = open("BoW/"+file_test_pos.name+".BoW", "wb")

for i in range(0,documents_to_use):
	pickle.dump(document_tf_idf[0*documents_to_use+i],file_train_neg_bow)
	print i
print "________________saved neg training data_____________"

for i in range(0,documents_to_use):
	pickle.dump(document_tf_idf[documents_to_use+i],file_train_pos_bow)
	print i
print "________________saved pos training data_____________"

for i in range(0,documents_to_use):
	pickle.dump(document_tf_idf[2*documents_to_use+i],file_test_neg_bow)
	print i
print "________________saved neg testing data_____________"

for i in range(0,documents_to_use):
	pickle.dump(document_tf_idf[3*documents_to_use+i],file_test_pos_bow)
	print i
print "________________saved pos testing data_____________"	

# accuracy: 0.872150