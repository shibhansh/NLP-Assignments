#import nltk and the corpus
import nltk
from nltk.corpus import brown

#getting the tagged sentences
brown_tagged_words = brown.tagged_words()

#distributing the data in test and train set
no_of_words = int(len(brown_tagged_words) * 0.9)
train_words = brown_tagged_words[:no_of_words]

#due to the format of evaluation of nltk
test_words = [brown_tagged_words[no_of_words:]]

#getting the tag distribution
tag_distribution = [tag for (word, tag) in train_words]
tagger = nltk.DefaultTagger(nltk.FreqDist(tag_distribution).max())

print tagger.evaluate(test_words)