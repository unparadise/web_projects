# Test the Python Yahoo Finance library
# The library can be found at https://github.com/JECSand/yahoofinancials
# --------------------
# Sudo code
# Open the S&P500.csv file
# Pass the tickers to Yahoo Finance to get PE ratios of the companies
# Write the PE ratios back to the S&P500.csv file
# --------------------
# Yahoo Finance Library other useful methods
# get_market_cap()


from yahoofinancials import YahooFinancials
import pandas as pd

companiesData = pd.read_csv('./S&P_500_tickers.csv')
#print(type(companiesData))

# Extract company tickers from the data frame and turn them into a list
companyTickers = companiesData['Symbol'].tolist()
# print(companyTickers)

pe_ratios = []
market_caps = []


# For each company in the S&P 500 list, extract its PE ratio and market cap and add each of them to its respective list
for ticker in companyTickers:
    yahoo_financials = YahooFinancials(ticker)
    print('Downloading data for ' + ticker + '...')
    pe_ratios.append(yahoo_financials.get_pe_ratio())
    market_caps.append(yahoo_financials.get_market_cap())

companiesData['P/E'] = pe_ratios
companiesData['Market Cap'] = market_caps

#print(companiesData)
companiesData.to_csv("./S&P_500.csv", index=False)
