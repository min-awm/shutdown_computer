import subprocess
import platform

def shutdown():
    os_name = platform.system()
    if os_name == "Windows":
        subprocess.run(["shutdown", "/s", "/t", "0"])
    elif os_name == "Darwin":  # macOS
        subprocess.run(["sudo", "shutdown", "-h", "now"])
    elif os_name == "Linux":
        subprocess.run(["sudo", "shutdown", "-h", "now"])
    else:
        print("Unsupported OS")