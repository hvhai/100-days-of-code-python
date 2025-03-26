import random

# List of words
WORDS = ["python", "hangman", "developer", "programming", "openai", "artificial"]

# ASCII Hangman Stages
HANGMAN_PICS = [
    """
       ------
       |    |
       |
       |
       |
       |
    =========
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    =========
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    =========
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    =========
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    =========
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    =========
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    =========
    """,
]


def choose_word():
    """Pick a random word from the list."""
    return random.choice(WORDS).upper()


def display_game(word, guessed_letters, attempts):
    """Display hangman stage, guessed word, and remaining attempts."""
    print(HANGMAN_PICS[attempts])

    # Display word with guessed letters or underscores
    display_word = " ".join(letter if letter in guessed_letters else "_" for letter in word)
    print(f"\nWord: {display_word}")
    print(f"Guessed Letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
    print(f"Attempts left: {len(HANGMAN_PICS) - 1 - attempts}\n")


def hangman():
    word = choose_word()
    guessed_letters = set()
    incorrect_attempts = 0
    max_attempts = len(HANGMAN_PICS) - 1

    print("\n🎩 Welcome to Hangman! Try to guess the word. 🎩\n")

    while incorrect_attempts < max_attempts:
        display_game(word, guessed_letters, incorrect_attempts)

        guess = input("Enter a letter: ").strip().upper()

        if not guess.isalpha() or len(guess) != 1:
            print("⚠️ Please enter a **single letter**.\n")
            continue

        if guess in guessed_letters:
            print("🔁 You already guessed that letter! Try another one.\n")
            continue

        guessed_letters.add(guess)

        if guess not in word:
            incorrect_attempts += 1
            print("❌ Wrong guess!\n")
        else:
            print("✅ Correct!\n")

        if all(letter in guessed_letters for letter in word):
            print(f"🎉 Congratulations! You guessed the word: {word} 🎉")
            break
    else:
        display_game(word, guessed_letters, incorrect_attempts)
        print(f"💀 Game Over! The word was: {word} 💀\n")


# Run the game
if __name__ == "__main__":
    hangman()
