import streamlit as st
import base64
from PIL import Image
import io

# Page configuration
st.set_page_config(
    page_title="Python Setup Guide for Beginners",
    page_icon="🐍",
    layout="wide"
)

# Helper function to create downloadable links with images
def get_image_download_link(img, filename, text):
    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    href = f'<a href="data:file/png;base64,{img_str}" download="{filename}">{text}</a>'
    return href

# Title and Introduction
st.title("Python Setup Guide for Complete Beginners 🐍")
st.markdown("""
Welcome to the Python installation guide for non-programmers! This step-by-step tutorial will help you set up everything 
you need to run Python, Jupyter Notebooks, Spyder, and install all necessary libraries for data analysis and machine learning.

**What you'll learn to install:**
- Python (the programming language)
- Required Python libraries for data analysis
- Jupyter Notebooks (for interactive coding)
- Spyder (a Python development environment)
""")

# Creating tabs for different operating systems
os_tabs = st.tabs(["Windows", "macOS", "Linux"])

# Windows Tab
with os_tabs[0]:
    st.header("Installing Python on Windows")
    
    st.subheader("Step 1: Download Python")
    st.markdown("""
    1. Visit the [official Python website](https://www.python.org/downloads/windows/)
    2. Click on "Download Python 3.x.x" (the latest version - currently 3.12)
    3. Select the "Windows installer (64-bit)" option
    """)
    
    st.subheader("Step 2: Install Python")
    st.markdown("""
    1. Run the downloaded installer (e.g., `python-3.12.0-amd64.exe`)
    2. **Important**: Check the box that says "Add Python to PATH"
    3. Click "Install Now" for a standard installation
    4. Wait for the installation to complete
    """)
    
    st.image("https://user-images.githubusercontent.com/25181517/183423507-c056a6f9-1ba8-4312-a350-19bcbc5a8697.png", width=500)
    
    st.subheader("Step 3: Verify Installation")
    st.markdown("""
    1. Open Command Prompt (search for "cmd" in the Start menu)
    2. Type `python --version` and press Enter
    3. You should see the Python version you installed
    4. Type `pip --version` and press Enter to verify pip is installed
    """)
    
    st.markdown("**Type this command:**")
    st.code("python --version", language="bash")
    
    st.markdown("**You should see something like this:**")
    st.code("Python 3.12.0", language="text")
    
    st.markdown("**Now type this command:**")
    st.code("pip --version", language="bash")
    
    st.markdown("**You should see something like this:**")
    st.code("pip 23.2.1 from C:\\Python312\\lib\\site-packages\\pip (python 3.12)", language="text")
    
    st.success("Congratulations! You've successfully installed Python on Windows!")

# macOS Tab
with os_tabs[1]:
    st.header("Installing Python on macOS")
    
    st.subheader("Step 1: Download Python")
    st.markdown("""
    1. Visit the [official Python website](https://www.python.org/downloads/macos/)
    2. Click on "Download Python 3.x.x" (the latest version - currently 3.12)
    3. Download the macOS installer package
    """)
    
    st.subheader("Step 2: Install Python")
    st.markdown("""
    1. Open the downloaded .pkg file
    2. Follow the installation wizard
    3. Complete the installation process
    """)
    
    st.subheader("Step 3: Verify Installation")
    st.markdown("""
    1. Open Terminal (you can find it in Applications > Utilities > Terminal)
    2. Type `python3 --version` and press Enter
    3. You should see the Python version you installed
    4. Type `pip3 --version` and press Enter to verify pip is installed
    """)
    
    st.markdown("**Type this command:**")
    st.code("python3 --version", language="bash")
    
    st.markdown("**You should see something like this:**")
    st.code("Python 3.12.0", language="text")
    
    st.markdown("**Now type this command:**")
    st.code("pip3 --version", language="bash")
    
    st.markdown("**You should see something like this:**")
    st.code("pip 23.2.1 from /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages/pip (python 3.12)", language="text")
    
    st.success("Congratulations! You've successfully installed Python on macOS!")

# Linux Tab
with os_tabs[2]:
    st.header("Installing Python on Linux")
    
    st.subheader("Step 1: Update Package Lists")
    st.markdown("""
    Open Terminal and run:
    ```
    sudo apt update
    ```
    """)
    
    st.subheader("Step 2: Install Python")
    st.markdown("""
    Most Linux distributions come with Python pre-installed. To ensure you have the latest version:
    """)
    
    st.markdown("### For Ubuntu/Debian, copy-paste this into your terminal:")
    copy_col1, _ = st.columns([3, 1])
    with copy_col1:
        st.code("sudo apt install python3 python3-pip", language="bash")
    
    st.markdown("""
    For other Linux distributions, use the appropriate package manager:
    """)
    
    st.markdown("### For Fedora/RHEL, copy-paste this into your terminal:")
    copy_col2, _ = st.columns([3, 1])
    with copy_col2:
        st.code("sudo dnf install python3 python3-pip", language="bash")
    
    st.markdown("### For Arch Linux, copy-paste this into your terminal:")
    copy_col3, _ = st.columns([3, 1])
    with copy_col3:
        st.code("sudo pacman -S python python-pip", language="bash")
    
    st.subheader("Step 3: Verify Installation")
    st.subheader("Step 3: Verify Installation")
    
    st.markdown("### Copy-paste this into your terminal:")
    copy_col1, _ = st.columns([3, 1])
    with copy_col1:
        st.code("python3 --version", language="bash")
    
    st.markdown("### You should see something like this:")
    st.code("Python 3.10.12", language="text")
    
    st.markdown("### Now copy-paste this into your terminal:")
    copy_col2, _ = st.columns([3, 1])
    with copy_col2:
        st.code("pip3 --version", language="bash")
    
    st.markdown("### You should see something like this:")
    st.code("pip 22.0.2 from /usr/lib/python3/dist-packages/pip (python 3.10)", language="text")
    
    st.success("Congratulations! You've successfully installed Python on Linux!")

# Installing Required Libraries
st.header("Installing Required Libraries")
st.markdown("""
Now that you have Python installed, you need to install the libraries that are used in your Python files.
You'll use pip, which is Python's package installer.
""")

st.subheader("Installing Core Libraries")
st.markdown("""
1. Open Command Prompt/Terminal
2. Run the following command to install the basic data science libraries:
""")

st.markdown("### Copy-paste this command into your terminal:")
copy_col1, _ = st.columns([3, 1])
with copy_col1:
    st.code("pip install pandas numpy matplotlib seaborn plotly", language="bash")

st.markdown("""
### You'll see: 
A lot of text showing download progress and installation status. At the end, you should see something like:
""")
st.code("""
Successfully installed ... [list of installed packages]
""", language="text")

st.subheader("Installing Jupyter Notebook")
st.markdown("""
Jupyter Notebook allows you to create and share documents that contain live code, equations, visualizations, and text:
""")

st.markdown("### Copy-paste this command into your terminal:")
copy_col1, _ = st.columns([3, 1])
with copy_col1:
    st.code("pip install notebook", language="bash")

st.markdown("""
### You'll see:
Download progress and installation status. When complete, you'll see:
""")
st.code("Successfully installed notebook-[version] ... [and other packages]", language="text")

st.subheader("Installing Spyder IDE")
st.markdown("""
Spyder is a powerful scientific environment for Python:
""")

st.markdown("### Copy-paste this command into your terminal:")
copy_col1, _ = st.columns([3, 1])
with copy_col1:
    st.code("pip install spyder", language="bash")

st.markdown("""
### You'll see:
Download progress and installation status. When complete, you'll see:
""")
st.code("Successfully installed spyder-[version] ... [and other packages]", language="text")

# Install all in one command
st.subheader("All-in-One Installation Command")
st.markdown("""
You can install all libraries at once with this command:
""")

st.markdown("### Copy-paste this single command into your terminal to install everything at once:")
copy_col1, _ = st.columns([3, 1])
with copy_col1:
    st.code("pip install pandas numpy matplotlib seaborn plotly openai sentence-transformers chromadb streamlit", language="bash")

st.markdown("""
### You'll see:
A lot of download and installation messages. This will take several minutes to complete depending on your internet speed. When finished, you'll see:
""")
st.code("Successfully installed ... [long list of installed packages]", language="text")

# Working with the Files
st.header("Running Your Python Files")
st.markdown("""
Now that you have everything installed, you can open Jupyter Notebooks and Spyder.
""")


st.markdown("### Copy-paste this command into your terminal:")
copy_col1, _ = st.columns([3, 1])
with copy_col1:
    st.code("jupyter notebook", language="bash")

st.markdown("""
### You'll see:
Several lines of text will appear, and then your web browser should automatically open with Jupyter. The terminal will show something like:
""")
st.code("""
[I 2023-04-04 10:15:32.123 ServerApp] Jupyter Server 2.0.0 is running at:
[I 2023-04-04 10:15:32.123 ServerApp] http://localhost:8888/lab
[I 2023-04-04 10:15:32.123 ServerApp] or http://127.0.0.1:8888/lab
""", language="text")

st.markdown("""
4. This will open Jupyter in your web browser
5. Once Jupyter opens you're done!
""")

st.subheader("Using Spyder IDE")
st.markdown("""
To run Spyder:

1. Open Command Prompt/Terminal
2. Simply type:
""")

st.markdown("### Copy-paste this command into your terminal:")
copy_col1, _ = st.columns([1, 3])
with copy_col1:
    st.code("spyder", language="bash")

st.markdown("""
### You'll see:
Some initialization text in the terminal, and then the Spyder application will open in a new window that looks like this:
""")

# Adding a placeholder image of Spyder
st.image("https://docs.spyder-ide.org/current/_images/mainwindow_default_1610.png", width=600, caption="Spyder IDE Interface")

st.markdown("""
3. This will open the Spyder IDE
4. If Spyder opens you're done!
""")

# Troubleshooting Section
st.header("Troubleshooting Common Issues")
with st.expander("Common Installation Problems and Solutions"):
    st.markdown("""
    ### 1. "Command Not Found" Error
    
    **Problem**: After installation, when you type `python` or `pip` in the terminal, you get "command not found" error.
    
    **Solution**: 
    - Windows: Make sure you checked "Add Python to PATH" during installation. If not, you may need to reinstall or manually add Python to PATH.
    - macOS/Linux: Try using `python3` and `pip3` commands instead.
    
    ### 2. Permission Errors During Installation
    
    **Problem**: You get permission errors when trying to install packages.
    
    **Solution**:
    - Windows: Run Command Prompt as Administrator
    - macOS/Linux: Use `sudo pip install [package]` or install for the current user only with `pip install --user [package]`
    
    ### 3. Library Import Errors
    
    **Problem**: When running your code, you get "ModuleNotFoundError" or "ImportError".
    
    **Solution**:
    - Make sure you've installed all required libraries listed above
    - Try installing the specific missing library using: `pip install [library_name]`
    
    ### 4. SSL Certificate Errors
    
    **Problem**: You get SSL certificate errors when using pip.
    
    **Solution**:
    ```
    pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org [package_name]
    ```
    
    ### 5. Jupyter Notebook Not Opening in Browser
    
    **Problem**: Jupyter Notebook server starts but doesn't open in your browser.
    
    **Solution**:
    - Manually open your browser and go to: http://localhost:8888
    - If that doesn't work, look at the terminal output for a URL with a token
    """)

# Resources Section
st.header("Additional Resources")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Learning Python")
    st.markdown("""
    - [Python.org Official Tutorial](https://docs.python.org/3/tutorial/)
    - [W3Schools Python Tutorial](https://www.w3schools.com/python/)
    - [Real Python](https://realpython.com/) - Great tutorials for all levels
    - [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/) - Free book
    """)

with col2:
    st.subheader("Data Science & Libraries")
    st.markdown("""
    - [Pandas Documentation](https://pandas.pydata.org/docs/)
    - [Matplotlib Gallery](https://matplotlib.org/stable/gallery/index.html)
    - [Seaborn Tutorial](https://seaborn.pydata.org/tutorial.html)
    - [Streamlit Documentation](https://docs.streamlit.io/)
    - [OpenAI API Documentation](https://platform.openai.com/docs/introduction)
    """)

# Footer
st.markdown("---")
st.markdown("""
### Need More Help?
If you encounter any issues not covered in this guide, here are some resources for getting help:
- [Stack Overflow](https://stackoverflow.com/questions/tagged/python) - search for similar issues or ask questions
- [Python.org Help](https://www.python.org/about/help/) - official Python help resources
- [r/learnpython](https://www.reddit.com/r/learnpython/) - a friendly community for Python beginners
""")

# FAQ Section
with st.expander("Frequently Asked Questions"):
    st.markdown("""
    ### Q: Do I need to install all these libraries?
    
    A: Yes, if you want to run the provided Jupyter notebook and Streamlit files without any errors. These libraries are imported in those files.
    
    ### Q: How much disk space will I need?
    
    A: A basic Python installation is around 100-150MB. With all the libraries listed here, expect to use about 1-2GB of disk space.
    
    ### Q: Can I use a different version of Python?
    
    A: It's recommended to use Python 3.8 or newer. The libraries in the provided files should work with Python 3.8 through 3.12.
    
    ### Q: Do I need to know programming to use these applications?
    
    A: The Streamlit app is designed to be user-friendly even for non-programmers. For modifying or creating new Python code, basic programming knowledge would be helpful.
    
    ### Q: How do I update Python or a library?
    
    A: To update a library: `pip install --upgrade library_name`
    Updating Python itself typically requires a new installation.
    """)

# Call to action
st.success("You're all set! Enjoy exploring Python and data analysis with your new tools! 🚀")