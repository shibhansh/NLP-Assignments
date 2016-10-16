#import nltk and the corpus
import nltk
import pickle
from nltk.corpus import brown
import numpy as np
import tensorflow as tf
import gensim
print "_______________________imported corpus_____________________________"
#getting the tagged words
brown_tagged_words = brown.tagged_words()
#getting the tagged sentences
brown_tagged_sentences = brown.tagged_sents()

from collections import defaultdict
counts = defaultdict(int)
from nltk.corpus import brown
for (word, tag) in brown.tagged_words():
	counts[tag] += 1

keys = []
for key in counts:
	keys.append(key)

count = 0
train_output =[]
for sent in brown_tagged_sentences[:]:
	current_tag_sequence = []
	for word in sent:
		temp = np.zeros(len(keys))
		temp[keys.index(word[1])] = 1
		current_tag_sequence.append(temp)
	train_output.append(current_tag_sequence)
	count = count + 1
	print count

file_name = 'brown_tags.onehot'
file = open(file_name,"wb")
# pickle.dump(train_output,file)

print "_____________________now loading google w2v_________________________"
model = gensim.models.Word2Vec.load_word2vec_format('/data/gpuuser2/Downloads/GoogleNews-vectors-negative300.bin', binary=True)
print "_____________________done loading word2vec__________________________"

file_name = 'brown_corpus'
w2v_file = open(file_name+".w2v", "wb")
print "___________________created file for w2v________________________"

count = 0
train_input = []
# train_input = brown_sents
for sent in brown.sents():
	current_sent_w2v = []
	for word in sent:
		if word in model.vocab:
			current_sent_w2v.append(model[word])
		else:
			current_sent_w2v.append(np.zeros(300))
	# pickle.dump(current_sent_w2v,w2v_file)
	train_input.append(current_sent_w2v)
	count = count + 1
	print count

no_of_tags = len(keys)

data = tf.placeholder(tf.float32, [1 ,None,300])
target = tf.placeholder(tf.float32, [1, None, no_of_tags])

num_hidden = 50
cell = tf.nn.rnn_cell.LSTMCell(num_hidden,state_is_tuple=True)

val, state = tf.nn.dynamic_rnn(cell, data, dtype=tf.float32)
# val = tf.transpose(val, [1, 0, 2])

weight = tf.Variable(tf.truncated_normal([num_hidden,no_of_tags]),tf.float32)

bias = tf.Variable(tf.constant(0.1, shape=[no_of_tags]))


max_length = target.get_shape()[1]
num_classes = target.get_shape()[2]
weight, bias = self._weight_and_bias(self._num_hidden, num_classes)
output = tf.reshape(output, [-1, self._num_hidden])
prediction = tf.nn.softmax(tf.matmul(output, weight) + bias)
prediction = tf.reshape(prediction, [-1, max_length, num_classes])



prediction = tf.nn.softmax(tf.matmul(val[0][:], weight) + bias)

cross_entropy = -tf.reduce_sum(target * tf.log(prediction))

optimizer = tf.train.AdamOptimizer()
minimize = optimizer.minimize(cross_entropy)

mistakes = tf.not_equal(tf.argmax(target, 1), tf.argmax(prediction, 1))

error = tf.reduce_mean(tf.cast(mistakes, tf.float32))

init_op = tf.initialize_all_variables()
sess = tf.Session()
sess.run(init_op)


batch_size = 1
no_of_batches = len(brown.sents())
epoch = 500
for i in range(epoch):
	ptr = 0
	for j in range(no_of_batches):
		inp = train_input[ptr:ptr+batch_size]
		out = train_output[ptr:ptr+batch_size]
		temp = np.empty([1,len(out[0]),472],dtype = int)
		temp[0][:][:] = out[0]
		out = temp
		ptr+=batch_size
		sess.run(minimize,{data: inp, target: out})
	print "Epoch - ",str(i)
incorrect = sess.run(error,{data: test_input, target: test_output})
print('Epoch {:2d} error {:3.1f}%'.format(i + 1, 100 * incorrect))
sess.close()