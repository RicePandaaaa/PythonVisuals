import streamlit as st

st.title("6: Planning and Design")
st.markdown("---")

# Introduction
st.header("6.1: Introduction")
st.markdown("""
            The most challenging aspect of programming is translating abstract human ideas into precise instructions that a computer can execute. As humans, we naturally interpret meaning and context from information, adapting our understanding based on nuance and implications. Computers, however, cannot interpret or contextualize: they simply follow instructions exactly as given, regardless of whether those instructions accomplish what we intended.

            This fundamental difference means we must develop the ability to decompose ideas and problems into increasingly specific steps, breaking them down until each component is precise enough to translate directly into code. This decomposition process requires two essential skills.

            - First, understanding what your programming language can accomplish—knowing the tools available to you and their capabilities.
            - Second, learning to distinguish critical information from irrelevant details, then systematically breaking that essential information into manageable pieces that can be logically sequenced.

            This second skill is the heart of planning and design in programming. It is the bridge between human creativity and computational precision, transforming fuzzy concepts into the step-by-step logic that computers require. In other words, it is the bridge between dreams and reality.
            """)
st.markdown("---")

# Planning
st.header("6.2: Input, Processing, and Output")
st.markdown("""
            It is my belief that planning and design is a very personal process. Even though there are general guidelines that can be followed, the details of how you plan and design are more than likely determined by your own personal style and preferences. Here, I will introduce my personal process of planning and design. Feel free to adapt any or all of this as necessary.

            For any prompt, I break it down into three major components:
            - Input: How will the user provide information to the program? Does the user even need to provide information?
            - Processing: What does the program need to do with the input?
            - Output: How will these results be displayed to the user?

            Personally, trying to plan all three at the same time simultaneously is just too difficult. The input, processing, and output are all dependent on each other, so I rather establish each component one at a time. I start with the input, then the output, and then the processing. 
            
            For now, the programs made with what have been taught so far are all terminal-based, which means there's not too many ways to go about doing something. Once more advanced concepts are introduced, especially libraries (modules), there has to be additional planning around selecting the correct library and ensuring that the library can be used. The analogy I use is cooking and cleaning both require two very different sets of tools and do very different things. I have to know whether I am cooking and cleaning and then ensure I select the right tools and that the actions I take are possible. However, that is for later. For now, let's focus on the three major components.
            """)
st.markdown("---")

# Input
st.subheader("6.2.1: Input")
st.markdown("""
            The input is the information that the user provides to the program. There are three main parts to input: receiving, sanitizing, and storing.

            Receiving is all about what information the user needs to provide and how the user will provide that information to the program. Figuring out what information the user needs to provide is the first step. Afterwards, you have to figure out what's the best way to for the user to enter each piece of information. As of now, that's really just with the `input()` function. However, there are other ways to receive input such as with data files or through a GUI (graphical user interface).

            Sanitizing is all about ensuring that the input is valid. This is two-fold: you can either fix the input yourself or validate the input and make the user re-enter the input if it is invalid. An example of this is the classic "Yes or No" prompt. There are 8 ways to say "yes" due to capitalization variations. You can fix the input yourself by converting the input to all uppercase and checking if it is either just "YES" or "NO", saving you time from having to check for all the variations. However, you have to ensure that even after capitalization, the input is either "YES" or "NO" (maybe the user misspelled and did not type either word).

            Storing is all about with which format is the input stored in and where the input is stored. For example, `input()` always gives you a string, so you might have to cast it to a `int` or `float` if you need to do math with the input. Maybe the input you got is actually several pieces of information all at once, so you have to split up the input correctly and store each piece in a separate variable. Storing correctly is very important to help with the processing step since it is dependent on how the information is stored and can be accessed.
            """)
st.markdown("---")

st.subheader("6.2.2: Output")
st.markdown("""
            It may be weird that I actually plan the output before processing. But, through personal experience, I found that it is much harder to ensure that the output format is compatible with what I have planned for processing than to ensure the processing is capable of generating the output format. Anyways, output really is just answering two questions: what results need to be displayed and how will they be displayed.

            Even if a program's job is just to do something, such as an installer that just downloads data, there usually still is feedback that informs the user that the job is done. For now, your output is probably some combination of `print()` and f-strings, but there are way many more ways of outputting information or feedback to the user.
            """)
st.markdown("---")

# Processing
st.subheader("6.2.3: Processing")
st.markdown("""
            Processing is all about what the program needs to do with the input. I always say that processing is threefold:
            - How would I normally use the input information to generate the output if I were to do it myself?
            - How would I convert those steps I would take into code?
            - How would I ensure the results or feedback can be properly displayed?

            Processing really is the link between the input and the output. I think the first question I ask is under-used. If you don't know how to do something yourself, how can you expect to be able to tell Python how to do that something? Once you really know how to do it yourself, you can start to think about how to convert those steps into code. A quick example would be, if I wanted to communicate "Hi!" to someone, I would usually just say it out loud. The Python equivalent would be `print("Hi!")`.

            Input was planned out first since this ensures that the data coming in is clean and usable right away. If the input has potential flaws, then it can really complicate the processing since now you also have to watch for edge cases. Output was planned out next since this can actually also affect with which additional technologies you will use. If your output requires an actual visual, then you need to use Python tools that are capable of generating those visuals.

            At this point, ideally, you should have trust that:
            - The input is clean and usable
            - The format of the input is all known
            - The output format is all known
            
            Perhaps while planning the processing, you realize that the input is not as clean or even too clean. You may have to adjust the input a bit to be more or less flexible. Maybe you realize that the output format is rather difficult to implement. You may have to change the output format to still show the desired results or feedback but in a different way that's more plausible to do. In my experience, this section of planning is where most potential changes are made.
            """)
st.markdown("---")

# Summary
st.header("6.3: Final Thoughts")
st.markdown("""
            Sometimes, planning isn't even necessary. Simple enough programs (for your skill level) can be written without any or much planning due to your experience and knowledge of the language. However, as the projects become more complex (in size or in difficulty), planning becomes more and more important. Sometimes, you can get away with planning in your head, but it probably will get to a point where it's best to write down and draw out your thoughts and ideas.

            Also, planning and design is not perfect! Expect to have to go back and change your plans to address problems or scenarios that you did not anticipate! And sometimes, you might only figure this out while you are actually writing the code. Planning and design is meant to give you the best guide possible, but it is not a guarantee that your code will work perfectly the first time.
            """)

st.markdown("---")
st.caption("© 2025 Anthony Ha-Anh Pham | Licensed under [GNU GPL 3.0](https://www.gnu.org/licenses/gpl-3.0.html) | View source code on [GitHub](https://github.com/RicePandaaaa/TonyIntroToPython)")
