# Modules
import os
import sprint
import platform

# Credit message
print(sprint.colored(f"Sprint v{sprint.__version__} by iiPython", "yellow"))
print(sprint.colored(f"Python version {platform.python_version()}, running on {platform.system()}", "yellow"))
print()

# Command grabber
def get_command(indent = 0):

    # Set our path
    path = os.getcwd()
    path = path.replace(os.getenv("HOME"), "~")

    # Fetch our command
    command = input(sprint.colored(f"{path} >>> {' ' * indent}", "green"))

    # Multi-line support
    if command.endswith("\\"):
        command = command[:-1]

        command = command + get_command(indent = indent + 2)

    # Return
    return command

# Main loop
parser = sprint.SprintParser()
while True:

    # Execute command
    try:
        cmd = get_command()

    except KeyboardInterrupt:
        print()  # Stop weird line break issues
        continue

    # Run our command
    parser.execute(cmd)
