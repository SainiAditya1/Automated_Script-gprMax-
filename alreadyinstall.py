
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

# Example usage
if check_installed_software('git'):
    print("Git is already installed. Upgrading to the latest version...")
    current_platform = platform.system()
    if current_platform == 'Windows':
        upgrade_software('git', 'choco upgrade git -y')
    elif current_platform == 'Darwin':  # macOS
        upgrade_software('git', 'brew upgrade git')
    else:  # Linux
        upgrade_software('git', 'sudo apt-get update && sudo apt-get install git -y')
else:
    print("Git is not installed. Installing Git...")
    current_platform = platform.system()
    if current_platform == 'Windows':
        install_software('git', 'choco install git -y')
    elif current_platform == 'Darwin':  # macOS
        install_software('git', 'brew install git')
    else:  # Linux
        install_software('git', 'sudo apt-get update && sudo apt-get install git -y')

if check_installed_software('conda'):
    print("Miniconda is already installed.Upgrading to the latest version...")
    current_platform = platform.system()
    if current_platform == 'Windows':
        upgrade_software('conda', 'choco install miniconda3 -y')
    elif current_platform == 'Darwin':  # macOS
        upgrade_software('conda', 'brew install miniconda')
    else:  # Linux
        upgrade_software('conda', 'conda update --all -y')
    
    
    
else:
    print("Miniconda is not installed. Installing Miniconda...")
    current_platform = platform.system()
    if current_platform == 'Windows':
        install_software('Miniconda', 'choco install miniconda3 -y')
    elif current_platform == 'Darwin':  # macOS
        install_software('Miniconda', 'brew install miniconda')
    else:  # Linux
        install_software('Miniconda', 'wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh && bash Miniconda3-latest-Linux-x86_64.sh -b -p $HOME/miniconda && rm Miniconda3-latest-Linux-x86_64.sh')




