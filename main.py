import streamlit as st

page1 = st.Page("app.py", title="The first page", icon="🤔")
page2 = st.Page("stats_page.py", title="The second page", icon="📈")

pg = st.navigation(pages=[page1, page2])
pg.run() 
