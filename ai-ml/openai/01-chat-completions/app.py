import os
from openai import OpenAI

# Access the API key from the environment variable
api_key = os.environ.get('OPENAI_API_KEY')

# Initialize the OpenAI API client
OpenAI.api_key = api_key

client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"}
  ]
)

print(completion.choices[0].message)