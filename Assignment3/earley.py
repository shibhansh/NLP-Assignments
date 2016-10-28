import copy
# to use different possible grammars put the requierd grammar at top
# 'teminals' is the list containing the terminals in grammar
terminals = ['book', 'inculde','I','she','me','flight','meal','money', 'prefer','Houston', 'TWA']
# 'non_teminals' is the list containing the non-terminals in grammar
non_terminals = ['S', 'NP', 'VP','X1','X2','PP','Det','Aux', 'V', 'Nominal', 'N']
# grammar is the dictionary containing the grammar rules, for every key we store all possible transistions from it a list.
grammar = {}
grammar['S'] =  [['NP', 'VP'],['X1','VP'],['book'],['include'],['prefer'],['V','NP'],['X2','PP'],['V','PP'],['VP','PP']]
grammar['X1'] = [['Aux','NP']]
grammar['NP'] = [['Det','Nominal'],['I'],['she'],['me'],['TWA'],['Houston']]
grammar['Nominal'] = [['book'],['flight'],['meal'],['money'],['Nominal','N'],['Nominal','PP']]
grammar['PP'] = [['P', 'NP']]
grammar['VP'] = [['V','PP'],['VP','PP'],['V','NP'],['X2','PP'],['book'],['include'],['prefer']]
grammar['X2'] = [['V','NP']]
grammar['Aux'] = []
grammar['Det'] = []
grammar['P'] = []
grammar['V'] = []
# POS is the dictionary for parts of speech in for all the terminals
POS = {}
POS['book'] = ['Nominal','VP']
POS['include'] = ['VP']
POS['I'] = ['NP']
POS['she'] = ['NP']
POS['me'] = ['NP']
POS['flight'] = ['Nominal']
POS['meal'] =['Nominal']
POS['money'] = ['Nominal']
POS['prefer'] = ['VP']
POS['Houston'] = ['NP']
POS['TWA'] = ['NP']
sent = ['astronomers', 'saw', 'stars', 'with', 'binoculars']
sent = ['I','prefer']

# method to enqueue elements in sub_list of chart
def enqueue(state,chart_index):
	found = False
	for current_state in chart[chart_index]:
		if current_state == state:
			found = True
	if found == False:
		chart[chart_index].append(state)
# method to check if the rule is yet inclomplete
def incomplete(state):
	if state[len(state)-(2+1)] != '.':
		return True
	else :
		return False
# mehtod to predict all the next possible rules
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
# method to find previous rules which are now completed
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
# method for scanner to add element in next sub_list of chart
def scanner(state):
	index_B = state.index('.')-1
	B = state[index_B]
	j = state[len(state)-(1+1)][1]
	if j < len(sent):
		if B in POS[sent[j]]:
			enqueue([B,sent[j],'.',[j,j+1],[]],j+1)
# method for core earley_parser
def earley_parser():
	# add the initial rule
	initial_state = ['root','.','S',[0,0],[]]
	enqueue(initial_state,0)
	# recurse over all sublists of chart
	for i in range(0,len(sent)+1):
		# recurse for all rules in of chart[i]
		current_index_in_chart = 0
		while current_index_in_chart != len(chart[i]):
			state = chart[i][current_index_in_chart]
			if incomplete(state):
				# find the non-terminal/terminal next to '.'
				if state[state.index('.')+1] in terminals:
					scanner(state)
				else :
					predictor(state)
			else :
				completer(state)
			current_index_in_chart += 1
# 'chart' is the data-structure for earley's algorithm
chart = [[] for i in range(0,len(sent)+1)]
earley_parser()
def print_parse_trees(state, sub_tree):
	# if the rule leads to a terminal, add the complete rule
	if state[len(state)-1] == []:
		sub_tree.append(state[0])
		sub_tree.append([state[1]])
	else:
		# add the LHS of rule
		sub_tree.append(state[0])
		element_on_rhs_of_rule = len(state[len(state)-1])
		# for all elements on RHS of rule, find there parses(parse tree)
		for i in range(0,element_on_rhs_of_rule):
			j = state[len(state)-1][i][0]
			k = state[len(state)-1][i][1]
			sub_sub_tree = []
			print_parse_trees( chart[j][k] , sub_sub_tree)
			sub_tree.append(sub_sub_tree)
# printing all the parse trees
for current_state in chart[len(chart)-1]:
	# for rules the where the sentence is completed
	if current_state[:3] == ['root','S','.']:
		parse_tree = []
		print_parse_trees(current_state,parse_tree)
		print parse_tree

# 'teminals' is the list containing the terminals in grammar
terminals = ['astronomers', 'saw', 'stars', 'with', 'binoculars','telescope']
# 'non_teminals' is the list containing the non-terminals in grammar
non_terminals = ['S', 'NP', 'VP', 'PP', 'P', 'V']
# grammar is the dictionary containing the grammar rules, for every key we store all possible transistions from it a list.
grammar = {}
grammar['S'] =  [['NP', 'VP']]
grammar['PP'] = [['P', 'NP']]
grammar['VP'] = [['V','NP'],['VP','PP']]
grammar['P'] = [['with']]
grammar['V'] = [['saw']]
grammar['NP'] = [['NP','PP'],['astronomers'],['binoculars'],['stars'],['telescope'],['saw']]
# POS is the dictionary for parts of speech in for all the terminals
POS = {}
POS['with'] = ['P']
POS['saw'] = ['V','NP']
POS['astronomers'] = ['NP']
POS['binoculars'] = ['NP']
POS['stars'] = ['NP']
POS['telescope'] = ['NP']
sent = ['astronomers', 'saw', 'stars', 'with', 'binoculars']

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
POS = {}
POS['Papa']		=	['NP']
POS['ate']		=	['Verb']
POS['the']		=	['Det']
POS['a']		=	['Det']
POS['caviar']	= 	['Noun']
POS['spoon']	=	['Noun']
POS['with']		=	['P']
sent = ['Papa','ate','the','caviar','with','a','spoon']

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