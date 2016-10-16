import nltk
from nltk.corpus import brown

print "_______________________imported corpus_____________________________"
brown_tagged_sents = brown.tagged_sents()

size = int(len(brown_tagged_sents) * 0.8)
train_sents = brown_tagged_sents[:size]
test_sents = brown_tagged_sents[size:]

file = open("train_data_opennlp", 'wb')

train_set = []
for sent in train_sents:
	for word in sent:
		temp = word[0] +'_' + word[1]
		file.write(temp+'\n')

file.close()

file = open("test_data_opennlp", 'wb')

test_set = []
for sent in test_sents:
	for word in sent:
		temp = word[0] +'_' + word[1]
		file.write(temp+'\n')

file.close()

# accuracy = 0.9023663424145947