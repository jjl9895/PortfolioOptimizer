from openai import OpenAI
import pandas as pd
from dotenv import load_dotenv
import os
import sys

# Load the environment variables from the .env file
def get_latest_news():
    load_dotenv()
    YOUR_API_KEY = os.getenv('PERPLEXITY_YOUR_API_KEY')

    client = OpenAI(api_key=YOUR_API_KEY, base_url="https://api.perplexity.ai")

    messages = [
        {"role": "system", "content": "You are a helpful assistant that provides accurate and concise information."},
        {"role": "user", "content": "Give me 5 of the most relevant and impactful business and financial news today with a focus on US, European, and Chinese markets. Provide each news item in the format: Title | Source | Date | Brief Summary"}
    ]

    response = client.chat.completions.create(
        model="llama-3.1-sonar-large-128k-online",
        messages=messages,
        max_tokens=2000
    )

    news_text = response.choices[0].message.content

    # Process the response and parse the news items
    news_items = news_text.strip().split('\n')

    titles = []
    sources = []
    dates = []
    summaries = []

    for item in news_items:
        parts = item.split(' | ')
        if len(parts) == 4:
            titles.append(parts[0])
            sources.append(parts[1])
            dates.append(parts[2])
            summaries.append(parts[3])

    # Convert to Pandas DataFrame first
    news_df = pd.DataFrame({
        'Title': titles,
        'Source': sources,
        'Date': dates,
        'Summary': summaries
    })

    return news_df

if __name__ == "__main__":
    if "--run_job" in sys.argv:
        news_df = get_latest_news()
        print(news_df)
