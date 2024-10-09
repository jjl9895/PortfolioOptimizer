from vectorDB.vectorizer import Vectorizer
from model.model_interface import model_call

class InvestmentRecommender:
    def __init__(self):
        self.vectorizer = Vectorizer()

    def add_investment_data(self, investment_texts, metadata=None):
        self.vectorizer.vectorize_and_store(investment_texts, metadata)

    def get_recommendation(self, query):
        relevant_contexts = self.vectorizer.query(query)
        context = "\n".join(relevant_contexts)
        prompt = f"""Based on the following investment information:

{context}

Please provide an investment recommendation for the following query: {query}

Your recommendation should be concise, well-reasoned, and based on the provided information."""

        recommendation = model_call(prompt)
        return recommendation

# Example usage
if __name__ == "__main__":
    recommender = InvestmentRecommender()
    
    # Add some sample investment data
    investment_data = [
        "Tech stocks have shown high volatility but strong growth potential.",
        "Bond yields are currently low, offering stability but limited returns.",
        "Renewable energy sector is expanding rapidly due to global climate initiatives.",
        "Real estate market is experiencing a slowdown in urban areas.",
        "Cryptocurrency remains a high-risk, high-reward investment option."
    ]
    recommender.add_investment_data(investment_data)

    # Get a recommendation
    query = "What's a good investment strategy for a risk-averse investor in the current market?"
    recommendation = recommender.get_recommendation(query)
    print(f"Query: {query}\n")
    print(f"Recommendation: {recommendation}")