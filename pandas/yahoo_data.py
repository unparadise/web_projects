from urllib.request import urlopen
from bs4 import BeautifulSoup

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Function to retrieve sector info from Yahoo Finance profile page
def getSector(ticker):
    try:
        profileUrl = "https://finance.yahoo.com/quote/" + ticker + "/profile"
        profilePage = urlopen(profileUrl)

        soup = BeautifulSoup(profilePage, features="lxml")
        
        #i = 0
        #for child in soup.findAll(text="Sector(s)")[0].parent.parent.contents:
        #    if(i == 4):
        #        print(child)
        #    i += 1
        
        sector  = soup.findAll(text="Sector(s)")[0].parent.parent.contents[4].string

        return (sector)
    except:
        print(f"{bcolors.WARNING}Warning: {bcolors.ENDC}No Sector info found for " + ticker)
        return ('N/A')

# Function to retrieve industry info from Yahoo Finance profile page
def getIndustry(ticker):
    try:
        profileUrl = "https://finance.yahoo.com/quote/" + ticker + "/profile"
        profilePage = urlopen(profileUrl)

        soup = BeautifulSoup(profilePage, features="lxml")

        #i = 0
        #for child in soup.findAll(text="Industry")[0].parent.#parent.contents:
        #    if(i == 10):
        #        print(child.string)
        #    i += 1

        industry = soup.findAll(text="Industry")[0].parent.parent.contents[10].string

        return (industry)
    except:
        print(f"{bcolors.WARNING}Warning: {bcolors.ENDC}No Industry info found for " + ticker)
        return ('N/A')

# Function to retrieve to company name info from Yahoo Finance 
# profile page
# Current issue with the function
# Sometimes the retrieved company name contains characters that
# are not visible on the web page. E.G. BRk-B : Berkshire Hathaway Inc. New. The word New does not show up on the web page.

def getName(ticker):
    try:
        profileUrl = "https://finance.yahoo.com/quote/" + ticker + "/profile"
        profilePage = urlopen(profileUrl)

        soup = BeautifulSoup(profilePage, features="lxml")
        companyName = str(soup.title.string).split("(")[0]

        return (companyName)
    except:
        print(f"{bcolors.WARNING}Warning: {bcolors.ENDC}No Name found for " + ticker)
        return ('N/A')

# Test
# print(getCompanyName('BRK-B'))