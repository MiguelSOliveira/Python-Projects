from bs4 import BeautifulSoup
import urllib

def main():
	i = 1
	while i < 5:
		html_doc = urllib.urlopen('https://buckysroom.org/trade/search.php?sort=offersmost&page=' + str(i))
		html_doc = html_doc.read()
		

		soup = BeautifulSoup(html_doc)
		allFromClass =  soup.find_all(attrs={'class' : 'item-name'} )

		for ocurrence in allFromClass:
			print ocurrence.get_text()
		print 'Page ' + str(i)
		i += 1

if __name__ == '__main__':
	main()