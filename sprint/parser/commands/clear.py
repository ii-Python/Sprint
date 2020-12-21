# Modules
import subprocess
from os import name

# Function to clear the screen
def main(args, flags, core):

    # Check our OS
    command = "clear"
    if name == "nt":
        command = "cls"

    # Execute
    subprocess.run([command])
