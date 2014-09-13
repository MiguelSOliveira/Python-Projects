import urllib
from bs4 import BeautifulSoup

def main():
	html_doc = urllib.urlopen('http://www.ligaportugal.pt/')
	soup = BeautifulSoup(html_doc)
	count = 0
	teams = 0
	print 'Pos', 'Clube', 'J', 'V', 'E', 'D', 'Pts.'
	for ocurrence in soup.find_all('td'):
		if count == 7:
			count = 0
			teams += 1
			print
		elif teams == 18:
			break
		print ocurrence.get_text(),
		count += 1

if __name__ == '__main__':
	main()