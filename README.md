**Chambulilo Chatbot**

- Chambulilo is an AI-powered chatbot developed using the OpenAI API. It is designed to interact with users in a conversational manner, providing responses based on user input.

**Developed By**
- Kasim
  
**Prerequisites**
- Python 3.7 or higher
- OpenAI Python client library

  
**Installation**
- Clone the repository

```
git clone https://github.com/your-repo/chambulilo-chatbot.git
cd chambulilo-chatbot
```
**Install dependencies**
- Use the package manager pip to install the required dependencies.

```
pip install openai
```
**Set up OpenAI API Key**
- Replace the placeholder in the script with your actual OpenAI API key. Do not hardcode your API key in the code for production environments. Use environment variables or a secure method to manage your keys.

```
openai.api_key = "your_openai_api_key_here"
```

**Usage**
- To start the chatbot, run the main.py script:

```
python main.py
```
- Once the script is running, you can interact with the chatbot by typing messages into the console.

**Example**
```
Human: Hello, Chambulilo!
Bot: Hello! How can I assist you today?
```

**Customization**
- You can customize the chatbot's behavior and responses by modifying the system_command variable in the script. The system command sets the initial instructions for the AI model.

```
system_command = '''
act as a chatbot
your name is chambulilo and you are developed by kasim!
'''
```

**Contributing**

If you have suggestions or would like to contribute to the project, feel free to open a pull request or submit an issue on the GitHub repository.
