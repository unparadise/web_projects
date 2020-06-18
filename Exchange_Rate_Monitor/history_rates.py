# This program retrieves historical exchange rateT
# from USD to RMB using https://ratesapi.io.

import datetime
from forex_python.converter import CurrencyRates
from get_rate import getRate

def createDates(startDate, endDate):
	"""This function puts a list of dates and returns
	these dates in a tuple"""
	dates = []

	start = datetime.datetime.strptime(startDate, '%Y-%m-%d')
	end = datetime.datetime.strptime(endDate, '%Y-%m-%d')
	step = datetime.timedelta(days=1)
	while start <= end:
	    # print(start.date())
	    dates.append(start.date())
	    start += step

	return dates
	
dates = createDates('2010-05-03', '2020-06-13')

rates = []
for date in dates:
	rates.append({'Date:':date, 'Rate': getRate(date, 'USD', 'CNY'), 'From': 'USD', 'To': 'CNY'})
	print(rates)

csvFile = './history_rates.csv'
csvColumns = ['Date', 'Rate', 'From', 'To']

saveRates(rates, csvFile, csvColumns)
