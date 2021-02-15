from urllib.request import urlopen
from bs4 import BeautifulSoup

def getProfile(ticker):
    profileUrl = "https://finance.yahoo.com/quote/" + ticker + "/profile"
    profilePage = urlopen(profileUrl)

    soup = BeautifulSoup(profilePage)
    soup.findAll(text="Sector(s):")

getProfile('MSFT')