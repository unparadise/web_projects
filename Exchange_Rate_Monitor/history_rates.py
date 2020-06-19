# This program retrieves historical exchange rateT
# from USD to RMB using https://ratesapi.io.

from create_dates import createDates
from forex_python.converter import CurrencyRates
from get_rate import getRate
from save_rates import saveRates
	
dates = createDates('2020-06-10', '2020-06-13')

rates = []
for date in dates:
	rates.append(getRate(date, 'USD', 'CNY'))
	# print(rates)

csvFile = './history_rates.csv'
csvColumns = ['Date', 'Rate', 'From', 'To']

saveRates(rates, csvFile, csvColumns)
