import datetime
import csv
from forex_python.converter import CurrencyRates

class ExchangeRate:
    """Base class for forex rate"""

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
