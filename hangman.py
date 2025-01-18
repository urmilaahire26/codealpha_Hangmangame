import random

def hangman_game():
    # List of words for the game
    words = ["python", "programming", "hangman", "developer", "engineer"]
    word = random.choice(words)  # Randomly select a word
    guessed_word = ["_"] * len(word)  # Word display with underscores
    guessed_letters = set()  # Track guessed letters
    attempts = 6  # Number of incorrect guesses allowed

    print("Welcome to Hangman!")
    print("You have 6 attempts to guess the word.")

    while attempts > 0 and "_" in guessed_word:
        print("\nCurrent word: ", " ".join(guessed_word))
        print(f"Guessed letters: {', '.join(guessed_letters) if guessed_letters else 'None'}")
        print(f"Remaining attempts: {attempts}")

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please guess a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            attempts -= 1

    if "_" not in guessed_word:
        print("\nCongratulations! You guessed the word:", word)
    else:
        print("\nGame Over! The word was:", word)

if __name__ == "__main__":
    hangman_game()
