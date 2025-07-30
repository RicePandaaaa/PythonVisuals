import streamlit as st

st.set_page_config(page_title="Intro to Python", layout="wide")

# Create pages with custom titles
home_page = st.Page("pages/home.py", title="00. Home")
setup_page = st.Page("pages/python_setup.py", title="01. Setup")
variables_page = st.Page("pages/variables_data_types.py", title="02. Variables & Data Types")
basic_output_page = st.Page("pages/basic_output.py", title="03. Basic Output")
basic_math_page = st.Page("pages/basic_math.py", title="04. Basic Math Operations")
user_input_page = st.Page("pages/user_input.py", title="05. User Input")
planning_design_page = st.Page("pages/planning_and_design.py", title="06. Planning & Design")
conditionals_page = st.Page("pages/conditionals.py", title="07. Conditionals")
functions_page = st.Page("pages/functions.py", title="08. Functions")
loops_page = st.Page("pages/loops.py", title="09. Loops")
lists_page = st.Page("pages/lists.py", title="10. Lists")

# Navigation with custom titles
pg = st.navigation([home_page, setup_page, variables_page, basic_output_page, basic_math_page, user_input_page, planning_design_page, conditionals_page, functions_page, loops_page, lists_page])
pg.run()