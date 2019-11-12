import spacy 
from spacy import displacy	

transactios = ['sale order','journal entry','purchase order', 'invoice']


def findTransaction(name):
	for t in transactios:
		if name.find(t)>=0:
			return t

def nlp(text):
	nlp = spacy.load("en")
	doc = nlp(text)
	normalized = '';
	for token in doc:	
		#print(token.text, token.lemma_, token.pos_, token.is_stop)
		normalized = normalized + token.lemma_ + ' '
	find = findTransaction(normalized)
	if find is not None:
		print("OPEN:", find)
	else:
		print("try 'open ...' e.g. open sales order")

# main
print("Charbot, type q to quit")
while True:
	line = input(">") 
	if line == "q":
		break
	nlp(line)