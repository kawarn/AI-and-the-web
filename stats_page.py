import streamlit as st


# ──────── Stats page for the guessing game app ────────────────────────────────────────────

# Layout
st.title("Stats Page")
st.info("Your game statistics:")

# get statistics from app.py
games_played = st.session_state.get("games_played", 0)
guessed_words = st.session_state.get("wordbank", [])
average_guesses = st.session_state.get("average_guesses", 0)

# Quality of guesses
score = 100
if average_guesses > 10:
    score -= (average_guesses - 10) * 5

if st.session_state.get("Average_quality", 0) > 0:
    score += st.session_state["Average_quality"]

if score >= 100:
    score = 100

# get and write total guesses per game
total_guesses_per_game = st.session_state.get("total_guesses_per_game", [])
st.write(f"Total guesses per game: {total_guesses_per_game}")

# display bar chart of total guesses per game
st.bar_chart(st.session_state["total_guesses_per_game"], use_container_width=True) 

# display statistics
st.table({
    "Games Played": [games_played],
    "Average Guesses": [f"{average_guesses:.2f}"],
    "Guessed Words": [guessed_words],
    "Qualityscore": [f"{st.session_state.get('score', 0):.2f}"]
})

# Information regarding the qualityscore
st.caption("*The Qualityscore contains a maximum of 100 points with additional points for correct letters and minus points for too many wrong guesses")


# ──────── further quality evaluation ────────────────────────────────────────────

# initialize counters for good, average, and bad games
bad_games = 0
average_games = 0
good_games = 0

# Layout
st.title("Quality of your guesses")
st.info("Feedback on the quality of your guesses based on the number of attempts made:")

# Set benchmarks for quality evaluation
for i in range(len(total_guesses_per_game)):
    if total_guesses_per_game[i] < average_guesses - 5 or total_guesses_per_game[i] <= 5:
        good_games += 1
    elif total_guesses_per_game[i] > average_guesses + 5 or total_guesses_per_game[i] < average_guesses - 5:
        average_games += 1
    else:
        bad_games += 1

# display quality evaluation
st.bar_chart({"Good Games": good_games, "Average Games": average_games, "Bad Games": bad_games}, use_container_width=True)