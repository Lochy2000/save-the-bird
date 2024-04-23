""" importing random providing a choice function, os and colorama """
import random
import cat_bird
from words import movements, equipment, abbrevations
import word_art
import os
from colorama import Fore, Back, Style


def clear_terminal():
    """
    Clears the screen from previous text, from:
    https://stackoverflow.com/questions/2084508/clear-the-terminal-in-python
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def validate_choice():
    """
    Asks the player to input a topic choice.
    If True the while loop breaks.
    If False player get to input a choice again.
    """
    while True:
        try:
            topic_input = int(input("Choose topic:\n"))
            if 1 <= topic_input <= 3:
                clear_terminal()
                print(cat_bird.stages[6])
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
            letter = input("\nPlease enter a letter:\n").upper()
            if len(letter) == 1 and letter.isalpha():
                clear_terminal()
                break
            else:
                print("Only enter one letter at a time and no numbers\n")
        except ValueError:
            print("Please enter a letter\n")
    return letter


def restart_game():
    """
    Asks the player if they want to play again,
    if Yes game restarts, if No game ends
    """
    while True:
        try:
            restart = input(" Want to play again? Y or N:\n").upper()
            if restart == "Y":
                clear_terminal()
                main()
                break
            elif restart == "N":
                print("Thanks for playing!")
                break
            else:
                raise ValueError("Please enter Y or N")
        except ValueError as e:
            print(e)


def check_letter(word_game):
    """
    Checks if the input letter is in the word
    and adds it to either the right or wrong count
    Displays the letter in the word if guess is correct
    Keeps track of number of wrong counts, and for every guess that
    is incorrect, the cat gets closer to the bird.
    When wrong_counts reaches 6 the game is over.
    """
    right_count = 0
    wrong_count = 6
    right = ""
    wrong = ""

    while right_count != len(word_game) and wrong_count != 0:
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
            print(cat_bird.stages[wrong_count])

            if right_count == len(word_game):
                clear_terminal()
                message = f" That's right, the word is {word_game}!\n"
                print(Style.BRIGHT + f"{message}" + Style.RESET_ALL)
                print(Fore.GREEN + Style.BRIGHT + word_art.win
                      + Style.RESET_ALL)
                restart_game()
        else:
            print("No, that's not correct...")
            wrong += letter
            print(f"You have tried these letters: {right + wrong}\n")
            wrong_count -= 1
            print(cat_bird.stages[wrong_count])
            if wrong_count == 0:
                clear_terminal()
                print()
                print(cat_bird.stages[0])
                message = f" NOOOOOOOOO...... The word was: {word_game}!\n"
                print(Style.BRIGHT + f"{message}" + Style.RESET_ALL)
                print(Fore.RED + Style.BRIGHT + word_art.lose
                      + Style.RESET_ALL)
                restart_game()


def main():
    """
    Start page with name of the game and the game rules
    """
    print(Fore.CYAN + Style.BRIGHT + word_art.start_page)
    print("You can choose from 3 different topics in this game:")
    print("Movements, Equipment and Abbrevations")
    print("They are all related to the lovely sport of CrossFit")
    print("You have to know your CrossFit in order to save the poor bird!")
    print("You have 6 attempts before the bird gets eaten...")
    print("Only letters allowed and only one letter per guess")
    print("Good luck!\n" + Style.RESET_ALL)
    print("Choose your topic. A number between 1-3:")
    print("1. Movements")
    print("2. Equipment")
    print("3. Abbrevations\n")

    option_number = validate_choice()
    word_game = get_word(option_number)
    check_letter(word_game)


main()
