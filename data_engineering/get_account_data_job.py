import alpaca_trade_api as tradeapi
import json
from dotenv import load_dotenv
import os

def get_trading_account_details():
    load_dotenv()
    # Replace with your actual API key and secret key
    API_KEY = os.getenv('ALPACA_API_KEY')
    SECRET_KEY = os.getenv('ALPACA_SECRET_KEY')
    BASE_URL = 'https://paper-api.alpaca.markets'  

    # Initialize the API connection
    api = tradeapi.REST(API_KEY, SECRET_KEY, BASE_URL)

    # Get account information (to retrieve the equity)
    account = api.get_account()

    # Get positions (your current holdings)
    positions = api.list_positions()

    # Calculate total portfolio equity
    total_equity = float(account.equity)

    # Loop through each position to calculate its percentage of the total portfolio
    positions_list = []

    # Iterate through each position
    for position in positions:
        symbol = position.symbol
        market_value = float(position.market_value)
        percentage = (market_value / total_equity) * 100
        
        # Create a dictionary for the current position
        position_dict = {
            "symbol": symbol,
            "market_value": market_value,
            "percentage_of_portfolio": round(percentage, 2)
        }

        # Append the dictionary to the list
        positions_list.append(position_dict)

    # Convert the list of positions to a JSON string
    json_result = json.dumps(positions_list, indent=4)

    # Return the JSON string
    return json_result

print(get_trading_account_details())
