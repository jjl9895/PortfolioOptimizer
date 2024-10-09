import pinecone
from sentence_transformers import SentenceTransformer
import os
from dotenv import load_dotenv

load_dotenv()

class Vectorizer:
    def __init__(self):
        pinecone.init(api_key=os.getenv('PINECONE_API_KEY'), environment=os.getenv('PINECONE_ENV'))
        self.index = pinecone.Index(os.getenv('PINECONE_INDEX'))
        self.model = SentenceTransformer('all-mpnet-base-v2')

    def vectorize_and_store(self, texts, metadata=None):
        vectors = self.model.encode(texts)
        if metadata is None:
            metadata = [{}] * len(texts)
        to_upsert = list(zip(
            [str(i) for i in range(len(texts))],
            vectors.tolist(),
            [{"text": text, **meta} for text, meta in zip(texts, metadata)]
        ))
        self.index.upsert(vectors=to_upsert)

    def query(self, query_text, top_k=5):
        query_vector = self.model.encode([query_text]).tolist()[0]
        results = self.index.query(query_vector, top_k=top_k, include_metadata=True)
        return [match['metadata']['text'] for match in results['matches']]