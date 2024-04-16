import random
#import colorama
import cat_bird
from words import movements, equipment, abbrevations
import word_art
import os




def validate_choice(data):
    """
    Validates the choice of topic input.
    """
    try:
        if data.isalpha():
            raise ValueError(
                f"You need to enter a number. You entered: {data}")
        if int(data) < 1:
            raise ValueError(f"You need to enter a number between 1 and 3. You entered: {data}")
        if int(data) > 3:
            raise ValueError(f"You need to enter a number between 1 and 3. You entered: {data}")
    except ValueError as e:
        print(f"Invalid input: {e}. Please try again.\n")
        return False
    return True

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

"""
def check_letter(input_letter):
    
    Checks if the input letter is in the word 
    and adds it to either the correct or wrong count
    
    
    correct_count = 0
    wrong_count = 6
    correct = " "
    wrong = " "

    for char in word_game:
    if(char in guessedLetters):
      print(word_game[counter], end=" ")
      rightLetters+=1
    else:
      print(" ", end=" ")
    counter+=1
  return rightLetters

    while correct_count != len(word_game.replace(' ', '')) and wrong_count != 0:
        display = ''
    for letter in word_game:
        if letter in correct:
                display += f'{letter}'
        else:
                display += '_ '
    print(display)
"""


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

    """
    Asks the player to input a topic choice.
    Checks the validate_choice function and if True the while loop breaks.
    If False player get to input a choice again.
    """
    while True:
        print("Choose your topic. A number between 1-3:")
        print("1. Movements")
        print("2. Equipment")
        print("3. Abbrevations\n")
        topic_input = input("Choose topic: ")
        if validate_choice(topic_input):
            break
    
    """
    Picks a list with random words chosen by the
    player depending on the topic. Then a random word is generated.
    """
    choice_words = {
        "1": movements,
        "2": equipment,
        "3": abbrevations
    }
        
    word_game = random.choice(choice_words[topic_input]).upper()
    for x in word_game:
        print("_", end=" ")
    
    letter = get_letter()

       


main()




