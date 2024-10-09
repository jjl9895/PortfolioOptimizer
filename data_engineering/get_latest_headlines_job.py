from openai import OpenAI
import pandas as pd

# Replace with your actual API key
YOUR_API_KEY = "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"

client = OpenAI(api_key=YOUR_API_KEY, base_url="https://api.perplexity.ai")

messages = [
    {"role": "system", "content": "You are a helpful assistant that provides accurate and concise information."},
    {"role": "user", "content": "Give me 30 of the most relevant and impactful business and financial news today with a focus on US, European, and Chinese markets. Provide each news item in the format: Title | Source | Date | Brief Summary"}
]

response = client.chat.completions.create(
    model="llama-3.1-sonar-large-128k-online",
    messages=messages,
    max_tokens=2000
)

news_text = response.choices[0].message.content

# Process the response and save to CSV (rest of the code remains the same)
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

news_df = pd.DataFrame({
    'Title': titles,
    'Source': sources,
    'Date': dates,
    'Summary': summaries
})

csv_file_path = 'business_financial_news.csv'
news_df.to_csv(csv_file_path, index=False)

print(f"News data saved to {csv_file_path}")