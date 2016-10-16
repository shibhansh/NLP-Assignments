import gensim
import numpy as np
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
import sys

w2v_dimensions=50

print "_________________importing files______________________"
text = open("train_neg.txt").read()
text += open("train_pos.txt").read()
text += open("test_neg.txt").read()
text += open("test_pos.txt").read()

print "_______________tokenizing sentences__________________"
sent_list = sent_tokenize(text)
tokenized_sent_list = []
for sent in sent_list:
	sent = word_tokenize(sent)
	tokenized_sent_list.append(sent)
print "_______________training the w2v model_________________"

model = gensim.models.Word2Vec(tokenized_sent_list,workers=3,size=w2v_dimensions)
model.save('imdb_model')
print "_____________done training word2vec___________________"