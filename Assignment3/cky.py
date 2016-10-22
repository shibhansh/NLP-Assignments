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


sent = ['I','prefer','book']
count = 0
for word in sent:
	for A in non_terminals:
		# if A goes to word in the grammar, consider it as one of the possibilities of parse
		if A in grammar:
			for sub_list in grammar[A]:
				if word in sub_list:
					count +=1

# store how are we getting at that rule, basically store the address of it's constituents in the cell
for span in range(2,len(sent)):
	for begin in range(0, len(sent)-span):
		end = begin + span
		for split in (begin+1,end-1):
			# Now fill these cells with whatever we want or need to