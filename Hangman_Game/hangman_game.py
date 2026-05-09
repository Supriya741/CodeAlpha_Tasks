import random

print("🎮 =================================")
print("🎯        HANGMAN GAME")
print("🎮 =================================")

# Player name
name = input("👤 Enter your name: ")

print(f"\n👋 Welcome {name}! Let's start the game.")

# List of predefined words
words = ["python", "turtle", "programmer", "robot", "keyboard"]

# Randomly choose a word
word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 8

# Game loop
while wrong_guesses < max_wrong_guesses:

    # Display word with blanks
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\n🔤 Word:", display_word)

    # Show guessed letters
    print("📝 Guessed letters:", guessed_letters)

    # Remaining attempts
    print("❤️ Remaining attempts:", max_wrong_guesses - wrong_guesses)

    # Win condition
    if "_" not in display_word:
        print(f"\n🎉 Congratulations {name}! You guessed the word: {word}")
        break

    # User input
    guess = input("👉 Guess a letter: ").lower()

    # Validate input
    if len(guess) != 1:
        print("⚠ Please enter only one letter.")
        continue

    # Check repeated guesses
    if guess in guessed_letters:
        print("🔁 You already guessed that letter.")
        continue

    # Check guess
    if guess in word:
        print("✅ Correct guess!")
        guessed_letters.append(guess)
    else:
        print("❌ Wrong guess!")
        wrong_guesses += 1
        guessed_letters.append(guess)

# Lose condition
if wrong_guesses == max_wrong_guesses:
    print(f"\n💀 Game Over {name}!")
    print("🏆 The word was:", word)

print("\n🙏 Thanks for playing Hangman!")