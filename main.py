import streamlit as st
import os
from openai import OpenAI

# ── ask for API Key, stop if not yet provided  ────────────────────────────────────────────

with st.sidebar:
    api_key = st.text_input(
        "UOS AI API-Key",
        type="password",
        key="uos_api_key",
        placeholder="sk-...",
    ).strip()

if not api_key:
    st.info("Please enter your Uni Osnabrück API key. If you don't have one, you can obtain it from https://ai-keys.uni-osnabrueck.de.")
    st.stop()
 
page1 = st.Page("app.py", title="Guessing game", icon="🎮")
page2 = st.Page("stats_page.py", title="Statistics", icon="📈")

pg = st.navigation(pages=[page1, page2])
pg.run() 
