import pandas as pd 
from initialised_data import get_data
from utils import get_stock_dict, get_cols, convert_to_date
from datetime import datetime

nifty_50_dict = get_stock_dict()
nifty_50_list = list(nifty_50_dict.values())

cols = get_cols()

for stock_symbol in nifty_50_list:
    df = get_data(stock_symbol, from_date='01-01-2015', to_date='31-12-2016')
    df = df.rename(columns=cols)
    
    df1 = get_data(stock_symbol, from_date='01-01-2017', to_date='31-12-2018')
    df1 = df1.rename(columns=cols)
    
    df2 = get_data(stock_symbol, from_date='01-01-2019', to_date='31-12-2020')
    df2 = df2.rename(columns=cols)
    
    df3 = get_data(stock_symbol, from_date='01-01-2021', to_date='31-12-2021')
    df3 = df3.rename(columns=cols)
    
    df4 = df.append(df1, ignore_index=True)
    df5 = df4.append(df2, ignore_index=True)
    df6 = df5.append(df3, ignore_index=True)
    
    df6.to_csv(stock_symbol+'.csv',index=False)
    

def transform_data(stock_symbol):
    df = pd.read_csv(stock_symbol+'.csv')
    
    df = convert_to_date(df)
        
    df = df.sort_values('date')
    
    df.to_csv(stock_symbol+'.csv',index=False)
    

for stock_symbol in nifty_50_list:
    transform_data(stock_symbol)