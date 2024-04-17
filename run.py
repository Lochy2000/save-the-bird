import random
#import colorama
import cat_bird
from words import movements, equipment, abbrevations
import word_art
import os


def validate_choice():
    """
    Asks the player to input a topic choice.
    If True the while loop breaks.
    If False player get to input a choice again.
    """
    while True:
        try:
            topic_input = int(input("Choose topic: "))
            if 1 <= topic_input <=3:
                break
            else:
                print("That is not a valid number, please try again!\n")
        except ValueError:
            print("You need to enter a number between 1 and 3.\n")
    return topic_input

def get_word(option_number):
    """
    Picks a list with random words chosen by the
    player depending on the topic. Then a random word is generated.
    """
    if option_number == 1:
        return random.choice(movements).upper()
    elif option_number == 2:
        return random.choice(equipment).upper()
    elif option_number == 3:
        return random.choice(abbrevations).upper()
    
        


def get_letter():
    """
    Prompts the user for a letter and checks that it
    is only one letter and no numbers
    """
    while True:
        try:
            letter = input("\n\nPlease enter a letter: ").upper()
            if len(letter) == 1 and letter.isalpha():
                break
            else:
                print("Please only wright one letter at a time and no numbers\n")
        except ValueError:
            print("Please enter a letter\n")          
    return letter 


def check_letter(word_game):
    """
    Checks if the input letter is in the word 
    and adds it to either the correct or wrong count
    """
    
    right_count = 0
    wrong_count = 6
    right = ""
    wrong = ""

    while right_count != len(word_game.replace(' ', '')) and wrong_count != 0:
        display = ''
        for letter in word_game:
            if letter in right:
                display += f'{letter}'
            else:
                display += '_ '
        print(display)

        letter = get_letter()

        if letter in right or letter in wrong:
            print(f"You have already tried {letter}, please try again!")
            continue

        if letter in word_game:
            print("That's correct!")
            right += letter
            print(f"You have tried these letters: {right + wrong}\n")
            right_count += word_game.count(letter)

            if right_count == len(word_game.replace(" ", "")):
                print(f"That's right, the word is {word_game}!\n")
                print(word_art.win)
        else:
            print("No, that's not correct...")
            print(f"You have tried these letters: {right + wrong}\n")
            wrong += letter
            wrong_count -= 1
            print(cat_bird.stages[wrong_count])
            if wrong_count == 0:
                print(word_art.lose)


def main():
    """
    Start page with name of the game and the game rules
    """
    print(word_art.start_page)
    print("You can choose from 3 different topics in this game:")
    print("Movements, Equipment and Abbrevations")
    print("They are all related to the lovely sport of CrossFit")
    print("You have to know your CrossFit in order to save the poor bird!")
    print("You have 6 attempts before the bird gets eaten...")
    print("Only letters allowed and only one letter per guess")
    print("Good luck!\n")
    print("Choose your topic. A number between 1-3:")
    print("1. Movements")
    print("2. Equipment")
    print("3. Abbrevations\n")
    
    option_number = validate_choice()
    word_game = get_word(option_number)
    #print(word_game)
    check_letter(word_game)
    
 

    
    """
        
    word_game = random.choice(choice_words[topic_input]).upper()
    for x in word_game:
        print("_", end=" ")
    
    letter = get_letter()
    """

       


main()




