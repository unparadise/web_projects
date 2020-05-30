import time
from forex_python.converter import CurrencyRates

c = CurrencyRates()
currentRate = c.get_rate('USD', 'CNY')
currentRate = format(currentRate, '.2f')
print(currentRate)


class exchangeRate:
    """Base class for forex rate"""

    fm = None
    to = None
    date = None
    rate = 0

    def __init__(self, fromCurrency, toCurrency):
        self.fm = fromCurrency
        self.to = toCurrency