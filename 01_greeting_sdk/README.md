# Hello World SDK Project

## Project Capabilities
This project demonstrates how to use the **SAP Generative AI Hub SDK** to build a simple "Hello World" AI agent. It serves as a foundational example for developers getting started with SAP Business Technology Platform (BTP) AI services.

**Key Capabilities:**
- **Connectivity**: Establishes a secure connection to SAP AI Core using service key credentials.
- **Model Interaction**: detailed demonstration of the `OpenAI` compatible client wrapper to interact with deployed Large Language Models (LLMs) like GPT-4.
- **Configuration Management**: Uses `python-dotenv` to securely load sensitive credentials from a `.env` file, keeping them out of source control.
- **Interactive Agent**: A simple CLI interface that accepts user input and generates a context-aware greeting response.

## Prerequisites
Before running this project, ensure you have:
1.  **SAP AI Core Service Key**: JSON key containing `client_id`, `client_secret`, `auth_url`, and `base_url`.
2.  **Deployment ID**: The ID specific to your model deployment (e.g., `gpt-4o`) found in SAP AI Launchpad.
3.  **Python 3.10+**: Python installed on your local machine or available in your environment.

## Installation and Execution

### 1. Visual Studio Code (VS Code)

1.  **Open the Project**:
    - Open Visual Studio Code.
    - Go to **File > Open Folder** and select the `01_hello_world_sdk` directory.

2.  **Create a Virtual Environment** (Recommended):
    - Open the integrated terminal (`Ctrl` + `~`).
    - Run the following command:
      ```powershell
      python -m venv venv
      ```
    - Activate the environment:
      - **Windows**: `.\venv\Scripts\activate`
      - **Mac/Linux**: `source venv/bin/activate`

3.  **Install Dependencies**:
    - With the virtual environment active, install the required packages:
      ```bash
      pip install -r requirements.txt
      ```

4.  **Configure Environment Variables**:
    - Create a new file named `.env` in the root of the project.
    - You can copy the structure from `.env.template`.
    - Fill in your **SAP AI Core Service Key** details and your **Deployment ID**.

5.  **Run the Application**:
    - Execute the main script:
      ```bash
      python main.py
      ```

### 2. SAP Business Application Studio (SAP BAS)

1.  **Import the Project**:
    - Drag and drop the `01_hello_world_sdk` folder into your SAP BAS Dev Space, or clone it if using Git.

2.  **Open a Terminal**:
    - Go to **Terminal > New Terminal**.

3.  **Create a Virtual Environment** (Recommended):
    - Run the following command to create a virtual environment:
      ```bash
      python3 -m venv venv
      ```
    - Activate it:
      ```bash
      source venv/bin/activate
      ```

4.  **Install Dependencies**:
    - With the virtual environment active, install packages:
      ```bash
      pip3 install -r requirements.txt
      ```
    - *Note: Since you are in a virtual environment, `--user` is not needed.*

5.  **Configure Environment Variables**:
    - Right-click in the file explorer and select **New File**. Name it `.env`.
    - Add your credentials in the following format (ensure no spaces around `=`):
      ```ini
      AICORE_CLIENT_ID=your_client_id
      AICORE_CLIENT_SECRET=your_client_secret
      AICORE_AUTH_URL=your_auth_url
      AICORE_BASE_URL=your_core_api_url
      AICORE_RESOURCE_GROUP=default
      ```

6.  **Run the Application**:
    - Execute the script using `python3` (or just `python` if active in venv):
      ```bash
      python3 main.py
      ```

## Project Structure
- `main.py`: The entry point script containing the agent logic.
- `requirements.txt`: List of Python dependencies (`sap-ai-sdk-gen`, `python-dotenv`).
- `.env`: Configuration file for secrets (ignored by Git).
- `.gitignore`: Specifies files to be ignored by version control.

## Git Integration (Exporting to Git)

> **Prerequisite**: Ensure **Git** is installed on your system.
> *   **VS Code (Local)**: Download and install from [git-scm.com](https://git-scm.com/downloads).
> *   **SAP BAS**: Git is pre-installed.

### 1. Visual Studio Code

1.  **Initialize Repository**:
    - Click on the **Source Control** icon in the sidebar (or press `Ctrl+Shift+G`).
    - Click **Initialize Repository**.
2.  **Stage Changes**:
    - You will see a list of files under "Changes".
    - Hover over the "Changes" header and click the **+** (Stage All Changes) icon.
3.  **Commit**:
    - Enter a message in the "Message" box (e.g., "Initial commit").
    - Click **Commit**.
4.  **Push to Remote**:
    - If you have a remote repository (e.g., GitHub), open the command palette (`Ctrl+Shift+P`).
    - Type `Git: Add Remote` and provide the URL.
    - Then use **Publish Branch** or **Push** from the Source Control menu.

### 2. SAP Business Application Studio (SAP BAS)

1.  **Initialize Repository**:
    - Click on the **Source Control** (Git) icon on the left sidebar.
    - Click **Initialize Repository**.
2.  **Stage Changes**:
    - Click the **+** icon next to "Changes" to stage all files.
3.  **Commit**:
    - Enter a commit message in the text box.
    - Click **Commit**.
4.  **Push to Remote**:
    - Open the command palette (`F1` or `Ctrl+Shift+P`).
    - Type `Git: Add Remote` and enter your repository URL.
    - Type `Git: Push` to push your changes.
