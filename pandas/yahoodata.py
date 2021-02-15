from urllib.request import urlopen
from bs4 import BeautifulSoup

def getSector(ticker):
    profileUrl = "https://finance.yahoo.com/quote/" + ticker + "/profile"
    profilePage = urlopen(profileUrl)

    soup = BeautifulSoup(profilePage, features="html.parser")
    
    #i = 0
    #for child in soup.findAll(text="Sector(s)")[0].parent.parent.contents:
    #    if(i == 4):
    #        print(child)
    #    i += 1
    
    sector  = soup.findAll(text="Sector(s)")[0].parent.parent.contents[4].string

    return (sector)


def getIndustry(ticker):
    profileUrl = "https://finance.yahoo.com/quote/" + ticker + "/profile"
    profilePage = urlopen(profileUrl)

    soup = BeautifulSoup(profilePage, features="html.parser")

    #i = 0
    #for child in soup.findAll(text="Industry")[0].parent.#parent.contents:
    #    if(i == 10):
    #        print(child.string)
    #    i += 1

    industry = soup.findAll(text="Industry")[0].parent.parent.contents[10].string

    return (industry)