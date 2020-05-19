#%%matplotlib inline
import matplotlib.pyplot as plt
from matplotlib import style

# Adjusting the size of matplotlib
import matplotlib as mpl

import pandas as pd
import datetime
import pandas_datareader.data as web
from pandas import Series, DataFrame


start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2020, 5, 16)

df = web.DataReader("AAPL", 'yahoo', start, end)
df.tail()

# write the price history data to an Excel file
# df.to_excel('./AAPL.xlsx', sheet_name='Price History')

close_px = df['Adj Close']
mavg = close_px.rolling(window=200).mean()


mpl.rc('figure', figsize=(8, 7))
mpl.__version__

# Adjusting the style of matplotlib
style.use('ggplot')

close_px.plot(label='AAPL')
mavg.plot(label='mavg')
plt.legend()
