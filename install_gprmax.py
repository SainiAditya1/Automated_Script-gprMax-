
import os
import platform
import subprocess

def is_conda_installed():
    try:
        subprocess.check_output(['conda', '--version'])
        return True
    except FileNotFoundError:
        return False
    
    
def install_conda():
    if platform.system() == "Windows":
        miniconda_url = "https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe"
        os.system(f"powershell -Command \"Invoke-WebRequest '{miniconda_url}' -OutFile 'Miniconda3-latest-Windows-x86_64.exe'\"")
        os.system("start Miniconda3-latest-Windows-x86_64.exe")
        input("Press Enter when Miniconda installation is complete...")
        
        # Add Conda folders to PATH
        conda_folders = [
            os.path.join(os.path.expanduser("~"), "miniconda3", "Scripts"),
            os.path.join(os.path.expanduser("~"), "miniconda3", "Library", "bin")
        ]
        current_path = os.environ.get("PATH", "")
        new_path = os.pathsep.join(conda_folders + [current_path])
        os.environ["PATH"] = new_path

    elif platform.system() == "Linux":
        miniconda_url = "https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh"
        os.system(f"wget {miniconda_url}")
        os.system("chmod +x Miniconda3-latest-Linux-x86_64.sh")
        os.system("./Miniconda3-latest-Linux-x86_64.sh -b -p $HOME/miniconda3")
        
        # Add Conda folders to PATH
        # conda_folders = [
        #     os.path.join(os.path.expanduser("~"), "miniconda3", "bin")
        # ]
        # current_path = os.environ.get("PATH", "")
        # new_path = os.pathsep.join(conda_folders + [current_path])
        # os.environ["PATH"] = new_path

    elif platform.system() == "Darwin":
        if platform.machine().endswith("64"):
            miniconda_url = "https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh"
        elif platform.machine().endswith("arm64"):
            miniconda_url = "https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh"
        os.system(f"curl -O {miniconda_url}")
        os.system("chmod +x " + os.path.basename(miniconda_url))
        os.system(f"./{os.path.basename(miniconda_url)} -b -p $HOME/miniconda3")
        
        # Add Conda folders to PATH
        conda_folders = [
            os.path.join(os.path.expanduser("~"), "miniconda3", "bin")
        ]
        current_path = os.environ.get("PATH", "")
        new_path = os.pathsep.join(conda_folders + [current_path])
        os.environ["PATH"] = new_path    
            
        
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



def choose_directory():
    while True:
        directory = input("Enter the directory path: ")
        if os.path.isdir(directory):
            return os.path.abspath(directory)
        else:
            print("Invalid directory. Please try again.")    
    
def update_gprMax():
    
    if platform . system () != " Windows " :
        subprocess . run ( " source ~/ miniconda3 / etc / profile . d / conda . sh && conda activate gprMax - devel && pip uninstall  gprMax " ,
    shell = True )
    else :
        subprocess . run ( " conda . bat activate gprMax - devel && pip uninstall  gprMax " , shell = True )
    
    
    os.system("git clone https://github.com/gprMax/gprMax.git -b devel")
    os.system("git checkout devel")
    os.system("pip install -e gprMax")         
          
        
        
        
        
        

def install_gprMax():
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
                print("Installing gprMax at another directory...")
                # to be implemeted
                
                selected_directory = choose_directory()
                subprocess.call(['bash', '-c', 'cd "{}" && exec bash'.format(selected_directory)])
            elif option == "3":
                print("Aborting installation...")
                exit()
            else:
                print("Invalid option")
        else:
            print("gprmax environment is not found. Installing gprMax...")
    
    
    
    
    
    else:
        print("Conda is not installed on the system.")
        continue_install = input("Continue installation? Enter 'yes' to continue: ")
        if continue_install.lower() == "yes":
            install_conda()
        else:
            print("Installation aborted.")
            exit()


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
    
    if platform . system () != " Windows " :
        subprocess . run ( " source ~/ miniconda3 / etc / profile . d / conda . sh && conda activate gprMax - devel && pip install -e gprMax " ,
    shell = True )
    else :
        subprocess . run ( " conda . bat activate gprMax - devel && pip install -e gprMax " , shell = True )
    
   
    subprocess.run(["python", "setup.py", "build"], shell=True)
    subprocess.run(["python", "setup.py", "install"], shell=True)

    print("gprMax installation complete.")


install_gprMax()

