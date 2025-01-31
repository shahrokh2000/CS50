# Hangman Game
#### Video Demo:  <https://youtu.be/vxcsULkQWYA>
#### Description:

This is a simple implementation of the classic Hangman game in Python. Hangman is a word-guessing game where the player attempts to guess a hidden word one letter at a time. For each incorrect guess, a part of a stick figure is drawn. The player wins if they correctly guess the entire word before the stick figure is fully drawn, and loses if the stick figure is completed before the word is guessed.

Game Flow

1. The game starts by randomly selecting a word from a predefined list. This list includes words related to computer science.
2. The player is welcomed to the game and presented with an initial display, showing the current state of the word to be guessed and an empty hangman figure.
3. The player is prompted to guess a letter. The game checks if the input is valid (a single alphabetical character that has not been guessed before).
4. The guessed letter is processed to update the word display, incorrect attempts count, and the set of guessed letters.
5. The game continues until the player either correctly guesses the word or exceeds the maximum allowed incorrect attempts.
6. The final outcome is displayed, indicating whether the player won by correctly guessing the word or lost by running out of attempts.

Functions

`choose_random_word()`

- Selects a random word from a predefined list of words.
- The list includes words like "hangman," "python," "programming," "computer," and "science."
- The `random.choice()` function is used to pick a random word from the list.

`display_hangman(incorrect_attempts)`

- Takes an argument `incorrect_attempts` which represents the number of incorrect guesses the player has made.
- Returns a string representing the current state of the hangman based on the number of incorrect attempts.
- Uses ASCII art to display the hangman figure in different stages.

`get_user_guess(guessed_letters)`

- Takes a set `guessed_letters` as an argument, representing the letters already guessed by the user.
- Uses a while loop to repeatedly prompt the user to guess a letter until a valid input is provided.
- Checks if the input is a single alphabetical character and if it has not been guessed before.
- Returns the lowercase guessed letter.

`process_guess(guess, word_to_guess, guessed_word, incorrect_attempts, guessed_letters)`

- Takes five arguments: `guess`, `word_to_guess`, `guessed_word`, `incorrect_attempts`, and `guessed_letters`.
- Checks if the guessed letter is already in `guessed_word` and raises a `ValueError` if so.
- Adds the guessed letter to `guessed_letters`.
- Updates `guessed_word` based on correct guesses in `word_to_guess`.
- Increments `incorrect_attempts` if the guessed letter is not in the word.
- Returns the updated `guessed_word`, `incorrect_attempts`, and `guessed_letters`.

`main()`

- The main game loop is implemented here.
- Calls `choose_random_word` to get a word for the player to guess.
- Initializes variables such as `guessed_word`, `incorrect_attempts`, and `guessed_letters`.
- Displays a welcome message and the initial state of the hangman.
- Iteratively prompts the user to guess a letter and updates the game state until the word is guessed or the player runs out of attempts.
- Prints a victory or defeat message based on the outcome.

How to Play

1. Run the script, and you will be prompted with a welcome message and the initial hangman figure.
2. Enter single letters as your guesses when prompted.
3. Continue guessing until you either successfully guess the word or run out of attempts.
4. The game will display the outcome, indicating whether you won or lost.

Enjoy playing Hangman!

