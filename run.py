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

def main():
    print(word_art.start_page)
    print("You can choose from 3 different topics in this game:")
    print("Movements, Equipment and Abbrevations")
    print("They are all related to the lovely sport of CrossFit")
    print("You have to know your CrossFit in order to save the poor bird!")
    print("You have 6 attempts before the bird gets eaten...")
    print("Only letters allowed and only one letter per guess")
    print("Good luck!")

    """
    Checks the validate_choice function and if True the while loop breaks.
    If False player get to input a choice again.
    """
    while True:
        print("Choose your topic. A number between 1-3:\n")
        print("1. Movements")
        print("2. Equipment")
        print("3. Abbrevations")
        topic_input = input("Choose topic: ")
        if validate_choice(topic_input):
            break

    """
    Picks a list with random words choosed by
    player depending on the topic chosen.
    """
    choice_words = {
        "1": movements,
        "2": equipment,
        "3": abbrevations
    }

main()




