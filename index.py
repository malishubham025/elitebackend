import os
from openai import OpenAI
# Initialize the OpenAI client with your secure API key
client = OpenAI(api_key=os.environ.get('openai'))

completion = client.chat.completions.create(
model="gpt-3.5-turbo",
messages=[
  {"role": "system", "content": "hello who are you"}

  ]
)
topic_name=completion.choices[0].message.content
print(topic_name)
    # Topics=completion.choices[0].message.content

