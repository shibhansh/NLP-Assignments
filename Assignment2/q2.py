import gensim
import numpy as np
from nltk.corpus import brown

sentences = brown.sents()
print "_____________improted sentences_____________________"

model = gensim.models.Word2Vec(sentences,workers=3,size=300)
model.save('brown_model')
print "_____________done training word2vec_____________________"

print "_____________loading google word2vec_____________________"
gmodel = gensim.models.Word2Vec.load_word2vec_format('imdb_movie_review/aclImdb/GoogleNews-vectors-negative300.bin', binary=True)
print "_____________ done loading google word2vec_____________________"

words = brown.words()

print "_____________calculating similarity_____________________"
similarity = []
for word in words:
	if word in model.vocab:
		if word in gmodel.vocab:
			word
			temp1 = model[word]
			temp = gmodel[word]
			cosine = np.inner(temp,temp1)/(np.linalg.norm(temp)*np.linalg.norm(temp1))
			similarity.append(cosine)

plt.hist(similarity, normed=True, bins=10)
plt.show()