# Save the Bird!

[Picture of startpage]()

Save the Bird is a Python terminal game deployed to Heroku.
The goal of the game is to test the players knowledge in the sport of CrossFit.
The player gets to choose from 3 different topics related to CrossFit and then guess what the hidden word is.
If the player is correct, the Bird escapes the Cat and survives. If the player's guess is wrong to many times, the Bird gets eaten by the Cat.

## User Experience (UX)

## Features

### Future Features
-   Ability to log in and save scores
-   A Highscore board

## Flowchart
![Image of the flowchart of the game](/documentation/project_description/flowchart.png)

## Testing

## Bugs
-   clear_terminal() function did not clear the terminal as expected when Y was chosen by the player on the Question to restart the game.
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




