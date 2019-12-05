#import datetime as datetime
#import matplotlib.pyplot as pyplot
# from matplotlib import style
#import pandas as pandas
#import pandas_datareader.data as web

from bs4 import BeautifulSoup
import urllib.request

url = urllib.request.urlopen('http://www.google.com')

soup = BeautifulSoup(url, 'html.parser')

print(soup.prettify())