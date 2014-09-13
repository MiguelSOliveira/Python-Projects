from bs4 import BeautifulSoup
import urllib

def main():
	link = 'http://www.fmylife.com/?page='

	for i in xrange(5):
		html_doc = urllib.urlopen(link+str(i))
		html_doc = html_doc.read()
		soup = BeautifulSoup(html_doc)
		for n in soup.find_all(attrs={'class' : 'fmllink'}):
			if 'FML' in n.get_text():
				print n.get_text()
				print
			else:
				print n.get_text()
		print "Page %d" % i



if __name__ == '__main__':
	main()