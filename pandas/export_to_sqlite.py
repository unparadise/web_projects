# Export data in the csv file to SQLite database

import pandas as pd
import sqlite3 as db

companiesData = pd.read_csv('./S&P_500.csv')
conn = db.connect('SP500.db')
companiesData.to_sql(name='SP500', con=conn)
