from datetime import datetime, date 
import sqlite3
import json 

with open('config.json') as file:
  config_data = json.load(file)

current_date = datetime.today()
day = current_date.strftime("%A")
str_current_date = current_date.strftime("%Y-%m-%d")

holiday_tbl_name = config_data['holiday_tbl_name']

def is_bank_holiday(holiday_tbl_name, current_date):
    conn = sqlite3.connect('../web/test.db')
    cursor = conn.cursor()

    query = ''' SELECT * FROM {holiday_tbl_name} '''.format(holiday_tbl_name=holiday_tbl_name)

    cursor.execute(query)

    result = cursor.fetchall();

    for i in range(0,len(result)):
        if current_date in result[i][0]:
            flag = True
            break
        else:
            flag = False

    return flag 

is_bank_holiday = is_bank_holiday(holiday_tbl_name, str_current_date)

if day.lower() == 'monday' or day.lower() == 'sunday' or is_bank_holiday:
    raise Exception("DAG cannot be scheduled today")
else:
   print("DAG can be scheduled today")