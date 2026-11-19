"""
Project: Rule-Based Chatbot
Internship: CodeOrbit Tech - Artificial Intelligence Internship
Developer: Iswariya C

A beginner-friendly chatbot that uses predefined rules and keywords.
"""


def chatbot_response(user_input):
    """Return a response based on simple keyword and phrase rules."""
    message = user_input.lower().strip()

    # Rule 1: Greetings
    if message in ["hi", "hello", "hey", "good morning", "good evening"]:
        return "Hello! Welcome. How can I help you?"

    # Rule 2: Chatbot identity
    elif "your name" in message or "who are you" in message:
        return "I am a Rule-Based Chatbot created using Python."

    # Rule 3: General conversation
    elif "how are you" in message:
        return "I am doing great! Thank you for asking."

    # Rule 4: Artificial Intelligence information
    elif "what is ai" in message or "artificial intelligence" in message:
        return (
            "AI stands for Artificial Intelligence. "
            "It helps machines perform tasks that normally require human intelligence."
        )

    # Rule 5: Python information
    elif "python" in message:
        return "Python is a simple and powerful programming language."

    # Rule 6: Help request
    elif "help" in message:
        return "Sure! I am here to answer your basic questions."

    # Rule 7: Thank-you response
    elif "thank" in message:
        return "You are welcome! Happy to help you."

    # Rule 8: Goodbye
    elif message in ["bye", "goodbye", "exit", "quit"]:
        return "Goodbye! Have a nice day."

    # Rule 9: Fallback for unknown input
    else:
        return "Sorry, I don't understand that question. Please try asking something else."


def main():
    """Run the chatbot conversation loop."""
    print("=" * 40)
    print("       WELCOME TO AI CHATBOT")
    print("=" * 40)
    print("Type 'bye' to end the conversation.")

    while True:
        user_input = input("\nYou: ")
        response = chatbot_response(user_input)
        print("Chatbot:", response)

        if user_input.lower().strip() in ["bye", "goodbye", "exit", "quit"]:
            break


if __name__ == "__main__":
    main()
