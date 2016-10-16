import numpy as np
import pickle
import sys
import os
import shutil
from sklearn.decomposition import PCA

documents_to_use = 12499
dimensions_after_pca = 300
directory = raw_input("Input the name of directory to process: ")
dimensions_after_pca = int(raw_input("Input the dimension of the vectors after PCA: "))
use_pca = raw_input('If want to use PCA press "y"')
documents_to_use = int(raw_input("Input the no. of documents to use in each file: "))

os.chdir(directory)

print "current working directory: "
print os.getcwd()

file_train_neg = open("train_neg.txt."+directory, "rb")
file_train_pos = open("train_pos.txt."+directory, "rb")
file_test_neg = open("test_neg.txt."+directory, "rb")
file_test_pos = open("test_pos.txt."+directory, "rb")
print "________________________imported files_____________________________"

if os.path.exists("pca"):
	shutil.rmtree("pca")
os.makedirs("pca")

pca_file_train_neg = open("pca/train_neg.txt.pca", "wb")
pca_file_test_neg = open("pca/test_neg.txt.pca", "wb")
pca_file_test_pos = open("pca/test_pos.txt.pca", "wb")
pca_file_train_pos = open("pca/train_pos.txt.pca", "wb")
print "______________________created file for pca_________________________"

print "__________________________loading data train_pos_____________________________"
X = []
for i in range(0,documents_to_use):
	X.append(pickle.load(file_train_pos))
print "__________________________loading data train_neg_____________________________"
for i in range(0,documents_to_use):
	X.append(pickle.load(file_train_neg))
print "__________________________loading data test_pos_____________________________"
for i in range(0,documents_to_use):
	X.append(pickle.load(file_test_pos))
print "__________________________loading data test_neg_____________________________"
for i in range(0,documents_to_use):
	X.append(pickle.load(file_test_neg))
print "__________________________data loaded______________________________"

if use_pca == 'y':
	print "_____________________________fitting_______________________________"
	pca = PCA(n_components=dimensions_after_pca)
	pca.fit(X)
	print "___________________________transforming____________________________"
	X_new = pca.transform(X)
else:
	X_new = X

pickle.dump(X_new[0*documents_to_use:1*documents_to_use],pca_file_train_pos)
pickle.dump(X_new[1*documents_to_use:2*documents_to_use],pca_file_train_neg)
pickle.dump(X_new[2*documents_to_use:3*documents_to_use],pca_file_test_pos)
pickle.dump(X_new[3*documents_to_use:4*documents_to_use],pca_file_test_neg)