#!/usr/bin/env python3.9

# Modules
import os
import sprint

import colorama
import platform

from os.path import isfile, expanduser

# Credit message
colorama.init()  # Fix windows colors

print(sprint.colored(f"Sprint v{sprint.__version__} by iiPython", "yellow"))
print(sprint.colored(f"Python version {platform.python_version()}, running on {platform.system()}", "yellow"))
print()

# Command grabber
def get_command(indent = 0):

    # Set our path
    path = os.getcwd()
    path = path.replace(os.getenv("HOME", expanduser("~")), "~")

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
            raw_lines = open(cmd, "r").read().split("\n")

        except PermissionError:
            print(sprint.colored("Missing permissions to read from file.", "red"))
            continue

        # Check for sprint
        if raw_lines[0] == ";sprint-file":

            # Remove all whitespace BEFORE parsing
            no_whitespaced_lines = []
            for line in raw_lines:

                # Ignore blank lines
                line = parser.remove_whitespace(line)
                if not line:
                    continue

                # Append this to our line data
                no_whitespaced_lines.append(line)

            # Parse the file
            multiline = False
            complete_line = None

            line_index = 0
            lines = []

            for line in no_whitespaced_lines:

                # Ignore blank lines
                line = parser.remove_whitespace(line)
                if not line:
                    continue

                # Check if this declares another line
                if line.endswith("\\") and not multiline:
                    multiline = True
                    complete_line = line[:-1]

                elif multiline:

                    # Check if this isn't really a multiple line
                    if not no_whitespaced_lines[line_index - 1].endswith("\\"):
                        multiline = False

                    # Remove the backslash (if exists)
                    if line.endswith("\\"):
                        line = line[:-1]

                    # Joining together
                    if multiline:
                        complete_line += " " + line

                    else:

                        # Check for our other line
                        if complete_line != "":
                            lines.append(complete_line)
                            lines.append(line)

                            # Reset our completed line
                            complete_line = ""

                else:
                    lines.append(line)

                # Increase our index
                line_index += 1

            # Execute our lines
            for line in lines:
                parser.execute(line)

            # Make sure to not execute the filename as a command
            continue

    # Run our command
    parser.execute(cmd)
