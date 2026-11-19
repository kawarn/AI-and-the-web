import streamlit as st
st.title("Stats Page")
st.info("This is the stats page. Here you can see the statistics of your game.")

total_guesses_per_game = st.session_state.get("total_guesses_per_game", [])
st.write(f"Total guesses per game: {total_guesses_per_game}")
st.bar_chart(st.session_state["total_guesses_per_game"], use_container_width=True)

average_guesses = st.session_state.get("average_guesses", 0)
st.write(f"Average guesses: {average_guesses}")