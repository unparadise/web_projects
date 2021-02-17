# Test the Python Yahoo Finance library
# The library can be found at https://github.com/JECSand/yahoofinancials
# --------------------
# Sudo code
# Open the S&P500.csv file
# Pass the tickers to Yahoo Finance to get PE ratios of the companies
# Write the PE ratios back to the S&P500.csv file
# --------------------

from yahoofinancials import YahooFinancials
import pandas as pd
import sqlite3 as db
from datetime import date
import yahoo_data as yahoo_data
import record_date as record_date

# There are two ticker files
# './sp500tickers.csv' is the file that has the S&P500 tickers and should be used for pulling down # real data
# './testTickers.csv' only has 'AAPL' and 'MSFT' and should be used for testing
test = False

date = str(date.today())
if test:
    tickerList = './testTickers.csv'
    outputFile = './testdata_' + date + '.csv'
else:
    tickerList = './sp500tickers.csv'
    outputFile = './sp500data_' + date + '.csv'

# Check the age of the S&P500 tickers list csv file.
# If it's older than 30 days. Suggest the user to run 'get_SP500_tickers.py' to
# update the list.



companiesData = pd.read_csv(tickerList)
#print(type(companiesData))

# Extract company tickers from the data frame and turn them into a list
companyTickers = companiesData['Ticker'].tolist()
# print(companyTickers)

pe_ratios = []
market_caps = []
dividend_yields = []
sectors = []
industries = []
names = []

# For each company in the S&P 500 list, extract its PE ratio and market cap and add each of them to its respective list
for ticker in companyTickers:
    yahoo_financials = YahooFinancials(ticker)
    print('Downloading data for ' + ticker + '...')
    pe_ratios.append(yahoo_financials.get_pe_ratio())
    market_caps.append(yahoo_financials.get_market_cap())
    try:
        dividend_yields.append(str(format(yahoo_financials.get_dividend_yield()*100, ".2f")) + '%')
    except:
        dividend_yields.append(str(yahoo_financials.get_dividend_yield()))
    sectors.append(yahoo_data.getSector(ticker))
    industries.append(yahoo_data.getIndustry(ticker))
    names.append(yahoo_data.getName(ticker))

companiesData['Name'] = names
companiesData['Sector'] = sectors
companiesData['Industry'] = industries
companiesData['P/E'] = pe_ratios
companiesData['Market Cap'] = market_caps
companiesData['Dividend Yield'] = dividend_yields

#print(companiesData)
companiesData.to_csv(outputFile, index=False)
record_date.recordDate('update_date.txt')

#conn = db.connect('SP500'+ date + '.db')
#companiesData.to_sql(name='SP500', con=conn)

# Another useful python library is the Fundamental Analysis library
# https://github.com/JerBouma/FundamentalAnalysis
