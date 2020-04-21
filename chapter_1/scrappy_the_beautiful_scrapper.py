from urllib.request import urlopen 
from bs4 import BeautifulSoup
import datetime
import random
import re

#   A script for getting wikipedia pages
#   by Goran Topic

wikipedia_url = 'http://en.wikipedia.org'
kissanime_url = 'https://kissanime.nz'
nudistFun_url = 'http://www.nudistfun.com'
imagefap_url = 'https://www.imagefap.com'


pages = set()


def getPage(url):
    # get all the links of a given url
    global pages

    html = urlopen( url )
    soup = BeautifulSoup( html, 'html.parser' )

    # leave here so that i can remeber what the command is
    #print( soup.prettify() )

    #print("-------------------------------------------------------------------")   
    for tag in soup.find_all('a', href=re.compile('.*') ):
        print( tag)
        print()

        #if 'href' in tag.attrs: print(tag.attrs['href'])
        #elif 'src' in tag.attrs: print(tag.attrs['src'])

    #print(soup.html.find_all('' ))

    

getPage(imagefap_url)
