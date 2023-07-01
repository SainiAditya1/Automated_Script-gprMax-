
import os
import subprocess
import platform



def check_installed_software(software):
    try:
        subprocess.check_output([software, '--version'])
        return True
    except (FileNotFoundError, subprocess.CalledProcessError):
        return False

def upgrade_software(software, upgrade_command):
    try:
        subprocess.check_call(upgrade_command, shell=True)
        print(f"{software} upgraded successfully.")
    except (FileNotFoundError, subprocess.CalledProcessError):
        print(f"Failed to upgrade {software}.")
        print(f"Please manually upgrade {software}.")

def install_software(software, install_command):
    try:
        subprocess.check_call(install_command, shell=True)
        print(f"{software} installed successfully.")
    except (FileNotFoundError, subprocess.CalledProcessError):
        print(f"Failed to install {software}.")
        print(f"Please manually install {software}.")


# starting of install_gprMax() function

def install_gprMax():
    # Step 1: Install Miniconda (Windows, Ubuntu, and macOS)
    
    if check_installed_software('conda'):
        print("Miniconda is already installed.Upgrading to the latest version...")
        current_platform = platform.system()
        if current_platform == 'Windows':
            subprocess.call(['conda', 'update', '-n', 'base', '-c', 'defaults', '--all', '-y'])
  # upgrade_software('conda', 'choco install miniconda3 -y')
        elif current_platform == 'Darwin':
            subprocess.call(['conda', 'update', '-n', 'base', '-c', 'defaults', '--all', '-y'])
            # upgrade_software('conda', 'brew install miniconda')
        elif current_platform == 'Linux':
            subprocess.call(['conda', 'update', '-n', 'base', '-c', 'defaults', '--all', '-y'])
            
          
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
    result = subprocess.run(["conda", "update", "conda", "-y"])
    if result.returncode != 0:
        print("Error updating conda. Aborting installation.")
        return

    result = subprocess.run(["conda", "install", "git", "-y"])
    if result.returncode != 0:
        print("Error installing Git. Aborting installation.")
        return

    result = subprocess.run(["git", "clone", "https://github.com/gprMax/gprMax.git"])
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
        result = subprocess.run(["conda", "install", "m2w64-toolchain", "-y"])
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

