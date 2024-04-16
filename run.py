import random
#import colorama
import cat_bird
from words import movements, equipment, abbrevations
import word_art

def game_start():
    """
    Shows the start page word art and the rules of the game. 
    Prompts the user to choose a topic.
    """
    print(word_art.start_page)
    print("You can choose from 3 different topics in this game:")
    print("Movements, Equipment and Abbrevations")
    print("They are all related to the lovely sport of CrossFit")
    print("You have to know your CrossFit in order to save the poor bird!")
    print("You have 6 attempts before the bird gets eaten...")
    print("Only letters allowed and only one letter per guess")
    print("Good luck!")

game_start()



