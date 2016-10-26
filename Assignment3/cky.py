terminals = ['book', 'I', 'she', 'me', 'TWA', 'Houston', 'flight', 'meal', 'money', 'include', 'prefer']
non_terminals = ['S', 'NP', 'VP', 'X1', 'Aux', 'Verb', 'PP', 'Det', 'Nominal', 'X2', 'Preposition', 'Noun']
grammar = {}
grammar['S'] =  [['NP', 'VP'], ['X1','VP'],['Verb','NP'],['X2','PP'], ['Verb','PP'], ['VP' ,'PP'],['book'], ['include'], ['prefer']]
grammar['X1'] = [['Aux' 'NP']]
grammar['NP'] = [['Det','Nominal'],['I'],['she'],['me'],['TWA'],['Houston']]
grammar['Nominal'] = [['Nominal','Noun'], ['Nominal','PP'],['book'],['flight'],['meal'],['money']]
grammar['VP'] = [['book'],['include'],['prefer'],['Verb','NP'],['X2','PP'],['Verb','PP'],['VP','PP']]
grammar['X2'] = [['Verb','NP']]
grammar['PP'] = [['Preposition', 'NP']]
POS = {}
POS['book']	= ['S','Nominal','VP']
POS['I']	= ['NP']
POS['she']	= ['NP']
POS['me']	= ['NP']
POS['TWA']	= ['NP']
POS['Houston']	= ['NP']
POS['flight']	= ['Nominal']
POS['meal']	= ['Nominal']
POS['money']	= ['Nominal']
POS['include']	= ['VP']
POS['prefer']	= ['VP']

sent = ['I','prefer']
count = 0

mat = [[[]for x in range(len(sent))]for y in range(len(sent))]
back = [[[]for x in range(len(sent))]for y in range(len(sent))]

# Write a DFS like function build the trees
# def dfs(mat,back,depth,tree,i,j):
# 	# if tree is completed we need to print it
# 	mat[i][j]
# 	dfs(mat,back,depth+1)

# filling the bottom diagonal which represents parse of exactly one word
for interator_sent in range(len(sent)):
	for A in grammar:
		# if A has word on right in the grammar, consider it as one of the possibilities of parse
		for sub_list in grammar[A]:
			if sent[interator_sent] in sub_list:
				# add this rule in the cell
				mat[interator_sent][interator_sent].append([A,sent[interator_sent]])

# store how we are getting that non-terminal, i.e. from which constituents are we getting it and where they are
for span in range(1,len(sent)):
	for begin in range(0, len(sent)-span):
		# begin & end store the address of the current cell
		end = begin + span
		print begin,end
		# now searching in all possible combination of cells
		for split in range(begin,end):
			print begin,split,"        ",split+1,end
			# Now search for the non-terminal whose one non-terminals are in mat[begin][split] , mat[split+1][end] & append the resulting non-terminal in mat[begin][end]
			# non_terminal_1 and non_terminal_2 in the cells respectively, check if they occur on right of any cell
			for non_terminal_1 in mat[begin][split][0]:
				for non_terminal_2 in mat[split+1][end][0]:
					for A in grammar:
						for sub_list in grammar[A]:
							if sub_list[0] == non_terminal_1 and sub_list[1] == non_terminal_2:
								# mat[begin][end] stores the rule i.e. which two constituents are making making which one
								mat[begin][end].append([A,non_terminal_1,non_terminal_2])
								# back stores corresponding to every entry in mat[begin][end] the location of non-terminals on the right side of rule
								back[begin][end].append([[begin,split],[split+1,end]])

# add part for back, so as to from where S was made
# new_found = True
# while new_found:
# 	for rule in mat[len(sent)-1][len(sent)-1]:
# 		if rule[0] = 'S':


# Grammar
# S → NP VP
# S → X1 VP
# S → book | include | prefer
# X1 → Aux NP
# S → Verb NP
# S → X2 PP
# S → Verb PP
# S → VP PP
# NP → I | she | me
# NP → TWA | Houston
# NP → Det Nominal
# Nominal → book | flight | meal | money
# Nominal → Nominal Noun
# Nominal → Nominal PP
# VP → book | include | prefer
# VP → Verb NP
# VP → X2 PP
# X2 → Verb NP
# VP → Verb PP
# VP → VP PP
# PP → Preposition NP