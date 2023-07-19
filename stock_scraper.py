import pandas as pd
import csv
import time
import os

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
pd.set_option("display.max_rows", None)

class StockScrape:
    def scraper(self, file_name):
        self.df = pd.read_csv('https://pkgstore.datahub.io/core/nyse-other-listings/nyse-listed_csv/data/3c88fab8ec158c3cd55145243fe5fcdf/nyse-listed_csv.csv')
        self.df1 = self.df.iloc[:, 0]
        output_path = os.path.join(os.getcwd(), file_name)
       # self.df1.to_csv('C:/Users/sanni/Anamoly_SentimentAnalysis/stocks/stocks.txt',index=False,header=None)
        print("Stocks downloaded at ", time.time())

