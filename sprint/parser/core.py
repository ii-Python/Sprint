# Modules
import string
from .runtime.exec import Executer
from ..utils.logging import Logger
from .runtime.globals import generate_globals

# Sprint parser
class SprintParser(object):

    def __init__(self, data, filename):
        self.data = data
        self.environment = {}

        self.globals = generate_globals()
        self.executer = Executer(self)

        self.logger = Logger(filename, nofile = True)
        self.flogger = Logger(filename)

    def remove_whitespace(self, line):

        for char in line:
            if char in string.whitespace:
                line = line.replace(char, "", 1)
            else:
                return line  # No more whitespace remaining

        return line

    def execute(self):

        """Executes the sprint data initialized"""

        lineNum = 1

        lines = self.data.split("\n")
        for line in lines:

            # Reinitialize globals
            self.globals = generate_globals() | self.environment

            # Format line with globals
            for glob in self.globals:
                line = line.replace(f"%{glob}", self.globals[glob])

            # Ignore whitespace
            command = self.remove_whitespace(line)
            if not command:
                continue

            # Load our information
            args = command.split(" ")
            arguments = []

            in_string = False
            string_data = ""
            for arg in args:

                # Check if we aren't in a string
                if not in_string:

                    # Is this the start of a string?
                    if arg.startswith("\""):
                        in_string = True
                        string_data += arg[1:] + " "

                    else:

                        # Normal argument
                        # Try and convert it to appropriate datatypes
                        if arg == "true":
                            arg = True
                        elif arg == "false":
                            arg = False

                        try:
                            arg = int(arg)
                        except ValueError:
                            pass

                        arguments.append(arg)

                elif arg.endswith("\""):

                    # The end of a string
                    in_string = False
                    string_data += arg[:-1]

                    arguments.append(string_data)
                    string_data = ""

                else:

                    # In the middle of a string
                    string_data += arg + " "

            # Process our arguments
            base = arguments[0]
            arguments = arguments[1:]

            # Command flags
            flags = []
            for argument in arguments:

                # Flags are strings-only
                if not isinstance(argument, str):
                    continue

                # Check if this is a flag
                if argument.startswith("-"):

                    # Correct, remove it and add it to flags
                    arguments.remove(argument)
                    flags.append(argument[1:])

            # Execute this line
            self.executer.execute(lineNum, base, arguments, flags)

            # Count up our line number
            lineNum += 1
