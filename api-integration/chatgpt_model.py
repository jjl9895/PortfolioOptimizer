from openai import OpenAI
import os


def get_chatgpt_response(user_query, model_name="gpt-4o-mini", system_prompt="You are an intelligent financial and wealth management advisor"):
    client = OpenAI(api_key=os.environ["CHATGPT_API_KEY"])
    return client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": system_prompt},
            {
                "role": "user",
                "content": user_query
            }
        ]
    ).choices[0].message