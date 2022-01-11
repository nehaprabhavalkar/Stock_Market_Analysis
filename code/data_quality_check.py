from datetime import datetime, date, timedelta
import pandas as pd
from utils import get_stock_dict

# row count check
# null values check
# check if data is populated for today's date

nifty_50_dict = get_stock_dict()
nifty_50_list = list(nifty_50_dict.keys())

today_date = date(2021,12,24) #datetime.today()
current_date = today_date - timedelta(1)
str_current_date = current_date.strftime('%Y-%m-%d')

def check_row_count(nifty_50_list):
    for stock in nifty_50_list:
        df = pd.read_csv('../data/'+stock+'.csv')

        if len(df) > 0:
            print("Row count check is successful")

        else:
            raise Exception("Row count check has failed")

def check_null_values(nifty_50_list):
    for stock in nifty_50_list:
        df = pd.read_csv('../data/'+stock+'.csv') 

        if df.isnull().values.any() == False:
            print("No null values found")

        else:
            raise Exception("There are null values in data")

def check_data_for_current_date(nifty_50_list):
    for stock in nifty_50_list:
        df = pd.read_csv('../data/'+stock+'.csv') 
        df = df[ df['date'] == str_current_date ]

        if len(df) > 0:
            print("Data for date {} is populated".format(current_date))

        else:
            raise Exception("Date for date {} is not populated".format(current_date))


if __name__=='__main__':
    check_row_count(nifty_50_list)
    check_null_values(nifty_50_list)
    check_data_for_current_date(nifty_50_list)