import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("api_key"),
    base_url="http://localhost:3001/v1"
)

response = client.chat.completions.create(
    model="auto",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "What is the value of sin 60 degrees?"}
    ]
)

print(response.choices[0].message.content)