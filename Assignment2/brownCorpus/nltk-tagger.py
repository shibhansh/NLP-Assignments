from __future__ import division
#import nltk and the corpus
import nltk
from nltk.corpus import brown

print "_______________________imported corpus_____________________________"
#getting the tagged sentences
brown_tagged_sentences = brown.tagged_sents()
brown_sentences = brown.sents()

#tagging the corpus using the nltk tagger
print "_________________tagging using the NLTK tagger______________________"
nltk_tagged = []
for sentence in brown_sentences:
	nltk_tagged.append(nltk.pos_tag(sentence))

print "_______________________tagging complete_____________________________"

count = 0
total_words = 0
i =0

#calculating the accuracy of the NLTK tagger
print "_______________checking accuracy of the NLTK tagger_________________"
for i in xrange(len(brown_tagged_sentences)):
	j = 0
	for j in xrange(len(brown_tagged_sentences[i])):
		total_words = total_words + 1
		if brown_tagged_sentences[i][j][1] == nltk_tagged[i][j][1]:
			count = count + 1

print "accuracy: %f"  % ( count/total_words)