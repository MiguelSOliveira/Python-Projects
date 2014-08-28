'''
Created on Aug 27, 2014
@author: miguel
'''

import urllib
if __name__ == '__main__':

    link = 'http://www.songlyrics.com/artistName/songName-lyrics/'
    artist = raw_input()
    artist = artist.replace("'", '-')
    artist = "-".join(artist.split())
    songName = raw_input()

    if songName == '*':
        link = 'http://www.songlyrics.com/' + artist + '/*/'
        url = urllib.urlopen(link)
        artist = artist.replace('-', ' ')
        artist = artist.split()
        artistName = []

        for word in artist:
            artistName.append(word[:1].capitalize() + word[1:])

        artist = None
        for line in url.readlines():
            # check the last tag b4 the name of the songs
            if  " ".join(artistName) + '">' in line:
                # split at just b4 song name and after song name
                answer = line.split(" ".join(artistName) + '">',1)[1].split('<',1)[0]
                print answer
    else:
        songName = songName.replace("'", '-')
        songName = "-".join(songName.split())
        print
        link = 'http://www.songlyrics.com/' + artist + '/' + songName + '-lyrics/'
        url = urllib.urlopen(link)
        url = url.read().split('iComment-text">', 1)[1].split('</div>', 1)
        print str(url[0]).replace('<br />', '').replace('</p', '')
        
        
        
        
        
        
        