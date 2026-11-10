import streamlit as st

st.title("Word guesser")

goal_word = "apple"
st.write("Welcome to our word guessing game:")
st.write("Your word has 5 letters - try your first one :)")
input_word = st.text_input ("Enter your guess here!")
if input_word:
    if len(input_word) != 5:
        st.write("Please enter a 5-letter word")
    elif input_word.lower() == goal_word:
        st.write("HURRAY - that is correct !!")
    else: 
        st.write("Try again - you can do this!")
if input_word:
    for i in range (5):
        if goal_word[i] == input_word[i]:
            st.write(f"Letter {i+1} is correct: {goal_word[i]}")

# st.link_button("see your stats", "https://share.streamlit.io/streamlit/examples/main/word_guesser.py")

if st.button("Reset game"):
    st.session_state.clear()