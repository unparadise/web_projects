#import datetime as datetime
#import matplotlib.pyplot as pyplot
# from matplotlib import style
#import pandas as pandas
#import pandas_datareader.data as web

from bs4 import BeautifulSoup
import urllib2

url = "https://www.pythonforbeginners.com"
content = urllib2.urlopen(url).read()

soup = BeautifulSoup(content)

print soup.prettify()
