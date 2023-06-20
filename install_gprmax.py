import os
import subprocess
import platform

def install_gprMax():
    # Step 1: Install Miniconda (Windows, Ubuntu, and macOS)
    if platform.system() == "Windows":
        # Download Miniconda for Windows
        miniconda_url = "https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe"
        os.system(f"powershell -Command \"Invoke-WebRequest '{miniconda_url}' -OutFile 'Miniconda3-latest-Windows-x86_64.exe'\"")
        os.system("start Miniconda3-latest-Windows-x86_64.exe")
        # Wait for the Miniconda installation to complete
        input("Press Enter when Miniconda installation is complete...")
        
        
    elif platform.system() == "Linux":
        # Download Miniconda for Linux
        miniconda_url = "https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh"
        os.system(f"wget {miniconda_url}")
        os.system("chmod +x Miniconda3-latest-Linux-x86_64.sh")
        os.system("./Miniconda3-latest-Linux-x86_64.sh")
        
        
    elif platform.system() == "Darwin":
        # Download Miniconda for macOS
        miniconda_url = "https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh"
        os.system(f"curl -O {miniconda_url}")
        os.system("chmod +x Miniconda3-latest-MacOSX-x86_64.sh")
        os.system("./Miniconda3-latest-MacOSX-x86_64.sh")

    # Step 2: Install Git and clone gprMax repository
    subprocess.run(["conda", "update", "conda", "-y"])
    subprocess.run(["conda", "install", "git", "-y"])
    subprocess.run(["git", "clone", "https://github.com/gprMax/gprMax.git"])
    os.chdir("gprMax")

    # Step 3: Create conda environment and install dependencies
    subprocess.run(["conda", "env", "create", "-f", "conda_env.yml"])

    # Step 4: Install C compiler supporting OpenMP (Windows, Ubuntu, and macOS)
    if platform.system() == "Windows":
        # Install GCC for Windows
        subprocess.run(["conda", "install", "m2w64-toolchain", "-y"])

    elif platform.system() == "Linux":
        # gcc should be already installed on Linux, so no action required
        pass

    elif platform.system() == "Darwin":
        # Install gcc on macOS using Homebrew
        subprocess.run(["brew", "install", "gcc"])

    # Step 5: Build and install gprMax
    conda_activate_cmd = "conda activate gprMax" if platform.system() != "Windows" else "activate gprMax"
    subprocess.run(["pip", "install", "-e", "gprMax"], env={"PATH": os.environ["PATH"]}, shell=True)

    print("gprMax installation complete.")

if __name__ == "__main__":
    install_gprMax()

