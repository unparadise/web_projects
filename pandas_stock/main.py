import pandas as pd
import datetime
import pandas_datareader.data as web
from pandas import Series, DataFrame


start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2020, 5, 16)

df = web.DataReader("AAPL", 'yahoo', start, end)
df.tail()

fo = open("AAPL.txt", "w")
fo.write(str(df))
fo.close()
print(df)