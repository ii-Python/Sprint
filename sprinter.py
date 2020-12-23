#!/usr/bin/env python3.9

# Modules
import os
import sprint

import platform
from os.path import isfile

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

    # Support for running files
    if isfile(cmd):

        # Load our lines
        try:
            lines = open(cmd, "r").read().split("\n")

        except PermissionError:
            print(sprint.colored("Missing permissions to read from file.", "red"))
            continue

        # Check for sprint
        if lines[0] == ";sprint-file":

            # Execute the file
            for line in lines:
                parser.execute(line)

            # Make sure to not execute the filename as a command
            continue

    # Run our command
    parser.execute(cmd)
