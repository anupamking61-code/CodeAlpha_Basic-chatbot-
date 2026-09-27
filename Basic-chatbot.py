def chatbot():
    print("Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user_input = input("You: ").strip().lower()

        if user_input == "hello":
            print("Chatbot: Hi!")

        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks!")

        elif user_input == "what is your name":
            print("Chatbot: I am a basic Python chatbot.")

        elif user_input == "bye":
            print("Chatbot: Goodbye!")
            break

        else:
            print("Chatbot: I am not sure how to respond to that.")


if __name__ == "__main__":
    chatbot()
