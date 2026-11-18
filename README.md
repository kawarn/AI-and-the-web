# Read me file for project one:

## idea:
Our idea was to create a **guessing game with words**. So we had to options in our mind: Let the player guess letter for letter and highlight the right ones *(maybe give tips for the location in the alphabet of the right letter)* or let the player guess whole words and highlight the right letters at the right place *(here tips would include the length of the word and the placement of corect letters)*
In our opinion the second option would be more fun. After some thinking we decided to give our guessing game a similar structure like the game **"wordle"**. 

## first programming steps:
To create a basic framework for our programm we used the word "apple" as a correct solution and built our programm around it. We wanted the **word length limited to five letters** and a reasonable response to user inputs. So the first steps were to create practical outputs, an user input and responses to that. Once we had everything set up so a working guessing game with the word "apple" was possible, we thought about how we could create a collection of five-letter words. *(this is where we wanted to implement the AI)*

But before we included the AI in our guessing game, we tried to complete the structure of our game with an array of five-letter words. So we changed our variable "goal_word" to the command "st.session_state["goal_word"] to **...** 
After that, the game was able to reset the goal word and select a new one. Aditionally to that we designed some outputs to help the users with their guesses: like count the number of correct letter in the correct positions and incorrect positions. Here we needed to be careful with words that contain double letter. - If the guessed word has for example a double 'p' but the goal word has only one 'p' the game should only display for one letter 'p' that is is correct. But if the goal has a double letter this shouldn't be ignored of course! 

## AI implemenation: 
After we had our basic structure set for the play page, we implemented the **LLM** to have the largest possible collection of words.
**...**

## Stats page:
With the AI implementation we had the game finished for now. For the user to see his/her **stats**, we created a second page including a bar chart for the average guesses and number of games played. **...**

**!!**
## Last steps:
After we had the basic requirements set, we wanted to give our game a nicer look and include some additional requirements 
**!!**