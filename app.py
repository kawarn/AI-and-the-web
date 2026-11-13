import streamlit as st
import random
import time

goal_word_list = ["apple", "grape", "peach", "mango", "berry","lemon", "melon", "hello", "pearl","fruit", "plant", "table", "chair", "couch", "piano", "drums", "flute"]

if "goal_word" not in st.session_state:
    st.session_state["goal_word"] = random.choice(goal_word_list)
    st.info("A new word has been selected.")
guessed_letters = 0
wrong_positions = 0
letter_safe = []
st.title("Word guesser")
st.write("Guess a word with 5 Letters.")
submit = st.button("submit")
stats = st.button("Stats")
input_word = st.text_input("Enter your guess here:")
if submit:    
    if input_word:
        #input_word.rerun()   
        if len(input_word) != 5:
            st.write("Please enter a 5-letter word.")

        elif input_word.lower() == st.session_state["goal_word"]:
            st.write("Congratulations! You guessed the correct word!: " + st.session_state["goal_word"])
            st.balloons()
            st.session_state["goal_word"] = ()
            st.session_state["goal_word"] = random.choice(goal_word_list)            
            time.sleep(3)
            #goal_word = goal_word_list.random.choice(goal_word_list)
            st.info("A new word is beeing selected.")
            time.sleep(3)
            st.rerun()
        else:
            st.write("Try again!")
        
        for i in range (5):
            if st.session_state["goal_word"][i] == input_word[i]:
                guessed_letters += 1               
            for j in range (5):
                if st.session_state["goal_word"][i] == input_word[j] and i != j and input_word[j] != st.session_state["goal_word"][j] and input_word[j] not in letter_safe:
                    wrong_positions += 1
                    letter_safe.append(input_word[j])
            

        st.write(f"You got {guessed_letters} correct letters.")
        st.write(f"You got {wrong_positions} right letters in the wrong position.")

st.write(f"Goal word: {st.session_state["goal_word"]}")

#if input_word.lower() not in goal_word_list:
#    goal_word_list.append(input_word.lower())'''

#if stats:
#    st.run(stats.py)
if stats:
    st.switch_page("Stats")

