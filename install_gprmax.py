import os
import platform
import subprocess
import sys

def install_gprmax():
    operating_system = platform.system()
    
    if operating_system == "Windows":
        install_gprmax_windows()
    elif operating_system == "Linux":
        install_gprmax_linux()
    elif operating_system == "Darwin":
        install_gprmax_macos()
    else:
        print(f"Unsupported operating system: {operating_system}")
        sys.exit(1)



def install_gprmax_windows():
    print("Installing GprMax on Windows...")
    try:
        # Check if Git is installed
        subprocess.run(["git", "--version"], check=True, stdout=subprocess.PIPE)
    except (FileNotFoundError, subprocess.CalledProcessError):
        print("Git is not installed. Please install Git and try again.")
        sys.exit(1)

    # Check if the gprMax repository exists
    if not os.path.exists("gprMax"):
        try:
            # Clone the GprMax repository
            subprocess.run(["git", "clone", "https://github.com/gprmax/gprMax.git"], check=True, stdout=subprocess.PIPE)
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while cloning the repository: {e}")
            sys.exit(1)
    
    try:
        # Install GprMax dependencies
        subprocess.run(["pip", "install", "numpy"], check=True, stdout=subprocess.PIPE)
        subprocess.run(["pip", "install", "-r", "gprMax/requirements.txt"], check=True, stdout=subprocess.PIPE)
        
        print("GprMax installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

def install_gprmax_linux():
    print("Installing GprMax on Linux...")
    try:
        # Install Git
        subprocess.run(["sudo", "apt", "install", "-y", "git"], check=True, stdout=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while installing Git: {e}")
        sys.exit(1)

    # Check if the gprMax repository exists
    if not os.path.exists("gprMax"):
        try:
            # Clone the GprMax repository
            subprocess.run(["git", "clone", "https://github.com/gprmax/gprMax.git"], check=True, stdout=subprocess.PIPE)
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while cloning the repository: {e}")
            sys.exit(1)

    try:
        # Install GprMax dependencies
        subprocess.run(["pip", "install", "numpy"], check=True, stdout=subprocess.PIPE)
        subprocess.run(["sudo", "pip", "install", "-r", "gprMax/requirements.txt"], check=True, stdout=subprocess.PIPE)

        print("GprMax installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

def install_gprmax_macos():
    print("Installing GprMax on macOS...")
    try:
        # Check if Homebrew is installed
        subprocess.run(["brew", "--version"], check=True, stdout=subprocess.PIPE)
    except (FileNotFoundError, subprocess.CalledProcessError):
        print("Homebrew is not installed. Please install Homebrew and try again.")
        sys.exit(1)

    # Check if the gprMax repository exists
    if not os.path.exists("gprMax"):
        try:
            # Clone the GprMax repository
            subprocess.run(["git", "clone", "https://github.com/gprmax/gprMax.git"], check=True, stdout=subprocess.PIPE)
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while cloning the repository: {e}")
            sys.exit(1)

