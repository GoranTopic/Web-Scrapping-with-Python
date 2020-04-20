from urllib.request import urlopen 
from bs4 import BeautifulSoup
import datetime
import random
import re

#   A script for getting wikipedia pages
#   by Goran Topic


random.seed(datetime.datetime.now())

string target_page = ''


pages = set()

def getLinks(url):
    global pages

    html = urlopen('http://en.wikipedia.org{}'.format(url))
    soup = BeautifulSoup( html, 'html.parser' )
    
    for link in bs.find_all('a', href=re.compile('^(/wiki/)')):

        print(    
        #if 'href' in link.attrs:
        #    if link.attrs['href'] not in pages:
        #        newPage = link.attrs['href']
        #        print(newPage)
        #        pages.add(newPage)
        #        getLinks(newPage)

getLinks('')
    

