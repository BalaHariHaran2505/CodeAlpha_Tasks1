import random

def hangman():
    words = ["python", "hangman", "program", "github", "codealpha"]
    
    while True:  # Main loop to allow restarting
        word = random.choice(words)
        guessed_word = ["_"] * len(word)
        attempts = 6
        guessed_letters = []

        print("\n🎮 Welcome to Hangman Game!")
        print("Type 'quit' anytime to exit.")
        print("Guess the word:", " ".join(guessed_word))

        while attempts > 0 and "_" in guessed_word:
            guess = input("Enter a letter: ").lower()

            # Quit option
            if guess == "quit":
                print("👋 You chose to quit. Thanks for playing!")
                return  # End the game

            # Validation
            if len(guess) != 1 or not guess.isalpha():
                print("⚠️ Please enter a single valid letter.")
                continue

            if guess in guessed_letters:
                print(f"⚠️ You already guessed '{guess}'. Try another.")
                continue

            guessed_letters.append(guess)

            if guess in word:
                print(f"✅ Good job! '{guess}' is in the word.")
                for i, letter in enumerate(word):
                    if letter == guess:
                        guessed_word[i] = guess
            else:
                attempts -= 1
                print(f"❌ Wrong guess! '{guess}' is not in the word.")
                print(f"Remaining attempts: {attempts}")

            print("Current word:", " ".join(guessed_word))

        # Game result
        if "_" not in guessed_word:
            print("🎉 Congratulations! You guessed the word:", word)
        else:
            print("💀 Game Over! The word was:", word)

        # Ask user if they want to play again
        again = input("Do you want to play again? (yes/no): ").lower()
        if again != "yes":
            print("👋 Thanks for playing! Goodbye!")
            break


# Run the game
if __name__ == "__main__":
    hangman()
