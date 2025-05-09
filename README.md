# Chatbot using LangChain and Ollama

This is a Python-based chatbot application built using `LangChain` and `Ollama` for natural language processing. The bot uses the Llama3 model to answer user queries in a friendly and helpful manner.

## Features

- Friendly and context-aware conversations.
- Remembers conversation history to maintain context for each query.
- Easily extendable for various use cases.

## Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/Bhavya773-coder/Simple_Local_Chatbot.git
   cd Simple_Local_Chatbot
Install the necessary dependencies:
pip install langchain_ollama langchain
Install any additional dependencies if required by the Ollama library, such as specific model files or services.
Usage

After cloning the repo and installing dependencies, run the following command to start the chatbot:
python chatbot.py
The bot will prompt you to input questions. You can type your questions, and the bot will answer them based on the context of the conversation.
To end the conversation, type exit.
Example interaction:

Welcome to the conversation! You can ask me anything.
You: What is the capital of France?
Bot: The capital of France is Paris.
You: What is the Eiffel Tower?
Bot: The Eiffel Tower is a famous landmark located in Paris, France.
Code Breakdown

OllamaLLM: Used to interact with the Llama3 model for natural language processing.
ChatPromptTemplate: A custom template that structures the input and output format for the model.
Conversation Context: The bot remembers the entire conversation history to provide relevant responses based on the context.
Contributing

Feel free to fork the repository, open issues, or submit pull requests for improvements. All contributions are welcome!


Contact

For any questions or suggestions, feel free to reach out to:

Email: mashrubhavya5@gmail.com
GitHub: @Bhavya773-coder
