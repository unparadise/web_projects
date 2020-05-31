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
    """Retrieve the exchange rate from https://ratesapi.io.
    The function returns a dictionary object with date, rate,
    from, and to keys
    """

    c = CurrencyRates()
    rate = c.get_rate(fromCurrency, toCurrency)
    rate = format(rate, '.2f')

    return {'Date': date, 'Rate': rate, 'From': fromCurrency, 'To': toCurrency}






date = getDate()
csvFile = './web_projects/Exchange_Rate_Monitor/exchange_rates.csv'

try:
    with open(csvFile) as csvFileHandle:
        exchangeRates = csv.DictReader(csvFileHandle, delimiter=",")
        exchangeRates = list(exchangeRates)
except IOError:
    print('exchange_rates.csv file does not exist')
    
# If today is not in the exchangeRates list then add today's date,
# rate, from, and to data as a dictionary item to the list
if len(exchangeRates) == 0 or exchangeRates[len(exchangeRates)-1]['Date'] != date:
        todaysRate = getRate(date, 'USD', 'CNY')
        exchangeRates.append(todaysRate)

# Write the exchangeRates list to the exchange_rates.csv file
# TODO: Update the code to only write the new data
csvColumns = ['Date', 'Rate', 'From', 'To']
try:
    with open(csvFile, 'w') as csvfile:
        writer = csv.DictWriter(csvfile,fieldnames=csvColumns)
        writer.writeheader()
        for data in exchangeRates:
            writer.writerow(data)
except IOError:
    print("I/O error")

print(exchangeRates)