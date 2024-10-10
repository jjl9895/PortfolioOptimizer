import time
from .api_integration.chatgpt_model import get_chatgpt_response

from .reccomederSystem.investment_reccomender import InvestmentRecommender
from .get_account_data_job import get_trading_account_details
import alpaca_trade_api as tradeapi

def generate_initial_response(special_request="Please adjust my portfolio to have less risk and more long-term gain."):
     # Read data
     headlines = []
     with open('news_output.txt', "r") as file:
         headlines = file.readlines()
     # Gets trading account details from Alpaca API 
     account_data = get_trading_account_details()
     str_account_data = str(account_data)
     # Generate prompts
     # headlines = [
     #     f"This is the headline and summary data: {row['Title']}: {row['Summary']}"
     #     for _, row in df.iterrows()
     # ]
     recommender = InvestmentRecommender()
     recommender.add_financial_news(headlines)
     response = recommender.get_recommendation(special_request, "user123",str_account_data)
     """
     initial_prompt = f"Based on the following context: \n {vector_context}\n and my portfolio {str_account_data}, provide recommendations to the portfolio based on the following request: {special_request}"
     # Add formatting to get formatted response
     format_response = f"{initial_prompt} Your recommendation should be concise, well-reasoned, and tailored to the user's preferences and risk profile. Provide the output in the relevant Headlines: Portfolio Impact: Recommended Changes: "
     # Call ChatGPT AI with prompt
     response = get_chatgpt_response(format_response).content
     """
     return response

if __name__ == "__main__":
    response = generate_initial_response("Please add more risk to my investment portfolio.")
    print(response)