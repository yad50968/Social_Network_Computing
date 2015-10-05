#-*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib.request

#  named three kind of type we will count
good_num = 0
no_num = 0
bad_num = 0
list1 = []
list2 = []
list3 = []
list4 = []

#use urllib library to read the html's source code 
htmlline = urllib.request.urlopen('https://www.ptt.cc/bbs/StupidClown/M.1443521969.A.C78.html').read() 

#use BeautifulSoup to parser it
soup = BeautifulSoup(htmlline,'html.parser')

#use BeautifulSoup function findAll()
for good in soup.findAll("span", {'class' : 'hl push-tag'}):
	good_num += 1

# 噓 and ->  in the same class : f1 hl push-tag
for other in soup.findAll("span", {'class':'f1 hl push-tag'}):
		
	if other.string.strip() == '噓':
		bad_num += 1
	else:
		no_num += 1
for a in soup.findAll('div',{'class':'push'}):

	if len(a.findAll('span',{'class':'hl push-tag'})) > 0:
		b = a.find('span',{'class':'hl push-tag'})
		list1.append(b.string.strip())
	if len(a.findAll('span',{'class':'f1 hl push-tag'})) > 0:
		b = a.find('span',{'class':'f1 hl push-tag'})
		list1.append(b.string.strip())
	name = a.find('span',{'class':'f3 hl push-userid'})	
	list2.append(name.string.strip())
	
	content = a.find('span',{'class':'f3 push-content'})
	list3.append(content.string)
	time = a.find('span',{'class':'push-ipdatetime'})
	list4.append(time.string.strip())

file = open('assigment1_3.html','w')
file.write('<html>')
file.write('<head><meta charset=\"UTF-8\">  Assigment1_3<br></head>')
file.write('<body>')
file.write('推 %d<br>' %good_num)
file.write('噓 %d<br>' %bad_num)
file.write('→ %d<br>' %no_num)
file.write('--------------------<br>')
for a in range(len(list1)):
	file.write('%s' %list1[a])
	file.write('%s' %list2[a])
	file.write('%s' %list3[a])
	file.write('%s<br>' %list4[a])
file.write('</body>')
file.write('</html>')
file.close()
