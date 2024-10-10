from .vectorDB.vectorizer import Vectorizer
from .model.model_interface import model_call
import json



class InvestmentRecommender:
    def __init__(self):
        self.vectorizer = Vectorizer()

    def add_financial_news(self, headlines, metadata=None):
        self.vectorizer.vectorize_and_store_news(headlines, metadata)

    def get_recommendation(self, query, user_id, risk_profile='moderate'):
        relevant_headlines = self.vectorizer.query_news(query)
        past_recommendations = self.vectorizer.query_recommendations(query, user_id)
        accepted, rejected = self.vectorizer.get_user_preferences(user_id)

        context = "\n".join(relevant_headlines)
        past_rec_context = json.dumps(past_recommendations, indent=2)
        accepted_context = json.dumps(accepted, indent=2)
        rejected_context = json.dumps(rejected, indent=2)

        prompt = f"""Based on the following information:

Recent financial news:
{context}

User's past recommendations:
{past_rec_context}

User's accepted recommendations:
{accepted_context}

User's rejected recommendations:
{rejected_context}

User's risk profile: {risk_profile}

Please provide a personalized investment recommendation for the following query: {query}

Your recommendation should be concise, well-reasoned, and tailored to the user's preferences and risk profile. 
Take into account the user's past responses to recommendations.
Give me the information in this format: 

Relevant Headlines: 

Portfolio Impact: 

Recommended Changes:
"""
        print(prompt)

        recommendation = model_call(prompt)
        return recommendation

    def store_user_response(self, recommendation, user_response, user_id, context, risk_profile='moderate'):
        if recommendation and user_response:
            self.vectorizer.store_recommendation(recommendation, user_response, user_id, context, risk_profile)
        else:
            print("Error: Recommendation or user response is missing.")

# Example usage
def reccomender():
    recommender = InvestmentRecommender()
    
    # Add some sample financial news
    headlines = [
        "Tech stocks surge as AI adoption accelerates",
        "Federal Reserve hints at potential interest rate cut",
        "Oil prices volatile amid Middle East tensions",
        "Green energy sector sees record investment inflows",
        "Cryptocurrency market stabilizes after recent volatility"
    ]
    recommender.add_financial_news(headlines)

    user_id = "user123"
    risk_profile = "moderate"

    # Get a recommendation
    query = "What's a good investment strategy given the current market conditions?"
    recommendation = recommender.get_recommendation(query, user_id, risk_profile)
    print(f"Query: {query}\n")
    print(f"Recommendation: ")
    print(recommendation)
    # for chunk in recommendation:
    #     if chunk.choices[0].delta.content is not None:
    #         print(chunk.choices[0].delta.content, end="")

    # Now, let's assume the user has responded to this recommendation
    # This would typically be called separately, after the user has made a decision
    user_response = "yes"  # or "no"
    if recommendation:  # Only store if we have a valid recommendation
        print("TRIAL")
        recommender.store_user_response(recommendation, user_response, user_id, headlines, risk_profile)

    # Get another recommendation (this time it will consider the previous response if it was stored)
    query = "Should I invest in tech stocks?"
    recommendation = recommender.get_recommendation(query, user_id, risk_profile)
    print(f"\nQuery: {query}\n")
    print(f"Recommendation: ")
    print(recommendation)

reccomender()
