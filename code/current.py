import os
from  datetime import timedelta , date , datetime
from csv import writer 
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
from initialised_data import get_data
from utils import get_stock_dict, convert_to_date

today_date = date(2021,12,29) #datetime.today() 
current_date = today_date - timedelta(1)
previous_date = current_date - timedelta(3)

current_date = current_date.strftime("%d-%m-%Y")
previous_date = previous_date.strftime("%d-%m-%Y")

#os.chdir('..\data')

nifty_50_dict = get_stock_dict()
nifty_50_list = list(nifty_50_dict.values())

for stock_symbol in nifty_50_list:
    company_df = get_data(stock_symbol,from_date=previous_date,to_date=current_date)
    current_record = company_df.head(1) 
    current_record = current_record.values.flatten().tolist()
    
    file_name = '../data/' + stock_symbol + '.csv'
    
    with open(file_name,'a') as file:
        writer_object = writer(file)
        writer_object.writerow(current_record)
        file.close()

    company_df = pd.read_csv('../data/'+stock_symbol+'.csv')
    company_df = company_df.append(current_record)
    print(company_df.dtypes)
    company_df = convert_to_date(company_df)
    company_df = company_df.sort_values(by=['date'])

    if stock_symbol =="M%26M":
        company_df.to_csv('M&M'+'.csv',index=False)
        os.remove('M%26M.csv')
    else:
        company_df.to_csv(stock_symbol+'.csv',index=False)

    company_df.to_csv('../data/'+stock_symbol+'.csv',index=False)

