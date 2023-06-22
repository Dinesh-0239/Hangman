"""
Date:- 
This is "Hangman" game created by me (Dinesh Singh) using basic concept of python programming.

To run this game:
    1. Open command prompt(cmd) and browse to the file using "cd <path-of-project>" command.
    2. run "python hangman.py"

"""
#Importing Libraries
import random
from hangman_art import stages, logo
from hangman_words import word_list 
from hangman_emotions import happy, sorrow
import sys,os

def clear_screen():
    if sys.platform.startswith('win'):
        # For Windows
        os.system('cls')
    else:
        # For Unix/Linux/Mac
        os.system('clear')
def show_logo():
    #Printing the logo of the game
    print("-"*50)
    print(logo)
    print("-"*50)

show_logo()
#lives
lives = len(stages) - 1

#choosing the random word from word_list
choose_word = random.choice(word_list)
#print(choose_word)

#genrating a '_' list of having same lenght as choose_word
display = []
for letter in choose_word:
    display += "_"
#printing dashed form of word
print(f"\nWord: {' '.join(display)}\n")    

tried_letters = []
#Main portion of the game
#Looping the portion of code until '_' is present in the display
while '_' in display:
    #taking a guess letter in a variable
    guess_letter = input("Guess the letter: ").lower()
    if len(guess_letter) != 1:
        print("Enter Single Character")
        continue
    #clearing the previous output
    clear_screen()
    
    #showing logo
    show_logo()
    
    #checking whether we are guessing the same letter or not?
    if guess_letter in display:
        print(f"You already guessed '{guess_letter}' before, try something else!")
    
    else:
        #checking guessed letter is present in the choosen word or not?
        if guess_letter not in choose_word:
            #checking whether you have tried particular letter or not    
            if guess_letter in tried_letters:
                print(f"You already tried '{guess_letter}' before, try something else!")
                tried_letters += guess_letter
                continue
            #printing the hangman ascii art as per remaining lives
            print(stages[lives])
            #checking whether we have lives or not, if not simply exit the game
            if lives == 0:
                print("You loss, better luck next time!")
                print(f"Word: {choose_word}")
                input("press any key to exit: ")
                exit()
            print(f"{random.choice(sorrow)}, you guessed a wrong letter, '{guess_letter}' is not present in the word, you have only {lives} lives left!")
            lives -= 1
        else:
            #Printing success message
            print(f"{random.choice(happy)}, you guessed a right one, '{guess_letter}' is present in the word, you still have {lives} lives!")
            #replacing the blanks with the guessed letter
            for position in range(len(choose_word)):
                if guess_letter == choose_word[position]:
                    display[position] = guess_letter
        
        #adding guess_letter in tried letter  
        tried_letters += guess_letter

        #printing the remaining portion of the display
        print(f"\nWord: {' '.join(display)}\n")    

if '_' not in display:
    print("Congrats, You win!")