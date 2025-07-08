import streamlit as st
import time

st.title("🔄 For Loop Number Generator")
st.markdown("See what numbers are generated in a for loop!")

# Controls
st.header("🎛️ Controls")
start_value = st.slider("Start value", value=0, min_value=-10, max_value=10, step=1)
end_value = st.slider("End value", value=10, min_value=-10, max_value=10, step=1)
step_size = st.slider("Step size", value=1, min_value=-10, max_value=10, step=1)

# Validate the inputs
if step_size > 0:
    # If step size is positive, end value must be greater than start value
    if end_value <= start_value:
        st.error("End value must be greater than start value for a positive step size.")
else:
    # If step size is negative, end value must be less than start value
    if end_value >= start_value:    
        st.error("End value must be less than start value for a negative step size.")

# Show the for loop
st.header("Code for sample for loop")

code = f"""
\"\"\"
The format of this loop is:

for loop_variable in range(start_value, end_value, step_size):
    # Code to execute

The loop will start at the 'start_value' and end right before the 'end_value'.
The 'step_size' is the amount that the 'loop_variable' will change after each iteration.

\"\"\"
for i in range({start_value}, {end_value}, {step_size}):
    print(i)
"""
st.code(code, language="python")


