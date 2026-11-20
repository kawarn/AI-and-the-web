import streamlit as st
import time
from openai import OpenAI

# ── Generate a random 5-letter word using the OpenAI API ───────────────────────────────

client = (
    OpenAI(
    base_url = "https://litellm.uni-osnabrueck.de/v1",
    api_key = st.session_state.get("uos_api_key", "")
))

resp = client.chat.completions.create(
    model = "google/gemma-4-E4B-it",
    max_tokens = 10000,
    messages = [{"role": "user", "content": "Give me one random word with 5 letters. Please only answer with that word, no other text. Do not use any words that have been used before."}]
)
chosen_word = resp.choices[0].message.content

# ── Main program logic starts here ────────────────────

# Check if a goal word is already set in the session state, if not, select a random word from the list
if "goal_word" not in st.session_state:
    st.session_state["goal_word"] = chosen_word.lower()
    st.info("A new word has been selected.")

# Initialize variables for the game 
guessed_letters = 0
wrong_positions = 0
letter_safe_goal = 0
letter_safe_input = 0

# Initialize variables for the session states
def Initialize_session_states(x,y):
    if x not in st.session_state:
        st.session_state[x] = y

Initialize_session_states("total_guesses_per_game", [])
Initialize_session_states("average_guesses", 0)
Initialize_session_states("games_played", 0)
Initialize_session_states("wordbank", [])
Initialize_session_states("guess_count", 0)
Initialize_session_states("quality_guess", 0)
Initialize_session_states("Average_quality", 0)
Initialize_session_states("wrong_words", [])
Initialize_session_states("notes", [])

def count_wrong(x, i, goal_list, user_list, counter):
    if goal_list[x] == user_list[i] and x != i and user_list[i] is not None:
        counter += 1
        goal_list[x] = None
        user_list[i] = None
    return counter, goal_list, user_list

# deletes empty slots
for x in st.session_state["wrong_words"]:
    if x == None:
        st.session_state["wrong_words"].remove(x)

# Streamlit app layout
st.title("Word guesser")
st.subheader("Guess a word with 5 Letters.")

# User input for guessing the word with streamlit chat component
input_word = st.chat_input("Enter your guess here:")

# noteblock
notes_input = st.text_area(
    "notes", 
    value = "\n".join(st.session_state["notes"]), 
    height = 150, 
    width = 200, 
    key = "notes_input"
    )

# Check if word is submitted 
if input_word:

    # Check if the input word is 5 letters long
    if len(input_word) != 5:
        error_message = "Please enter a 5-letter word."
        st.error(error_message)

    # Check if the word is already used by the user
    elif input_word.lower() in st.session_state["wrong_words"]:
        st.error("⚠️ You have already guessed this word. Please try another one. ⚠️")   
        
    # Check if the input word matches the goal word
    elif input_word.lower() == st.session_state["goal_word"]:
        st.success("🎉 HURRAY!! You guessed the correct word!: " + st.session_state["goal_word"])
        st.balloons()
        
        # add guess count to the list of total guesses per game and add one to games played
        st.session_state["total_guesses_per_game"].append(st.session_state["guess_count"] + 1)
        st.session_state["games_played"] += 1

        # Checks for guess quality by checking for right letters and calculate average quality per game
        if guessed_letters >= 3:
            st.session_state["quality_guess"] += 2
        if wrong_positions >= 3:
            st.session_state["quality_guess"] += 1
        st.session_state["Average_quality"] = st.session_state["quality_guess"] / st.session_state["games_played"] if st.session_state["games_played"] > 0 else 0
        
        # Save the guessed word to the wordbank 
        st.session_state["wordbank"].append(st.session_state["goal_word"])
        
        # Reset goal word and variables & select a new word
        st.session_state["goal_word"] = ()
        st.session_state["goal_word"] = chosen_word.lower()    
        st.session_state["guess_count"] = 0      
        st.session_state["wrong_words"] = []          
        with st.spinner("A new word is being selected …"):
            time.sleep(2)
            st.rerun()

    # If guess is wrong        
    else:
        st.session_state["guess_count"] += 1
        st.error("❌ Try again!")
        st.session_state["wrong_words"].append(input_word)

        goal_word_safe = list(st.session_state["goal_word"])
        input_word_list = list(input_word)

        current_guessed_letters = 0
        current_wrong_positions = 0
        
        # Count the number of correct letters in the correct position
        for i in range(5):
            if goal_word_safe[i] == input_word_list[i]:
                current_guessed_letters += 1
                goal_word_safe[i] = None     

            # Count the number of correct letters in the wrong position            
        
        for j in range (5):
            if input_word_list[j] is not None:
                for x in range(5):
                    current_wrong_positions, goal_word_safe, input_word_list = count_wrong(
                    x, j, goal_word_safe, input_word_list, current_wrong_positions
                    )

        guessed_letters = current_guessed_letters
        wrong_positions = current_wrong_positions
            
        # Display results 
        st.table ({
            "correct letters in the correct position": [guessed_letters],
            "correct letters in the wrong position": [wrong_positions]
        })

        st.info(f"Guessed words so far: {st.session_state['wrong_words']}") 
        st.caption(f"Guess count: {st.session_state['guess_count']}")

        # Display all guessed words except the last one
        st.info(f"Guessed words so far: {st.session_state['wrong_words']}") 

        # Display guess count
        st.caption(f"Guess count: {st.session_state["guess_count"]}") 

        # hints depending on guess count
        if st.session_state["guess_count"] >= 26:
            st.error("Hint: The first four letters are: " + st.session_state["goal_word"][:4])
        elif st.session_state["guess_count"] >= 21:
            st.warning("Hint: The first three letters are: " + st.session_state["goal_word"][:3])
        elif st.session_state["guess_count"] >= 16:
            st.info("Hint: The first two letters are: " + st.session_state["goal_word"][:2])
        elif st.session_state["guess_count"] >= 11:
            st.success("Hint: The first letter of the word is: " + st.session_state["goal_word"][0])
            if st.session_state["guess_count"] == 11:
                        st.warning("You have made more than 10 guesses. Consider trying a different strategy.")
        elif st.session_state["guess_count"] > 30:
            st.warning(f"😓 you have failed to guess the word 😓    The correct word would have been {st.session_state["goal_word"]}") 
            
            # Reset goal word and variables & select a new word
            st.session_state["goal_word"] = ()
            st.session_state["goal_word"] = chosen_word.lower()    
            st.session_state["guess_count"] = 0      
            st.session_state["wrong_words"] = []          
            with st.spinner("A new word is being selected …"):
                time.sleep(2)
                st.rerun()
            

# Updates the average guesses if there are any recorded guesses
if len(st.session_state["total_guesses_per_game"]) > 0:
    st.session_state["average_guesses"] = sum(st.session_state["total_guesses_per_game"]) / st.session_state["games_played"]