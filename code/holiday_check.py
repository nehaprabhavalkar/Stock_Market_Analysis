from datetime import datetime, date 

current_date = datetime.today()

day = current_date.strftime("%A")

if day.lower() in ['monday', 'sunday']:
    raise Exception("DAG cannot be scheduled today")
else:
    print("DAG can be scheduled today")
