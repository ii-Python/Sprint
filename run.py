# Modules
import sys
import sprint
from os.path import exists
from sprint.parser import SprintParser
from sprint.utils import colored, error

# Credit message
print(colored(f"Sprint v{sprint.__version__} by iiPython", "yellow"))

# Initialization
args = sys.argv[1:]
if not args:

    # Live interpreter
    print(colored("Live interpreter activated.", "yellow"))
    print()

    while True:
        cmd = input(colored(">>> ", "green"))

        # Run our command
        parser = SprintParser(cmd, "<internal>")
        parser.execute()

else:
    path = args[0]

path = path.replace("\\", "/")  # Fix for windows
print()

# Load raw data
if not exists(path):
    error("FileError", "The specified path could not be found.")

try:
    with open(path, "r") as file:
        raw = file.read()

except IsADirectoryError:
    error("ReadError", "The path is a directory.")
except PermissionError:
    error("PermissionError", "Permission denied to access file.")

# Run our raw data
parser = SprintParser(raw, path.split("/")[-1])
parser.execute()
