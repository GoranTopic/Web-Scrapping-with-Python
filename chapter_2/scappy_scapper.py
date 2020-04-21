from urllib.request import urlopen 
from bs4 import BeautifulSoup 

import re


pythonscraping = 'http://www.pythonscraping.com/pages/page3.html'
watchcartoon = 'https://www.thewatchcartoononline.tv/tenchi-muyou-ryo-ohki-4-ova-episode-1-english-subbed'


html  = urlopen (watchcartoon)

bs = BeautifulSoup( html, 'html.parser')


# print everything
for tag in bs.find_all():
    print(tag)

"""
# for pinting evey child of the of the table with id giftlist
for child in  bs.find('table', { 'id' : 'giftList'}).children: 
    print(child)
    print("--------------------------------------------------")

"""

"""
# for printing all of the sibling of the tables
for sibling  in  bs.find('table', { 'id' : 'giftList'}).tr.next_siblings: 
    print(sibling)
    print("--------------------------------------------------")
"""





