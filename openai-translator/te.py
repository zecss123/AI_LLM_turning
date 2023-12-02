import openai
from openai import OpenAI
client = OpenAI(
                        base_url="https://api.openai-sb.com/v1/",
                        api_key="sb-d6efde3bcd856bd5da4b4f3b6ed0df7b6642717d8438b123"
                    )#export OPENAI_API_KEY="sb-d6efde3bcd856bd5da4b4f3b6ed0df7b6642717d8438b123"
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": 'hi'}
    ]
)
print(response)
translation = response.choices[0].message['content'].strip()