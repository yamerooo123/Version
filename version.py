import subprocess
import sys

def get_version(binary_name):
    try:
        # Check -version first since some tool  like Nmap will mistake it as the command
        result = subprocess.run([binary_name, '-version'], capture_output=True, text=True, check=True)
        print(f"{binary_name} version: {result.stdout.strip()}")
        return
    except subprocess.CalledProcessError:
        pass  

    try:
        # Check version with  '--version'
        result = subprocess.run([binary_name, '--version'], capture_output=True, text=True, check=True)
        print(f"{binary_name} version: {result.stdout.strip()}")
        return
    except subprocess.CalledProcessError:
        pass

    try:
        # Check version with  '-version'
        result = subprocess.run([binary_name, 'version'], capture_output=True, text=True, check=True)
        print(f"{binary_name} version: {result.stdout.strip()}")
        return
    except subprocess.CalledProcessError:
        pass  

    try:
        # Check version with '-v'
        result = subprocess.run([binary_name, '-v'], capture_output=True, text=True, check=True)
        print(f"{binary_name} version: {result.stdout.strip()}")
    except subprocess.CalledProcessError:
        pass

    except FileNotFoundError:
        print(f"Error: Are you sure you have {binary_name} installed?")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Under development"
              "Created by Suphawith Phusanbai"
              "Usage: version <BINARY>")
    else:
        binary_name = sys.argv[1]
        get_version(binary_name)
