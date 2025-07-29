import streamlit as st

st.title("4: Basic Math Operations")
st.markdown("-" * 20)

# Introduction
st.header("4.1: Overview")
st.markdown("""
            Python supports the primary four math operations. The table below shows how they are written in Python:
            """)
st.table([
    {
        "Operation": "Addition",
        "Symbol": "\+",
    },
    {
        "Operation": "Subtraction",
        "Symbol": "\-",
    },
    {
        "Operation": "Multiplication",
        "Symbol": "\*",
    },
    {
        "Operation": "Division",
        "Symbol": "/",
    },
])

st.markdown("""
            There are also some other math operations that are supported. The table below shows how they are written in Python:
            """)
st.table([
    {
        "Operation": "Exponentiation",
        "Symbol": "**",
    },
    {
        "Operation": "Modulus",
        "Symbol": "%",
    },
    {
        "Operation": "Floor Division",
        "Symbol": "//",
    }
])
st.markdown("""
            Modulus is the remainder you get when you divide two numbers (i.e. the remainder from long division). For example, `10 % 3` is `1` because `10 / 3` is `3` with a remainder of `1`. Floor division is the same as division, but it rounds down to the nearest integer. For example, `10 // 3` is `3`. In other words, it is the integer part of the division.
            """)
st.markdown("-" * 20)

# Using math operations
st.header("4.2: Using math operations")
st.markdown("""
            It's pretty easy to actually use these operations. Just type the expressions out as you would in a calculator, and assign the result to a variable or a function. For example, if we want to add `1` and `2`, we can do the following:

            ```python
            x = 1 + 2
            print(x)
            ```

            or the more direct:

            ```python
            print(1 + 2)
            ```

            As long the two values on each side have some value, you can do the math. This means, you can do math with variables and oddly enough, even strings:

            ```python
            x = 1
            y = 2
            print(x + y)
            ```

            Note that all the math operations work with any number, regardless of the type or even if the two values are of different types. You can add two `int`s, two `float`s, or even an `int` and a `float`. For order of operations, Python follows standard mathematical order of operations. This allows you to use multiple operations in the same  For brackets/parentheses, you just use parentheses in Python:
            
            ```python
            a = (1 + 2) * 3
            print(a)   # This gets you 9 because 1 + 2 is 3, and 3 * 3 is 9
            ```
            """)

# Quiz about basic printing math expressions and order of operations
st.subheader("Quiz: Evaluating and order of operations")
st.markdown("""
            **Q1:** What is the output of the following code?
            ```python
            print(1 + 2 * 3)
            ```
            """)
user_answer = st.text_input("Enter your answer (hit Enter to submit):", key="q1")
if user_answer == "7":
    st.success("Correct! The multiplication is done first, and then the addition. 2 * 3 is 6, and 1 + 6 is 7.")
elif len(user_answer) > 0:
    st.error("Incorrect! The multiplication is done first, and then the addition. 2 * 3 is 6, and 1 + 6 is 7.")

st.markdown("""
            **Q2:** What is the output of the following code?
            ```python
            print((1 + 2) * 3)
            ```
            """)
user_answer = st.text_input("Enter your answer (hit Enter to submit):", key="q2")
if user_answer == "9":
    st.success("Correct! The addition is done first due to the parentheses, and then the multiplication. 1 + 2 is 3, and 3 * 3 is 9.")
elif len(user_answer) > 0:
    st.error("Incorrect! The addition is done first due to the parentheses, and then the multiplication. 1 + 2 is 3, and 3 * 3 is 9.")

st.markdown("-" * 20)

# Data types
st.header("4.3: Rules regarding math with certain data types")
st.markdown("""
            Now although these operations are very flexible, there are certain rules that need to be remembered. These rules are important to know because they will help you avoid errors and understand the behavior of your code:

            - Certain math operations can be used with strings, but others cannot
            - Any math with a `float` will cause the final result to be a `float`, no matter what
            - Certain math operations *always* return a `float` (in this case, just normal division)
            """)

st.subheader("4.3.1: Math with Strings")
st.markdown("""
            Strings can be thought of just a sequence of characters. It would make logical sense that you can combine two strings together to make a larger string. This is actually possible! This process is called **concatenation**. You just add the two strings together with a `+` sign between them:

            ```python
            first_name = "John"
            last_name = "Doe"
            full_name = first_name + " " + last_name
            print(full_name)
            ```

            The output is `John Doe`, and the resulting string stored in `full_name` is `\"John Doe\"`. Note that adding two strings does not naturally insert a space between the two strings. You have to manually add the space in the string. `\"John\" + \"Doe\"` is `\"JohnDoe\"`.

            Multiplication is known to be repeated addition. Python accepts this as well, and you can multiply a string by an integer to repeat the string that many times:

            ```python
            print("Hello" * 3)
            ```

            The output is `HelloHelloHello`, and the string `\"Hello\"` is repeated three times. None of the other math operations are supported with strings. Also note that doing a number times a string or a string times a number will have the same result (e.g. `3 * "Hello"` and `"Hello" * 3` both give `HelloHelloHello`).
            """)

st.subheader("4.3.2: The power of `float`")
st.markdown("""
            To simplify things, `float` is just more flexible than `int`. Remember, if you convert a `float` to an `int`, you will lose the decimal part (e.g `int(1.5)` is `1`). However, if you convert an `int` to a `float`, you will not lose any information. In fact, you gain some information (i.e. the decimal part is added). This means, if math is done with both `int`s and `float`s, the final result will be a `float` to ensure that no information is lost. The rule of thumb is that if you are doing math with a `float`, the final result will be a `float` no matter how many `int`s you have in the expression. Of course, this means, if there are no `float`s in the expression, the final result will be an `int`.

            Now, there is one notable exception. If you do division with two `int`s, the final result is still a `float`. Even `1 / 1` is `1.0`! Now modulus and floor division still return an `int` even if there are only `int`s.

            ```python
            print(1 / 1)   # 1.0
            print(1 % 1)   # 0
            print(1 // 1)  # 1
            ```

            The output for each line is `1.0`, `0`, and `1` respectively.
            """)

# Quiz about rules regarding math with certain data types
st.subheader("Quiz: String and float rules")
st.markdown("""
            **Q1:** What is the output of the following code?
            ```python
            print("Ant" + "hony")
            ```
            """)
user_answer = st.text_input("Enter your answer (hit Enter to submit):", key="q3")
if user_answer == "Anthony":
    st.success("Correct! The `+` sign is used to concatenate strings.")
elif user_answer == "Ant hony":
    st.error("Incorrect! The `+` sign is used to concatenate strings. However, it does not insert a space between the two strings. The result in this case is `Anthony`.")
elif len(user_answer) > 0:
    st.error("Incorrect! Remember, the `+` sign is used to concatenate strings (without adding a space in between). The result in this case is `Anthony`.")

st.markdown("""
            **Q2:** What is the output of the following code?
            ```python
            print("Alana" * 3)
            ```
            """)
user_answer = st.text_input("Enter your answer (hit Enter to submit):", key="q4")
if user_answer == "AlanaAlanaAlana":
    st.success("Correct! The `*` sign is used to repeat a string.")
elif len(user_answer) > 0:
    st.error("Incorrect! Remember, the `*` sign is used to repeat a string a certain amount of times. The result in this case is `AlanaAlanaAlana`.")

st.markdown("---")
st.caption("© 2025 Anthony Ha-Anh Pham | Licensed under [GNU GPL 3.0](https://www.gnu.org/licenses/gpl-3.0.html) | View source code on [GitHub](https://github.com/RicePandaaaa/TonyIntroToPython)")

