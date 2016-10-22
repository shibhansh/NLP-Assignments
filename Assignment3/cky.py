# import grammar

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


sent = ['I','book']
count = 0

mat = [[[]for x in range(len(sent))]for y in range(len(sent))]
back = [[[]for x in range(len(sent))]for y in range(len(sent))]

for word in sent:
	for A in grammar:
		# if A goes to word in the grammar, consider it as one of the possibilities of parse
		for sub_list in grammar[A]:
			if word in sub_list:
				# add this rule in the cell
				mat[sent.index(word)][sent.index(word)].append(A)

# store how are we getting at that rule, basically store the address of it's constituents in the cell
for span in range(1,len(sent)):
	for begin in range(0, len(sent)-span):
		# begin & end store the address of the current cell
		end = begin + span
		print begin,end
		for split in range(begin,end):
			# These should be the indices of the places to search in
			print begin,split,"        ",split+1,end
			# Now search for the rule whose one part is in mat[begin][split] , mat[split+1][end] & append the result in mat[begin][end]
			for non_terminal1 in mat[begin][split]:
				for non_terminal2 in mat[split+1][end]:
					for A in grammar:
						for sub_list in grammar[A]:
							if sub_list[0] == non_terminal1 and sub_list[1] == non_terminal2:
								mat[begin][end].append(A)
								back[begin][end].append([[begin,split],[split+1,end]])
								print A, non_terminal1, non_terminal2
			# Now fill these cells with whatever we want or need to