import streamlit as st

st.title("Setup")

st.write("---")

# Python Installation
st.header("Python Installation")

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
