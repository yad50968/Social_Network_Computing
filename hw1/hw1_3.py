#-*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib.request


good_num = 0
no_num = 0
bad_num = 0

htmlline = urllib.request.urlopen('https://www.ptt.cc/bbs/StupidClown/M.1443521969.A.C78.html').read() 
soup = BeautifulSoup(htmlline,'html.parser')

for good in soup.findAll("span", {'class' : 'hl push-tag'}):
	good_num += 1
for other in soup.findAll("span", {'class':'f1 hl push-tag'}):
		
	if other.string.strip() == '噓':
		bad_num += 1
	else:
		no_num += 1

print("推",good_num)
print("噓",bad_num)
print("→",no_num)
