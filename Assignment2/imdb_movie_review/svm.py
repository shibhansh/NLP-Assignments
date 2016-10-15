from __future__ import division
import numpy as np
import pickle
from sklearn import svm
import sys
w2v_dimension = 300

directory = raw_input("Input the name of directory to prpcess\n Note that the directory should contain the vectors after PCA: ")
w2v_dimension = int(raw_input("Please input the dimension of the vectors after PCA: "))

with open(directory + "/pca/train_neg.txt.pca", 'rb') as file:
	list_train_neg = pickle.load(file)
print "_________loaded negative train file___________"

with open(directory + "/pca/train_pos.txt.pca", 'rb') as file:
	list_train_pos = pickle.load(file)
print "_________loaded positive train file___________"

with open(directory + "/pca/test_neg.txt.pca", 'rb') as file:
	list_test_neg = pickle.load(file)
print "__________loaded negative test file___________"

with open(directory + "/pca/test_pos.txt.pca", 'rb') as file:
	list_test_pos = pickle.load(file)
print "__________loaded positive test file___________"


print "___________creating training data______________"
data_train = np.ndarray(shape=(len(list_train_pos)+len(list_train_neg),w2v_dimension))
data_train_target = np.ndarray(shape=len(list_train_pos)+len(list_train_neg))
for i in range(0,len(list_train_pos)):
	data_train[i]=list_train_pos[i]
	data_train_target[i] = 1

for i in range(len(list_train_pos),len(list_train_pos)+len(list_train_neg)):
	data_train[i]=list_train_neg[i-len(list_train_pos)]
	data_train_target[i] = -1
print "____________created training data______________"

print "____________fitting in classifier______________"
clf = svm.SVC(gamma=0.001, C=100.)
clf.fit(data_train[:], data_train_target[:])  
print "____________fitted in classifier______________"

print "___________creating test data______________"
data_test_pos = np.ndarray(shape=(len(list_test_pos),w2v_dimension))
for i in range(0,len(list_test_pos)):
	data_test_pos[i] = list_test_pos[i]

data_test_neg = np.ndarray(shape=(len(list_test_neg),w2v_dimension))
for i in range(0,len(list_test_neg)):
	data_test_neg[i] = list_test_neg[i]
print "____________created test data______________"


print "__________________testing__________________"
result_test_pos = clf.predict(data_test_pos[:])
result_test_neg = clf.predict(data_test_neg[:])

print "______________calculating_accuracy______________"
count = 0
for i in range(0,len(result_test_neg)):
	if result_test_neg[i] == -1:
		count = count+1
for i in range(0,len(result_test_pos)):
	if result_test_pos[i] 	== 1:
		count = count+1

print "accuracy: %f"  % ( count/(len(list_test_pos)+len(list_test_neg)))