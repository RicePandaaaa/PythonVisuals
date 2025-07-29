import streamlit as st

st.title("9: Loops")

st.markdown("""
            Loops are a fundamental concept in programming. They allow you to repeat a block of code multiple times. There are two types of loops in Python: `for` loops and `while` loops.

            A `for` loop is used to iterate over a sequence (e.g. a string) and execute a block of code for each item in the sequence. It is also commonly used to execute a block of code a specific number of times.

            A `while` loop is used to execute a block of code repeatedly until a condition is met. The number of times the code is executed is not known beforehand, unlike a `for` loop.

            Be sure to note this difference very carefully: a `for` loop is used when you know exactly how many times you want to do something no matter what while a `while` loop is used when you only know the condition for the loop to continue. 
            """)

st.markdown("---")

st.subheader("9.1: `for` loops")

st.subheader("9.1.1: Overview")

st.markdown("""
            `for` loops are used to iterate over a sequence (e.g. a string) and execute a block of code for each item in the sequence.

            The general syntax of a `for` loop is:
            ```python
            for item in sequence:
                # code to execute for each item in the sequence
            ```

            Note the indentation of the code block. It is very important to indent the code block correctly. Only code that is indented directly after the `for` loop will be looped over. Code not indented will be treated as outside of the loop. Also, don't forget the colon at the end of the `for` loop line!

            `item` is usually a variable local to the loop, and it is used to hold the current item in the sequence. It does not need to be created beforehand. In most cases, it's actually preferred that you don't create the variable beforehand because it can cause confusion. If you use a pre-existing variable, the loop will change the value of the variable.

            `sequence` is the sequence you want to iterate over. It can be a string, but for now, it's most common to be a `range()`. `in` is just required to be there. Don't worry too much about what exactly it does, just know that it's required.
            """)

st.markdown("---")

st.subheader("9.1.2: `range()`")

st.markdown("""
            `range()` is a built-in function that returns a sequence of numbers. It is commonly used in `for` loops.

            The general syntax of `range()` is:
            ```python
            range(start, stop, step)
            ```

            `start` is the starting number of the sequence. It defaults to 0. `stop` is the ending number of the sequence. It is not included in the sequence. `step` is the difference between each number in the sequence. It defaults to 1. For example, `range(1, 10, 2)` will return `[1, 3, 5, 7, 9]`. 

            `step` also has an additional rule: it cannot be 0, ever. All three parameters must also be integers. If any of them are not integers, you will get an error.

            Note that since `start` defaults to 0 and `step` defaults to 1, you can actually just put in one number into `range()` and it will return a sequence of numbers from 0 to that number. For example, `range(10)` will return `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`. 
            
            This is incredibly useful if you know how many times you want to loop. Note that `range(n)` will generate a list from 0 to n-1, which is a list of `n` numbers. What does this mean? You can use a `for` loop to just do something `n` times, even if you don't care about the loop variable!

            For example, if you want to `print("Hi")` 10 times, you can do:
            ```python
            for _ in range(10):
                print("Hi")
            ```
            
            The usage of `_` is a convention to indicate that the loop variable is not used. It's a throwaway variable. However, you can just name it something else, such as `i` (arguably the most common loop variable name). Note that `_` actually does store the current number the loop is on, but it doesn't have to be used. It's just there in case you need it (and also because the syntax demands the existance of a loop variable).

            For an example of actually using the loop variable, we can make a simple star pyramid:
            ```python
            for i in range(6):
                print("*" * i)
            ```
            
            Remember that a string multiplied by an integer will repeat the string that many times. So in this case, `"*" * i` will repeat the `"*"` character `i` times. As the loop variable `i` goes from 0 to 5, the number of stars will increase from 0 to 5, creating a pyramid made out of stars (the `*` is the star). Also remember that the `stop` number is not included in the sequence, so the last line has 6-1, or 5 stars.

            Output:
            ```

            *
            **
            ***
            ****
            *****
            ```

            The empty line is due to the 0 star line (0 stars means there's just nothing in that line).
            """)

# Basic quiz for `for` loops
# Ask about what keyword makes a for loop
st.subheader("Quiz: `for` loop basics")
st.markdown("""
            **Q1:** What keyword is used for a `for` loop?
            """)
user_answer = st.text_input("Enter your answer:", key="for_loop_q1")

if user_answer.lower() == "for":
    st.success("Correct!")
elif len(user_answer) > 0:
    st.error("Incorrect. `for` is the keyword used.")

st.markdown("""
            Refer to the following code for the next four questions:
            ```python
            for i in range(4):
                print("Hi")
            print("Bye")
            ```
            """)

st.markdown("""
            **Q2:** What is the loop variable in the code above?
            """)
user_answer = st.text_input("Enter your answer:", key="for_loop_q2")

if user_answer == "i":
    st.success("Correct!")
elif len(user_answer) > 0:
    st.error("Incorrect. The loop variable is `i`.")

st.markdown("""
            **Q3:** How many lines of output will there be?
            """)
user_answer = st.text_input("Enter your answer:", key="for_loop_q3")

if user_answer == "5":
    st.success("Correct!")
elif len(user_answer) > 0:
    st.error("Incorrect. There are 5 lines of output (4 `Hi`s and 1 `Bye`). `range(4)` will generate a list from 0 to 3, which is 4 numbers. The `for` loop will then go through each number, printing `Hi` each time, resulting in 4 `Hi`s. Then, the loop will finish, and the `print(\"Bye\")` will execute, resulting in 1 `Bye`. This is why there are 5 lines of output.")

st.markdown("---")

st.subheader("9.1.3: Advanced `range()` usages")

st.markdown("""
            `range()` can be defined using just two numbers, the `start` and `stop`. The `step` defaults to 1. For example, `range(10, 20)` will return `[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]`. This isn't exactly very advanced, but it's good to know that you can provide one, two, or all three numbers to `range()`.

            `range()` can also be used to create a sequence of numbers in reverse. For example, `range(10, 0, -1)` will return `[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]`.

            You can also use a negative `step` to create a sequence of numbers in reverse. For example, `range(10, 0, -2)` will return `[10, 8, 6, 4, 2]`. Note that if `step` is positive, then the loop only works if `start < stop`. If `start > stop`, then the loop will not run at all, because `start` already exceeds `stop`. The same thing happens if `step` is negative. If `start < stop`, then the loop will not run at all, because `start` is already less than `stop`.

            As code examples, these two `for` loops will never run:
            ```python
            # step > 0, start > stop
            for i in range(10, 0, 1):
                print("Hi")

            # step < 0, start < stop
            for i in range(0, 10, -1):
                print("Hi")
            ```
            """)

# Questions about possible combinations
st.subheader("Quiz: `range()` combinations")

st.markdown("""
            **Q1:** If you provide just one number to `range()`, what parameter does the number correspond to?
            """)
user_answer = st.text_input("Enter your answer:", key="range_q1")

if user_answer.lower() == "stop":
    st.success("Correct!")
elif len(user_answer) > 0:
    st.error("Incorrect. The number corresponds to the `stop` parameter.")

st.markdown("""
            **Q2:** If you provide two numbers to `range()`, what parameters do the numbers correspond to?
            """)
user_answer = st.radio("Answers:", ["start, stop", "stop, step", "start, step"], key="range_q2", index=None)

if user_answer == "start, stop":
    st.success("Correct! The first number corresponds to the `start` parameter, and the second number corresponds to the `stop` parameter.")
elif user_answer is not None:
    st.error("Incorrect. The first number corresponds to the `start` parameter, and the second number corresponds to the `stop` parameter.")

st.markdown("""
            **Q3:** If `start > stop`, then `step` must be what?
            """)
user_answer = st.radio("Answers:", ["positive", "negative", "zero"], key="range_q3", index=None)

if user_answer == "negative":
    st.success("Correct! If `start > stop`, then `step` must be negative! This allows the sequence to start at the higher number (`start`) and decreases over time until it reaches the lower number (`stop`).")
elif user_answer is not None:
    st.error("Incorrect. If `start > stop`, then `step` must be negative! This allows the sequence to start at the higher number (`start`) and decreases over time until it reaches the lower number (`stop`).")

st.markdown("""
            **Q4:** If `start < stop`, then `step` must be what?
            """)
user_answer = st.radio("Answers:", ["positive", "negative", "zero"], key="range_q4", index=None)

if user_answer == "positive":
    st.success("Correct! If `start < stop`, then `step` must be positive! This allows the sequence to start at the lower number (`start`) and increases over time until it reaches the higher number (`stop`).")
elif user_answer is not None:
    st.error("Incorrect. If `start < stop`, then `step` must be positive! This allows the sequence to start at the lower number (`start`) and increases over time until it reaches the higher number (`stop`).")

st.markdown("---")

st.subheader("9.2: `while` loops")

st.subheader("9.2.1: Overview")
st.markdown("""
            `while` loops are used to execute a block of code repeatedly while a condition is met.

            The general syntax of a `while` loop is:
            ```python
            while condition:
                # code to execute while the condition is true
            ```

            The only `keyword` here is `while`, and the condition just needs to be evaluable to a boolean value. Some times, people want a `while` loop to run forever, so they just use `True` as the condition. There are ways around this, but that is just to make the point that as long Python can evaluate that condition to either `True` or `False`, the loop is legal. Do note that although `while` loops are known to have an unknown amount of iterations, there are times you can still determine the number of iterations:

            ```python
            i = 0
            while i < 10:
                print(i)
                i += 1
            ```

            When it is said that `while` loops do not have a fixed number of iterations, this is due to the unpredictablity of the conditions used *in general*. It does not mean you can *never* determine the number of iterations. Some loop usages, such as the one shown above, give enough context to determine the number of iterations. That being said, you should be using a `for` loop if you *already* know the number of iterations itself. If you know *when* the loop should be running instead of *how many times* it should be running, then a `while` loop is the way to go.
            """)

# Quiz about `while` loops
st.subheader("Quiz: `while` loops")

st.markdown("""
            **Q1:** What keyword is used for a `while` loop?
            """)
user_answer = st.text_input("Enter your answer:", key="while_loop_q1")
if user_answer.lower() == "while":
    st.success("Correct!")
elif len(user_answer) > 0:
    st.error("Incorrect. `while` is the keyword used.")

st.markdown("""
            **Q2:** What is the condition in the code below?
            ```python
            i = 0
            while i < 10:
                print(i)
                i += 1
            ```
            """)
user_answer = st.text_input("Enter your answer:", key="while_loop_q2")
if len(user_answer) > 0 and "".join(user_answer.split()).lower() == "i<10":
    st.success("Correct!")
elif len(user_answer) > 0:
    st.error("Incorrect. The condition is `i < 10`.")

st.markdown("""
            **Q3:** Is this an infinite loop?
            ```python
            while True:
                print("Hi")
            ```
            """)
user_answer = st.radio("Answers:", ["Yes", "No"], key="while_loop_q3", index=None)
if user_answer == "Yes":
    st.success("Correct! The loop will run forever because the condition is always `True`.")
elif user_answer is not None:
    st.error("Incorrect. The loop will run forever because the condition is always `True`.")

st.markdown("---")

st.markdown("---")
st.caption("© 2025 Anthony Ha-Anh Pham | Licensed under [GNU GPL 3.0](https://www.gnu.org/licenses/gpl-3.0.html) | View source code on [GitHub](https://github.com/RicePandaaaa/TonyIntroToPython)")