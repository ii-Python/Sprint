# Modules
import os
import sprint
import platform

# Credit message
print(sprint.colored(f"Sprint v{sprint.__version__} by iiPython", "yellow"))
print(sprint.colored(f"Python version {platform.python_version()}, running on {platform.system()}", "yellow"))
print()

# Main loop
parser = sprint.SprintParser()
while True:

    # Set our path
    path = os.getcwd()
    path = path.replace(os.getenv("HOME"), "~")

    # Execute command
    try:
        cmd = input(sprint.colored(f"Sprint@{path} >>> ", "green"))

    except KeyboardInterrupt:
        print()  # Stop weird line break issues
        continue

    # Run our command
    parser.execute(cmd)
