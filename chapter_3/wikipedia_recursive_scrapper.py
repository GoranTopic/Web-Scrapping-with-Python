from urllib.request import urlopen 
from bs4 import BeautifulSoup
import datetime
import random
import re

#   A script for getting wikipedia pages
#   by Goran Topic

url = ''

pages = set()

def getLinks(url):
    # get all the links of a given url
    global pages

    html = urlopen('http://en.wikipedia.org{}'.format(url))
    soup = BeautifulSoup( html, 'html.parser' )

    for link in soup('a', href=re.compile('^(/wiki/)')):
       if 'href' in link.attrs:
           #check is we have already visited the page
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)

getLinks(url)
    

