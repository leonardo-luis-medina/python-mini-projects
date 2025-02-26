import random

def choose_word():
    words = ["python", "hangman", "developer", "code", "programming"]
    return random.choice(words)

def display(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    word = choose_word()
    guessed_letters = set()
    attempts = 6

    print("Welcome to Hangman!")
    
    while attempts > 0:
        print("\nWord:", display(word, guessed_letters))
        print(f"Attempts left: {attempts}")

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.add(guess)
            if all(letter in guessed_letters for letter in word):
                print(f"Congratulations! You guessed the word: {word}")
                return
        else:
            attempts -= 1
            print(f"Wrong guess! {attempts} attempts left.")

    print(f"Game over! The word was: {word}")

hangman()
