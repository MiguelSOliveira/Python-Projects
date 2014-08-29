'''
Created on Aug 29, 2014

@author: miguel
'''

import re, urllib
if __name__ == '__main__':
    
    link = 'http://tv.sapo.pt/programacao/detalhe/'
    print 'Insere o nome do canal'
    channel = raw_input()
    channel = "-".join(channel.split())
    link += channel
    htmlText = urllib.urlopen(link)
    htmlText = htmlText.read()
    regex = '<a href="#" class="pinfo">\s+(.+?)\s+</a>'
    regex2 = '<p>(\d.+?\d)</p>'
    showPattern = re.compile(regex)
    timePattern = re.compile(regex2)
    showInfo = {}
    showName = re.findall(showPattern, htmlText)
    showTime = re.findall(timePattern, htmlText)
    for name, time in zip(showName, showTime):
        showInfo[time.replace('&rarr;', '')] = name

    for item in sorted(showInfo):
        print item + ' \t' + showInfo[item]
