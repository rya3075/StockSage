import pandas as pd
import logging

def format_stock_data(data):
    #formats stock datd into dataframe

    try : 
        df = pd.DataFrame(data)
        return df.to_string(index=False)
    except Exception as e :
        logging.error(f"Error formatting stock data: {e}")
        return "Error formatting stock data"
    
def validate_stock_symbol(symbol):
    #checks the stock symbol is valid

    if symbol.isalnum() and symbol.isupper():
        return True
    logging.warning(f"Invalid stock symbol: {symbol}")
    return False

def format_datetime(dt):
    return dt.strftime("%Y-%m-%d %H:%M:%S")