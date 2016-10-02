#import nltk and the corpus
import nltk
from nltk.corpus import brown

#getting the tagged sentences
brown_tagged_sents = brown.tagged_sents()
brown_sents = brown.sents()

#distributing the data in test and train set
size = int(len(brown_tagged_sents) * 0.9)
train_sents = brown_tagged_sents[:size]
test_sents = brown_tagged_sents[size:]

#getting the tag distribution
tags_distribution = [tag for (word, tag) in brown.tagged_words()]
tagger = nltk.DefaultTagger(nltk.FreqDist(tags_distribution).max())

print tagger.evaluate(test_sents)