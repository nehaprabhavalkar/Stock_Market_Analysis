import os
from  datetime import timedelta , date , datetime
from csv import writer 
from initialised_data import get_data
from utils import nifty_50_list

current_date = date(2021,12,10) #datetime.today() 
previous_date = current_date - timedelta(3)

current_date = current_date.strftime("%d-%m-%Y")
previous_date = previous_date.strftime("%d-%m-%Y")

os.chdir('..\data')

for stock_symbol in nifty_50_list:
    company_df = get_data(stock_symbol,from_date=previous_date,to_date=current_date)
    current_record = company_df.head(1) 
    current_record = current_record.values.flatten().tolist()
    file_name = stock_symbol + '.csv'
    with open(file_name,'a') as file:
        writer_object = writer(file)
        writer_object.writerow(current_record)
        file.close()
