from nltk.tokenize import sent_tokenize
from array import *
import os
import sys

#read filename from the command line
if len(sys.argv) != 2:
	print "Incorrect number of arguments"
	exit()

text = open(sys.argv[1]).read()

number_of_periods = 0
looping_variable = 0
length_of_text = len(text)

#counting the no. of periods
while looping_variable < length_of_text:
	if text[looping_variable] == '.':
		number_of_periods = number_of_periods + 1
	looping_variable += 1

print "number of periods: " ,number_of_periods

#initialze the lable array
labels = array('i',[])

#check if the period is terminating a sentence
sentence_list = sent_tokenize(text)

number_of_sentences = len(sentence_list)
print "number of sentences: ", number_of_sentences

looping_variable = 0
inner_looping_variable = 0
number_of_sentence_terminating_preriods = 0

#looping through each sentence & counting no. of sentence terminating periods
#save the label corresponding to each period
while looping_variable < len(sentence_list):
	current_sentence = sentence_list[looping_variable]
	length_of_current_sentence = len(current_sentence)

	inner_looping_variable = 0
	while inner_looping_variable < length_of_current_sentence:
		if current_sentence[inner_looping_variable] == '.':
			if inner_looping_variable == length_of_current_sentence - 1:
				labels.append(1)
				number_of_sentence_terminating_preriods += 1
			else:
				labels.append(0)
		inner_looping_variable += 1

	looping_variable += 1

#writing the lables in the label file
label_file = open(sys.argv[1]+'.label','w')
for label in labels:
		label_file.write("%d\n" %label)
label_file.close()

print "number_of_sentence_terminating_preriods: ", number_of_sentence_terminating_preriods