from datetime import datetime, date, timedelta
import plotly
import plotly.express as px

current_date = datetime.today()

def convert_to_date(df):
    for i in range(0,len(df)):
        df['date'][i] = datetime.strptime(df['date'][i], '%d-%b-%Y').date()
    return df

def convert_to_string(df):
    for i in range(0,len(df)):
        df['date'][i] = df['date'][i].strftime('%d-%b-%Y')
    return df

def plot_graph(df):
    fig = px.line(df, x='date', y='close')
    return fig

def get_previous_trading_day(day_delta):
    previous_date = current_date - timedelta(day_delta)
    shift = timedelta(max(1,(previous_date.weekday() + 6) % 7 - 3))
    previous_date = previous_date - shift
    return previous_date

def get_stock_list():
    nifty_50_list = [ 
                        'ADANIPORTS',
                        'ASIANPAINT',
                        'AXISBANK',
                        'BAJAJ-AUTO',
                        'BAJAJFINSV',
                        'BAJFINANCE',
                        'BHARTIARTL',
                        'BPCL',
                        'BRITANNIA',
                        'CIPLA',
                        'COALINDIA',
                        'DIVISLAB',
                        'DRREDDY',
                        'EICHERMOT',
                        'GRASIM',
                        'HCLTECH',
                        'HDFC',
                        'HDFCBANK',
                        'HDFCLIFE',
                        'HEROMOTOCO',
                        'HINDALCO',
                        'HINDUNILVR',
                        'ICICIBANK',
                        'INDUSINDBK',
                        'INFY',
                        'IOC',
                        'ITC',
                        'JSWSTEEL',
                        'KOTAKBANK',
                        'LT',
                        'M&M',
                        'MARUTI',
                        'NESTLEIND',
                        'NTPC',
                        'ONGC',
                        'POWERGRID',
                        'RELIANCE',
                        'SBILIFE',
                        'SBIN',
                        'SHREECEM',
                        'SUNPHARMA',
                        'TATACONSUM',
                        'TATAMOTORS',
                        'TATASTEEL',
                        'TCS',
                        'TECHM',
                        'TITAN',
                        'ULTRACEMCO',
                        'UPL',
                        'WIPRO' 
                    ] 

    return nifty_50_list


