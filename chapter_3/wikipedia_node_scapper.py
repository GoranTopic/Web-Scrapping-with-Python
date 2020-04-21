#!/usr/bin/python

#   a program to scrap an store the whole wikipedia vertex and edges,
#   so that an ofline program can find the shortes path on this data
#   istahd of having to do online html requests, which take time
#   by Goran Topic

from urllib.request import urlopen 
from bs4 import BeautifulSoup
from queue import Queue 
import networkx as nx
import pickle
import datetime
import random
import re
import os.path

# Basic besite url for wikipedia
wikipedia_base_url = 'https://en.wikipedia.org' 

# target wiki page
target_page = '/wiki/Hippie'

# starting wiki page 
current_page = start_page = '/wiki/Transport'

# a dictionary  of visited pages, has to be a dict
# so that time complexity is kept at o(1)
visited_pages = {}

# queue of pages to visit 
queued_pages = Queue()

# graph structure for storing the wikipedia nodes
WG = nx.Graph()



def get_links( url ):
    ''' Get all the unvisited links form the given url '''
    links = []
    try:
        # get html page
        page_html = urlopen(url)
        # make soup....hmmm yummi =) lxml to make it fast 
        soup = BeautifulSoup( page_html, 'lxml' )
        # for a tag found to have a tribute href which starts with 'wiki'
        return soup('a', href=re.compile('^(\/wiki\/(?!File|Portal:|Wikipedia:|Special:|Help:|Talk:))'))
    except URLError as e:
        print("URLError")
        print( url)
        return e

def panic_save_everything():
    





def start_crawler():
    ''' Starts the crawler '''
    # check if there is error file
    # check if there are files
    if os.path.isfile("exited_on_error"):
        print("reading from file left behind in previus seccion...")

        # delete errror file 
    else:
        print("Starting crawler...")


    #f = open("exited_on_error","w+") 
        
    while current_page is not target_page:
    
        # Add current node to the graph
        WG.add_node(current_page)
        # try to get the links for the current url
    try:
        pages = get_links( wikipedia_base_url + current_page ):
    except:
        #if it failed, saved everything we got so far! 
        # make a file indicating that the previous try has encounted an error


        
    else:

        for page in pages: 
         # if page is has not bee visited appedn then to the queue
            if page is target_page: 
                print("PAGE FOUND")
                break
            if page not in visited_pages:
                WG.add_node( page['href'] )
                WG.add_edge( current_page,  page['href'] )
                queued_pages.put( page['href'] )
        visited_pages[current_page] = True
        current_page = queued_pages.get()
    nx.write_gpickle(WG, "data_graph.nx")

    print()
    print(  "queue size: "        +  str(queued_pages.qsize())    )
    print(  "visited pages: "     +  str(len(visited_pages))      )
    print(  "current page: "      +  current_page                 )
    print(  "number of nodes: "   +  str( WG.number_of_nodes())   )
    print(  "number of edges: "   +  str( WG.number_of_edges())   )
'''


start_crawler()
