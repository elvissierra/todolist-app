import random
from words import words
import string

def get_valid_word(words):
    word= random.choice(words) #randomly chooses smth from list
    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word.upper()

def hangman():
    word= get_valid_word(words)
    word_letters= set(word) #letters in the word
    alphabet= set(string.ascii_uppercase) 
    used_letters= set() #what the user has guessed

    lives= 6

    #getting user input
    while len(word_letters) > 0 and lives > 0:
        #letters already used
        print('You have', lives, 'lives left you have used these letters:',''.join(used_letters))
        

        #what current word is (ie W_RD)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' ' .join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives= lives -1 
                print('\nLetter is not in word.')

        elif user_letter in used_letters:
            print('\nYou have already guessed that player, try again.')

        else:
            print('\nInvalid character, please try again.')

    #get here when len(word_letters)== 0 or when lives == 0
    if lives == 0:
        print('You died, The word was', word)
    else:
        print('You guessed the word', word, '!!')



hangman()