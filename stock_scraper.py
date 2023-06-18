import pandas as pd
import csv
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
pd.set_option("display.max_rows", None)


df = pd.read_csv('https://pkgstore.datahub.io/core/nyse-other-listings/nyse-listed_csv/data/3c88fab8ec158c3cd55145243fe5fcdf/nyse-listed_csv.csv')
df1=df.iloc[:, 0]
#df1.iloc[1: , :]
df1.to_csv('C:/Users/sachi/surpriver-master/stocks/stocks.txt', index=False,header=None)
