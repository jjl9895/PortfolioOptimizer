# In your file that handles user responses
from investment_recommender import InvestmentRecommender

recommender = InvestmentRecommender()

def handle_user_response(recommendation, user_response, user_id, context, risk_profile):
    recommender.store_user_response(recommendation, user_response, user_id, context, risk_profile)

# Example usage
recommendation = "Based on current market conditions, consider diversifying your portfolio with a mix of tech stocks and stable dividend-paying companies."
user_response = "yes"
user_id = "user123"
context = ["Tech stocks surge", "Federal Reserve hints at rate cut"]
risk_profile = "moderate"

handle_user_response(recommendation, user_response, user_id, context, risk_profile)