# While loop
stages = [
    '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
'''
]

import random
import hangman_words
from hangman_words import word_list
from hangman_art import logo, stages

print(logo)
# word_list = ["aardvark", "baboon", "camel"]
random_word = random.choice(hangman_words.word_list)
rand_wo = len(random_word)
#print(random_word)

end_of_game = False

#display ----- for random_word
display = []
for _ in range(rand_wo):
  display += "_"
print(display)
lives = 6
while not end_of_game:
  # guess lett
  guess_lett = input("Guess a letter:").lower()
  if guess_lett in display:
    print(f"you have already enter {guess_lett}")
  #print(guess_lett)
# repacle your guess letter with blank
  for position in range(rand_wo):
    letter = random_word[position]
    if letter == guess_lett:
      display[position] = letter
  print(display)
  #check _ in programl
  if '_' not in display:
    end_of_game = True
    print("you win")

  # keep track for lives
  if guess_lett not in random_word:
    lives = lives - 1
    print(f"\nWrong Guess \nYou have {lives} chances")
  if lives == 0:
    end_of_game = True
    print("You lose, Please try again")
    print(f"The chosen word was: {rand_wo}")
  print(stages[lives])
  if lives != 0 and guess_lett not in random_word:
    hint = input("Do you want hint?Type yes or no:").lower()
    # Index of the character to extract
    if hint == "yes":
     index = int(input("Enter the index of the character you want to extract: "))
     character = random_word[index]
     print("The character at index", index, "is:", character)
     display[index] = character
     print(display)
  
