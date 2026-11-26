import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url=os.getenv("endpoint"),
    api_key=os.getenv("api_key"),
)

response = client.chat.completions.create(
    model="gpt-5.4-mini",
    messages=[
        {"role": "system", "content": "You are an AI assistant that provides insightful and inspiring motivational quotes. Your goal is to uplift and encourage users. You should always be positive and thoughtful. Do not generate quotes that are generic or cliché."},
        {"role": "user", "content": "Tell me a quote about perseverance."},
    ],
)

print(response.choices[0].message.content)
