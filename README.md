# Save the Bird!

![Picture of startpage](/documentation/startpage.png)

Save the Bird is a Python terminal game deployed on Heroku.
The goal of the game is to test the players knowledge in the sport of CrossFit.
The player gets to choose from 3 different topics related to CrossFit and then guess what the hidden word is.
If the player is correct, the Bird escapes the Cat and survives. If the player's guess is wrong to many times, the Bird gets eaten by the Cat.

The deployed version of the app can be accessed [here](https://save-the-bird-604fc56d90f3.herokuapp.com/)

## User Experience (UX)

### Site Purpose
The pupose of the site is to provide a simple and fun platform for the user to try their luck in a new version of the traditional Hangman game and guess the computers random hidden word.

### Audience
Anyone that is interested in, or passionate about games, and looking for a simple and fun platform to play with.

### Communication
The game interface shows clear print statements to guide users through each turn, ensuring an error-free and engaging gaming experience. It also provides animations and colored word art for a visually appealing element to the game.

### User Goals
The primary goal is to entertain the users and at the same time get them to learn more about the sport of CrossFit.

### Future Goals
To add a highscore board so that users can see other players scores and encurage them to set new High scores in order to learn more on the way.


### Flowchart
![Image of the flowchart of the game](/documentation/flowchart.png)


## Features
-   At the start page the user is asked to choose from three different topics by entering a number between 1 and 3.

![Picture of the choice of topics](/documentation/choose_topic.png)

-   Once the choice is made, the game begins. A picture of a cat sneeking up to a bird is shown and the user is asked to guess a letter in the word.

![Picture of first stage of the game](/documentation/first_cat_bird.png)

-   If the guessed letter is wrong, the cat gets one step closer to the bird.

![Picture of cat closer to bird](/documentation/cat_closer.png)

-   and the guessed letter is added to the list of letters tried:

![Picture of message when incorrect guess](/documentation/not_correct.png)

-   If the player already tried the entered letter, a message is displayed saying that and askes the player to try again.

![Picture of message when letter already entered](/documentation/tried_letter.png)

-   If the guessed letter is correct, the letter is added to the word and the guessed letter is added to the list of letters tried.
 
![Picture of message when correct guess](/documentation/correct_guess.png)

![Picture of letter entered in word](/documentation/letter_in_word.png)

-   If the number of incorrect guesses reaches 6, the cat got all the way to the bird. The game is lost and the bird gets eaten.

![Picture of game lost](/documentation/lose.png)

-   If the user manages to guess the correct word, the game is won and the bird is saved!

![Picture of game won](/documentation/new_win.png)

-   When the game is over, the player is asked if they want to play again. If yes, the game restarts, if no the game ends and a message is displayed:

![Picture with Thanks for playing message](/documentation/end_game.png)

### Error Handling

-   When the player is asked to enter a topic choice, between 1 and 3, and they enter another number, they are asked to enter a number between 1 and 3.
If they enter a letter, or a space, or Enter, or any other character, it says "Invalid input, please enter a valid number" 

![image](https://github.com/user-attachments/assets/5f970dce-5af2-439c-bcdb-9d327a5e19bd)


-   When the player is asked to guess a letter in the word and they enter a number, more than one letter, a space, just Enter, or any other character, they are asked to enter only one letter and no numbers:

![Picture of entered number](/documentation/get_letter_error2.png)

-   At the end of the game, when the player is asked if they want to play again, they have the options to enter Y or N. If they enter another letter, a number, a space, any other character or just press Enter, they are asked to enter Y or N.

![Picture of invalid input when restart game](/documentation/restart_game_error2.png)

### Future Features
-   Ability to save scores
-   A Highscore board
-   A possibility to the user to get an explanation on all abbrevations


## Testing
-   During the development I tested the code in small portions using print statements to be sure that the code was working as I expected.

-   I asked my fellow students for user acceptance testing and Raneem Yad made me aware of that animation disappeared when letter was guessed twice. So I added the stage of animation to remain on the screen.

- I had an issue with the error handling in the restart_game function that I discussed with my fellow student Patricia and I solved it with her help.

-   I tested the game both in my local Gitpod terminal and the Heroku terminal.


### Feature testing
-  I tested that all functions running the game was working as it should by checking:
    -   Only a number between 1 and 3 allowed in the input of topic choice.
    -   Only letters allowed in the guess 
    -   Only one letter per guess
    -   That correct letters were added to the word and to the list of guessed letters
    -   That incorrect letters were added in the background to the count of wrong guesses, and to the list of guessed letters.
    -   That the right animation stage was applied when an incorrect guess was made.
    -   That after number of guesses run out, the final stage of the cat_bird animation was displayed and that the game ended.
    -    That after the word was correctly guessed, the word_art for winning the game was displayed and geme ended.
    -   That efter game ended, the function restart_game was run and the question to play again appeared.
    -   That all errors were handled and clear to the user.

-   This is the testing sheet that I used:

![Picture of testing sheet](/documentation/testing_doc.png)

### Validator Testing
-   I used the [CI Python Linter](https://pep8ci.herokuapp.com/) to test the code. I ran all .py files through it. 
-   Both run.py and words.py had no errors or warnings.

![Picture of pep8 test on run.py](/documentation/pep8_run_new.png)
![Picture of pep8 test on words.py](/documentation/pep8_words.png)

-   cat_bird.py and word_art.py have warnings diplayed that I cannot do anything about. It is due to the special characters used to create the animations and word art.

![Picture of pep8 test on word_art.py](/documentation/pep8_word_art.png)
![Picture of pep8 test on cat_bird.py](/documentation/pep8_cat_bird.png)


## Bugs

-   In the mock terminal there was an empty line in the cat_bird animations that I didn't see in the code nor in the Gitpod terminal.

    ![Picture of blank line in animation](/documentation/animation_bug.png)
    
    But after fixing the lenght of the lines and removing some white space according to the [pep8 tests](https://pep8ci.herokuapp.com/), I managed to get rid of that bug. 


### Unfixed bugs

-   No unfixed bugs as far as I know.

## Deployment

### Version Control
-   The site was created using Gitpod editor and pushed to Github to the remote repository 'save-the-bird'.
-   Git commands were used throughout the development to push the code to the remote repository. The following git commands were used:
    -   git add .  - to add the files to the staging area before being committed.
    -   git commit -m "commit message" - to commit changes to the local repository queue that are ready for the final step.
    -   git push - to push all committed code to the remote repository on Github.   

### Page Deployment
-   The app was deployed with Heroku following these steps:
    -   After creating a Heroku account, click "New" to create a new app from the dashboard.
    -   Create a name of the app, that needs to be unique, and select your region. Press "Create app"
    -   Go to settings and add the necessary Config_vars and buildpacks. Make sure that the buildpacks are set to "Python" and "NodeJS", in that order.
    -   Go to Deploy tab and scroll down to Deployment Method.
    -   Select GitHub and search for your GitHub repository.
    -   Scroll down to deploy options.
    -   For this project the Manual Deploy method was chosen.
    -   Choose main branch and click Deploy Branch. This will deploy the current state of the branch specified.
    -   Now the app is being built and when Deploy to Heroku has a green check mark, the build is finished.
    -   Click View button to open the app in a browser window.

### Cloning of the Repository Code locally
-   Go to the Github repository that you want to clone.
-   Click on the Code button located above all the project files.
-   Click on HTTPS and copy the repository link.
-   Open the IDE of your choice and and paste the copied git url into the IDE terminal.
-   The project is now created as a local clone.


## Content

### Technologies Used

-   Programming language was Python.

-   I used the following Libraries:
    -   random, to select a random word.
    -   os, for the clear tool to clear the terminal window.
    -   colorama, to color and style text.

-   Github was used to store the repository for submission.

-   Heroku was used to deploy the the live version of the terminal.

-   [Lucid](https://lucid.app/documents#/documents?folder_id=recent) was used to create the flowchart

-   [Fancy Text Pro](https://www.fancytextpro.com/) was used to create the word art.

-   [Ascii Art](https://www.asciiart.eu/) is the source of the animations in the game.

-   [PEP8 CI Python Linter](https://pep8ci.herokuapp.com/) was used to run the code through to check it.
 

## Credits
-   First of all I want to thank my mentor Spencer Bariball for motivating me to start this project when I had no inspiration to do so.
    As always he has been a great help on the way!

-   I also got some very helpful tips from my co-student Patricia when I was struggling with error handling. Very thankful for that!

-   Raneem Yad made some user acceptance tests and me aware of that the animation disappeared at one stage in the game, which I then could fix. Also very thankful for that!

-   I took some initial inspiration and guidelines to this project from:
    -   [Kite YouTube channel](https://www.youtube.com/watch?v=m4nEnsavl6w&t=205s)
    -   [CodeFather Blog](https://codefather.tech/blog/hangman-game-python/)

-   I got the information on how to install Colorama from [pypi.org](https://pypi.org/project/colorama/)



