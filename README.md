# Save the Bird!

![Picture of startpage](/documentation/startpage.png)

Save the Bird is a Python terminal game deployed to Heroku.
The goal of the game is to test the players knowledge in the sport of CrossFit.
The player gets to choose from 3 different topics related to CrossFit and then guess what the hidden word is.
If the player is correct, the Bird escapes the Cat and survives. If the player's guess is wrong to many times, the Bird gets eaten by the Cat.

## User Experience (UX)
-   At the start page the user is asked to choose from three different topics by entering a number between 1 and 3.
-   Once the choice is made, the game begins. A picture of a cat sneeking up to a bird is shown and the user is asked to guess a letter in the word.
![Picture of first stage of the game]()
-   If the guessed letter is wrong, the cat gets one step closer to the bird.
![Picture of message when incorrect guess]()
-   If the guessed letter is correct, the letter is added to the word.
![Picture of message when correct guess]()
-   There is a list of letters displayed to the user to know what letters they have guessed.
![Picture of list of guessed letters]()
-   If the user wrong guesses reaches 6, the game is lost and the bird gets eaten.
![Picture of game lost]()
-   If the user manages to guess the correct word, the game is won and the bird is saved!
![Picture of game won](/documentation/win.png)   


## Features

### Future Features
-   Ability to save scores
-   A Highscore board

## Flowchart
![Image of the flowchart of the game](/documentation/flowchart.png)

## Testing
During the development I tested the code in small portions using print statements to be sure that the code was working as I expected.

-   Feature testing
    -  I tested that the function running the game was working as it should by checking:
        -   Only letters allowed in the guess 
        -   Only one letter per guess
        -   That correct letters were added to the word and to the list of guessed letters
        -   That incorrect letters were added in the background to the count of wrong guesses, and to the list of guessed letters.
        -   That the right animation stage was applied when an incorrect guess was made.
        -   That after number of guesses run out, the final stage of the cat_bird animation was displayed and that the game ended.
        -    That after the word was correctly guessed, the word_art for winning the game was displayed and geme ended.
        -   That efter game ended, the function restart_game was run and the question to play again appeared.


## Bugs

-   In the mock terminal there is an empty line in the cat_bird animations that I don't see in the code or in the Gitpod terminal.

### Unfixed bugs

## Deployment
-   The app was deployed with Heroku following these steps:
    -   After creating a Heroku account, click "New" to create a new app from the dashboard.
    -   Create a name of the app, that needs to be unique, and select your region. Press "Create app"
    -   Go to settings and add the necessary Config_vars and buildpacks. Make sure that the buildpacks are set to "Python" and "NodeJS", in that order.
    -   Go to Deploy tab and scroll down to Deployment Method.
    -   Select GitHub and search for your GitHub repository.
    -   Scroll down to deploy options.
    -   For this project the Manual Deploy method was chosen.
    -   Chose main branch and click Deploy Branch. This will deploy the current state of the branch specified.
    -   Now the app is being built and when Deploy to Heroku has a green check mark, the build is finished.
    -   Click View button to open the app in a browser window.

## Credits

### Content

### Media
-   I got the information on how to install Colorama from [pypi.org](https://pypi.org/project/colorama/)




