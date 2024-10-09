from pinecone import Pinecone, ServerlessSpec
from sentence_transformers import SentenceTransformer
import os
from dotenv import load_dotenv
import json
from datetime import datetime

load_dotenv()

class Vectorizer:
    def __init__(self):
        self.pc = Pinecone(api_key=os.getenv('PINECONE_API_KEY'))
        self.news_index_name = "financial-news-index"
        self.recommendations_index_name = "investment-recommendations-index"
        self.ensure_indexes_exist()
        self.news_index = self.pc.Index(self.news_index_name)
        self.recommendations_index = self.pc.Index(self.recommendations_index_name)
        self.model = SentenceTransformer('all-mpnet-base-v2')

    def ensure_indexes_exist(self):
        for index_name in [self.news_index_name, self.recommendations_index_name]:
            if index_name not in self.pc.list_indexes().names():
                self.pc.create_index(
                    name=index_name,
                    dimension=768,
                    metric='cosine',
                    spec=ServerlessSpec(
                        cloud='aws',
                        region='us-east-1'
                    )
                )
                print(f"Created new index: {index_name}")
            else:
                print(f"Using existing index: {index_name}")

    def vectorize_and_store_news(self, headlines, metadata=None):
        vectors = self.model.encode(headlines)
        if metadata is None:
            metadata = [{}] * len(headlines)
        to_upsert = list(zip(
            [f"headline_{datetime.now().timestamp()}_{i}" for i in range(len(headlines))],
            vectors.tolist(),
            [{"text": headline, "type": "financial_news", "timestamp": datetime.now().isoformat(), **meta} 
             for headline, meta in zip(headlines, metadata)]
        ))
        self.news_index.upsert(vectors=to_upsert)
        print(f"Stored {len(headlines)} headlines in the news index")

    def store_recommendation(self, recommendation, user_response, user_id, context, risk_profile='moderate'):
        vector = self.model.encode([recommendation]).tolist()[0]
        timestamp = datetime.now().isoformat()
        id = f"rec_{user_id}_{timestamp}"
        metadata = {
            "recommendation": recommendation,
            "user_response": user_response,
            "user_id": user_id,
            "context": json.dumps(context),
            "risk_profile": risk_profile,
            "timestamp": timestamp
        }
        self.recommendations_index.upsert(vectors=[(id, vector, metadata)])
        print(f"Stored recommendation for user {user_id}")

    def query_news(self, query_text, top_k=5):
        query_vector = self.model.encode([query_text]).tolist()[0]
        results = self.news_index.query(vector=query_vector, top_k=top_k, include_metadata=True)
        return [match['metadata']['text'] for match in results['matches']]

    def query_recommendations(self, query_text, user_id, top_k=5):
        query_vector = self.model.encode([query_text]).tolist()[0]
        results = self.recommendations_index.query(
            vector=query_vector,
            top_k=top_k,
            include_metadata=True,
            filter={"user_id": user_id}
        )
        return [match['metadata'] for match in results['matches']]

    def get_user_preferences(self, user_id):
        results = self.recommendations_index.query(
            vector=[0] * 768,  # Dummy vector
            top_k=1000,
            include_metadata=True,
            filter={"user_id": user_id}
        )
        accepted = [r['metadata'] for r in results['matches'] if r['metadata']['user_response'] == 'yes']
        rejected = [r['metadata'] for r in results['matches'] if r['metadata']['user_response'] == 'no']
        return accepted, rejected