import streamlit as st

st.title("5: User Input")

# User input
st.header("5.1: Introduction")
st.markdown("""
            A lot of programs require the user to input information. For example, a calculator requires the user to input the numbers they want to calculate. A game requires the user to input the moves they want to make. A website requires the user to input the information they want to store.

            In Python, the most basic way of getting user input is from the terminal. This is done using the `input()` function. There are many other ways to get user input, but they usually require other libraries or are just simply far more complex to implement.
            """)

st.markdown("---")

# Using input()
st.header("5.2: Using `input()`")
st.markdown("""
            The `input()` function is used to get user input from the terminal. It takes an optional string as an argument, which is the prompt that will be displayed to the user. It returns a string of the user's input.

            ```python
            name = input("What is your name: ")
            ```

            Note that the user is supposed to type their input directly after the prompt. Personally, I like to add a colon and a space after the prompt to make it clear that the user should type their input after the colon. Also, the space helps to separate the prompt from the user's input.

            Also note that no matter what the user types (if anything at all), the input will be returned as a string. This means that if the user types a number, it will be returned as a string. This is important to remember because if you want to do math with the user's input, you will need to convert it to a number first. If they type in nothing but hit Enter anyways, the input will be an empty string.
            """)

# Quiz on what goes inside input() and the return type
st.subheader("Quiz: `input()` basics")
st.markdown("""
            **Q1:** What goes inside the `input()` function (if you were to add something inside)?
            """)

user_answer = st.radio("Choose your answer:", ("The prompt", "The variable that stores the input"), key="q1", index=None)
if user_answer == "The prompt":
    st.success("Correct! Remember that the prompt has to be a string! Also, the prompt is optional, so you can just do `input()` if you want.")
elif user_answer == "The variable that stores the input":
    st.error("Incorrect! To store the input, you would assign the `input()` function to a variable, not put the variable inside the parentheses.")

st.markdown("""
            **Q2:** What is the return type of the `input()` function?
            """)

user_answer = st.radio("Choose your answer:", ("A number", "A boolean", "A string", "A list"), key="q2", index=None)
if user_answer == "A string":
    st.success("Correct! The `input()` function returns a string of the user's input.")
elif user_answer is not None:
    st.error("Incorrect! The `input()` function returns a string of the user's input.")

st.markdown("---")

# Using input() with a prompt
st.header("5.3: Typecasting")
st.markdown("""
            Typecasting was already covered in "Variables & Data Types". However, it is important to note that the `input()` function returns a string. This means that if you want to do math with the user's input, you will need to convert it to a number first. If they type in nothing but hit Enter anyways, the input will be an empty string. If you know that the user will always type in a number, you can use the `int()` or `float()` function to convert the input to a number:

            ```python
            age = int(input("How old are you: "))
            print(f"You are {age} years old.")

            weight = float(input("How much do you weigh (in lbs): "))
            print(f"You weigh {weight} lbs.")
            ```

            The above is just an example. Do note that the `int()` and `float()` functions can return errors if what is typed in cannot be coverted into a valid `int` or `float`. Input validation is a whole other topic that will be covered in a future section by itself. For now, you can assume that the user will always type in a valid number. In practice, you would want to check if the input is a valid number before converting it to a number, but the techniques to do so require more advanced concepts that will be covered in future sections.
            """)

st.markdown("---")
st.caption("© 2025 Anthony Ha-Anh Pham | Licensed under [GNU GPL 3.0](https://www.gnu.org/licenses/gpl-3.0.html) | View source code on [GitHub](https://github.com/RicePandaaaa/TonyIntroToPython)")
