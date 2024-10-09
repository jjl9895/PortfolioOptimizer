import time
import pandas as pd
from api_integration.chatgpt_model import get_chatgpt_response
from get_account_data_job import get_trading_account_details
import alpaca_trade_api as tradeapi

# Read data
df = pd.read_csv('../data_engineering/business_financial_news.csv')

# Gets trading account details from Alpaca API 
account_data = get_trading_account_details()
str_account_data = str(account_data)

# Adds account data to the initial prompt
initial_prompt = "Here is my account data:"
initial_prompt += str_account_data

# Generate prompts
headlines = [
    f"This is the headline and summary data: {row['Title']}: {row['Summary']}"
    for _, row in df.iterrows()
]

# Add Headlines to initial prompt
headlines_string = str(headlines)
initial_prompt += headlines_string

# Add formatting to get formatted response
format_response = "Give me the information in this format: Relevant Headlines: Portfolio Impact: Recommended Changes: "
initial_prompt += format_response

# Call ChatGPT AI with prompt
response = get_chatgpt_response(initial_prompt).content

# print(response)



# # test_message = get_chatgpt_response("Hello, how are you?").content
# # print(test_message)