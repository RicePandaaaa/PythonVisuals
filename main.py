import streamlit as st

st.set_page_config(page_title="Intro to Python", layout="wide")

# Create pages with custom titles
home_page = st.Page("pages/home.py", title="00. Home")
setup_page = st.Page("pages/python_setup.py", title="01. Setup")
variables_page = st.Page("pages/variables_data_types.py", title="02. Variables & Data Types")

# Navigation with custom titles
pg = st.navigation([home_page, setup_page, variables_page])
pg.run()