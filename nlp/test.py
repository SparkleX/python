from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
  
mytext = "Hello Mr. Adam, how are you? I hope everything is going well. Today is a good day, see you dude."
print(sent_tokenize(mytext))
print(word_tokenize(mytext))


mytext = "Bonjour M. Adam, comment allez-vous? J'espère que tout va bien. Aujourd'hui est un bon jour."
print(sent_tokenize(mytext))
print(sent_tokenize(mytext, "french"))