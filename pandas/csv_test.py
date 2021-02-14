import csv

tickers = ['MMM', 'AAPL', 'MSFT']
with open('csv_test.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(tickers)
