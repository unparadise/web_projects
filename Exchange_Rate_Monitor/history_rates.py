# This program retrieves historical exchange rate
# from USD to RMB using https://ratesapi.io.

import datetime
from forex_python.converter import CurrencyRates


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

rate = {'Date': None, 'Rate': 0, 'From': None, 'To': None}

print(dates)
