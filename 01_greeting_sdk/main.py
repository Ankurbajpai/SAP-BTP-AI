import os
from dotenv import load_dotenv
from gen_ai_hub.proxy.native.openai import OpenAI

def run_greeting_agent():
    """
    Main entry point for the SAP AI Core SDK Greeting Agent.
    Updated to use the modern OpenAI-compatible interface of the Generative AI Hub SDK.
    """
    load_dotenv()
    
    # -------------------------------------------------------------------------
    # IMPORTANT: In SAP AI Core, 'model' refers to your DEPLOYMENT ID.
    # You can find this in SAP AI Launchpad under 'Deployments'.
    # -------------------------------------------------------------------------
    deployment_id = "gpt-4o" # Replace this with your actual Deployment ID
    
    print("--- SAP AI Core SDK Greeting Agent ---")
    
    # 1. Initialize the OpenAI Client for Generative AI Hub
    try:
        print(f"Connecting to SAP AI Core using Deployment ID: {deployment_id}...")
        # The client automatically picks up configuration from .env variables
        client = OpenAI()
    except Exception as e:
        print(f"CRITICAL ERROR: Could not initialize SAP AI Core client.")
        print(f"Details: {e}")
        print("\nPlease ensure:")
        print("1. Your .env file contains: AICORE_CLIENT_ID, AICORE_CLIENT_SECRET, AICORE_AUTH_URL, AICORE_BASE_URL")
        print("2. You have a valid deployment ID set in the 'deployment_id' variable.")
        return

    # 2. Define the Agent Persona & Interaction
    name = input("\nWhat is your name? ") or "Developer"
    
    system_message = (
        "You are a helpful SAP AI Assistant. Your personality is professional, "
        "encouraging, and knowledgeable about SAP BTP. Greet the user and "
        "mention that they are successfully using the SAP AI Core SDK."
    )
    
    user_message = f"Hello! My name is {name}. I've just set up my first SAP AI Core SDK project. I want a guide to develope more use-cases in SAP AI Core."

    # 3. Request Chat Completion
    try:
        print("\nAgent is thinking...")
        response = client.chat.completions.create(
            model=deployment_id,
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_message}
            ]
        )
        
        # 4. Display the result
        ai_greeting = response.choices[0].message.content
        print(f"\n--- AI RESPONSE ---\n")
        print(ai_greeting)
        print(f"\n--------------------\n")
        
    except Exception as e:
        print(f"Error during AI generation: {e}")
        print("\nTIP: If you get a 404, double-check that your 'deployment_id' matches the ID in AI Launchpad.")

if __name__ == "__main__":
    run_greeting_agent()
