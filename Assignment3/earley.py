import copy

terminals = ['Papa', 'ate', 'the', 'a', 'caviar', 'spoon', 'with']
non_terminals = ['root','S', 'NP', 'VP','Verb', 'PP','Noun','Det','P']
grammar = {}
grammar['root'] = [['S']]
grammar['S']	 =  [['NP', 'VP']]
grammar['NP']	= [['Det','Noun'],['NP','PP'],['Papa']]
grammar['VP']	 = [['VP','PP'],['Verb','NP']]
grammar['PP']	 = [['P','NP']]
grammar['Verb']	 = [['ate']]
grammar['Det']	= [['the'],['a']]
grammar['Noun'] = [['caviar'],['spoon']]
grammar['P']	= [['with']]

# First completely understand the algorithm and the re-implement
POS = {}
POS['Papa']		=	['NP']
POS['ate']		=	['Verb']
POS['the']		=	['Det']
POS['a']		=	['Det']
POS['caviar']	= 	['Noun']
POS['spoon']	=	['Noun']
POS['with']		=	['P']

sent = ['Papa','ate','the','caviar','with','a','spoon']
chart = [[] for i in range(0,len(sent)+1)]
earley_parser()

def earley_parser():
	initial_state = ['root','.','S',[0,0]]
	enqueue(initial_state,0)
	for i in range(0,len(sent)+1):
		print i
		# To-do for all states of the
		current_index_in_chart = 0
		while current_index_in_chart != len(chart[i]):
			# print len(chart),i, len(chart[i]), current_index_in_chart
			state = chart[i][current_index_in_chart]
			# print state
			if incomplete(state):
				# find the thing next to '.'
				if state[state.index('.')+1] in terminals:
					scanner(state)
				else :
					predictor(state)
			else :
				completer(state)
			current_index_in_chart += 1

def enqueue(state,chart_index):
	found = False
	for current_state in chart[chart_index]:
		# if chart_index == 1:
		# 	print state, current_state
		if current_state == state:
			found = True
	if found == False:
		chart[chart_index].append(state)
		# print state

def incomplete(state):
	if state[len(state)-2] != '.':
		return True
	else :
		return False

def predictor(state):
	index_B = state.index('.')+1
	j = state[len(state)-1][1]
	B = state[index_B]
	if B in grammar:
		for rhs_rule in grammar[B]: #rhs_rule is the RHS of the grammar rule
			new_state = [B,'.']
			for element in rhs_rule:
				new_state.append(element)
			new_state.append([j,j])
			enqueue(new_state, j)

def scanner(state):
	index_B = state.index('.')-1
	B = state[index_B]
	j = state[len(state)-1][1]
	if j < len(sent):
		if B in POS[sent[j]]:
			enqueue([B,sent[j],'.',[j,j+1]],j+1)

def completer(state):
	j = state[len(state)-1][0]		#Note this 0
	for current_state in chart[j]:
		if current_state[current_state.index('.')+1] == state[0]:
			new_state = copy.deepcopy(current_state)
			new_state[current_state.index('.')]   = current_state[current_state.index('.')+1]
			new_state[current_state.index('.')+1] =	current_state[current_state.index('.')] 
			new_state[len(new_state)-1][1] = state[len(state)-1][1]
			enqueue(new_state,state[len(state)-1][1])

chart = [[] for i in range(0,len(sent)+1)]
earley_parser()

print chart

count = 0
for list_ in chart:
	print count
	for sub_list in list_:
		print sub_list
	count += 1