import gensim
import numpy as np
from nltk.tokenize import sent_tokenize
from nltk.corpus import brown
import sys

w2v_dimensions=50
if len(sys.argv) == 2:
	print "converting to w2v of dimension %f"  % ( count/(len(list_test_pos)+len(list_test_neg)))
	w2v_dimensions = sys.argv[1]

print "_________________importing files______________________"
text = open("train_neg.txt").read()
text += open("train_pos.txt").read()
text += open("test_neg.txt").read()
text += open("test_pos.txt").read()

print "_______________tokenizing sentences__________________"
sent_list = sent_tokenize(text)

print "_______________training the w2v model_________________"

model = gensim.models.Word2Vec(sent_list,workers=3,size=w2v_dimensions)
model.save('imdb_model')
print "_____________done training word2vec___________________"