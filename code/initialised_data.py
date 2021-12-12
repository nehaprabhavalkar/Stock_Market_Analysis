import requests
from io import StringIO
import pandas as pd
from  datetime import datetime , timedelta
import bs4
import os
from utils import nifty_50_list

session = requests.session()

head = {
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/87.0.4280.88 Safari/537.36 "
}

def get_data(company, from_date, to_date):
    session.get("https://www.nseindia.com", headers=head)
    session.get("https://www.nseindia.com/get-quotes/equity?symbol=" + company, headers=head)
    session.get("https://www.nseindia.com/api/historical/cm/equity?symbol="+company, headers=head)
    url = "https://www.nseindia.com/api/historical/cm/equity?symbol=" + company + "&series=[%22EQ%22]&from=" + from_date + "&to=" + to_date + "&csv=true"
    webdata = session.get(url=url, headers=head)
    company_df = pd.read_csv(StringIO(webdata.text[3:]))
    return company_df

os.chdir('..\data')

for stock_symbol in nifty_50_list:
    company_df = get_data(stock_symbol,from_date='06-12-2021',to_date='09-12-2021')
    company_df.to_csv(stock_symbol+'.csv',index=False)