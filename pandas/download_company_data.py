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
import yahoodata as yahoodata

#companiesData = pd.read_csv('./sp500tickers.csv')
companiesData = pd.read_csv('./testTickers.csv')
#print(type(companiesData))

# Extract company tickers from the data frame and turn them into a list
companyTickers = companiesData['Ticker'].tolist()
# print(companyTickers)

pe_ratios = []
market_caps = []
dividend_rates = []
sectors = []
industries = []

# For each company in the S&P 500 list, extract its PE ratio and market cap and add each of them to its respective list
for ticker in companyTickers:
    yahoo_financials = YahooFinancials(ticker)
    print('Downloading data for ' + ticker + '...')
    pe_ratios.append(yahoo_financials.get_pe_ratio())
    market_caps.append(yahoo_financials.get_market_cap())
    dividend_rates.append(yahoo_financials.get_dividend_rate())
    sectors.append(yahoodata.getSector(ticker))
    industries.append(yahoodata.getIndustry(ticker))
    
companiesData['P/E'] = pe_ratios
companiesData['Market Cap'] = market_caps
companiesData['Dividend Rate'] = dividend_rates
companiesData['Sector'] = sectors
companiesData['Industry'] = industries

#print(companiesData)
date = str(date.today())
companiesData.to_csv("./sp500data_" + date + ".csv", index=False)
#conn = db.connect('SP500'+ date + '.db')
#companiesData.to_sql(name='SP500', con=conn)

# Another useful python library is the Fundamental Analysis library
# https://github.com/JerBouma/FundamentalAnalysis
