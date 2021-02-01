# Program to import the S&P500 csv file and extract the tickers

import pandas as pd
sp_500 = pd.read_csv('./S&P_500.csv')

# print the symbols to the terminal
print(sp_500['Symbol'])

#sp_500['Symbol'].to_csv('S&P_500_tickers.csv', index=False)
