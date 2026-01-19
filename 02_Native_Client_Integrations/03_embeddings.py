from dotenv import load_dotenv
load_dotenv()

from gen_ai_hub.proxy.native.openai import embeddings

print("--- OpenAI Embeddings ---")

try:
    input_text = "Every decoding is another encoding."
    model_name = "text-embedding-ada-002"
    
    print(f"Generating embeddings for input: '{input_text}' using model: {model_name}")
    
    response = embeddings.create(
        input=input_text,
        model_name=model_name
    )
    
    # Check if we have data
    if hasattr(response, 'data') and len(response.data) > 0:
        embedding_vector = response.data[0].embedding
        print(f"Success! Embedding vector length: {len(embedding_vector)}")
        print(f"First 5 values: {embedding_vector[:5]}...")
    else:
        print("Response received but no embedding data found.")
        print(response)

except Exception as e:
    print(f"Error generating embeddings: {e}")
    print("Tip: Check if the model_name matches a deployed model in your SAP AI Core instance.")
