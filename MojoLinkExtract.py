from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv

# extract links to the site pages the provide links to each of the movies available on box office mojo.

url = "http://www.boxofficemojo.com/movies/alphabetical.htm?letter=A&p=.htm"

html = urlopen(url).read()
soup = BeautifulSoup(html, 'lxml')

partialLinksIndex = []
for link in soup.select("tr a"):
	if link.get('href')[0:20] == '/movies/alphabetical' and link.get('href') not in partialLinksIndex:
		partialLinksIndex.append(link.get('href'))

for i in range(0,len(partialLinksIndex)+1):
	url = "http://www.boxofficemojo.com" + partialLinksIndex[i]
	html = urlopen(url).read()
	soup = BeautifulSoup(html, 'lxml')
	for link in soup.select("tr a"):
		if link.get('href')[0:20] == '/movies/alphabetical' and link.get('href') not in partialLinksIndex:
			partialLinksIndex.append(link.get('href'))
print('\n')

# extract the movie links for each movie on box office mojo
print(len(partialLinksIndex))
print(partialLinksIndex[144])
print('\n')

movieLinks = []
for i in range (0,len(partialLinksIndex)):
	print('--- processing link %d/%d/%s ---' %(i+1,len(partialLinksIndex),partialLinksIndex[i]))
	url = "http://www.boxofficemojo.com" + partialLinksIndex[i]
	html = urlopen(url).read()
	soup = BeautifulSoup(html, 'lxml')
	partialLinks = []
	for link in soup.select("tr a"):
		partialLinks.append(link.get('href'))
	for element in partialLinks:
		if element[0:9] ==  '/movies/?':
			movieLinks.append(element)

# print size of movie links list
print(len(movieLinks))
print(movieLinks[4])
print(movieLinks[5])
print(movieLinks[6])

# deal with unicode
movieLinksClean = []
for i in range(0, len(movieLinks)):
	movieLinksClean.append(movieLinks[i].encode('ascii', 'ignore'))

# write output to csv file: movieLinks.txt
with open('movieLinks.txt', 'w') as f:
	wr = csv.writer(f, quoting = csv.QUOTE_ALL)
	wr.writerow(movieLinksClean)
