from urllib.request import urlopen 
from bs4 import BeautifulSoup
import datetime
import random
import re

#   A dijkstras implemetation of a searching form 
#  
#   by Goran Topic

# Basic besite url for wikipedia
wikipedia_base_url = 'https://en.wikipedia.org/wiki/' 

# target wiki page
target_url = 'Insect'

# starting wiki page 
start_url = 'Transport'

visited_pages = set()




# 
def get_links( url ):
    ''' Get all the unvisited links form the given url '''
    global visited_pages
    links = []
    # get html page
    page_html = urlopen(url)
    # make soup....hmmm yummi =) lxml to make it fast 
    soup = BeautifulSoup( page_html, 'lxml' )
    # for a tag found to have a tribute href which starts with 'wiki'
    for link in soup('a', href=re.compile('^(/wiki/)((?!File)|(?!Special)|(?!About)|(?!Wikipedia))')  ):
        #if 'href' in link.attrs:
        print( link['href'])
           #check is we have already visited the page
            #if link.attrs['href'] not in visited_pages:
                #newPage = link.attrs['href']
           
        




get_links( wikipedia_base_url + start_url )


'''
def getLinks(url):
    # get all the links of a given url
    global pages

    html = urlopen('http://en.wikipedia.org{}'.format(url))
    soup = BeautifulSoup( html, 'lxml' )

    for link in soup('a', href=re.compile('^(/wiki/)')):
       if 'href' in link.attrs:
           #check is we have already visited the page
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)

getLinks(url)
    
'''

