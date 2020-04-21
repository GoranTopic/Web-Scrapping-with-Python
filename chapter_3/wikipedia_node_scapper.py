from urllib.request import urlopen 
from bs4 import BeautifulSoup
from queue import Queue 
import networkx as nx
import datetime
import random
import re



#   a program to scrap an store the whole wikipedia vertex and edges,
#   so that an ofline program can find the shortes path on this data
#   istahd of having to do online html requests, which take time
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

# graph structure for storing the wikipedia nodes
WG = nx.Graph()





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
    
    # Add current node ot the graph
    WG.add_node(current_page)

    for page in get_links( wikipedia_base_url + current_page ):
        # if page is has not bee visited appedn then to the queue
        if page is target_page: 
            print("PAGE FOUND")
            break
        if page not in visited_pages:
            WG.add_node( page['href'] )
            WG.add_edge( current_page,  page['href'] )
            queued_pages.put( page['href'] )
    visited_pages.add(current_page)
    current_page = queued_pages.get()
    nx.write_gpickle(WG, "data_graph.nx")

    print()
    print(  "queue size: "        +  str(queued_pages.qsize())    )
    print(  "visited pages: "     +  str(len(visited_pages))      )
    print(  "current page: "      +  current_page                 )
    print(  "number of nodes: "   +  str( WG.number_of_nodes())   )
    print(  "number of edges: "   +  str( WG.number_of_edges())   )
       

