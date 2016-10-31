import nltk
import pickle
import numpy as np
import tensorflow as tf
import gensim
import numpy as np
# to do 
# Assume that the sequences are padded with zero vectors to fill up the remaining time steps in the batch
# give large batch size ~ 1000
# The tags corresponding to zeros will also be all zero.
# Check the output for some function
# Use vectors of size 50 
from tf.nn.rnn import rnn_cell
from tensorflow.models.rnn import rnn
from scipy import sparse
from collections import defaultdict
from nltk.corpus import brown
print "_______________________imported corpus_____________________________"

brown_tagged_words = brown.tagged_words()
brown_tagged_sentences = brown.tagged_sents()

tag_count = defaultdict(int)
tag_set = []
modified_tagged_sents = []
min_tag_count = 20
# to generate tag_count & tag_set
def pre_processing():
	global tag_count
	global tag_set
	global modified_tagged_sents
	global min_tag_count
	# counting no of occurences of each tag
	print "__________________counting occurences of tags_____________________"
	for (word, tag) in brown.tagged_words():
		tag_count[tag] += 1
	for key in tag_count:
		tag_set.append(key)
	# if count[key] is less then 10 put it as NONE
	print "_______________changing low occuring tags to NONE___________________"
	for sent in brown.tagged_sents():
		modified_sent = []
		for index,word in enumerate(sent):
			tag = word[1]
			if tag_count[word[1]] <= min_tag_count:
				tag = 'NONE'
			modified_sent.append([word[0], tag])
		modified_tagged_sents.append(modified_sent)
	print "___________________creating tag_set & tag_count_____________________"
	tag_count = defaultdict(int)
	tag_set = []
	for sent in modified_tagged_sents:
		for word in sent:
			tag = word[1]
			tag_count[tag] += 1
	for key in tag_count:
		tag_set.append(key)

pre_processing()

label_sent =[]
sparse_label_sent =[]
def generate_labels(to_save):
	# save decides weather to save the model in a file or not
	global label_sent
	global sparse_label_sent
	no_of_tags = len(tag_set)
	label_sent = []
	sparse_label_sent = []
	for index, sent in enumerate(modified_tagged_sents):
		current_tag_sequence = []
		sparse_tag_senquence = []
		for word in sent:
			temp = np.zeros(no_of_tags)
			temp[tag_set.index(word[1])] = 1
			current_tag_sequence.append(temp)
			sparse_tag_senquence.append(sparse.csr_matrix(temp))
		label_sent.append(current_tag_sequence)
		sparse_label_sent.append(sparse_tag_senquence)
		print len(modified_tagged_sents)-index
	print "___________________converted to one hot representation____________________"
	# file_name = 'sparse_brown_tags.onehot'
	# file = open(file_name,"wb")
	# pickle.dump(sparse_label_sent,file)
	if to_save == True:
		file_name = 'brown_tags.onehot'
		file = open(file_name,"wb")
		pickle.dump(label_sent,file)

generate_labels(False)

w2v_sent = []
def generate_w2v(to_save):
	print "_____________________now loading w2v model__________________________"
	model = gensim.models.Word2Vec.load('/home/shibhansh/cs671/Assignments/Assignment2/brownCorpus/brown_model')
	print "_____________________done loading word2vec__________________________"
	global w2v_sent
	for sent in brown.sents():
		current_sent_w2v = []
		for word in sent:
			if word in model.vocab:
				current_sent_w2v.append(model[word])	
			else:
				current_sent_w2v.append(np.zeros(300))
		w2v_sent.append(current_sent_w2v)
	if to_save == True:
		file_name = 'brown_corpus'
		w2v_file = open(file_name+".w2v", "wb")
		print "_____________________created file for w2v________________________"
		pickle.dump(current_sent_w2v,w2v_file)

generate_w2v(False)


no_of_tags = len(tag_set)
num_hidden = 50

# Batch size x time steps x features.
sequence = tf.placeholder(tf.float32, [None, None, 300])
target = tf.placeholder(tf.float32, [None, None, no_of_tags])
network = tf.nn.rnn_cell.GRUCell(num_hidden)

output, state = tf.nn.dynamic_rnn(network, sequence, dtype=tf.float32)	#output is [batch_size, max_time, cell.output_size]

# Softmax layer
weight = tf.Variable(tf.truncated_normal([num_hidden, no_of_tags], stddev=0.1))
bias = tf.Variable(tf.constant([0.1]*no_of_tags))

# Flatten to apply same weights to all time steps.
output = tf.reshape(output, [-1, num_hidden])		# Converted to 2-D with column lenth fixed to num_hidden
prediction = tf.nn.softmax(tf.matmul(output, weight) + bias)
prediction = tf.reshape(prediction, [-1, no_of_tags])

cross_entropy = -tf.reduce_sum(target * tf.log(prediction), reduction_indices=1)
cross_entropy = tf.reduce_mean(cross_entropy)

learning_rate = 0.003
optimizer = tf.train.RMSPropOptimizer(learning_rate)
minimize = optimizer.minimize(cross_entropy)

mistakes = tf.not_equal(tf.argmax(target, 0), tf.argmax(prediction, 0))
error = tf.reduce_mean(tf.cast(mistakes, tf.float32))

init_op = tf.initialize_all_variables()
sess = tf.Session()
sess.run(init_op)

batch_size = 1
no_of_batches = len(brown.sents())/batch_size
epoch = 40
train = w2v_sent[:]
train_target = label_sent[:]
train_error = []
for i in range(epoch):
	ptr = 0
	for j in range(no_of_batches):
		# need to convert input to a single tensor as in sequence
		# output is a single tensor 
		# print j
		inp = np.array(train[ptr])
		inp = inp.reshape(1,np.shape(inp)[0],300)
		out = np.array(train_target[ptr])
		out = out.reshape(1,np.shape(out)[0],no_of_tags)
		ptr += batch_size
		sess.run(minimize,{sequence: inp, target: out})		
	print "Epoch - ",str(i)
	incorrect = 0
	for j in range(no_of_batches):
		test = np.array(train[j])
		test = test.reshape(1,np.shape(test)[0],300)
		test_target = np.array(train_target[j])
		test_target = test_target.reshape(1,np.shape(test_target)[0],no_of_tags)
		incorrect += sess.run(error,{sequence: test, target: test_target})
	print('Epoch {:2d} error {:3.1f}%'.format(i + 1, 100*incorrect/no_of_batches))
	train_error.append(100*incorrect/no_of_batches)
sess.close()

test = np.array(train[1])
test = test.reshape(1,np.shape(test)[0],300)
test_target = np.array(train_target[1])
test_target = test_target.reshape(1,np.shape(test_target)[0],no_of_tags)
incorrect = sess.run(error,{sequence: test, target: test_target})
print('Epoch {:2d} error {:3.1f}%'.format(i + 1, 100 * incorrect))