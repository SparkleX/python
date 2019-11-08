https://blog.csdn.net/Tw6cy6uKyDea86Z/article/details/102791493
import spacy 
from spacy import displacy	


def cleanup(token, lower = True):
    if lower:
        token = token.lower()
    return token.strip()
'''
nlp = spacy.load("en")
document = open("test.txt").read()
document = nlp(document)

labels = set([w.label_ for w in document.ents]) 
for label in labels: 
    entities = [cleanup(e.string, lower=False) for e in document.ents if label==e.label_] 
    entities = list(set(entities)) 
    print(label, entities)
'''

nlp = spacy.load("en")

text = "The rain in Spain falls mainly on the plain."	
doc = nlp(text)
svg = displacy.render(doc, )

f = open("out.html", "a")
f.write(svg)
f.close()