import numpy as np
import pickle
import sys
import os
import shutil
from sklearn.decomposition import PCA

vectors_to_load = 12499
new_dimensions = 300
directory = raw_input("Input the name of directory to process: ")
new_dimensions = int(raw_input("Input the dimension of the vectors after PCA: "))
vectors_to_load = int(raw_input("Input the no. of documents to use in each file: "))

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

print "__________________________loading data_____________________________"
X = []
for i in range(0,vectors_to_load):
	X.append(pickle.load(file_train_pos))
for i in range(0,vectors_to_load):
	X.append(pickle.load(file_train_neg))
for i in range(0,vectors_to_load):
	X.append(pickle.load(file_test_pos))
for i in range(0,vectors_to_load):
	X.append(pickle.load(file_test_neg))
print "__________________________data loaded______________________________"

print "_____________________________fitting_______________________________"
pca = PCA(n_components=new_dimensions)
pca.fit(X)

print "___________________________transforming____________________________"

# with open('my_dumped_classifier.pkl', 'wb') as fid:
# 	pickle.dump(pca, fid)

# with open('my_dumped_classifier.pkl', 'rb') as fid:
#     pca_loaded = pickle.load(fid)

X_new = pca.transform(X)
pickle.dump(X_new[0*vectors_to_load:1*vectors_to_load],pca_file_train_pos)
pickle.dump(X_new[1*vectors_to_load:2*vectors_to_load],pca_file_train_neg)
pickle.dump(X_new[2*vectors_to_load:3*vectors_to_load],pca_file_test_pos)
pickle.dump(X_new[3*vectors_to_load:4*vectors_to_load],pca_file_test_neg)