import spacy 
from spacy import displacy	



def nlp(line):
  print(line)

# main
print("Charbot, type q to quit")
while True:
	line = input(">") 
	if line == "q":
		break
	nlp(line)