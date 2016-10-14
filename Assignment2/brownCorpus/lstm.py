#import nltk and the corpus
import nltk
from nltk.corpus import brown
import numpy as np

print "_______________________imported corpus_____________________________"
#getting the tagged words
brown_tagged_words = brown.tagged_words()

#getting the tagged sentences
brown_tagged_sentences = brown.tagged_sents()

size = int(len(brown_tagged_sents) * 0.9)
train_sents = brown_tagged_sents[:size]
test_sents = brown_tagged_sents[size:]

import keras.backend as K
from keras.layers import LSTM, Input

I = Input(shape=(None, 200)) # unknown timespan, fixed feature size
lstm = LSTM(20)


keras.layers.recurrent.LSTM(output_dim, init='glorot_uniform', inner_init='orthogonal', forget_bias_init='one', activation='tanh', inner_activation='hard_sigmoid', W_regularizer=None, U_regularizer=None, b_regularizer=None, dropout_W=0.0, dropout_U=0.0)


























f = K.function(inputs=[I], outputs=[lstm(I)])


data1 = np.random.random(size=(1, 100, 200)) # batch_size = 1, timespan = 100
print f([data1])[0].shape
# (1, 20)

data2 = np.random.random(size=(1, 314, 200)) # batch_size = 1, timespan = 314
print f([data2])[0].shape
# (1, 20)

