from dotenv import load_dotenv
load_dotenv()

from gen_ai_hub.proxy.native.google_vertexai.clients import GenerativeModel
from gen_ai_hub.proxy.core.proxy_clients import get_proxy_client

print("--- Vertex AI Gemini Generation ---")

try:
    proxy_client = get_proxy_client('gen-ai-hub')
    
    # Using 'gemini-1.5-flash' as a standard modern model. 
    # Adjust 'model_name' if your deployment differs.
    kwargs = dict({'model_name': 'gemini-2.5-pro'})
    
    print(f"Initializing GenerativeModel with {kwargs['model_name']}...")
    model = GenerativeModel(proxy_client=proxy_client, **kwargs)

    content = [{"role": "user", "parts": [{"text": "Write a haiku about a software bug."}]}]
    
    print("Sending generate_content request...")
    model_response = model.generate_content(content)
    
    print("Response received:")
    print(model_response)
    if hasattr(model_response, 'text'):
        print("\nText:", model_response.text)
except Exception as e:
    print(f"Error calling Vertex AI: {e}")
    print("Tip: Check if the model_name matches a deployed model in your SAP AI Core instance.")
