from urllib.request import urlopen 
from bs4 import BeautifulSoup
from queue import Queue 
import datetime
import random
import re

#   A Breath first search  implemetation of a searching form one wikipedia page to an other
#   This UNforunally turned out to be extremly slowly and tedeaus, as to throw each note it has to 
#   make an html call, thus is I might resort to stroing the whole wiikipedia graph into a graph structure
#   by Goran Topic

# Basic besite url for wikipedia
wikipedia_base_url = 'https://en.wikipedia.org' 

# target wiki page
target_page = '/wiki/Insect'

# starting wiki page 
current_page = start_page = '/wiki/Transport'

# set of visited pages
visited_pages = set()

# queue of pages to visit 
queued_pages = Queue()



def get_links( url ):
    ''' Get all the unvisited links form the given url '''
    links = []
    # get html page
    page_html = urlopen(url)
    # make soup....hmmm yummi =) lxml to make it fast 
    soup = BeautifulSoup( page_html, 'lxml' )
    # for a tag found to have a tribute href which starts with 'wiki'
    return soup('a', href=re.compile('^(\/wiki\/(?!File|Portal:|Wikipedia:|Special:|Help:|Talk:))'))
        
        
        
while current_page is not target_page:

    for page in get_links( wikipedia_base_url + current_page ):
        # if page is has not bee visited appedn then to the queue
        if page is target_page: 
            print("PAGE FOUND")
            break
        if page not in visited_pages:
            queued_pages.put( page['href'] )



    current_page = queued_pages.get()
    print()
    print(  "queue size: "    +  str(queued_pages.qsize()) )
    print(  " current page: " +  current_page              )
       

