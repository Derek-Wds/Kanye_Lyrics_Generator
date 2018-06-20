import string, csv, re
import urllib.request as urllib2
from bs4 import BeautifulSoup
from unidecode import unidecode

global filename1, filename2
filename1 = 'data\\songs.csv'
filename2 = 'data\\lyrics.csv'

def get_songs():
    out = open(filename1, 'w', newline='')
    for i in range(1, 7):
        quote_page = "http://www.metrolyrics.com/kanye-west-alpage-{}.html".format(i)
        page = urllib2.urlopen(quote_page)
        soup = BeautifulSoup(page, 'html.parser')
        titles = soup.find('div', attrs={'class': "switchable lyrics clearfix"})
        for title in titles.text.split("\n"):
            if "Lyrics" not in title:
                pass
            else:
                csv_write = csv.writer(out, dialect='excel')
                csv_write.writerow([title])
    out.close()



def get_lyrics():
    num = 0
    song_names = csv.reader(open(filename1, 'r'))
    lyrics_file = open(filename2, 'w', newline='')
    quote_page = "http://www.metrolyrics.com/{}-kanye-west.html"
    for title in song_names:
        s = title[0].lower().split()
        for i in range(len(s)):
            temp = []
            for char in s[i]:
                if char in string.punctuation:
                    pass
                else:
                    temp.append(char)
            s[i] = ''.join(temp)
        song = '-'.join(s)
        page = urllib2.urlopen(quote_page.format(song))
        soup = BeautifulSoup(page, 'html.parser')
        verses = soup.find_all('p', attrs={'class': 'verse'})
        lyrics = ''
        for verse in verses:
            text = verse.text.strip()
            text = re.sub(r"\[.*\]\n", "", unidecode(text))
            if lyrics == '':
                lyrics = lyrics + text.replace('\n', '|-|')
            else:
                lyrics = lyrics + '|-|' + text.replace('\n', '|-|')
        csv_write = csv.writer(lyrics_file, dialect='excel')
        csv_write.writerow([num, title[0], str(lyrics)])
        print(num, 'writing to .csv')
        num += 1
    lyrics_file.close()

get_lyrics()