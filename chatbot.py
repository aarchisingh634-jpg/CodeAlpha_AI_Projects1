print("Chatbot started! Type 'exit' to stop.")

while True:
    user = input("You: ")

    if user.lower() == "hi":
        print("Bot: Hello!")
    elif user.lower() == "how are you":
        print("Bot: I am fine!")
    elif user.lower() == "exit":
        break
    else:
        print("Bot: I don't understand")
