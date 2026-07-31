from datetime import datetime


def chatbot():

    print("=" * 50)
    print("CODE ALPHA SMART CHATBOT")
    print("=" * 50)
    print("Type 'help' to see available commands.")
    print("Type 'bye' to exit.\n")

    while True:

        user = input("You : ").lower().strip()

        if user == "hello":
            print("Bot : Hello! Nice to meet you.")

        elif user == "hi":
            print("Bot : Hi! How can I help you?")

        elif user == "how are you":
            print("Bot : I am fine. Thanks for asking.")

        elif user == "your name":
            print("Bot : My name is CodeAlpha Bot.")

        elif user == "python":
            print("Bot : Python is a powerful programming language.")

        elif user == "time":
            # use timezone-aware datetime (local timezone)
            current_time = datetime.now().astimezone().strftime("%H:%M:%S")
            print("Bot : Current Time is", current_time)

        elif user == "date":
            # use timezone-aware datetime (local timezone)
            current_date = datetime.now().astimezone().strftime("%d-%m-%Y")
            print("Bot : Today's Date is", current_date)

        elif user == "help":
            print("\nAvailable Commands")
            print("----------------------------")
            print("hello")
            print("hi")
            print("how are you")
            print("your name")
            print("python")
            print("time")
            print("date")
            print("bye")
            print("----------------------------")

        elif user == "bye":
            print("Bot : Thank you. Have a great day!")
            break

        else:
            print("Bot : Sorry! I don't understand that.")

chatbot()