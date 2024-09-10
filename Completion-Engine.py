import openai  # Use lowercase 'openai' for the library import

# Ensure your OpenAI API key is set
openai.api_key = 'your-api-key-here'  # Replace with your actual OpenAI API key

# Create a completion request using the ChatCompletion class
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a code completion engine, you will assist the user in writing code based on code-base context."},
        {"role": "user", "content": "Please help me complete this code snippet."}
    ],
    max_tokens=1000,
    temperature=0.7
)

# Extract the completion from the response
completion = response['choices'][0]['message']['content']

# Print the completion
print(completion)
