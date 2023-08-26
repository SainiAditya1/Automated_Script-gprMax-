# Google Summer of Code 2023
# Project Title: Improved Installation Tools
![GSoC_logo](https://github.com/SainiAditya1/CSV_Plot/assets/114948505/0770d5ff-095a-4048-9132-66e00b03c425)

# Synopsis
The aim of this project is to create a simplified and more user-friendly installation workflow for the gprMax is predominantly written in Python, but some of the performance-critical parts of the code are written in Cython, which must be built and compiled.The current installation involves building a Python environment, installing a C compiler with OpenMP support, and building and installing the gprMax package. This can be a lengthy and complex procedure, depending on your operating system, especially for first-time or inexperienced users.
# Deliverables

# 1) Automated Python Script to installl gprMax

# To test the script on different operating systems, you can follow these steps:

# Windows:

Ensure that Git and Python are installed on your Windows machine.
Open a command prompt or PowerShell.
Navigate to the directory where the script is saved.
Run the script using the Python interpreter:
``` 
python install_gprmax.py
```

# Ubuntu:

Open a terminal
Install Git and Python if they are not already installed:
```
sudo apt update
```

```
sudo apt install git python3
```
Navigate to the directory where the script is saved.
Run the script using the Python interpreter
```
python3 install_gprmax.py
```


# macOS:

Ensure that Homebrew and Python are installed on your macOS machine.
Open a terminal.
Install Git and Python if they are not already installed
```
brew install git python3
```
Navigate to the directory where the script is saved.
Run the script using the Python interpreter.
```
python3 install_gprmax.py
```
# 2) Docker Image
