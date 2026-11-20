# Read me file for project one:

## idea:
Our idea was to create a **guessing game with words**. So we had two options in our mind: Let the player guess letter for letter and highlight the right ones *(maybe give tips for the location in the alphabet of the right letter)* or let the player guess whole words and highlight the right letters at the right place *(here tips would include the length of the word and the placement of corect letters)*
In our opinion the second option would be more fun. After some thinking we decided to give our guessing game a similar structure like the game **"wordle"**. 

## first programming steps:
To create a basic framework for our programm we used the word "apple" as a correct solution and built our programm around it. We wanted the **word length limited to five letters** and a reasonable response to user inputs. So the first steps were to create practical outputs, an user input using the chat component of streamlit and responses to that. 
Once we had everything set up so a working guessing game with the word "apple" was possible, we continued to develop our app based on that foundation - we worked with the command session state so the program could work correctly with our variable and included already some tips *(e.g. checking the letters)* and some other information in the output like a guess count or the words the users have already guessed before. 
With our foundations set we thought about how we could create a collection of five-letter words. *(this is where we wanted to implement the AI)*

## AI implementation: 
To implement the AI we included the **API** key in our main page (were the user can choose between game and stats) and the **LLM** in our app to have the largest possible collection of words. Unfortunately, this has significantly slowed down the game's running speed.

## Stats page:
With the AI implementation we had the game finished for now. For the user to see his/her **stats**, we created a second page including some general statistics about the game and some additional regarding the guess qualities. So there are information about **the number of games played, the amount of guesses per game, the average guesses per game and a wordbank that saves all words that have been already guessed**. Then there is a **„Qualityscore“** which has a maximum of 100 point and works with the average guesses *(for the purpose of transparency, we have provided additional information on the stats page)* and a bar chart that tells something about **how good the game was** depending on the amount of guesses in the specific game and the average guesses. 

## Last steps:
In our last steps we worked with the **layout** *(e.g. using commands like st.info(…), st.warning(…)…)* to make is logical and good looking for the user, fixed a **few remaining bugs**, tried to **organize the code** as clean as possible and wrote our last **comments**. 
