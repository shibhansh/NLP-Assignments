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

sent = ['astronomers', 'saw', 'stars', 'with', 'binoculars']

# mat is the data-structure for the CKY algorithm & back contains the pointers to retrace the trees
mat = [[[]for x in range(len(sent))]for y in range(len(sent))]
back = [[[]for x in range(len(sent))]for y in range(len(sent))]

# function to cleanly print a matrix
def print_mat(mat):
	for sub_list in mat:
		print sub_list

def  initialize():
	global mat 
	mat = [[[]for x in range(len(sent))]for y in range(len(sent))]
	global back
	back = [[[]for x in range(len(sent))]for y in range(len(sent))]
	# filling the bottom diagonal which represents parse of exactly one word
	for interator_sent in range(len(sent)):
		for A in grammar:
			# if A has word on right in the grammar, consider it as one of the possibilities of parse
			for sub_list in grammar[A]:
				if sent[interator_sent] in sub_list:
					# add this rule in the cell
					mat[interator_sent][interator_sent].append([A,sent[interator_sent]])

initialize()

# constructing the matrix for CKY algorithm
for span in range(1,len(sent)):
	for begin in range(0, len(sent)-span):
		# begin & end store the address of the current cell
		end = begin + span
		# print begin,end
		# Searching in all possible combination of cells
		for split in range(begin,end):
			# print begin,split,"        ",split+1,end
			# Searching for the non-terminal whose rule's RHS are in mat[begin][split] & mat[split+1][end]
			# append the resulting rule in mat[begin][end]
			# print mat[begin][split]
			for index_rule_1,rule_1 in enumerate(mat[begin][split]):
				non_terminal_1 = rule_1[0]
				for index_rule_2,rule_2 in enumerate(mat[split+1][end]):
					non_terminal_2 = rule_2[0]
					for A in grammar:
						for sub_list in grammar[A]:
							if len(sub_list) == 2:
								if sub_list[0] == non_terminal_1 and sub_list[1] == non_terminal_2:
									# print A, non_terminal_1, non_terminal_2
									# mat[begin][end] stores the rule, i.e. A -> non_terminal_1 , non_terminal_2
									mat[begin][end].append([A,non_terminal_1,non_terminal_2])
									# back stores corresponding to every entry in mat[begin][end] the location of non-terminals on the RHS of rule & their location in their cell
									back[begin][end].append([[begin,split,index_rule_1],[split+1,end,index_rule_2]])

# row_cell is the row_cell^th row
def print_parse_trees(index_in_cell,row_cell,column_cell,sub_tree):
	if row_cell == column_cell:
		sub_tree.append(mat[row_cell][column_cell][index_in_cell])
	else:
		sub_tree.append( mat[row_cell][column_cell][index_in_cell][0] )
		sub_sub_tree = []
		left_row_cell = back[row_cell][column_cell][index_in_cell][0][0]
		left_cloumn_cell = back[row_cell][column_cell][index_in_cell][0][1]
		left_index_in_cell = back[row_cell][column_cell][index_in_cell][0][2]
		print_parse_trees(left_index_in_cell, left_row_cell, left_cloumn_cell, sub_sub_tree)
		sub_tree.append(sub_sub_tree)
		right_row_cell = back[row_cell][column_cell][index_in_cell][1][0]
		right_cloumn_cell = back[row_cell][column_cell][index_in_cell][1][1]
		right_index_in_cell = back[row_cell][column_cell][index_in_cell][1][2]
		sub_sub_tree = []
		print_parse_trees(right_index_in_cell, right_row_cell, right_cloumn_cell,sub_sub_tree)
		sub_tree.append(sub_sub_tree)

for index, rule in enumerate(mat[0][len(sent)-1]):
	if rule[0] == 'S':
		parse_tree = []
		i = 0
		j = len(sent)-1
		print_parse_trees(index,i,j,parse_tree)
		print parse_tree

# Grammar
# S -> NP VP
# S -> X1 VP
# S -> book | include | prefer
# X1 -> Aux NP
# S -> Verb NP
# S -> X2 PP
# S -> Verb PP
# S -> VP PP
# NP -> I | she | me
# NP -> TWA | Houston
# NP -> Det Nominal
# Nominal -> book | flight | meal | money
# Nominal -> Nominal Noun
# Nominal -> Nominal PP
# VP -> book | include | prefer
# VP -> Verb NP
# VP -> X2 PP
# X2 -> Verb NP
# VP -> Verb PP
# VP -> VP PP
# PP -> Preposition NP

# terminals = ['book', 'I', 'she', 'me', 'TWA', 'Houston', 'flight', 'meal', 'money', 'include', 'prefer']
# non_terminals = ['S', 'NP', 'VP', 'X1', 'Aux', 'Verb', 'PP', 'Det', 'Nominal', 'X2', 'Preposition', 'Noun']
# grammar = {}
# grammar['S'] =  [['NP', 'VP'], ['X1','VP'],['Verb','NP'],['X2','PP'], ['Verb','PP'], ['VP' ,'PP'],['book'], ['include'], ['prefer']]
# grammar['X1'] = [['Aux' 'NP']]
# grammar['NP'] = [['Det','Nominal'],['I'],['she'],['me'],['TWA'],['Houston']]
# grammar['Nominal'] = [['Nominal','Noun'], ['Nominal','PP'],['book'],['flight'],['meal'],['money']]
# grammar['VP'] = [['book'],['include'],['prefer'],['Verb','NP'],['X2','PP'],['Verb','PP'],['VP','PP']]
# grammar['X2'] = [['Verb','NP']]
# grammar['PP'] = [['Preposition', 'NP']]
# POS = {}
# POS['book']	= ['S','Nominal','VP']
# POS['I']	= ['NP']
# POS['she']	= ['NP']
# POS['me']	= ['NP']
# POS['TWA']	= ['NP']
# POS['Houston']	= ['NP']
# POS['flight']	= ['Nominal']
# POS['meal']	= ['Nominal']
# POS['money']	= ['Nominal']
# POS['include']	= ['VP']
# POS['prefer']	= ['VP']

# sent = ['I','prefer']
# count = 0