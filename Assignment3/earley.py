terminals = ['book', 'TWA', 'Houston', 'flight', 'meal', 'money', 'include', 'prefer','this','that','a','does','from','to','on']
non_terminals = ['S', 'NP', 'VP', 'Aux', 'Verb', 'PP', 'Det', 'Nominal', 'Prep', 'Noun','Proper-Noun']
grammar = {}
grammar['S'] =  [['NP', 'VP'], ['Aux','NP','VP'],['VP']]
grammar['NP'] = [['Det','Nominal'],['Proper-Noun']]
grammar['Nominal'] = [['Noun'],['Noun','Nominal'],['Nominal','Prep']]
grammar['VP'] = [['Verb']['Verb','NP']]
grammar['Verb'] = [['book'],['include'],['prefer']]
grammar['Det']  = [['this'],['that'],['a']]
grammar['Noun'] = [['book'],['flight'],['meal'],['money']]
grammar['Aux']  = [['does']]
grammar['Prep'] = [['from'],['to'],['on']]
grammar['Proper-Noun'] = [['Houston'],['TWA']]
POS = {}
POS['book']		=	['Noun','Verb']
POS['TWA']		=	['Proper-Noun']
POS['Houston']	=	['Proper-Noun']
POS['flight']	=	['Noun']
POS['meal']		=	['Noun']
POS['money']	=	['Noun']
POS['include']	=	['Verb']
POS['prefer']	=	['Verb']
POS['that']		=	['Det']
POS['this']		=	['Det']
POS['a']		=	['Det']
POS['does']		= 	['Aux']
POS['from']		=	['Prep']
POS['to']		=	['Prep']
POS['on']		=	['Prep']
sent = ['book','this','flight']
chart = [[] for i in range(0,len(sent))]
def EarleyParser(grammar):
	enqueue(['gamma','.','S',[0,0]],0)
	for i in range(0,len(sent)):
		for state in chart[i]:
			if incomplete(state):
				if state[state.index('.')+1] in terminals:
					scanner(state,i+1)
				else:
					predictor(state)
			else:
				completer(state)

def enqueue(state,chart_entry):
	print "________________enqueue________________________-----------------------------------------------------------------__"
	Found = False
	for sub_list in chart[chart_entry]:
		if sub_list == state:
			Found = True
	if Found == False:
		chart[chart_entry].append(state)
		for sub_list in state:
			print sub_list
	print "____________________end of enqueue______________-----------------------------------------------------------------__"

def incomplete(state):
	print "_______________incomplete_________________________"
	if state[len(state)-2] == '.':
		return False
	else :
		return True

def predictor(state):		# A -> alpha.B Beta, [i,j]		# find the location of B
	print "________________predictor________________________"
	index_B = state.index('.') + 1
	print state, len(state), index_B, state[index_B]
	j = state[len(state)-1][1]
	B = state[index_B]
	if B in grammar.keys():
		for sub_list in grammar[B]:
			if len(sub_list) == 3:
				enqueue([B,'.',sub_list[0],sub_list[1],sub_list[2],[j,j]],j)
			if len(sub_list) == 2:
				enqueue([B,'.',sub_list[0],sub_list[1],[j,j]],j)
			else:
				enqueue([B,'.',sub_list[0],[j,j]],j)
			print sub_list, sub_list[0]
# something wrong here
def scanner(state,j):			# A -> alpha.B Beta, [i,j]
	print "_______________scanner________________________________"
	# find the location of B
	index_B = state.index('.') + 1
	B = state[index_B]
	print B, POS[sent[j]]
	if B == sent[j]:
		enqueue([POS[B][0],sent[j],'.',[j,j+1]],j)

def completer(state):
	print "_________________completer_____________________________"
	k = state[len(state)-1][1]
	for sub_list in chart[state[len(state)-1][0]]:
		if sub_list[sub_list.index('.')-1] == state[0]:
			new_state = state
			index_B = sub_list.index('.') + 1
			new_state[index_B], new_state[index_B-1] = new_state[index_B-1],new_state[index_B]
			enqueue(new_state,k)

EarleyParser(grammar)

print chart

for list_ in chart[0]:
	print list_
