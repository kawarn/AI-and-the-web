import streamlit as st
import random
import time

# List of possible goal words
goal_word_list = ["apple", "grape", "peach", "mango", "berry", "lemon", "melon", "hello", "pearl", "fruit", "plant", "table", "chair", "couch", "piano", "drums", "flute"]

# Check if a goal word is already set in the session state, if not, select a random word from the list
if "goal_word" not in st.session_state:
    st.session_state["goal_word"] = random.choice(goal_word_list)
    st.info("A new word has been selected.")

# Initialize variables 
guessed_letters = 0
wrong_positions = 0
letter_safe = 0
letter_compare = 0

# Streamlit app layout
st.title("Word guesser")
st.write("Guess a word with 5 Letters.")
submit = st.button("submit")
stats = st.button("Stats")

# User input for guessing the word
input_word = st.text_input("Enter your guess here:")

# Check if word is submited   
if submit:  
    if input_word:
        # Check if the input word is 5 letters long
        if len(input_word) != 5:
            st.write("Please enter a 5-letter word.")

        # Check if the input word matches the goal word
        elif input_word.lower() == st.session_state["goal_word"]:
            st.write("HURRAY!! You guessed the correct word!: " + st.session_state["goal_word"])
            st.balloons()
            # Reset goal word & select a new one
            st.session_state["goal_word"] = ()
            st.session_state["goal_word"] = random.choice(goal_word_list)            
            time.sleep(3)
            st.info("A new word is beeing selected.")
            time.sleep(3)
            st.rerun()
        else:
            st.write("Try again!")

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
                            letter_safe += 1
                            # Count the number of occurrences of the letter in the input word
                            for y in range (5):
                                if input_word[y] == input_word[j]:
                                    letter_compare += 1
                                    # Determine the minimum of the two counts to avoid overcounting letters
                                    if letter_safe < letter_compare:
                                        wrong_positions = letter_safe
                                    else:
                                        wrong_positions = letter_compare

        # Display results                    
        st.write(f"You got {guessed_letters} correct letters in the correct position.")
        st.write(f"You got {wrong_positions} correct letters in the wrong position.")

# !! Display the current goal word for debugging purposes !! - D E L E T E
st.write(f"Goal word: {st.session_state["goal_word"]}")
# DELETE !!!

# Navigate to the stats page if the "Stats" button is clicked
if stats:
    st.switch_page("Stats")

