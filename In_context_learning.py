client = OpenAI(api_key="<OPENAI_API_TOKEN>")

response = client.chat.completions.create(
   model="gpt-4o-mini",
   # Add a user and assistant message for in-context learning
   messages=[
     {"role": "system", "content": "You are a helpful Python programming tutor."},
     {"role": "user", "content":"Explain what the min() Python function does"},
     {"role":"assistant", "content":"The min() function returns the smallest item from an iterable"},
     {"role": "user", "content": "Explain what the type() function does."}
   ]
)

print(response.choices[0].message.content)