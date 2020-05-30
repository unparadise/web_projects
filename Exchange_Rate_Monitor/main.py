import datetime
import csv
from forex_python.converter import CurrencyRates

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