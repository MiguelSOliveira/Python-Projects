from bs4 import BeautifulSoup
import urllib

def main():
	link = 'http://www.fmylife.com/random/'
	html_doc = urllib.urlopen(link)
	html_doc = html_doc.read()
	soup = BeautifulSoup(html_doc)
	for result in soup.find_all('a', { "class": "fmllink" }):
		if 'FML' in str(result.get_text):
			print result.get_text()
			print
		else:
			print result.get_text()

if __name__ == '__main__':
	main()