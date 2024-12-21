
#  ____________________________________________________________
                    #   Day 7 complete project

import random

from hangman_words import word_list
from hangman_art import stages, logo


lives = 6
print(logo)
word = random.choice(hangman_words.word_list)
print(word)

len_of_word = len(word)

#preparing empty string to store place holder under scores
placeholder = ""
for position in range(len_of_word):
    placeholder += "_"
print(placeholder)

game_over = False

correct_letter = []
while not game_over:
    guess = input("Guess the Letter: ").lower()

    if guess in correct_letter:
        print(f"You have already guessed{guess}.")
    print(guess)
    display = ""
    for letter in word:
        if letter == guess:
            display += letter
            correct_letter.append(guess)
        elif letter in correct_letter:
            display += letter
        else:
            display += "_"
    print("word to guess: " + display)

    if guess not in word:
        lives -= 1
        print(f"you guessed {guess} that's not in the word. You lose a life.")
        if lives == 0:
            game_over = True
            print(f"****************IT WAS {word}! YOU LOSE******************************")
 
    if  "_" not in display:
        game_over = True
        print("You Win!!")

#  ____________________________________________________________

