import nltk
from nltk.util import ngrams
from collections import Counter

def doit(string,i):
	tokenize = []
	str = ''
	tokenize = ngrams(nltk.word_tokenize(string),i)
	
	dictionary =  Counter(tokenize)
	mos = dictionary.most_common(5)
	for a,b in mos:
		for j in a:
			tmp  = j
			str += j
			str += ' '
		print(str,b)
		str = ''
	print('\n')
	dictionary.clear() 


file = open("big-sequence.txt",'r')

text = file.read()
string = ''
n =0
for a in text:
	if a == '\n':
		string += ' qqq'+str(n)+'a '
		n += 1
		if(n==5000):
			n=0
	else:
		string += str(a)

print('----Top five 1-words sequences\n')
doit(string,1)
print('----Top five 2-words sequences\n')
doit(string,2)
print('----Top five 3-words sequences\n')
doit(string,3)
print('----Top five 4-words sequences\n')
doit(string,4)
print('----Top five 5-words sequences\n')
doit(string,5)
