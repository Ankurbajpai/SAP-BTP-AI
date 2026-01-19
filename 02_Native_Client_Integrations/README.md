# Native Client Integrations

## Motive
The **Native Client Integrations** project demonstrates how to leverage the **SAP Generative AI Hub SDK** to natively integrate SAP applications with various global AI Model Providers.

Traditionally, interacting with SAP AI Core might require specific SAP libraries. However, this project showcases how you can use **standard, industry-favorite SDKs**—such as the official OpenAI Python library, Google's Vertex AI SDK, Amazon's Boto3, and LangChain—while seamlessly routing your requests through SAP AI Core for governance, security, and compliance.

**Key Benefits:**
- **Zero Friction**: Use the tools and libraries you already know (e.g., `import openai`).
- **Unified Governance**: All traffic is proxied and managed by SAP AI Core.
- **Multi-Provider Support**: Switch between OpenAI GPT-4, Google Gemini, and Amazon Bedrock models easily.

## Project Overview

This project provides two ways to explore the integrations:
1.  **Standalone Python Scripts**: Simple, single-file examples to run in your terminal. Great for learning the syntax.
2.  **Full Web Application**: A SAP Fiori (UI5) frontend connected to a FastAPI backend. Great for seeing an end-to-end implementation pattern.

## Prerequisites

Before you start, ensure you have the following:
- **SAP BTP Account** with SAP AI Core subscription (Generative AI Hub plan).
- **Service Key** for your SAP AI Core instance.
- **Python 3.10+** installed.
- **Node.js** (v16 or higher) and **npm**.

## Setup & Configuration

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/Ankurbajpai/SAP-BTP-AI.git
    cd SAP-BTP-AI/02_Native_Client_Integrations
    ```

2.  **Create Environment File**
    Create a file named `.env` in this directory (`02_Native_Client_Integrations`).
    Add the credentials from your SAP AI Core Service Key:
    ```env
    AICORE_AUTH_URL=<url>
    AICORE_CLIENT_ID=<clientid>
    AICORE_CLIENT_SECRET=<clientsecret>
    AICORE_BASE_URL=<serviceurls.AI_API_URL>
    AICORE_RESOURCE_GROUP=<resource_group_id>
    ```

3.  **Install Dependencies**
    
    ### Option A: VS Code (Local Development)
    
    Open a terminal in the `02_Native_Client_Integrations` directory:
    ```powershell
    # Windows
    python -m venv venv
    .\venv\Scripts\activate
    
    # Mac/Linux
    python3 -m venv venv
    source venv/bin/activate
    
    # Install Python Dependencies
    pip install -r requirements.txt

    # Install Frontend Dependencies
    npm install
    ```

    ### Option B: SAP Business Application Studio (BAS)
    
    Open a Terminal in BAS:
    ```bash
    # Create Virtual Environment (Optional but recommended)
    python3 -m venv venv
    source venv/bin/activate

    # Install Python Dependencies
    pip install -r requirements.txt

    # Install Frontend Dependencies
    npm install
    ```

## Usage Option 1: Standalone Scripts (Quick Start)

Run these scripts directly to test connectivity and see the code in action.

*Note: You may need to edit the `model_name` inside these scripts to match the specific Deployment ID or Model Name in your SAP AI Core instance.*

```powershell
# Run OpenAI Example
python 01_openai_completion.py

# Run Vertex AI (Gemini) Example
python 02_vertex_ai_completion.py
```
*(Run other scripts similarly: `03_embeddings.py`, `04_langchain_chat.py`, `05_amazon_bedrock.py`)*

## Usage Option 2: Full Web Application

### Run in VS Code (Local)

1.  **Start the Backend Server**
    Open a terminal and run:
    ```powershell
    # Ensure your virtual environment is active (.\venv\Scripts\activate)
    npm run start:backend
    ```
    *Starts the FastAPI server on `http://localhost:8090`.*

2.  **Start the Frontend Application**
    Open a **new** terminal and run:
    ```powershell
    npm run start
    ```
    *Starts the Fiori app on `http://localhost:8080` and opens it in your default browser.*

### Run in SAP Business Application Studio (BAS)

1.  **Start the Backend Server**
    Open a Terminal and run:
    ```bash
    # Ensure virtual environment is active (source venv/bin/activate)
    # You might need to use python3 explicitly if the npm script fails
    python3 -m backend.server
    ```
    *A pop-up notification will appear asking to **"Expose Port 8090"**. Click **"Expose"** or "Open".*

2.  **Start the Frontend Application**
    Open a **new** Terminal and run:
    ```bash
    npm run start
    ```
    *A pop-up will appear to open the application in a new tab.*

## Project Structure

- **`01_openai_completion.py`** to **`05_amazon_bedrock.py`**: Standalone example scripts.
- **`backend/`**: Contains `server.py`, the FastAPI backend that powers the web app.
- **`webapp/`**: Contains the SAPUI5 (Fiori) frontend source code.
- **`package.json`**: Scripts for running the full stack application.
- **`requirements.txt`**: Python dependencies.
