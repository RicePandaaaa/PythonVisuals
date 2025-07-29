import streamlit as st

st.title("3: Basic Output")

st.markdown("---")

# Printing to the console
st.header("3.1: Printing to the console")
st.markdown("""
            The most basic way to output information is to use the `print()` function. Whenever you run a Python script, a terminal window will open up. This terminal is how Python executes your code and also displays certain outputs. `print()` is Python's primary way to output information to this terminal (also called the console).

            For most values, `print()` will output the value as is. For example, if we have `print(123)`, the output will be `123`. However, the main exception is with strings, where `print()` will not output the quotes that enclose the string. For example, if we have `print('Hello, world!')`, the output will be `Hello, world!`.

            ```python
            print(123)
            ```

            Note in the example above, there is no variable involved. `print()` doesn't give you a value to use, it just outputs the value you give it.
            """)

# Ask about printing different data types
st.subheader("Quiz: Printing different data types")
st.markdown("""
            **Q1: What is the output of the following code?**
            ```python
            print('Hello, world!')
            ```
            """)
user_answer = st.radio("Choose the correct answer for Q1:", ["Hello, world!", "\'Hello, world!\'"], key="print_q1", index=None)
if user_answer == "Hello, world!":
    st.success("Correct! `print()` will not output the quotes that enclose the string.")
elif user_answer == "\'Hello, world!\'":
    st.error("Incorrect. `print()` will not output the quotes that enclose the string.")

st.markdown("""
            **Q2: What is the output of the following code?**
            ```python
            print(123)
            ```
            """)
user_answer = st.radio("Choose the correct answer for Q2:", ["123", "\'123\'"], key="print_q2", index=None)
if user_answer == "123":
    st.success("Correct! `print()` will output the value as is.")
elif user_answer == "\'123\'":
    st.error("Incorrect. `print()` will output the value as is.")

st.markdown("---")

# Printing multiple values
st.header("3.2: Printing multiple values")

st.subheader("3.2.1: Adding multiple values in a single `print()`")
st.markdown("""
            What if you wanted to `print` multiple values (usually mutliple variables) out at the same time? Writing out one `print()` for each value would be tedious and inefficient. Instead, you can use a comma to separate the values you want to print within the `print()` function:

            ```python
            name_one = "Alana"
            name_two = "Adolin"

            print(name_one, name_two)
            ```

            The output will be:

            ```
            Alana Adolin
            ```

            Note that the values are separated by a space. This is the default behavior of `print()` when it comes to printing multiple values.
            """)

# One question about the output
st.subheader("Quiz: Printing multiple values")
st.markdown("""
            **Q1: What is the output of the following code?**
            ```python
            name_one = "123"
            name_two = 456
            print(name_one, name_two)
            ```
            """)
user_answer = st.radio("Choose the correct answer for Q1:", ["\'123\' 456", "123 456"], key="print_q3", index=None)
if user_answer == "123 456":
    st.success("Correct! `print()` will print both values on the same line, separated by a space. With the string, the outside quotes will be stripped before printing.")
elif user_answer == "\'123\' 456":
    st.error("Incorrect. `print()` will remove the outside quotes from the string before printing.")

st.markdown("---")

# Extra parameters for print()
st.header("3.3: Adjusting `print()` behavior")
st.markdown("""
            The `print()` function has a few extra parameters that can be used to adjust its behavior. These parameters are optional, and can be used to modify the default behavior of `print()`.

            **`sep` parameter**: This parameter is used to specify the separator between the values you want to print. For example, if we have `print(123, 456, sep='-')`, the output will be `123-456`. The default value of `sep` is a space.

            **`end` parameter**: This parameter is used to specify the string to print at the end of the output. For example, if we have `print(123, 456, end='-')`, the output will be `123-456-`. Note that the default value of `end` is `'\\n'`, which means that the output will be printed on a new line.

            They are used by adding them after the values we want to print:

            ```python
            print(123, 456, sep='-', end='+')
            ```

            The output will be:

            ```
            123-456+
            ```

            You can choose to use only `sep`, only `end`, both, or neither. If you do choose to use at least one of these parameters, make sure that you add them after all the values you want to print.
            """)

# Ask some questions about the extra parameters
st.subheader("Quiz: Adjusting `print()` behavior")
st.markdown("""
            **Q1: If you wanted to separate values with a comma instead of a space, what would you use?**
            """)
user_answer = st.radio("Choose the correct answer for Q1:", ["`end=','`", "`sep=','`"], key="print_q4", index=None)
if user_answer == "`sep=','`":
    st.success("Correct! `sep` is used to specify the separator between the values you want to print.")
elif user_answer == "`end=','`":
    st.error("Incorrect. `end` is used to specify the string to print at the end of the output. `sep` is used to specify the separator between the values you want to print.")

st.markdown("""
            **Q2: How many lines will the following code print?**

            ```python
            print("Alana", end="|")
            print("Alana")
            """)
user_answer = st.radio("Choose the correct answer for Q2:", ["1", "2"], key="print_q5", index=None)
if user_answer == "1":
    st.success("Correct! The value for `end` in the first `print` does not contain a newline character (`\\n`), so the second `print` will be printed on the same line as the first one.")
elif user_answer == "2":
    st.error("Incorrect. The value for `end` in the first `print` does not contain a newline character (`\\n`), so the second `print` will be printed on the same line as the first one.")

st.markdown("---")

# f-strings
st.header("3.4: f-strings")

st.markdown("""
            So far, we've been printing values by inserting them directly into the `print()` function. However, this is not the only way to print values. We can also use f-strings to print values.

            F-strings are a way to embed variables in strings. They are created by prefixing the string with `f` and then using curly braces to embed the variable name.

            ```python
            name = "Tony"
            print(f"Hello, {name}!")
            ```

            The output will be:

            ```
            Hello, Tony!
            ```

            F-strings are a powerful way to print values, and are often used in Python code.
            """)

# Quick question about f-string syntax
st.subheader("Quiz: f-string syntax")
st.markdown("""
            **Q1: What are the two parts of an f-string?**
            """)
user_answer = st.radio("Choose the correct answer for Q1:", ["`f` and the curly braces", "`f` and a variable name", "curly braces and a variable name"], key="print_q6", index=None)
if user_answer == "`f` and the curly braces":
    st.success("Correct! The `f` is the prefix, and the curly braces are used to embed any value.")
elif user_answer == "`f` and a variable name":
    st.error("Incorrect. The variable name is actually not needed since any value can be embedded. However, the curly braces are needed to show where the value is embedded.")
elif user_answer == "curly braces and a variable name":
    st.error("Incorrect. The variable name is actually not needed since any value can be embedded. However, `f` prefix is needed to tell Python that this is an f-string.")

st.markdown("---")

# Formatting the f-string insertions
st.header("3.5: Formatting the f-string insertions")
st.markdown("""
            What if you wanted to control how the value is embedded in the string? For example, what if you wanted to print a number with a certain number of decimal places? Or what if you wanted to ensure a certain alignment or spacing of a string?

            The `:` character helps define different formatting options for the value directly before it. The table below shows some of the most common formatting options:
            """)
st.table([
    {
        "Format": "`:,d`",
        "Description": "Adds commas to the number (integers only). `d` is the format specifier for integers. Can be used with the `f` specifier to format floats."
    },
    {
        "Format": "`:.yf`",
        "Description": "Force `y` decimal places. If there are too many, round to `y` decimal places. If there are too few, add zeros to the right. `f` is the format specifier for floats."
    },
    {
        "Format": "`:a<b`",
        "Description": "Left-align the number, output with at least `b` characters. Replace `<` with `^` to center the text or `>` to right-align the text. Replace `a` to change which character is used to fill the space. Remove `a` just to use blank space as the filler. The alignment option though can be applied to both numbers and strings."
    }
])
st.markdown("""
            There are many more formatting options available, but these are the most common ones. You can find a full list of formatting options [here](https://docs.python.org/3/library/string.html#format-specification-mini-language). The three shown are the three that I believe are the most useful right away. For example, you can use `:,"` just to add commas to a number (e.g. `100000` becomes `100,000`). Feel free to experiment with all the formatting options for your needs!

            Note that the value to be formatted is placed immediately before the `:` character. For example, if we have `print(f"{100000:,}")`, the output will be `100,000`. Instead of some quiz questions, play with the code below to see how the formatting options work:
            """)

# Example for formatting a string
# Align left, center, or right
st.subheader("String alignment example")
alignment = st.radio("Choose which alignment you want to use:", ["Left", "Center", "Right"], key="print_q7")
size = st.slider("Choose the size of the text:", min_value=1, max_value=10, value=5, step=1, key="print_q8")
filler = st.text_input("Choose the filler character (hit Enter to apply):", value=" ", key="print_q9")

# Convert filler choice to format symbol
if len(filler) > 1:
    filler = filler[0]
    st.error("Only the first character of the filler will be used as the filler character can only be one character.")
elif len(filler) == 0:
    filler = " "

# Convert alignment choice to format symbol
if alignment:
    align_symbol = {"Left": "<", "Center": "^", "Right": ">"}[alignment]

# Code block
st.markdown("**Code:**")
st.markdown(f"""
            ```python
            print(f"{{'abc':{filler}{align_symbol}{size}s}}")
            ```
            """)
st.markdown("**Output:**")
st.code(f"{'abc':{filler}{align_symbol}{size}s}")

# Example for adding commas to a number
st.subheader("3.5.1: Adding commas to a number")
number_of_zeros = st.slider("Enter the number of zeros to add:", min_value=0, max_value=10, value=4, step=1, key="print_q10")

# Code block
st.markdown("**Code:**")
st.markdown(f"""
            ```python
            print(f"{{{int("1" + "0" * number_of_zeros)}:,d}}")
            ```
            """)
st.markdown("**Output:**")
st.code(f"{int('1' + '0' * number_of_zeros):,d}")

# Example for formatting a float
st.subheader("3.5.2: Formatting a float")
number_of_decimals = st.slider("Enter the number of decimal places to show:", min_value=0, max_value=10, value=2, step=1, key="print_q11")

# Code block
st.markdown("**Code:**")
st.markdown(f"""
            ```python
            from math import pi
            print(f"{{pi:.{number_of_decimals}f}}")
            ```
            """)
st.markdown("**Output:**")
from math import pi
st.code(f"{pi:.{number_of_decimals}f}")

st.markdown("---")
st.caption("© 2025 Anthony Ha-Anh Pham | Licensed under [GNU GPL 3.0](https://www.gnu.org/licenses/gpl-3.0.html) | View source code on [GitHub](https://github.com/RicePandaaaa/TonyIntroToPython)")
