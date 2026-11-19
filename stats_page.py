import streamlit as st
# Stats page for the guessing game app
st.title("Stats Page")
st.info("your game statistics will be displayed here.")

total_guesses_per_game = st.session_state.get("total_guesses_per_game", [])
st.write(f"Total guesses per game: {total_guesses_per_game}")
st.bar_chart(st.session_state["total_guesses_per_game"], use_container_width=True)

average_guesses = st.session_state.get("average_guesses", 0)
st.write(f"Your average guesses: {average_guesses}")

games_played = st.session_state.get("games_played", 0)
st.write(f"You have played {games_played} games.")

guessed_words = st.session_state.get("wordbank", [])
st.write(f"Guessed words: {guessed_words}")

# Quality of guesses

# initialize counters for good, average, and bad games
bad_games = 0
average_games = 0
good_games = 0

st.title("Quality of your guesses")
st.info("This section provides feedback on the quality of your guesses based on the number of attempts made.")

for i in range(len(total_guesses_per_game)):
    if total_guesses_per_game[i] < average_guesses - 5 or total_guesses_per_game[i] < 5:
        good_games += 1
    elif total_guesses_per_game[i] > average_guesses + 5 or total_guesses_per_game[i] < average_guesses - 5:
        average_games += 1
    else:
        bad_games += 1

st.bar_chart({"Good Games": good_games, "Average Games": average_games, "Bad Games": bad_games}, use_container_width=True)