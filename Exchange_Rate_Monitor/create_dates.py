# Module to generate a list of date based on the given parameters

import datetime

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