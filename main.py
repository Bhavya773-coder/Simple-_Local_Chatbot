from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

templet ="""
Awnser the following question in a friendly and helpful manner.
Conversation History:{context}
User Question: {question}
Assistant Answer:"""

model = OllamaLLM(model="llama3")
prompt=ChatPromptTemplate.from_template(templet)
chain=prompt | model


def handle_conversation():
    context = ""
    print("Welcome to the conversation! You can ask me anything.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        result = chain.invoke(
            {
                "context": context,
                "question": user_input
            }
        )
        print("Bot:", result)
        context+= f"User: {user_input}\nBot: {result}\n"


result=chain.invoke(
    {
        "context": "",
        "question": "What is the capital of France?"
    }
)

print(result)
if __name__ == "__main__":
    handle_conversation()