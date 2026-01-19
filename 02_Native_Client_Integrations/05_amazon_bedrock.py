from dotenv import load_dotenv
load_dotenv()
import json
from gen_ai_hub.proxy.native.amazon.clients import Session

print("--- Amazon Bedrock Integration ---")

try:
    # Initialize the Amazon Bedrock session via SAP AI Core proxy
    # Adjust 'model_name' to match a deployed model in your SAP AI Core instance.
    # Example: "amazon--titan-text-express" or "anthropic--claude-3-sonnet" (if proxied via Bedrock)
    model_name = "anthropic--claude-3-sonnet"
    
    print(f"Initializing Session for model: {model_name}...")
    bedrock = Session().client(model_name=model_name)
    
    body = json.dumps({
        "inputText": "Please recommend books with a theme similar to the movie 'Inception'.",
        "textGenerationConfig": {
            "maxTokenCount": 512,
            "stopSequences": [],
            "temperature": 0,
            "topP": 1
        }
    })
    
    print("Invoking model...")
    response = bedrock.invoke_model(body=body)
    
    response_body = json.loads(response.get("body").read())
    print("\nResponse Body:")
    print(response_body)
    
    # Extract text if possible (Titan format)
    if 'results' in response_body:
        print("\nGenerated Text:", response_body['results'][0]['outputText'])

except Exception as e:
    print(f"Error calling Amazon Bedrock: {e}")
    print("Tip: Check if the model_name matches a deployed model in your SAP AI Core instance.")
