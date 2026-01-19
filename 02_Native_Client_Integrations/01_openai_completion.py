from dotenv import load_dotenv
load_dotenv()

from gen_ai_hub.proxy.native.openai import chat

print("--- OpenAI Chat Completion ---")

# Define the messages for the chat
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Explain quantum computing in one sentence."}
]

# Configure the request
# ensuring we use a model likely to be available. 'gpt-4o' or 'gpt-35-turbo' are common.
# You may need to change 'model_name' to match your specific SAP AI Core deployment.
kwargs = dict(model_name='gpt-4o', messages=messages) 

try:
    print(f"Sending request to OpenAI model: {kwargs['model_name']}...")
    response = chat.completions.create(**kwargs)
    print("Response received:")
    print(response)
    print("\nContent:", response.choices[0].message.content)
except Exception as e:
    print(f"Error calling OpenAI: {e}")
    print("Tip: Check if the model_name matches a deployed model in your SAP AI Core instance.")
