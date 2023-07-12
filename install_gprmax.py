
import os
import subprocess
import platform
import shutil




    
    
# Check if Conda is installed
def is_conda_installed():
    try:
        subprocess.check_output(['conda', '--version'])
        return True
    except subprocess.CalledProcessError:
        return False

# Check if gprmax environment exists
def is_gprmax_environment_present():
    try:
        output = subprocess.check_output(['conda', 'info', '--envs']).decode('utf-8')
        return 'gprMax' in output
    except subprocess.CalledProcessError:
        return False       
    
    
def print_options():
    print("1. Update gprMax")
    print("2. Install gprMax at other directory")
    print("3. Abort installation")

def get_option():
    option = input("Enter your option: ")
    return option       
    
    
def update_gprMax():
    os.system("conda activate gprMax")
    os.system("pip uninstall gprMax")
    # os.system("git clone https://github.com/gprMax/gprMax.git")
    os.system("git clone https://github.com/gprMax/gprMax.git -b devel")
    os.system("git checkout devel")
    os.system("pip install -e gprMax")    
    
    
    
    
    


# starting of install_gprMax() function

def install_gprMax():
    # Step 1: Install Miniconda (Windows, Ubuntu, and macOS)

    if is_conda_installed():
        print("Conda is installed on the system.")
        if is_gprmax_environment_present():
            print("gprmax environment is already present.")
            print_options()
            option = get_option()
            if option == "1":
                print("Updating gprMax...")
                update_gprMax()
                exit()
            elif option == "2":
                print("Installing gprMax at other directory...")
                 # Get the current directory.
                current_directory = os.getcwd()
                # Get the directory where gprMax is already installed.
                # installed_directory = os.path.join(current_directory, "gprMax")
                # shutil.move(installed_directory, os.path.join(current_directory, "gprMax_"))
            elif option == "3":
                print("Aborting installation...")
                exit()    
            else:
                print("Invalid option")
        else:
            print("gprmax environment is not found.Installing gprMax")
# else:
#     print("Conda is not installed on the system.")
        
            
          
    else:
        if platform.system() == "Windows":
            
        # Download Miniconda for Windows
            miniconda_url = "https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe"
            os.system(f"powershell -Command \"Invoke-WebRequest '{miniconda_url}' -OutFile 'Miniconda3-latest-Windows-x86_64.exe'\"")
            os.system("start Miniconda3-latest-Windows-x86_64.exe")
        # Wait for the Miniconda installation to complete
            input("Press Enter when Miniconda installation is complete...")
        
        
        elif platform.system() == "Linux":
            
            miniconda_url = "https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh"
            os.system(f"wget {miniconda_url}")
            os.system("chmod +x Miniconda3-latest-Linux-x86_64.sh")
            os.system("./Miniconda3-latest-Linux-x86_64.sh")
        
        elif platform.system() == "Darwin":
            
            if platform.machine().endswith("64"):
                miniconda_url = "https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh"
            elif platform.machine().endswith("arm64"):
                miniconda_url = "https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh"
            os.system(f"curl -O {miniconda_url}")
            os.system("chmod +x " + os.path.basename(miniconda_url))
            os.system(f"./{os.path.basename(miniconda_url)}")

        continue_install = input("Continue installation? Enter 'yes' to continue: ")
        if continue_install.lower() != "yes":
            print("Installation aborted.")
            return

    # Step 2: Install Git and clone gprMax repository
   

    result = subprocess.run(["conda", "install", "git", "-y"])
    if result.returncode != 0:
        print("Error installing Git. Aborting installation.")
        return
    result = subprocess.run(["git", "clone", "https://github.com/gprMax/gprMax.git", "-b", "devel"])
    if result.returncode != 0:
        print("Error cloning gprMax repository. Aborting installation.")
        return

    os.chdir("gprMax")

    continue_install = input("Continue installation? Enter 'yes' to continue: ")
    if continue_install.lower() != "yes":
        print("Installation aborted.")
        return

    # Step 3: Create conda environment and install dependencies
    result = subprocess.run(["conda", "env", "create", "-f", "conda_env.yml"])
    if result.returncode != 0:
        print("Error creating conda environment. Aborting installation.")
        return

    # Step 4: Install C compiler supporting OpenMP (Windows, Ubuntu, and macOS)
    if platform.system() == "Windows":
        # Install GCC for Windows
        result = subprocess.run(["conda", "install", "gcc", "-y"])
        if result.returncode !=0:
            print("Error Installing C compiler. Aborting installation.")
            return

    elif platform.system() == "Linux":
        # gcc should be already installed on Linux, so no action required
        pass

    elif platform.system() == "Darwin":
        # Install gcc on macOS using Homebrew
        result = subprocess.run(["brew", "install", "gcc"])
        if result.returncode !=0:
            print("Error Installing C compiler. Aborting installation.")
            return 

    # Step 5: Build and install gprMax
    conda_activate_cmd = "conda activate gprMax" if platform.system() != "Windows" else "activate gprMax"
    subprocess.run(["pip", "install", "-e", "gprMax"], env={"PATH": os.environ["PATH"]}, shell=True)
    subprocess.run([conda_activate_cmd, "&&", "python", "setup.py", "build"], shell=True)
    subprocess.run([conda_activate_cmd, "&&", "python", "setup.py", "install"], shell=True)

    print("gprMax installation complete.")

if __name__ == "__main__":
    install_gprMax()

