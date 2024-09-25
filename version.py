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
        print(f"Error: Unable to retrieve version for {binary_name}.")

    except FileNotFoundError:
        print(f"Error: {binary_name} not found on your system.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: version <BINARY>")
    else:
        binary_name = sys.argv[1]
        get_version(binary_name)
