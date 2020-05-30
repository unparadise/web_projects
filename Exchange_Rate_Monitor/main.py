import datetime
import csv
from forex_python.converter import CurrencyRates

"""
class ExchangeRate:

    fm = None
    to = None
    date = None
    rate = 0

    def __init__(self, fromCurrency, toCurrency):
        self.fm = fromCurrency
        self.to = toCurrency

        x = datetime.datetime.now()
        self.date = str(x.year) + '.' + str(x.month) + '.' + str(x.day)
        
        c = CurrencyRates()
        self.rate = c.get_rate(self.fm, self.to)
        self.rate = format(self.rate, '.2f')
    
    def printRate(self):
        print(self.date, ':', self.rate)


usdToCny = ExchangeRate('USD', 'CNY')
usdToCny.printRate()
"""

exchangeRates = []
todaysRate = {'Date': None, 'Rate': 0, 'From': None, 'To': None}

def getDate():
    x = datetime.datetime.now()
    d = str(x.year) + '.' + str(x.month) + '.' + str(x.day)

    return d

def getRate(date, fromCurrency, toCurrency):
    c = CurrencyRates()
    rate = c.get_rate(fromCurrency, toCurrency)
    rate = format(rate, '.2f')

    return {'Date': date, 'Rate': rate, 'From': fromCurrency, 'To': toCurrency}

date = getDate()
todaysRate = getRate(date, 'USD', 'CNY')
exchangeRates.append(todaysRate)
print(exchangeRates)