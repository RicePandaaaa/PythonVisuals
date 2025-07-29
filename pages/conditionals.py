import streamlit as st

st.title("7: Conditionals")
st.markdown("---")

# Introduction
st.header("7.1: Introduction")
st.markdown("""
            We make decisions in our lives every day. By considering certain pieces of information, we can determine what course of action to take. In programming, we can have Python also make decisions based on whether certain conditions are met or not met. Fundamentally, conditionals are all about whether something is `True` or `False`. There is no risk assessment or any probability involved. We may take the *best* course of action, even if some of the conditions are not entirely met. However, Python will only take certain actions if *all* the given conditions are met.
            """)
st.markdown("---")

# Boolean data type
st.header("7.2: Boolean Data Type")
st.markdown("""
            Booleans represent the truth values `True` and `False`. These values mean exactly what they say: `True` means that something is true, and `False` means that something is false. Generally, you never directly use `True` or `False` in your code. Instead, you use conditional statements that evaluate to either `True` or `False`.

            As an advanced note, the `bool` data type is actually a subclass of the `int` data type. This means that `True` is equivalent to `1` and `False` is equivalent to `0`. This is useful for when you need to do math with booleans. I won't teach you boolean algebra, but there are some weird side effects that you may encounter.
            """)
st.markdown("---")

# If statement
st.header("7.3: `if`")
st.markdown("""
            This keyword is used to make conditional statements, and what can be referred to as a code block. A code block is a group of code that is executed together as part of a particular statement. In this case, the code block is the code that is executed if the immediate condition above it is `True`. That code will never execute on any other condition.

            ```python
            if {condition}:
                {code block}
            
            {not code block}
            ```

            Note the code block immediately follows the `if`, `elif`, or `else` keyword. You cannot have code between the code block and the conditional keyword that does not belong to the code block. Also note that the way for Python to know what code belongs to a conditional statement is the indentation. Indentation is almost always four spaces. Some IDEs allow for two or eight spaces, but any other number is not recommended and is likely to cause an error. You also need to be consistent with indentation (i.e. it's always two or four or eight spaces).

            Here are some examples of what not to do:
            ```python
            # Illegal indentation (wrong amount of spaces)
            if {condition}:
               {code block}   # 3 spaces
            
            # Lack of indentation (if statement can't be empty)
            if {condition}:
            {code block}

            # Code block is not connected
            if {condition}:
                {code block}
            {not code block}
                {desired code block}
            ```
            """)

# Quiz to test syntax understanding
st.subheader("Quiz: `if` statements")

st.markdown("""
            For the next two questions, refer to the code below
            ```python
            if {condition}:
                print("Hello", end=" ")
            print("World")
            ```
            """)
st.markdown("""
            **Q1:** If the condition is `True`, what will be printed?
            """)
user_answer = st.radio("Answers:", ["Hello World", "Hello", "World"], key="if_1", index=None)
if user_answer == "Hello World":
    st.success("Correct! The code block is executed because the condition is `True`, and the second `print()` executes no matter what since it is not tied to the condition.")
elif user_answer == "Hello":
    st.error("Incorrect. The second `print()` executes no matter what since it is not tied to the condition, so the answer is `Hello World`.")
elif user_answer == "World":
    st.error("Incorrect. The condition is `True`, so the `Hello ` is printed. The correct answer is `Hello World`.")

st.markdown("""
            **Q2:** If the condition is `False`, what will be printed?
            """)
user_answer = st.radio("Answers:", ["Hello World", "Hello", "World"], key="if_2", index=None)
if user_answer == "World":
    st.success("Correct! The code block is not executed because the condition is `False`, and the second `print()` executes no matter what since it is not tied to the condition.")
elif user_answer is not None:
    st.error("Incorrect. The condition is `False`, so the code block is not executed, and the second `print()` executes no matter what since it is not tied to the condition. The correct answer is `World`.")

st.markdown("---")

# Relational operators
st.header("7.4: Relational Operators")
st.markdown("""
            Relational operators are used to compare two values. The result of a relational operator is a boolean value. The table below shows the relational operators and their results.
            """)
st.table([
    {
        "Operator": "`==`",
        "Description": "Equal to",
        "Example": "`5 == 5`",
        "Result": "`True`"
    },
    {
        "Operator": "`!=`",
        "Description": "Not equal to",
        "Example": "`5 != 5`",
        "Result": "`False`"
    },
    {
        "Operator": "`>`",
        "Description": "Greater than",
        "Example": "`6 > 5`",
        "Result": "`True`"
    },
    {
        "Operator": "`<`",
        "Description": "Less than",
        "Example": "`6 > 5`",
        "Result": "`False`"
    },
    {
        "Operator": "`>=`",
        "Description": "Greater than or equal to",
        "Example": "`5 >= 5`",
        "Result": "`True`"
    },
    {
        "Operator": "`<=`",
        "Description": "Less than or equal to",
        "Example": "`5 <= 5`",
        "Result": "`True`"
    }
])
st.markdown("""
            Note that regardless of operator, the result is always a boolean value. This means that a comparison of two values can be used in `if` statements. Try adjusting the code below to see the output.
            """)

# Code example for relational operators
st.subheader("7.4.1: Code example: Relational operators")
operator = st.radio("Choose the operator:", ["`==`", "`!=`", "`>`", "`<`", "`>=`", "`<=`"], key="rel_op", index=0)
if operator is not None:
    operator = operator[1:-1]
left_value = st.slider("Choose the left value:", min_value=0, max_value=10, value=5, key="rel_op_left", step=1)
right_value = st.slider("Choose the right value:", min_value=0, max_value=10, value=5, key="rel_op_right", step=1)

st.markdown(f"""
            Code:
            ```python
            if {left_value} {operator} {right_value}:
                print("The condition is True.")
            else:
                print("The condition is False.")
            ```

            Output:
            """)

outcome_if_true = "The condition is True."
outcome_if_false = "The condition is False."
if operator is not None:
    if operator == "==":
        st.markdown(f"```\n{outcome_if_true if left_value == right_value else outcome_if_false}\n```")
    elif operator == "!=":
        st.markdown(f"```\n{outcome_if_true if left_value != right_value else outcome_if_false}\n```")
    elif operator == ">":
        st.markdown(f"```\n{outcome_if_true if left_value > right_value else outcome_if_false}\n```")
    elif operator == "<":
        st.markdown(f"```\n{outcome_if_true if left_value < right_value else outcome_if_false}\n```")
    elif operator == ">=":
        st.markdown(f"```\n{outcome_if_true if left_value >= right_value else outcome_if_false}\n```")
    elif operator == "<=":
        st.markdown(f"```\n{outcome_if_true if left_value <= right_value else outcome_if_false}\n```")

st.markdown("---")

# Chaining conditionals
st.header("7.5: `and` and `or`")
st.markdown("""
            Sometimes, you want to check if all conditions are met or if just one of the conditions are met (or just some of the conditions are met). This is where the `and` and `or` keywords come in.

            `and` only gives you `True` if both the left and right conditions are `True`. `or` only gives you `True` if at least one of the two conditions are `True`. The table below, called a truth table, shows the results of the `and` and `or` operators.

            `and` table:
            """)
st.table([
    {
        "Left": "`True`",
        "Right": "`True`",
        "Result": "`True`"
    },
    {
        "Left": "`True`",
        "Right": "`False`",
        "Result": "`False`"
    },
    {
        "Left": "`False`",
        "Right": "`True`",
        "Result": "`False`"
    },
    {
        "Left": "`False`",
        "Right": "`False`",
        "Result": "`False`"
    }
])
st.markdown("""
            `or` table:
            """)
st.table([
    {
        "Left": "`True`",
        "Right": "`True`",
        "Result": "`True`"
    },
    {
        "Left": "`True`",
        "Right": "`False`",
        "Result": "`True`"
    },
    {
        "Left": "`False`",  
        "Right": "`True`",
        "Result": "`True`"
    },
    {
        "Left": "`False`",
        "Right": "`False`",
        "Result": "`False`"
    }
])

st.markdown("""
            Note that `and` is `True` only if both conditions are `True`, and `or` is `False` only if both conditions are `False`. This is a neat way to remember quickly what the result of `and` or `or` should be. If any condition is `False`, the result of `and` is `False`, and if any condition is `True`, the result of `or` is `True`.
            """)

st.subheader("7.5.1: Multiple `and`, `or`, and relational operators")
st.markdown("""
            You can also use multiple `and` and `or` operators in a single statement. Note that `and` is evaluated before `or`. But usually, you use parentheses to group pairs of conditions together to avoid ambiguity or relying on the reader to memorize the order of operations. Example:

            ```python
            if ({condition1} and {condition2}) or {condition3}:
                {code block}
            ```

            Depending on the conditions you're combining with `and` specifically, you can just combine them into one. One common example is if you're checking if a number is between two other numbers. Normally, you might write it as:

            ```python
            num = int(input("Enter a number: "))

            if (0 < num) and (num < 10):
                print("The number is between 0 and 10.")
            ```

            However, that is the equivalent of just `0 < num < 10`. This is a common pattern, and it's a good idea to use it when you can to save yourself some typing. The above code can be rewritten to:

            ```python
            num = int(input("Enter a number: "))

            if 0 < num < 10:
                print("The number is between 0 and 10.")
            ```

            A misconception is that this simplification is similar to math where you slowly condense an expression left to right, using the new values as you go:

            ```
            1 + 2 + 3
            (1 + 2) + 3
            3 + 3
            6
            ```

            Python, for conditionals, actually checks each of the conditions one by one, then combines them together with the equivalent of `and` (essentially undoing the simplification):

            ```python
            0 < 5 < 10
            (0 < 5) and (5 < 10)
            True and True
            True
            ```

            This is why you can't use `and` and `or` to chain together multiple conditions. You can only use them to combine two conditions at a time.
            """)

# Short quiz on and/or
st.subheader("Quiz: `and` and `or`")
st.markdown("""
            **Q1:** Do you use `and` or `or` for checking if both conditions are met?
            """)
user_answer = st.radio("Answers:", ["`and`", "`or`"], key="and_or_1", index=None)
if user_answer == "`and`":
    st.success("Correct! `and` is used to check if both conditions are met.")
elif user_answer == "`or`":
    st.error("Incorrect. `or` is used to check if at least one of the conditions are met.")

st.markdown("""
            **Q2:** Can you use `and` and `or` to chain together multiple conditions?
            """)
user_answer = st.radio("Answers:", ["Yes", "No"], key="and_or_2", index=None)
if user_answer == "Yes":
    st.success("Correct! You can use `and` and `or` to chain together multiple conditions.")
elif user_answer == "No":
    st.error("Incorrect. You can use `and` and `or` to chain together multiple conditions.")


st.subheader("7.5.2: Smart `and` and `or`")
st.markdown("""
            This is a rarely used feature, but Python is actually incredibly smart with how it evaluates `and` and `or` statements.

            For `and`, if the left condition is `False`, the right condition is not evaluated because Python knows the result will be `False` no matter what. For `or`, if the left condition is `True`, the right condition is not evaluated because Python knows the result will be `True` no matter what.

            I sometimes use the `and` feature as a way of circumventing errors. It's probably not the best way to do it, but I can at least guarentee that I only evaluate a certain condition if something is legal. This example uses concepts from future sections, but I'll show it anyways. For context, Python throws an error if I try to access a position in a string that does not exist. For example, if my string is empty and I try to access the first position, Python will throw an error. I might check it like this:

            ```python
            # Check if the string is not empty
            if len(string) > 0:
                # Check if the first character is "a"
                if string[0] == "a":
                    print("The first character is 'a'.")
            ```

            This is perfectly readable and safe. However, I kinda hate indentation, so I might rewrite it like this:

            ```python
            if len(string) > 0 and string[0] == "a":
                print("The first character is 'a'.")
            ```

            Now is this slightly less readable? Probably. This is just a stylistic choice I made for myself. However for you, it's probably better to just use the first version. It is more flexible and easier to debug. I just wanted to use this as an example of Python's smart evaluation in action.
            """)

st.markdown("---")

# elif and else
st.header("7.6: `elif` and `else`")
st.markdown("""
            What if we want to Python to have different options of what to do based on different conditions? This is where `elif` and `else` come in.

            `elif`, short for "else if", is used to check for additional conditions if the previous conditions were not met. `else` is used to specify what to do if none of the previous conditions were met. Before we get to usage, let's talk about how you define "previous conditions". 
            
            `elif` must be used directly after an `if` or `elif` statement. `else` must be used directly after an `if` or `elif` statement. The heirarchy of `if`, `elif`, and `else` is as follows:

            ```python
            if {condition1}:
                {code block}
            elif {condition2}:
                {code block}
            elif {condition3}:
                {code block}
            ...
            else:
                {code block}
            ```

            The way you would evaluate this is:
            - Check if `condition1` is `True`. If it is, execute the code block.
            - If `condition1` is `False`, check if `condition2` is `True`. If it is, execute the code block.
            - If `condition2` is `False`, check if `condition3` is `True`. If it is, execute the code block.
            - If `condition3` is `False`, check if `condition4` is `True`. If it is, execute the code block.
            - ...
            - If all conditions above are `False`, execute the code block after the `else` statement.

            Note that there is only one `if` statement. Once there is a new `if` statement, you start over in that evaluation list. For example:

            ```python
            x = 2
            y = 5

            if x > 2:
                print("x is greater than 2")
            elif x > 1:
                print("x is greater than 1")
            else:
                print("x is less than 1")
            
            if y < 3:
                print("y is less than 3")
            elif y < 4:
                print("y is less than 4")
            else:
                print("y greater than 4")
            ```

            The first `if` statement is `False`, but the `elif` right after is `True`. This doesn't mean the rest of the conditional statements are ignored because there's another `if` statement! The first `else` is skipped because the `elif` above it was `True`. However, the second `if` statement is checked because it's an `if` statement (which is always checked). That statement and the `elif` right after it are both `False`, so the `else` is executed. The output is thus:

            ```
            x is greater than 1
            y is greater than 4
            ```
            """)

# Quiz to check understanding on elif/else
st.subheader("Quiz: `elif` and `else`")

# Ask about order of elif and else
st.markdown("""
            **Q1:** What is the order of execution for `if`, `elif`, and `else`?
            """)
user_answer = st.radio("Answers:", ["`if` first, then `else`, then `elif`", "`if` first, then `elif`, then `else`", "`else` first, then `if`, then `elif`", "`elif` first, then `if`, then `else`"], key="elif_else_1", index=None)
if user_answer == "`if` first, then `elif`, then `else`":
    st.success("Correct! `if` is checked first, then `elif`, then `else`.")
elif user_answer is not None:
    st.error("Incorrect. `if` is checked first, then `elif`, then `else`.")

# How many elif can you have
st.markdown("""
            **Q2:** How many `elif` statements can you have after an `if` statement?
            """)
user_answer = st.radio("Answers:", ["1", "2", "3", "Unlimited"], key="elif_else_2", index=None)
if user_answer == "Unlimited":
    st.success("Correct! You can have as many `elif` statements as you want.")
elif user_answer is not None:
    st.error("Incorrect. You can have as many `elif` statements as you want.")

# How many else's can you have
st.markdown("""
            **Q3:** How many `else` statements can you have in following an `elif` or `if` statement?
            """)
user_answer = st.radio("Answers:", ["1", "2", "3", "Unlimited"], key="elif_else_3", index=None)
if user_answer == "1":
    st.success("Correct! You can only have one `else` statement after an `elif` or `if` statement.")
elif user_answer is not None:
    st.error("Incorrect. You can only have one `else` statement after an `elif` or `if` statement.")

st.markdown("---")

# Nested conditionals
st.header("7.7: Nested Conditionals")
st.markdown("""
            Sometimes, you have more decisions to make after checking one condition. This is where nested conditionals come in. Nested conditionals are conditionals that are inside other conditionals. There is nothing really special about them other than the indentation:

            ```python
            if {condition1}:
                if {condition2}:
                    {code block}
                else:
                    {code block}
            else:
                {code block}
            ```

            As you "nest" more conditiionals, the more you have to indent. The indentation rule then becomes you need to indent relative to the `if`/`elif`/`else` that the code block belongs to. In theory, you could nest an infinite amount of times (but why?):

            ```python
            if {condition1}:
                if {condition2}:
                    if {condition3}:
                        if {condition4}:
                            if {condition5}:
                                {code block}
            ```

            The inner most code block only executes of all five conditions are `True`. Of course, this can be simplified to one long statement with a lot of `and`s, but once there are `if`/`elif`/`else` statements nested in one another, that shortcut cannot be done since there are too many possibilities.
            """)

# Quiz about nesting
st.subheader("Quiz: Nested Conditionals")

# Ask a question about output
st.markdown("""
            **Q1:** Which `print()` statement will be executed?

            ```python
            a = 20
            b = 4

            if a > 10:
                if b > 5:
                    print("a is greater than 10 and b is greater than 5")  # 1
                else:
                    print("a is greater than 10 and b is less than 5")  # 2
            else:
                print("a is less than 10")  # 3
            """)
user_answer = st.radio("Answers:", ["1", "2", "3"], key="nested_1", index=None)
if user_answer == "2":
    st.success("Correct! The first `print()` statement is executed because the first `if` statement is `True` and the second `if` statement is `True`.")
elif user_answer == "1":
    st.error("Incorrect. `a > 10` indeed is `True`, but `b > 5` is `False`, so the second `print()` statement is executed instead of the first `print()` statement.")
elif user_answer == "3":
    st.error("Incorrect. The condition for the first `if` statement is `True`, so that `else` is skipped, and thus the third `print()` statement is not executed. `a > 10` is `True` and `b > 5` is `False`, so the second `print()` statement is executed instead.")

st.markdown("---")
st.caption("© 2025 Anthony Ha-Anh Pham | Licensed under [GNU GPL 3.0](https://www.gnu.org/licenses/gpl-3.0.html) | View source code on [GitHub](https://github.com/RicePandaaaa/TonyIntroToPython)")