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

if len(exchangeRates) == 0 or exchangeRates[len(exchangeRates)-1]['Date'] != date:
        todaysRate = getRate(date, 'USD', 'CNY')

exchangeRates.append(todaysRate)

csvColumns = ['Date', 'Rate', 'From', 'To']

csvFile = './exchange_rates.csv'
try:
    with open(csvFile, 'w') as csvfile:
        writer = csv.DictWriter(csvfile,fieldnames=csvColumns)
        writer.writeheader()
        for data in exchangeRates:
            writer.writerow(data)
except IOError:
    print("I/O error")



print(exchangeRates)