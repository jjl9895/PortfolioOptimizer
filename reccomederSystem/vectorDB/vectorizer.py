from pinecone import Pinecone, ServerlessSpec
from sentence_transformers import SentenceTransformer
import os
from dotenv import load_dotenv

load_dotenv()

class Vectorizer:
    def __init__(self):
        self.pc = Pinecone(api_key=os.getenv('PINECONE_API_KEY'))
        self.index_name = "financial-news-index"
        self.ensure_index_exists()
        self.index = self.pc.Index(self.index_name)
        self.model = SentenceTransformer('all-mpnet-base-v2')

    def ensure_index_exists(self):
        if self.index_name not in self.pc.list_indexes().names():
            self.pc.create_index(
                name=self.index_name,
                dimension=768,  # Dimension of the all-mpnet-base-v2 model
                metric='cosine',
                spec=ServerlessSpec(
                    cloud='aws',
                    region='us-west-2'
                )
            )
            print(f"Created new index: {self.index_name}")
        else:
            print(f"Using existing index: {self.index_name}")

    def vectorize_and_store(self, headlines, metadata=None):
        vectors = self.model.encode(headlines)
        if metadata is None:
            metadata = [{}] * len(headlines)
        to_upsert = list(zip(
            [f"headline_{i}" for i in range(len(headlines))],
            vectors.tolist(),
            [{"text": headline, "type": "financial_news", **meta} for headline, meta in zip(headlines, metadata)]
        ))
        self.index.upsert(vectors=to_upsert)
        print(f"Stored {len(headlines)} headlines in the index")

    def query(self, query_text, top_k=5):
        query_vector = self.model.encode([query_text]).tolist()[0]
        results = self.index.query(vector=query_vector, top_k=top_k, include_metadata=True)
        return [match['metadata']['text'] for match in results['matches']]