
#%pip install alpaca-trade-api

import alpaca_trade_api as tradeapi

# Replace with your actual API key and secret key
API_KEY = 'your_api_key'
SECRET_KEY = 'your_secret_key'
BASE_URL = 'https://paper-api.alpaca.markets'  # Use live URL for live trading

# Initialize the API connection
api = tradeapi.REST(API_KEY, SECRET_KEY, BASE_URL)

# Get account information (to retrieve the equity)
account = api.get_account()

# Get positions (your current holdings)
positions = api.list_positions()

# Calculate total portfolio equity
total_equity = float(account.equity)

# Loop through each position to calculate its percentage of the total portfolio
for position in positions:
    symbol = position.symbol
    market_value = float(position.market_value)
    percentage = (market_value / total_equity) * 100
    print(f"Symbol: {symbol}, Market Value: ${market_value}, Percentage of Portfolio: {percentage:.2f}%")

