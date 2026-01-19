from dotenv import load_dotenv
load_dotenv()

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from gen_ai_hub.proxy.langchain.init_models import init_llm

print("--- LangChain Chat Integration (Harmonized) ---")

try:
    # Initialize the LLM using the harmonized init_llm function
    # This handles proxy client creation and model instantiation automatically.
    # Ensure the model name matches a deployment in your SAP AI Core.
    model_name = 'gpt-4o' 
    print(f"Initializing model: {model_name}...")
    
    # init_llm returns a LangChain compatible model (LLM or ChatModel)
    llm = init_llm(model_name)

    # Define a chat prompt
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant that speaks like a pirate."),
        ("user", "{text}")
    ])

    # Create a chain
    chain = prompt_template | llm | StrOutputParser()

    input_text = "I would like to learn about SAP AI Core."
    print(f"Input: {input_text}")
    
    # Invoke the chain
    response = chain.invoke({'text': input_text})
    print("\nResponse:", response)

except Exception as e:
    print(f"Error calling LangChain: {e}")
    print("Tip: Check if the model_name matches a deployed model in your SAP AI Core instance.")
