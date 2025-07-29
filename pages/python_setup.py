import streamlit as st

st.title("1: Setup")

st.write("---")

# Python Installation
st.header("1.1: Python Installation")

st.write("""
        Python is a popular programming language that is easy to learn and use. It is a general-purpose language that can be used for a wide range of applications.

        To install Python, you can download the installer from the [official website](https://www.python.org/downloads/). Feel free to download the latest stable version. When you download Python, you download an installer that will allow you to install Python on your computer.
         
        When you run the installer, the first screen will ask you how you would like to install Python. At the very bottom, you should see an option to "Add Python to PATH". This is very important because it allows you to use Python from the command line. Even if you don't know what this means, it is very important that you select this option.
         
        After this, you can continue the installation as normal and using the default options that Python provides. Feel free to select different options if you know what you are doing.

        Below is a handy checklist for the installation process:
        """)

# Create the checklist
download_checkbox = st.checkbox("Download the installer from the [official website](https://www.python.org/downloads/).")
installer_checkbox = st.checkbox("Run the installer and follow the instructions.")
path_checkbox = st.checkbox("Select the option to 'Add Python to PATH'.")
install_checkbox = st.checkbox("Continue the installation as normal and using the default options that Python provides.")

st.write("---")

# IDE Setup
st.header("1.2: IDE Setup")

st.write("""
        An IDE (Integrated Development Environment) is a software application that allows you to more easily write and test your code. For Python, there are several options to choose from:
        """)

st.subheader("1.2.1: IDE Options")
st.write("""
                 - [repl.it](https://repl.it/languages/python3)
          - Online IDE (requires internet connection)
          - Requires an account (sign up)
          - Limited amount of projects without a subscription
          - Good for fast code testing, not so good for projects/large amounts of files
        - [VSCode](https://code.visualstudio.com/): Accessible online and offline, great as a flexible code editor, not as powerful as PyCharm
          - Offline IDE (just install to your computer)
          - Lightweight and fast
          - Customizable with extensions
          - Works for various languages, not just Python
        - [PyCharm](https://www.jetbrains.com/pycharm/): Extremely powerful for Python, but all the Python features can be a bit overwhelming
          - Offline IDE (just install to your computer)
          - Powerful and feature-rich
          - Made specifically for Python
          - Community (free) version is slightly limited but still very powerful

        My personal recommendation is VSCode. It is a very powerful code editor that is free and open source. The installation process is pretty simple, and there's a lot of personalization options with extensions. However, feel free to try all sorts of IDEs (or look at videos of people using them on YouTube) and see which one you like best.
        """)

st.subheader("1.2.2: Installation Guides")
st.write("""
        The installation guides for the three mentioned IDEs are below:
        - [Install repl.it](https://repl.it/languages/python3)
        - [Install VSCode](https://code.visualstudio.com/docs/setup/setup-overview)
        - [Install PyCharm](https://www.jetbrains.com/pycharm/download/#section=windows)
         
        If you are using your own IDE, it should have its own installation guide online somewhere.
        """)

st.markdown("---")
st.caption("© 2025 Anthony Ha-Anh Pham | Licensed under [GNU GPL 3.0](https://www.gnu.org/licenses/gpl-3.0.html) | View source code on [GitHub](https://github.com/RicePandaaaa/TonyIntroToPython)")
