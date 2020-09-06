import datetime
import csv
from get_date import getDate
from save_rates import saveRates
from get_rate import getRate
from send_email import sendEmail


exchangeRates = []
todaysRate = {'Date': None, 'Rate': 0, 'From': None, 'To': None}
alertRate = 7.0

date = getDate()
# TODO: Remove time from returned date data
#csvFile = './web_projects/Exchange_Rate_Monitor/exchange_rates.csv'
csvFile = './Exchange_Rate_Monitor/exchange_rates.csv'
csvColumns = ['Date', 'Rate', 'From', 'To']

try:
    with open(csvFile) as csvFileHandle:
        exchangeRates = csv.DictReader(csvFileHandle, delimiter=",")
        exchangeRates = list(exchangeRates)
except IOError:
    print('exchange_rates.csv file does not exist')
    
# If today is not in the exchangeRates list then add today's date,
# rate, from, and to data as a dictionary item to the list
## TODO: move the code that decides whether there is new data to the save_rates.py file
if len(exchangeRates) == 0 or exchangeRates[len(exchangeRates)-1]['Date'] != str(date):
    todaysRate = getRate(date, 'USD', 'CNY')
    exchangeRates.append(todaysRate)
    #if float(todaysRate['Rate']) < alertRate:
    #    sendEmail(todaysRate['Date'], todaysRate['Rate'], todaysRate['From'], todaysRate['To'], 'lianchen16@gmail.com')

    # Write the exchangeRates list to the exchange_rates.csv file
    saveRates(exchangeRates, csvFile, csvColumns)
    print(todaysRate)
    #for date in exchangeRates:
    #    print(f"{date['Date']} : {date['Rate']}")
    #print(exchangeRates)

else:
    print('Today\'s rate is already retrieved.')
    #for date in exchangeRates:
    #    print(f"{date['Date']} : {date['Rate']}")
    # print(exchangeRates[len(exchangeRates)-1])
