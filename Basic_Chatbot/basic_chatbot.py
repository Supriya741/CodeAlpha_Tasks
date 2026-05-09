import time

print("🤖 ===============================")
print("🤖    WELCOME TO AI CHATBOT")
print("🤖 ===============================")

name = input("👤 Enter your name: ")

print(f"\n🤖 Hello {name}! I am your virtual assistant.")
print("🤖 Type 'bye' anytime to exit.\n")

while True:

    user = input(f"{name}: ").lower()

    # Greeting
    if user == "hello":
        print("🤖 Hello there! 😊")

    # How are you
    elif user == "how are you":
        print("🤖 I'm doing great! Thanks for asking 💙")

    # Name
    elif user == "what is your name":
        print("🤖 My name is CodeAlpha Bot 😎")

    # Joke
    elif user == "tell me a joke":
        print("🤖 Why do programmers hate bugs?")
        time.sleep(1)
        print("🤖 Because they make them debug all day 😂")

    # Motivation
    elif user == "motivate me":
        print("🤖 Believe in yourself. You can do amazing things! ✨")

    # Favorite language
    elif user == "best programming language":
        print("🤖 Python of course 🐍🔥")

    # Bye
    elif user == "bye":
        print(f"🤖 Goodbye {name}! Have a great day 🌸")
        break

    elif user == "thank you":
        print("🤖 You're welcome 😊")

    elif user == "who created you":
         print("🤖 I was created by M.Supriya ✨")

    # Unknown input
    else:
        print("🤖 Sorry, I didn't understand that 😅")