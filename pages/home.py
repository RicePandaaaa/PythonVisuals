import streamlit as st

st.title("Home")

# Tell users what the layout is
st.markdown("""
            Welcome to this Intro to Python notes collection! It was designed as a quick reference for the basics of Python. Each page has a different set of topics and contains examples and questions to test your understanding. **This is a work in progress, so expect to see updates and changes in the near future!**

            The chapters can be selected from the sidebar on the left. If you can't see it, there should be a button in the top left corner of the page that looks like \">>\". This sidebar is collapsible, so you can collapse it if you want to.

            The chapters are as follows:
            - 00\. Home
            - 01\. Setup
            - 02\. Variables and Data Types
            - 03\. Basic Output
            - 04\. Basic Math Operations
            - 05\. User Input
            - 06\. Planning and Design
            - 07\. Conditionals
            - 08\. Functions
            - 09\. Loops
            - 10\. Lists
            """,)
st.markdown("---")

st.header("About the Author")
st.markdown("""
            Howdy, my name is Anthony Pham, and I am currently pursuing a Master's of Science in Engineering Technology at Texas A&M! I started teaching myself Python with the help and encouragement of my dad when I was 10 years old, and I have been coding as a hobby ever since! I also love tutoring my friends, and I am blessed to have the privilege to help teach Python to freshmen engineering students at my university as a peer teacher for three years during my undergrad!

            My love of Python started with a book called "Hello World!: Computer Programming for Kids and Other Beginners, 2nd Edition" by Warren and Carter Sande. It is my belief that with the right starting point, anyone can learn how to code and enjoy it too! I have made this mini-textbook as a free way for students and anyone else curious about Python to learn the basics of Python in an interactive way. There are other resources out there for sure, but I just wanted to add in my own twist to the mix, using my personal experience from self-teaching and teaching others.
            
            Within this mini-textbook, I have included notes, questions, and code snippets to play with! Soon, I plan to add labs (mini projects), projects, and videos as well! If you have any feedback, please feel free to contact me at [anthony.ha.pham@gmail.com](mailto:anthony.ha.pham@gmail.com).
            """)

st.markdown("---")
st.caption("© 2025 Anthony Ha-Anh Pham | Licensed under [GNU GPL 3.0](https://www.gnu.org/licenses/gpl-3.0.html) | View source code on [GitHub](https://github.com/RicePandaaaa/TonyIntroToPython)")

