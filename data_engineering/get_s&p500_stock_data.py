import alpaca_trade_api as tradeapi
import pandas as pd
import requests
from datetime import datetime, timedelta
import os


def get_sp500_data(): 
    # URL to get the list of S&P 500 companies
    sp500_url = 'https://datahub.io/core/s-and-p-500-companies/r/constituents.csv'
    
    # Read the CSV file into a DataFrame
    sp500_df = pd.read_csv(sp500_url)
    
    # Extract the list of stock symbols
    symbols = sp500_df['Symbol'].tolist()
    
    # Replace with your actual API credentials
    API_KEY = os.getenv('ALPACA_API_KEY')
    SECRET_KEY = os.getenv('ALPACA_SECRET_KEY')
    BASE_URL = 'https://data.alpaca.markets' 
    
    api = tradeapi.REST(API_KEY, SECRET_KEY, BASE_URL, api_version='v2')
    
    # Define the time range
    end_date = datetime.now() - timedelta(minutes=15)
    start_date = end_date - timedelta(days=60)
    
    # Format dates as ISO strings
    start = start_date.strftime('%Y-%m-%dT%H:%M:%SZ')
    end = end_date.strftime('%Y-%m-%dT%H:%M:%SZ')
    
    # Define the timeframe (1 day bars)
    timeframe = '1Day'
    
    # Initialize a dictionary to store the data
    data_dict = {}
    
    # Function to split symbols into chunks
    def chunk_symbols(symbols_list, chunk_size):
        for i in range(0, len(symbols_list), chunk_size):
            yield symbols_list[i:i + chunk_size]
    
    # Alpaca allows up to 200 symbols per request
    chunk_size = 200
    
    for symbol_chunk in chunk_symbols(symbols, chunk_size):
        try:
            # Fetch bar data for the chunk of symbols
            barset = api.get_bars(symbol_chunk, timeframe, start=start, end=end).df
    
            # Process and store data for each symbol
            for symbol in symbol_chunk:
                symbol_data = barset[barset['symbol'] == symbol]
                if not symbol_data.empty:
                    data_dict[symbol] = symbol_data
                else:
                    print(f"No data for {symbol}")
        except Exception as e:
            print(f"Error fetching data for symbols {symbol_chunk}: {e}")
    
    # # Save each stock's data to a separate CSV file
    # for symbol, df in data_dict.items():
    #     df.to_csv(f"{symbol}_60days.csv")
    
    # Or combine all data into a single CSV file
    combined_df = pd.concat(data_dict)
    combined_df.to_csv("sp500_60days_data.csv")
    return combined_df

if __name__ == "__main__":
    if "--run_job" in sys.argv:
        sp500_data_df = get_sp500_data() 
        print(sp500_data_df)

