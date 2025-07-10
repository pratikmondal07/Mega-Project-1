from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(api_key="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",)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "what is coding"}
  ]
)

print(completion.choices[0].message.content)