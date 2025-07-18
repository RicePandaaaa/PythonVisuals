import streamlit as st

st.title("Variables and Data Types")

st.markdown("---")

# Introduction
st.header("Introduction")
st.markdown("""
            A variable is what we use to store information in a program. If the information can be represented as some sort of tangible value or object (e.g. a number or some text), then we can store in a variable. For Python to understand the information being stored, it has specific data types that it can work with. The core three are `int`, `float`, and `str`.
            """)

st.markdown("---")

# Number data types
st.header("Number data types")
st.markdown("""
            `int` and `float` are used to store numbers. `int` is used to store **int**eger values, while `float` is used to store **float**ing point values (decimal numbers). An example of an `int` is `1`, while an example of a `float` is `1.5`. Note that as long as the number has a decimal point, it will be stored as a `float`, even if the number itself could be rewritten as an `int` (e.g. `1.0` is a `float` even though 1 does not inherently have a fractional part).
            """)

# Create a table of examples of ints and floats
st.markdown("""
            Here are some examples of `int` and `float` values:
            """)
st.table([
    {"float": "1.5", "int": "1"},
    {"float": "2.0", "int": "2"},
    {"float": "-2.12345", "int": "-212345"}
])

# Ask the student whether a value is an int or a float
st.subheader("Quiz: `int` or `float`?")
st.markdown("""
            **Q1: Is 0.0 an `int` or a `float`?**
            """)
user_answer = st.radio("Choose the correct answer for Q1:", ["int", "float"], key="num_q1", index=None)
if user_answer == "float":
    st.success("Correct! Even though 0.0 is equal to 0, it is still a `float` because it has a decimal point.")
elif user_answer == "int":
    st.error("Incorrect. Even though 0.0 is equal to 0, it is still a `float` because it has a decimal point.")

st.markdown("""
            **Q2: Is 123 an `int` or a `float`?**
            """)
user_answer = st.radio("Choose the correct answer for Q2:", ["int", "float"], key="num_q2", index=None)
if user_answer == "int":
    st.success("Correct! 123 is an `int` because it does not have a decimal point.")
elif user_answer == "float":
    st.error("Incorrect. 123 is an `int` because it does not have a decimal point.")

st.markdown("---")

# String data type
st.header("String data type")
st.markdown("""
            `str` is used to store **string** values. A string is a sequence of characters. An example of a `str` is `"Hello, world!"`. Notice the use of quotes to indicate that the value is a string. These quotes are not part of the string itself, but are used to indicate that the value is a string. Without these quotes, Python would think you are typing some code instead. Also notice that the quotes can be single or double quotes, but they must be consistent (i.e. the string must be enclosed in the same type of quotes).
            """)
st.markdown("""
            **Note 1:** A string can be empty, which is represented by two quotes with nothing in between. For example, `""` is a valid `str` value.

            **Note 2:** A string cannot *contain* the same quote character that is used to enclose the string. For example, `"Hello, world!"` is a valid `str` because the string is enclosed in double quotes, but `"Hello, world!"` is not a valid `str` because the string is enclosed in double quotes and contains a double quote.
            """)

# Create a table of examples of strings
st.markdown("""
            Here are some examples of valid and invalid`str` values:
            """)
st.table([
    {"Valid": "\"Hello, world!\"", "Invalid": "\'Hello, world!\""},
    {"Valid": "\'12345\'", "Invalid": "\"12345"},
    {"Valid": "\"Tony\"", "Invalid": "Tony"},
])
st.markdown("""
            The left side of the table all have some sort of text (letters, numbers, etc.) enclosed by a pair of double or single quotes. The right side of the table shows incorrect syntax with either mixmatched types of quotes or just missing quotes.
            """)

# Ask the student whether a value is a valid string or not
st.subheader("Quiz: Is the string valid?")
st.markdown("""
            **Q1: Is `'Hello, world!'` a valid `str`?**
            """)
user_answer = st.radio("Choose the correct answer for Q1:", ["Yes", "No"], key="str_q1", index=None)
if user_answer == "Yes":
    st.success("Correct! `'Hello, world!'` is a valid `str` because it is enclosed in single quotes.")
elif user_answer == "No":
    st.error("Incorrect. `'Hello, world!'` is a valid `str` because it is enclosed by the same type of quotes! Single or double quotes are both valid.")

st.markdown("""
            **Q2: Is `'Howdy''` a valid `str`?**
            """)
user_answer = st.radio("Choose the correct answer for Q2:", ["Yes", "No"], key="str_q2", index=None)
if user_answer == "No":
    st.success("Correct! `'Howdy''` is invalid because it is both enclosed in single quotes and contains a single quote.")
elif user_answer == "Yes":
    st.error("Incorrect. `'Howdy''` is invalid because it is both enclosed in single quotes and contains a single quote. To use the single quote, use double quotes instead to enclose the string (e.g. `\"can't\")`")

st.markdown("""
            **Q3: Is `'\"cat'` a valid `str`?**
            """)
user_answer = st.radio("Choose the correct answer for Q3:", ["Yes", "No"], key="str_q3", index=None)
if user_answer == "Yes":
    st.success("Correct! `'\"cat'` is a valid `str` because it is enclosed in double quotes and contains a single quote.")
elif user_answer == "No":
    st.error("Incorrect. `'\"cat'` is a valid `str` because it is enclosed in double quotes and contains a single quote.")

st.markdown("""
            **Q4: Is `'\"` a valid `str`?**
            """)
user_answer = st.radio("Choose the correct answer for Q4:", ["Yes", "No"], key="str_q4", index=None)
if user_answer == "No":
    st.success("Correct! `'\"` is not a valid string because the quotes are different. A string can be empty, but it cannot be enclosed in different types of quotes.")
elif user_answer == "Yes":
    st.error("Incorrect. `'\"` is not a valid string because the quotes are different. A string can be empty, but it cannot be enclosed in different types of quotes.")

st.markdown("---")

# Variable assignment
st.header("Variable Assignment")
st.markdown("""
            To store these values in a variable, the variable needs to be created and assigned. The syntax for this is:
            ```python
            variable_name = value
            ```

            If `variable_name` already exists, it will be overwritten with the new value. Otherwise, a new variable will be created with that value. Notice that the variable name is on the left side of the assignment operator (`=`) and the value is on the right side. This is *always* the case, and is a key concept to remember when programming.

            Note that if a variable is written on the right side, then it is assumed that we want to assign the *value* of that variable to the variable on the left. For example, if we have `x = 1` and `y = x`, then `y` will be assigned the value `1`.
            """)

# Quiz: Assign a value to a variable
st.subheader("Quiz: Value assignment")
st.markdown("""
            **Q1: Assign the value `123` to the variable `x`**
            """)
user_answer = st.radio("Choose the correct answer for Q1:", ["x = 123", "123 = x", "= 123 x", "x 123 ="], key="var_q1", index=None)
if user_answer == "x = 123":
    st.success("Correct! `x = 123` is the correct syntax to assign the value `123` to the variable `x`.")
elif user_answer == "123 = x":
    st.error("Incorrect. The variable needs to be on the left side of the assignment operator (`=`) and the value needs to be on the right side.")
elif (user_answer == "= 123 x") or (user_answer == "x 123 ="):
    st.error("Incorrect. The assignment operator needs to be in the middle, with the name of the variable on the left and the value on the right.")

st.markdown("""
            **Q2: Suppose we have the following code:**
            ```python
            a = 1
            b = 4
            a = 7
            b = 8
            a = b
            ```

            **What is the final value of `a`?**
            """)
user_answer = st.radio("Choose the correct answer for Q2:", ["1", "4", "7", "8"], key="var_reassign_q1", index=None)
if user_answer == "8":
    st.success("Correct! The final assignment of `a` was the value of `b`. `b`'s final value is `8`, so `a` is assigned the value `8`.")
elif user_answer == "4":
    st.error("Incorrect. `b` did have the value `4` initially, but it was overwritten by the value `8` right before `a` took on the value of `b`. This means that when `a = b` is executed, `b` was already changed to `8`, and thus `a` is assigned the value `8`.")
elif user_answer == "7":
    st.error("Incorrect. `a` was assigned a different value two lines after with `a = b`. This means that `a` is now assigned the value `8` since `b` is 8 at the time of that assignment.")
elif user_answer == "1":
    st.error("Incorrect. `a` gets assigned two more different values after the initial assignment of `1`. With the final assignment being `a = b`, `a` is assigned the value stored in `b`, which is `8`.")

# Casting to a different data type

