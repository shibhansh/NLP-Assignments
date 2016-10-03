import nltk

train_neg = open("train_neg.txt", "rb")

#store the docs in a list
document = train_neg.readlines()
#removing the extra newline character in every dcoument and word
document = [x[:-1] for x in document]

vocabulary = open("imdb.vocab", "rb")
vocab = vocabulary.readlines()
vocab = [x[:-1] for x in vocab]

dictionary = {}
count = 0
for word in vocab:
	dictionary[word] = count
	count = count + 1

count = 0
bBoWs = []

#creating vector representations for documents
for doc in document:
	document[count] = nltk.word_tokenize(doc)
	doc = document[count]
	print count
	count = count + 1
	current_BoW = [0]*len(vocab)	
	for word in doc:
		key_location = 0
		for key in vocab:
			if key == word:
				current_BoW[key_location] = 1
				break
			key_location = key_location + 1
	bBoWs.append(current_BoW)

# print bBoWs[0][6]

file = open("train_neg.bBoW", "wb")
for item in bBoWs:
	file.write("%s\n" % item)

# for doc in document:
# 	document[count] = nltk.word_tokenize(doc)
# 	doc = document[count]
# 	print count
# 	count = count + 1
# 	current_BoW = [0]*len(vocab)
# 	for word in doc:
# 		if word in dictionary.keys():
# 			current_BoW[dictionary[word]] = 1
# 	bBoWs.append(current_BoW)