from nltk.tokenize import sent_tokenize
from array import *
import os
import sys
import nltk
import numpy

global text

def extract_features(line_index, period_index):
	line_index += 1
	current_character = text[line_index]
	looping_variable = line_index

	while current_character != '\n':
		current_character = text[looping_variable]
		#taking care for the cases of N, V, PL, ADJ, PUN, CNJ, PL, ART, DET, INF, PN, PRP, ADV, PART, INF, 17 cases overall
		if current_character == 'N':
			features[period_index][0] = 1
		elif current_character == 'V':
			if text[looping_variable + 1] == ' ' or text[looping_variable + 1] =='\n':
				features[period_index][1] = 1
		elif current_character == 'P' and text[looping_variable + 1] == 'L':
			features[period_index][2] = 1
		elif current_character == 'A' and text[looping_variable + 1] == 'D' and text[looping_variable + 2] == 'J':
			features[period_index][3] = 1
		elif current_character == 'P' and text[looping_variable + 1] == 'U' and text[looping_variable + 2] == 'N':
			features[period_index][4] = 1
		elif current_character == 'C' and text[looping_variable + 1] == 'N' and text[looping_variable + 2] == 'J':
			features[period_index][5] = 1
		elif current_character == 'P' and text[looping_variable + 1] == 'L':
			features[period_index][6] = 1
		elif current_character == 'A' and text[looping_variable + 1] == 'R' and text[looping_variable + 2] == 'T':
			features[period_index][7] = 1
		elif current_character == 'D' and text[looping_variable + 1] == 'E' and text[looping_variable + 2] == 'T':
			features[period_index][8] = 1
		elif current_character == 'I' and text[looping_variable + 1] == 'N' and text[looping_variable + 2] == 'F':
			features[period_index][9] = 1
		elif current_character == 'A' and text[looping_variable + 1] == 'D' and text[looping_variable + 2] == 'J':
			features[period_index][10] = 1
		elif current_character == 'P' and text[looping_variable + 1] == 'N':
			features[period_index][11] = 1
		elif current_character == 'P' and text[looping_variable + 1] == 'R' and text[looping_variable + 2] == 'P':
			features[period_index][12] = 1
		elif current_character == 'A' and text[looping_variable + 1] == 'D' and text[looping_variable + 2] == 'V':
			features[period_index][13] = 1
		elif current_character == 'P' and text[looping_variable + 1] == 'A' and text[looping_variable + 2] == 'R' and text[looping_variable + 3] == 'T':
			features[period_index][14] = 1
		elif current_character == 'P' and text[looping_variable + 1] == 'R' and text[looping_variable + 2] == 'O' and text[looping_variable + 3] == 'G':
			features[period_index][15] = 1
		elif current_character == 'I' and text[looping_variable + 1] == 'N' and text[looping_variable + 2] == 'F':
			features[period_index][16] = 1
		looping_variable += 1

	return

#read filename from the command line
if len(sys.argv) != 2:
	print "Incorrect number of arguments"
	exit()

#preprocessing
os.system('./preprocessing.sh')

text = open('temp.txt').read()

os.system('rm temp.txt')

length_of_text = len(text)

#only the first work of each line of text contains the '.'
looping_variable = 0
number_of_periods = 0
current_character = ' '

features = numpy.zeros((100,17))

# counting the number of '.' in the text
while looping_variable < length_of_text:
	current_character = text[looping_variable]
	number_of_periods_in_current_line = 0
	if current_character == '\n':
		while current_character != ' ' and looping_variable < length_of_text -1 :
			if current_character == '.':
				number_of_periods += 1
				number_of_periods_in_current_line +=1
			looping_variable += 1
			current_character = text[looping_variable]
	looping_variable += 1

#for every period, if it's alone in it's line
#check the previous line and extract the features
looping_variable = 0
previous_line_pointer = 0
current_line_pointer = 0
current_period_number = -1

while looping_variable < length_of_text:
	current_character = text[looping_variable]
	number_of_periods_in_current_line = 0

	if current_character == '\n':														#newline has started
		previous_line_pointer = current_line_pointer
		current_line_pointer = looping_variable

		while current_character != ' ' and looping_variable < length_of_text -1 :
			if current_character == '.':
				number_of_periods_in_current_line +=1
				current_period_number += 1
			looping_variable += 1
			current_character = text[looping_variable]

		if number_of_periods_in_current_line == 1:										#only if we have one '.' in a line do we care
			#now extract features from the previous line
			extract_features(previous_line_pointer,current_period_number)
	looping_variable += 1

looping_variable = 0

#writing the features in feature file
feature_file = open(sys.argv[1]+'.features','w')
for looping_variable in range(0,100):
	feature_file.write("%s\n" %features[looping_variable])

feature_file.close()