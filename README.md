## CDLPredictionGame
This is a game for fans of the CDL to make predictions on a number of different categories. 

#What Does it do?


#How does it work?

The process of the game is split up into two parts:
-Making the predictions
-Getting the results

#Making the Predictions
To make the predictions you must first open the CDLGamePredictions.py 

![Image of the Predictor application HomePage](https://github.com/J-Alexander99/CDLPredictionGame/assets/148716418/e73627a6-7584-4681-9ba8-5a5929ee1da1)

From here there are two buttons, the first is the "Get Players" and the second is the "Save Predictions" button. Now we have yet to make our predictions so we need to click on the "Get Players" button first.
This brings us to the next page. Quite self explanatory here we enter the number of players making the predictions. This program can accept any number of players. 

![Predictor application, number of players page](https://github.com/J-Alexander99/CDLPredictionGame/assets/148716418/e6438759-1d4c-43f2-b59c-5b246bdd1a49)

After entering the number of players you will be prompted to give names for the players. Do as such. (and dont use any full colons in the name... it will break the code and make me upset..)

![Player name page](https://github.com/J-Alexander99/CDLPredictionGame/assets/148716418/8c089b62-3818-43b2-a919-fb21f7bbc74a)

From here we find ourselves at the team selections page. This is probably the most complicated part of the application.
We need to add in the teams that we will be predicting for. To do this we need to first go to https://www.breakingpoint.gg/matches and find the match we are predicting for.
Once we find out match take note of the order of the two teams. THIS IS IMPORTANT. 
![image](https://github.com/J-Alexander99/CDLPredictionGame/assets/148716418/645c0eeb-c25d-4dec-819d-5599f3343c63)
Notice how in this example Miami is on the Left and New York is on the RIght. This is important to remember as this is the order you are going to enter the teams into the program.

![image](https://github.com/J-Alexander99/CDLPredictionGame/assets/148716418/a1f70bd6-eccb-48d8-80b3-e96ba6be5896)


For our example we will enter Miami as Team A and enter New York as Team B like so:
![image](https://github.com/J-Alexander99/CDLPredictionGame/assets/148716418/338b1d36-a2f6-4a14-8efd-ec719eb48b44)

Once this is complete, we move to the next step. From Here it is all just following the instructions on screen to make predictions until the windows close.

The Hardpoint, Search and Destroy and Control predictions are simple. Just enter what you belive the final scoreline to be.
![image](https://github.com/J-Alexander99/CDLPredictionGame/assets/148716418/b8664fdb-17d1-4653-9290-9c78aada11fd)

Then comes the individual player predictions. Simply select the player from the drop down list for each category. 
The categories include:
Most Kills,
Least Kills,
Most Deaths,
Least Deaths,
Best K/D,
Worst K/D,
Most Damage,
Least Damage
![image](https://github.com/J-Alexander99/CDLPredictionGame/assets/148716418/79d087ac-5b8e-4113-beae-b40fb4dc5219)

Once this is complete you will be returned to the main menu. with out predictions now made we simply click the "Save Predictions" button. This will save your predictions to a .txt file
This will be saved within a data folder, within a CDLGame folder in the desktop. 
*Please remember to move the predictions.txt file if you intend to predict multiple matches at the same time, otherwise the sedcond prediction will overwrite the first*

#Getting the results

Once the match is over it is time to get the results.
Thanks to a recent update the rest of the program can be launched from the file named Launcher.py as seen below
![image](https://github.com/J-Alexander99/CDLPredictionGame/assets/148716418/f9e0f9b8-da70-4f81-b39e-9735087c18a8)

This launcher allows you to access the rest of the programs from one location. To do so, simply enter the link to BreakingPointGG database for the match in particular into the entry field.
There are then three buttons as follow:
-First accesses the website to gather the individual player stats
-Second grabs the scoreline *this is why getting the team order is important*
-Third will compare the predictions to the results and assign points to the players based on their predictions. *Click this one last*
*Also please give the programs time to complete*


