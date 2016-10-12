import nltk

if len(sys.argv) != 2:
	print "Incorrect number of arguments"
	exit()

file_content = open(sys.argv[1]).read()

tokens = nltk.word_tokenize(file_content)
print tokens