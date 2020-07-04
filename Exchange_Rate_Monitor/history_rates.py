# This program retrieves historical exchange rateT
# from USD to RMB using https://ratesapi.io.

from create_dates import createDates
from forex_python.converter import CurrencyRates
from get_rate import getRate
from save_rates import saveRates
import sys

try:
	startDate = sys.argv[1]
	endDate = sys.argv[2]
except:
	print('Try history_rates.py [start date] [end date]')

dates = createDates(startDate, endDate)

rates = []
for date in dates:
	rates.append(getRate(date, 'USD', 'CNY'))
	# print(rates)

csvFile = './history_rates_test.csv'
csvColumns = ['Date', 'Rate', 'From', 'To']

saveRates(rates, csvFile, csvColumns)
