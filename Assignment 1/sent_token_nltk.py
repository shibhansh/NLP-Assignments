from nltk.tokenize import sent_tokenize
import os

#read filename from the command line
if len(sys.argv) != 2:
	print "Incorrect number of arguments"
	exit()
text = open(sys.argv[1]).read()

#segment the sentences
sent_list = sent_tokenize(text)

#print sent_list
no_of_sent = len(sent_list)

for i in range(no_of_sent):
	print i, sent_list[i], "\n"
	i = i+1