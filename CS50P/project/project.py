import random

def main():
    word_to_guess = choose_random_word()
    guessed_word = ['_'] * len(word_to_guess)
    incorrect_attempts = 0
    max_attempts = 6
    guessed_letters = set()

    print("Welcome to Hangman!")
    print(display_hangman(incorrect_attempts))
    print(" ".join(guessed_word))

    while '_' in guessed_word and incorrect_attempts < max_attempts:
        guess = get_user_guess(guessed_letters)

        try:
            guessed_word, incorrect_attempts, guessed_letters = process_guess(guess, word_to_guess, guessed_word, incorrect_attempts, guessed_letters)
        except ValueError as e:
            print(f"Error: {e}")

        print(display_hangman(incorrect_attempts))
        print(" ".join(guessed_word))

    if '_' not in guessed_word:
        print("Congratulations! You guessed the word.")
    else:
        print(f"Sorry, you ran out of attempts. The word was: {word_to_guess}")

def choose_random_word():
    words = ["hangman", "python", "programming", "computer", "science"]
    return random.choice(words)

def display_hangman(incorrect_attempts):
    hangman_stages = [
        """
         ------
         |    |
         |
         |
         |
         |
        ---
        """
        ,
        """
         ------
         |    |
         |    O
         |
         |
         |
        ---
        """
        ,
        """
         ------
         |    |
         |    O
         |    |
         |
         |
        ---
        """
        ,
        """
         ------
         |    |
         |    O
         |   /|
         |
         |
        ---
        """
        ,
        """
         ------
         |    |
         |    O
         |   /|\\
         |
         |
        ---
        """
        ,
        """
         ------
         |    |
         |    O
         |   /|\\
         |   /
         |
        ---
        """
        ,
        """
         ------
         |    |
         |    O
         |   /|\\
         |   / \\
         |
        ---
        """
    ]
    return hangman_stages[incorrect_attempts]

def get_user_guess(guessed_letters):
    guess = input("Guess a letter: ").lower()

    while not guess.isalpha() or len(guess) != 1 or guess in guessed_letters:
        if guess in guessed_letters:
            print("You've already guessed that letter.")
        else:
            print("Invalid input. Please enter a valid single letter.")
        guess = input("Guess a letter: ").lower()

    return guess

def process_guess(guess, word_to_guess, guessed_word, incorrect_attempts, guessed_letters):
    if guess in guessed_word:
        raise ValueError("You've already guessed that letter.")

    guessed_letters.add(guess)

    if guess in word_to_guess:
        for i, letter in enumerate(word_to_guess):
            if letter == guess:
                guessed_word[i] = guess
    else:
        incorrect_attempts += 1

    return guessed_word, incorrect_attempts, guessed_letters

if __name__ == "__main__":
    main()
