from urllib.request import urlopen
from urllib.request import HTTPError
from bs4 import BeautifulSoup

#a basic fuction of the web scrapper for using...
#by Goran Topic


def getTitle(url):  
    #function for gtting to the top the h1 of a url wiht error handeling 
    try:
        html = urlopen(url)
    except HTTPError as e:
        #Could not get reponse from website
        return None
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        title = bs.body.h1
    except AttributeError as e:
        # if not able to get find h1 tag
        return None
    return title




title = getTitle('http://www.pythonscraping.com/pages/page1.html')

if title  == None:
    print("Somthing went worng")
else:
    print(title)




