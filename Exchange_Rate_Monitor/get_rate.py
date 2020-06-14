# Function takes date, fromCurrency, and toCurrency and
# returns a dictionary with date, exchange rate, fromCurreny,
# and toCurrency

import datetime
from forex_python.converter import CurrencyRates


def getRate(date, fromCurrency, toCurrency):
    """Retrieve the exchange rate from https://ratesapi.io.
    The function returns a dictionary object with date, rate,
    from, and to keys
    """

    c = CurrencyRates()
    rate = c.get_rate(fromCurrency, toCurrency, date)
    rate = format(rate, '.2f')

    return {'Date': str(date.date()), 'Rate': rate, 'From': fromCurrency, 'To': toCurrency}