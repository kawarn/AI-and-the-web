import streamlit as st
import time
from openai import OpenAI

# ── Generate a random 5-letter word using the OpenAI API ───────────────────────────────

client = (OpenAI(
    base_url="https://litellm.uni-osnabrueck.de/v1",
    api_key=st.session_state.get("uos_api_key", "")
))
resp = client.chat.completions.create(
    model="google/gemma-4-E4B-it",
    max_tokens=10000,
    messages=[{"role": "user", "content": "Give me one random word with 5 letters. Please only answer with that word, no other text. Do not use any words that have been used before."}]
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

# Initialize a list to store the guessed words
# guessed_words = []

# initialize variable for the session states
def Initialize_session_states(x,y):
    if x not in st.session_state:
        st.session_state[x] = y

Initialize_session_states("total_guesses_per_game", [])
Initialize_session_states("average_guesses", 0)
Initialize_session_states("games_played", 0)
Initialize_session_states("wordbank", [])
Initialize_session_states("guess_count", 0)
Initialize_session_states("wrong_words", [])

for x in st.session_state["wrong_words"]:
    if x == None:
        st.session_state["wrong_words"].remove(x)

# Streamlit app layout
st.title("Word guesser")
st.subheader("Guess a word with 5 Letters.")

# User input for guessing the word 
input_word = st.chat_input("Enter your guess here:")


# Check if word is submitted   
  
if input_word:
    # Check if the input word is 5 letters long
    if len(input_word) != 5:
        error_message = "Please enter a 5-letter word."
        st.error(error_message)

    elif input_word.lower() in st.session_state["wrong_words"]:
        st.warning("You have already guessed this word. Please try a different one.")   
        
    # Check if the input word matches the goal word
    elif input_word.lower() == st.session_state["goal_word"]:
        st.success("🎉 HURRAY!! You guessed the correct word!: " + st.session_state["goal_word"])
        st.balloons()
        st.session_state["total_guesses_per_game"].append(st.session_state["guess_count"] + 1)
        st.session_state["games_played"] += 1
        # Reset goal word & select a new one
        st.session_state["goal_word"] = ()
        st.session_state["goal_word"] = chosen_word.lower()    
        st.session_state["guess_count"] = 0      
        st.session_state["wrong_words"] = []          
        with st.spinner("A new word is being selected …"):
            time.sleep(2)
            st.rerun()
    else:
        st.session_state["guess_count"] += 1
        st.error("❌  Try again!")
        st.session_state["wrong_words"].append(input_word)
        
        # Count the number of correct letters in the correct position
        for i in range (5):
            if st.session_state["goal_word"][i] == input_word[i]:
                guessed_letters += 1     
            # Count the number of correct letters in the wrong position          
            for j in range (5):
                # Check if the letter in the input word matches a letter in the goal word but is in the wrong position
                if st.session_state["goal_word"][i] == input_word[j] and input_word[j] != st.session_state["goal_word"][j] and input_word[j]:
                    # Count the number of occurrences of the letter in the goal word
                    for x in range (5):
                        if st.session_state["goal_word"][x] == input_word[j]:
                            letter_safe_goal += 1
                            # Count the number of occurrences of the letter in the input word
                            for y in range (5):
                                if input_word[y] == input_word[j]:
                                    letter_safe_input += 1
                                    # Determine the minimum of the two counts to avoid overcounting letters
                                    if letter_safe_goal < letter_safe_input:
                                        wrong_positions = letter_safe_goal
                                    else:
                                        wrong_positions = letter_safe_input

        # Display results    
        st.write(f"You got {guessed_letters} correct letters in the correct position.")
        st.write(f"You got {wrong_positions} correct letters in the wrong position.")

        # Display all guessed words except the last one
        st.info(f"Guessed words so far: {st.session_state['wrong_words']}") 

        st.write(st.session_state["guess_count"])    


        # quality of guesses 
        if st.session_state["guess_count"] == 11:
            st.warning("You have made more than 10 guesses. Consider trying a different strategy.")

        # hints
        if st.session_state["guess_count"] >= 25:
            st.error("Hint: The first four letters are: " + st.session_state["goal_word"][:4])
        elif st.session_state["guess_count"] >= 20:
            st.warning("Hint: The first three letters are: " + st.session_state["goal_word"][:3])
        elif st.session_state["guess_count"] >= 15:
            st.info("Hint: The first two letters are: " + st.session_state["goal_word"][:2])
        elif st.session_state["guess_count"] >= 10:
            st.success("Hint: The first letter of the word is: " + st.session_state["goal_word"][0])

# Update the average guesses if there are any recorded guesses
if len(st.session_state["total_guesses_per_game"]) > 0:
    st.session_state["average_guesses"] = sum(st.session_state["total_guesses_per_game"]) / st.session_state["games_played"]
       
# Save the guessed word to the wordbank 
    st.session_state["wordbank"].append(st.session_state["goal_word"])

# !! Display the current goal word for debugging purposes !! - D E L E T E
st.write(f"Goal word: {st.session_state["goal_word"]}")
# DELETE !!!


