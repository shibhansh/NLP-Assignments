import copy

terminals = ['this', 'that', 'a', 'book', 'flight' 'meal', 'money', 'prefer', 'does', 'from', 'to', 'on', 'Houston', 'TWA']
non_terminals = ['root','S', 'NP', 'VP', 'Aux', 'Verb', 'Det', 'Nominal', 'Proper-Noun', 'Noun','Prep']
grammar = {}
grammar['root'] = [['S']]
grammar['S'] =  [['NP', 'VP'], ['Aux','NP', 'VP'],['VP']]
grammar['NP'] = [['Det','Nominal'],['Proper-Noun']]
grammar['Nominal'] = [['Noun'], ['Noun','Nominal'],['Nominal','Prep']]
grammar['VP'] = [['Verb','NP'],['Verb']]
grammar['X2'] = [['Verb','NP']]
grammar['PP'] = [['Preposition', 'NP']]
grammar['Det']= [['this'],['that'],['a']]
grammar['Noun']= [['book'],['flight'],['meal'],['money']]
grammar['Verb']= [['book'],['include'],['prefer']]
grammar['Aux'] = [['does']]
grammar['Prep']= [['from'],['to'],['on']]
grammar['Proper-Noun'] = [['Houston'],['TWA']]
POS = {}
POS['book']	= ['Noun','Verb']
POS['include'] = ['Verb']
POS['prefer'] = ['Verb']
POS['this']	= ['Det']
POS['that']	= ['Det']
POS['a']	= ['Det']
POS['flight'] = ['Noun']
POS['meal'] = ['Noun']
POS['money'] = ['Noun']
POS['TWA']	= ['Proper-Noun']
POS['Houston']	= ['Proper-Noun']
POS['does']		= ['Aux']
POS['from']		= ['Prep']
POS['to']		= ['Prep']
POS['on']		= ['Prep']
sent = ['book','that','flight']


def enqueue(state,chart_index):
	found = False
	for current_state in chart[chart_index]:
		if current_state == state:
			found = True
	if found == False:
		chart[chart_index].append(state)

def incomplete(state):
	if state[len(state)-(2+1)] != '.':
		return True
	else :
		return False

def predictor(state):
	index_B = state.index('.')+1
	j = state[len(state)-(1+1)][1]
	B = state[index_B]
	if B in grammar:
		for rhs_rule in grammar[B]: #rhs_rule is the RHS of the grammar rule
			new_state = [B,'.']
			for element in rhs_rule:
				new_state.append(element)
			new_state.append([j,j])
			new_state.append([])
			enqueue(new_state, j)

def completer(state):
	j = state[len(state)-(1+1)][0]		#Note this 0
	k = state[len(state)-(1+1)][1]
	for current_state in chart[j]:
		if current_state[current_state.index('.')+1] == state[0]:
			new_state = copy.deepcopy(current_state)
			new_state[current_state.index('.')]   = current_state[current_state.index('.')+1]
			new_state[current_state.index('.')+1] =	current_state[current_state.index('.')] 
			new_state[len(new_state)-(1+1)][1] = state[len(state)-(1+1)][1]
			new_state[len(new_state)-1].append([k,chart[k].index(state)])
			enqueue(new_state,state[len(state)-(1+1)][1])

def scanner(state):
	index_B = state.index('.')-1
	B = state[index_B]
	j = state[len(state)-(1+1)][1]
	if j < len(sent):
		if B in POS[sent[j]]:
			enqueue([B,sent[j],'.',[j,j+1],[]],j+1)

def earley_parser():
	initial_state = ['root','.','S',[0,0],[]]
	enqueue(initial_state,0)
	for i in range(0,len(sent)+1):
		current_index_in_chart = 0
		while current_index_in_chart != len(chart[i]):
			state = chart[i][current_index_in_chart]
			if incomplete(state):
				# find the thing next to '.'
				if state[state.index('.')+1] in terminals:
					scanner(state)
				else :
					predictor(state)
			else :
				completer(state)
			current_index_in_chart += 1

# def backtrace()
chart = [[] for i in range(0,len(sent)+1)]
earley_parser()

count = 0
for list_ in chart:
	print count
	for sub_list in list_:
		print sub_list
	count += 1

def print_parse_trees(state, string_to_print):
	# Now we have to recurse
	if state[len(state)-1] == []:
		# string_to_print
		print "" + state[0] + "->" + state[1] + "",
	else:
		print ""+ state[0] + "->(",
		for i in range(0,len(state[len(state)-1])) :
			j = state[len(state)-1][i][0]
			k = state[len(state)-1][i][1]
			print_parse_trees( chart[j][k] , string_to_print)
			if i != len(state[len(state)-1])-1:
				print ",",
		print ")",

for current_state in chart[len(chart)-1]:
	if current_state[:3] == ['root','S','.']:
		string_to_print = ""
		print_parse_trees(current_state,string_to_print)

# terminals = ['Papa', 'ate', 'the', 'a', 'caviar', 'spoon', 'with']
# non_terminals = ['root','S', 'NP', 'VP','Verb', 'PP','Noun','Det','P']
# grammar = {}
# grammar['root'] = [['S']]
# grammar['S']	 =  [['NP', 'VP']]
# grammar['NP']	= [['Det','Noun'],['NP','PP'],['Papa']]
# grammar['VP']	 = [['VP','PP'],['Verb','NP']]
# grammar['PP']	 = [['P','NP']]
# grammar['Verb']	 = [['ate']]
# grammar['Det']	= [['the'],['a']]
# grammar['Noun'] = [['caviar'],['spoon']]
# grammar['P']	= [['with']]

# # First completely understand the algorithm and the re-implement
# POS = {}
# POS['Papa']		=	['NP']
# POS['ate']		=	['Verb']
# POS['the']		=	['Det']
# POS['a']		=	['Det']
# POS['caviar']	= 	['Noun']
# POS['spoon']	=	['Noun']
# POS['with']		=	['P']
# sent = ['Papa','ate','the','caviar','with','a','spoon']