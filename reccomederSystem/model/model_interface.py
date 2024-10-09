from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

def model_call(prompt_data):
  client = OpenAI(
    base_url = "https://integrate.api.nvidia.com/v1",
    api_key = os.getenv('NVIDIA_API_KEY')
  )

  prompt = "Give investment reccomndations using this context: "+prompt_data
  completion = client.chat.completions.create(
    model="meta/llama-3.1-405b-instruct",
    messages=[{"role":"user","content":prompt}],
    temperature=0.2,
    top_p=0.7,
    max_tokens=1024,
    stream=True
  )

  for chunk in completion:
    if chunk.choices[0].delta.content is not None:
      print(chunk.choices[0].delta.content, end="")

