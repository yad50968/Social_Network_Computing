import nltk
from nltk.util import ngrams
from collections import Counter

def doit(string,i):
	tokenize = []
	tokenize = ngrams(nltk.word_tokenize(string),i)
	
	dictionary =  Counter(tokenize)
	mos = dictionary.most_common()
	for j in range(5):
		print(mos[j][0],mos[j][1])
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


doit(string,1)
doit(string,2)
doit(string,3)
doit(string,4)
doit(string,5)
#tokenize = ngrams(nltk.word_tokenize(string),4)
#dic = Counter(tokenize)
#mos = dic.most_common()
#for j in range(5):
#	print(mos[j][0],mos[j][1])
