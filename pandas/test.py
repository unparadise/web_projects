from yahoofinancials import YahooFinancials

tech_stocks = ['AAPL', 'MSFT', 'INTC']

yahoo_financials_tech = YahooFinancials(tech_stocks)
print(type(yahoo_financials_tech.get_pe_ratio()))
# get_pr_ratio() returns a dictionary
#print(yahoo_financials_tech.get_pe_ratio())
