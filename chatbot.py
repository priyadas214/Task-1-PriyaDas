# =================================
# RULE-BASED AI CHATBOT
# Internship Project
# =================================

name = input("Enter your name: ")

print("\n=================================")
print("WELCOME TO RULE-BASED AI CHATBOT")
print("=================================")
print(f"Hello, {name}! 👋")
print("Type 'menu' to see available commands.")
print("Type 'bye' to exit.\n")

message_count = 0

while True:

    user_input = input("You: ").lower().strip()
    message_count += 1

    # Greetings
    if user_input in ["hello", "hi", "hey"]:
        print(f"Bot: Hello, {name}! How can I help you today?")

    elif user_input == "good morning":
        print("Bot: Good Morning! Hope you have a productive day.")

    elif user_input == "good afternoon":
        print("Bot: Good Afternoon!")

    elif user_input == "good evening":
        print("Bot: Good Evening!")

    # General Questions
    elif user_input == "how are you":
        print("Bot: I am doing well. Thanks for asking!")

    elif user_input == "your name":
        print("Bot: My name is RuleBot.")

    elif user_input == "who made you":
        print("Bot: I was created by an AI Internship student using Python.")

    elif user_input == "what can you do":
        print("Bot: I can answer simple questions using rule-based logic.")

    elif user_input == "help":
        print("Bot: Type 'menu' to see all available commands.")

    # AI Related Questions
    elif user_input == "what is ai":
        print("Bot: AI stands for Artificial Intelligence.")

    elif user_input == "what is machine learning":
        print("Bot: Machine Learning enables computers to learn from data.")

    elif user_input == "what is python":
        print("Bot: Python is a popular programming language used in AI and Data Science.")

    # Mood Detection
    elif user_input == "i am happy":
        print("Bot: That's wonderful! Keep smiling. 😊")

    elif user_input == "i am sad":
        print("Bot: I hope things get better soon. Stay positive! 💙")

    elif user_input == "i am tired":
        print("Bot: Remember to take breaks and stay hydrated.")

    # Thank You
    elif user_input in ["thank you", "thanks"]:
        print("Bot: You're welcome! 😊")

    # Menu
    elif user_input == "menu":
        print("""
======== AVAILABLE COMMANDS ========

Greetings:
- hello
- hi
- hey
- good morning

General:
- how are you
- your name
- who made you
- what can you do
- help

AI Related:
- what is ai
- what is machine learning
- what is python

Mood:
- i am happy
- i am sad
- i am tired

Others:
- thank you
- menu
- bye

====================================
""")

    # Exit
    elif user_input == "bye":
        print(f"\nBot: Goodbye, {name}! 👋")
        print(f"Bot: Total messages exchanged: {message_count}")
        print("Bot: Thank you for using Rule-Based AI Chatbot.")
        break

    # Unknown Input
    else:
        print("Bot: Sorry, I don't understand that.")
        print("Bot: Type 'menu' to see available commands.")