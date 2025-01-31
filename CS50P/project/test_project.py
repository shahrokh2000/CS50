import pytest
from project import choose_random_word, display_hangman, get_user_guess, process_guess

def test_choose_random_word():
    words = ["hangman", "python", "programming", "computer", "science"]
    assert choose_random_word() in words

def test_display_hangman():
    assert display_hangman(0).strip() == '''
         ------
         |    |
         |
         |
         |
         |
        ---
        '''.strip()
    assert display_hangman(3).strip() =="""
         ------
         |    |
         |    O
         |   /|
         |
         |
        ---
        """.strip()

def test_get_user_guess(monkeypatch):
    # Use monkeypatch to simulate user input
    monkeypatch.setattr('builtins.input', lambda _: 'a')

    # Test valid input
    with pytest.raises(ValueError, match="You've already guessed that letter."):
        get_user_guess(set(['a']))

    # Reset monkeypatch for subsequent tests
    monkeypatch.undo()

    # Test invalid input
    with pytest.raises(ValueError, match="Invalid input. Please enter a valid single letter."):
        get_user_guess(set(), '1')



def test_process_guess():
    # Test correct guess
    assert process_guess('a', 'hangman', ['_','_','_','_','_','_'], 0, set()) == (['a', '_', '_', '_', '_', '_'], 0, {'a'})

    # Test incorrect guess
    with pytest.raises(ValueError, match="Incorrect guess!"):
        process_guess('x', 'hangman', ['_','_','_','_','_','_'], 0, set())
