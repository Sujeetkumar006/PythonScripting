from urllib.request import urlopen
from bs4 import BeautifulSoup
url = input('Enter your start url:')
co = input('Enter your count:')
posi = input('Enter your position:')

for i in range(int(co)):
	html = urlopen(url).read()
	soup = BeautifulSoup(html)
	tags = soup('a')
	number = 0
	for tag in tags:
		number += 1
		if number == int(posi):
			url = tag.get('href')
			if i == int(co)-1:
				print (tag.contents[0])
			break
			
#This is assignment of courseera
#Need to pick data for this

'''
from urllib.request import urlopen
from bs4 import BeautifulSoup

page = urlopen(input("Enter URL: "))
soup = BeautifulSoup(page, "html.parser")


spans = soup('span')

numbers = []

for span in spans:
    numbers.append(int(span.string))

#print(numbers)
print(sum(numbers))
'''
































			
